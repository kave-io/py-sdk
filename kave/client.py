from __future__ import annotations

import grpc
import grpc.aio

from kave.control.v1 import control_pb2_grpc  # type: ignore[import]
from kave.runtime.v1 import runtime_pb2_grpc  # type: ignore[import]
from kave.audit.v1 import audit_pb2_grpc  # type: ignore[import]


class KaveClient:
    """Async Kave control-plane client.

    Usage::

        from kave.control.v1 import control_pb2

        async with KaveClient("localhost:8080", token="kv-...") as kave:
            org = await kave.control.CreateOrganization(
                control_pb2.CreateOrganizationRequest(name="acme", slug="acme")
            )
    """

    def __init__(
        self,
        addr: str = "localhost:8080",
        *,
        token: str | None = None,
        tls: bool = False,
        credentials: grpc.ChannelCredentials | None = None,
    ) -> None:
        self._addr = addr
        self._token = token
        self._tls = tls
        self._creds = credentials
        self._channel: grpc.aio.Channel | None = None

    def _make_channel(self) -> grpc.aio.Channel:
        interceptors: list[grpc.aio.ClientInterceptor] = []
        if self._token:
            interceptors.append(_TokenInterceptor(self._token))

        if self._creds is not None:
            return grpc.aio.secure_channel(self._addr, self._creds, interceptors=interceptors)
        if self._tls:
            return grpc.aio.secure_channel(
                self._addr, grpc.ssl_channel_credentials(), interceptors=interceptors
            )
        return grpc.aio.insecure_channel(self._addr, interceptors=interceptors)

    async def __aenter__(self) -> KaveClient:
        self._channel = self._make_channel()
        self.control = control_pb2_grpc.ControlPlaneServiceStub(self._channel)
        self.runtime = runtime_pb2_grpc.RuntimeServiceStub(self._channel)
        self.audit = audit_pb2_grpc.AuditServiceStub(self._channel)
        return self

    async def __aexit__(self, *_: object) -> None:
        if self._channel:
            await self._channel.close()
            self._channel = None


class _TokenInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    def __init__(self, token: str) -> None:
        self._meta = [("authorization", f"Bearer {token}")]

    async def intercept_unary_unary(  # type: ignore[override]
        self, continuation, client_call_details, request
    ):
        if client_call_details.metadata is None:
            client_call_details.metadata = []
        client_call_details.metadata.extend(self._meta)
        return await continuation(client_call_details, request)
