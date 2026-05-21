from __future__ import annotations

from collections.abc import Iterable

Metadata = Iterable[tuple[str, str]] | None


def inject_traceparent(metadata: Metadata) -> list[tuple[str, str]]:
    out = list(metadata or [])
    try:
        from opentelemetry.propagate import inject  # type: ignore[import-not-found]
    except Exception:
        return out
    carrier: dict[str, str] = {}
    inject(carrier)
    for key, value in carrier.items():
        out.append((key.lower(), value))
    return out
