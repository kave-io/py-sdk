from __future__ import annotations

import functools
import inspect
from typing import Callable, TypeVar

from kave.contrib.django.client import get_client, resolve_runtime_context
from kave.contrib.django.tenant import UserAgentManager
from kave.control.v1 import budget_pb2
from kave.runtime.v1 import runtime_pb2, span_pb2

F = TypeVar("F", bound=Callable)


def kave_span(name: str, *, agent: str | None = None) -> Callable[[F], F]:
    def decorate(fn: F) -> F:
        if inspect.iscoroutinefunction(fn):
            @functools.wraps(fn)
            async def async_wrapper(*args, **kwargs):
                ctx = resolve_runtime_context(agent)
                req = runtime_pb2.OpenSpanRequest(
                    span=span_pb2.SpanInput(
                        project_id=ctx.project_id,
                        env_id=ctx.env_id,
                        agent_id=ctx.agent_id,
                        name=name,
                        kind=span_pb2.SPAN_KIND_OBSERVED_ACTION,
                        source=span_pb2.SPAN_SOURCE_REPORT,
                    )
                )
                with get_client().with_span(req):
                    return await fn(*args, **kwargs)

            return async_wrapper  # type: ignore[return-value]

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            ctx = resolve_runtime_context(agent)
            req = runtime_pb2.OpenSpanRequest(
                span=span_pb2.SpanInput(
                    project_id=ctx.project_id,
                    env_id=ctx.env_id,
                    agent_id=ctx.agent_id,
                    name=name,
                    kind=span_pb2.SPAN_KIND_OBSERVED_ACTION,
                    source=span_pb2.SPAN_SOURCE_REPORT,
                )
            )
            with get_client().with_span(req):
                return fn(*args, **kwargs)

        return wrapper  # type: ignore[return-value]

    return decorate


def kave_budget(*, agent: str | None = None) -> Callable[[F], F]:
    def decorate(fn: F) -> F:
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            ctx = resolve_runtime_context(agent)
            get_client().control.GetBudget(budget_pb2.GetBudgetRequest(agent_id=ctx.agent_id))
            return fn(*args, **kwargs)

        return wrapper  # type: ignore[return-value]

    return decorate


def kave_user_agent(*, auto_create: bool = True) -> Callable[[F], F]:
    def decorate(fn: F) -> F:
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            request = args[0] if args else None
            user_key = getattr(request, "kave_user_key", None) if request is not None else None
            if user_key and auto_create:
                UserAgentManager(client=get_client()).ensure_user_agent(str(user_key))
            return fn(*args, **kwargs)

        return wrapper  # type: ignore[return-value]

    return decorate
