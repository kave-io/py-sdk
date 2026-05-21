from __future__ import annotations

import asyncio
import random
import time
from dataclasses import dataclass
from typing import Awaitable, Callable, TypeVar

from kave.errors import is_deadline_exceeded, is_unavailable

T = TypeVar("T")


@dataclass(frozen=True)
class RetryPolicy:
    max_attempts: int = 3
    base_ms: float = 200.0
    cap_ms: float = 5000.0
    jitter_fraction: float = 0.2


DEFAULT_RETRY_POLICY = RetryPolicy()
NO_RETRY = RetryPolicy(max_attempts=1)


def normalize_retry_policy(policy: RetryPolicy | None) -> RetryPolicy:
    if policy is None:
        return DEFAULT_RETRY_POLICY
    if policy.max_attempts <= 0:
        return NO_RETRY
    return RetryPolicy(
        max_attempts=policy.max_attempts,
        base_ms=policy.base_ms if policy.base_ms > 0 else DEFAULT_RETRY_POLICY.base_ms,
        cap_ms=policy.cap_ms if policy.cap_ms > 0 else DEFAULT_RETRY_POLICY.cap_ms,
        jitter_fraction=max(0.0, policy.jitter_fraction),
    )


def is_retriable(err: BaseException) -> bool:
    return is_unavailable(err) or is_deadline_exceeded(err)


def should_retry_rpc(rpc_name: str) -> bool:
    short = rpc_name.rsplit("/", 1)[-1].split(".")[-1]
    return short.startswith(("List", "Get", "Watch"))


def backoff_ms(policy: RetryPolicy, attempt: int) -> float:
    policy = normalize_retry_policy(policy)
    delay = min(policy.base_ms * (2**attempt), policy.cap_ms)
    jitter = delay * policy.jitter_fraction * (random.random() * 2 - 1)
    return max(0.0, delay + jitter)


def retry_sync(policy: RetryPolicy, fn: Callable[[], T]) -> T:
    policy = normalize_retry_policy(policy)
    last_err: BaseException | None = None
    for attempt in range(policy.max_attempts):
        try:
            return fn()
        except Exception as err:
            last_err = err
            if not is_retriable(err) or attempt == policy.max_attempts - 1:
                raise
            time.sleep(backoff_ms(policy, attempt) / 1000.0)
    raise last_err  # type: ignore[misc]


async def retry_async(policy: RetryPolicy, fn: Callable[[], Awaitable[T]]) -> T:
    policy = normalize_retry_policy(policy)
    last_err: BaseException | None = None
    for attempt in range(policy.max_attempts):
        try:
            return await fn()
        except Exception as err:
            last_err = err
            if not is_retriable(err) or attempt == policy.max_attempts - 1:
                raise
            await asyncio.sleep(backoff_ms(policy, attempt) / 1000.0)
    raise last_err  # type: ignore[misc]
