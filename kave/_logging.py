from __future__ import annotations

import logging
import time
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def rpc_timer(logger: logging.Logger | None, rpc: str, request_id: str) -> Iterator[None]:
    if logger is None:
        yield
        return
    started = time.perf_counter()
    status = "OK"
    try:
        yield
    except Exception as exc:
        status = getattr(getattr(exc, "code", None), "value", exc.__class__.__name__)
        raise
    finally:
        logger.debug(
            "kave rpc",
            extra={
                "request_id": request_id,
                "rpc": rpc,
                "latency_ms": round((time.perf_counter() - started) * 1000, 2),
                "status": status,
            },
        )
