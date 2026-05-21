from __future__ import annotations

import inspect
import logging
import uuid
from dataclasses import dataclass
from typing import Any, Callable, Iterable

import grpc
import grpc.aio

from kave import highlevel, iterators
from kave._logging import rpc_timer
from kave._tracing import inject_traceparent
from kave.audit.v1 import audit_pb2_grpc  # type: ignore[import]
from kave.control.v1 import control_pb2_grpc, rbac_pb2_grpc  # type: ignore[import]
from kave.errors import wrap_error
from kave.retry import DEFAULT_RETRY_POLICY, RetryPolicy, retry_async, retry_sync, should_retry_rpc
from kave.runtime.v1 import runtime_pb2_grpc  # type: ignore[import]

Metadata = Iterable[tuple[str, str]] | None


@dataclass
class ClientOptions:
    addr: str = "localhost:19090"
    token: str | None = None
    tls: bool = False
    credentials: grpc.ChannelCredentials | None = None
    timeout: float = 30.0
    retry: RetryPolicy | None = DEFAULT_RETRY_POLICY
    logger: logging.Logger | None = None
    tracer: Any | None = None


class _SyncServiceProxy:
    def __init__(self, target: Any, options: ClientOptions) -> None:
        self._target = target
        self._options = options

    def __getattr__(self, name: str) -> Any:
        attr = getattr(self._target, name)
        if not callable(attr):
            return attr

        def call(request: Any, *, timeout: float | None = None, metadata: Metadata = None, **kwargs: Any) -> Any:
            rpc = getattr(attr, "_method", name)
            rpc_name = rpc.decode() if isinstance(rpc, bytes) else str(rpc)
            request_id = str(uuid.uuid4())
            call_metadata = _metadata(self._options, metadata, request_id)

            def invoke() -> Any:
                try:
                    with _span(self._options.tracer, rpc_name):
                        with rpc_timer(self._options.logger, rpc_name, request_id):
                            return attr(
                                request,
                                timeout=self._options.timeout if timeout is None else timeout,
                                metadata=call_metadata,
                                **kwargs,
                            )
                except grpc.RpcError as err:
                    raise wrap_error(err) from err

            if self._options.retry and should_retry_rpc(name):
                return retry_sync(self._options.retry, invoke)
            return invoke()

        return call


class _AsyncServiceProxy:
    def __init__(self, target: Any, options: ClientOptions) -> None:
        self._target = target
        self._options = options

    def __getattr__(self, name: str) -> Any:
        attr = getattr(self._target, name)
        if not callable(attr):
            return attr

        async def call(request: Any, *, timeout: float | None = None, metadata: Metadata = None, **kwargs: Any) -> Any:
            rpc = getattr(attr, "_method", name)
            rpc_name = rpc.decode() if isinstance(rpc, bytes) else str(rpc)
            request_id = str(uuid.uuid4())
            call_metadata = _metadata(self._options, metadata, request_id)

            async def invoke() -> Any:
                try:
                    with _span(self._options.tracer, rpc_name):
                        with rpc_timer(self._options.logger, rpc_name, request_id):
                            result = attr(
                                request,
                                timeout=self._options.timeout if timeout is None else timeout,
                                metadata=call_metadata,
                                **kwargs,
                            )
                            if inspect.isawaitable(result):
                                return await result
                            return result
                except grpc.RpcError as err:
                    raise wrap_error(err) from err

            if self._options.retry and should_retry_rpc(name):
                return await retry_async(self._options.retry, invoke)
            return await invoke()

        return call


def _metadata(options: ClientOptions, metadata: Metadata, request_id: str) -> list[tuple[str, str]]:
    out = list(metadata or [])
    if options.token:
        out.append(("authorization", f"Bearer {options.token}"))
    out.append(("x-request-id", request_id))
    return inject_traceparent(out)


class _NoopSpan:
    def __enter__(self) -> None:
        return None

    def __exit__(self, *_: object) -> None:
        return None


def _span(tracer: Any, rpc_name: str) -> Any:
    if tracer is None:
        return _NoopSpan()
    start = getattr(tracer, "start_as_current_span", None)
    if not callable(start):
        return _NoopSpan()
    return start(f"kave.{rpc_name.rsplit('/', 1)[-1]}")


class SyncClient(highlevel.SyncHighLevelMixin, iterators.SyncIteratorMixin):
    def __init__(
        self,
        addr: str | None = None,
        *,
        token: str | None = None,
        tls: bool = False,
        credentials: grpc.ChannelCredentials | None = None,
        timeout: float = 30.0,
        retry: RetryPolicy | None = DEFAULT_RETRY_POLICY,
        logger: logging.Logger | None = None,
        tracer: Any | None = None,
        options: ClientOptions | None = None,
    ) -> None:
        self.options = options or ClientOptions(
            addr=addr or "localhost:19090",
            token=token,
            tls=tls,
            credentials=credentials,
            timeout=timeout,
            retry=retry,
            logger=logger,
            tracer=tracer,
        )
        self._channel = self._make_channel()
        self.control = _SyncServiceProxy(control_pb2_grpc.ControlPlaneServiceStub(self._channel), self.options)
        self.rbac = _SyncServiceProxy(rbac_pb2_grpc.RBACServiceStub(self._channel), self.options)
        self.runtime = _SyncServiceProxy(runtime_pb2_grpc.RuntimeServiceStub(self._channel), self.options)
        self.audit = _SyncServiceProxy(audit_pb2_grpc.AuditServiceStub(self._channel), self.options)

    def _make_channel(self) -> grpc.Channel:
        if self.options.credentials is not None:
            return grpc.secure_channel(self.options.addr, self.options.credentials)
        if self.options.tls:
            return grpc.secure_channel(self.options.addr, grpc.ssl_channel_credentials())
        return grpc.insecure_channel(self.options.addr)

    def __enter__(self) -> SyncClient:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def close(self) -> None:
        self._channel.close()


class AsyncClient(highlevel.AsyncHighLevelMixin, iterators.AsyncIteratorMixin):
    def __init__(
        self,
        addr: str | None = None,
        *,
        token: str | None = None,
        tls: bool = False,
        credentials: grpc.ChannelCredentials | None = None,
        timeout: float = 30.0,
        retry: RetryPolicy | None = DEFAULT_RETRY_POLICY,
        logger: logging.Logger | None = None,
        tracer: Any | None = None,
        options: ClientOptions | None = None,
    ) -> None:
        self.options = options or ClientOptions(
            addr=addr or "localhost:19090",
            token=token,
            tls=tls,
            credentials=credentials,
            timeout=timeout,
            retry=retry,
            logger=logger,
            tracer=tracer,
        )
        self._channel = self._make_channel()
        self.control = _AsyncServiceProxy(control_pb2_grpc.ControlPlaneServiceStub(self._channel), self.options)
        self.rbac = _AsyncServiceProxy(rbac_pb2_grpc.RBACServiceStub(self._channel), self.options)
        self.runtime = _AsyncServiceProxy(runtime_pb2_grpc.RuntimeServiceStub(self._channel), self.options)
        self.audit = _AsyncServiceProxy(audit_pb2_grpc.AuditServiceStub(self._channel), self.options)

    def _make_channel(self) -> grpc.aio.Channel:
        if self.options.credentials is not None:
            return grpc.aio.secure_channel(self.options.addr, self.options.credentials)
        if self.options.tls:
            return grpc.aio.secure_channel(self.options.addr, grpc.ssl_channel_credentials())
        return grpc.aio.insecure_channel(self.options.addr)

    async def __aenter__(self) -> AsyncClient:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.close()

    async def close(self) -> None:
        await self._channel.close()


KaveClient = AsyncClient
Client = SyncClient
