from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class KaveDjangoSettings:
    addr: str = "kave:19090"
    token: str | None = None
    tls: bool = False
    default_agent: str = "default"
    org_slug: str = "maktab"
    project_slug: str = "maktab"
    environment: str = "development"
    monthly_hard_cap: str = "100.00"
    monthly_soft_cap: str = "80.00"
    currency: str = "USD"
    llm_proxy_base_url: str = "http://kave:18081/v1"
    user_agent_prefix: str = "user"
    user_policy_name: str = "django-user-default"
    user_policy_description: str = "Django per-user default policy"


def load_settings() -> KaveDjangoSettings:
    from django.conf import settings

    raw = getattr(settings, "KAVE", {}) or {}
    return KaveDjangoSettings(
        addr=raw.get("ADDR", "kave:19090"),
        token=raw.get("TOKEN"),
        tls=bool(raw.get("TLS", False)),
        default_agent=raw.get("DEFAULT_AGENT", "default"),
        org_slug=raw.get("ORG_SLUG", raw.get("PROJECT_SLUG", "maktab")),
        project_slug=raw.get("PROJECT_SLUG", "maktab"),
        environment=raw.get("ENVIRONMENT", "development"),
        monthly_hard_cap=str(raw.get("MONTHLY_HARD_CAP", "100.00")),
        monthly_soft_cap=str(raw.get("MONTHLY_SOFT_CAP", "80.00")),
        currency=raw.get("CURRENCY", "USD"),
        llm_proxy_base_url=raw.get("LLM_PROXY_BASE_URL", "http://kave:18081/v1"),
        user_agent_prefix=raw.get("USER_AGENT_PREFIX", "user"),
        user_policy_name=raw.get("USER_POLICY_NAME", "django-user-default"),
        user_policy_description=raw.get("USER_POLICY_DESCRIPTION", "Django per-user default policy"),
    )
