from __future__ import annotations

from kave.contrib.django.decorators import kave_budget
from kave.contrib.django.tenant import UserAgentManager

try:
    from rest_framework.permissions import BasePermission
    from rest_framework.throttling import BaseThrottle
except Exception:  # pragma: no cover
    BasePermission = object  # type: ignore[misc,assignment]
    BaseThrottle = object  # type: ignore[misc,assignment]


class KaveBudgetPermission(BasePermission):
    message = "kave_budget_unavailable"

    def has_permission(self, request, view) -> bool:
        user_key = getattr(request, "kave_user_key", None)
        if user_key:
            UserAgentManager().ensure_user_agent(str(user_key))
        agent = getattr(request, "kave_agent", None)
        kave_budget(agent=agent)(lambda: None)()
        return True


class KaveBudgetThrottle(BaseThrottle):
    def allow_request(self, request, view) -> bool:
        user_key = getattr(request, "kave_user_key", None)
        if user_key:
            UserAgentManager().ensure_user_agent(str(user_key))
        agent = getattr(request, "kave_agent", None)
        kave_budget(agent=agent)(lambda: None)()
        return True

    def wait(self):
        return None
