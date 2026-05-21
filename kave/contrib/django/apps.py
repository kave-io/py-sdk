from __future__ import annotations

try:
    from django.apps import AppConfig
except Exception:  # pragma: no cover
    AppConfig = object  # type: ignore[misc,assignment]


class KaveDjangoConfig(AppConfig):
    name = "kave.contrib.django"
    label = "kave_django"
    verbose_name = "Kave Django"

    def ready(self) -> None:
        from kave.contrib.django.client import get_client

        get_client()
