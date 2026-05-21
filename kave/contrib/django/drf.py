from __future__ import annotations

from kave.contrib.django.decorators import kave_budget

try:
    from rest_framework.permissions import BasePermission
    from rest_framework.throttling import BaseThrottle
except Exception:  # pragma: no cover
    BasePermission = object  # type: ignore[misc,assignment]
    BaseThrottle = object  # type: ignore[misc,assignment]


class KaveBudgetPermission(BasePermission):
    message = "kave_budget_unavailable"

    def has_permission(self, request, view) -> bool:
        agent = getattr(request, "kave_agent", None)
        kave_budget(agent=agent)(lambda: None)()
        return True


class KaveBudgetThrottle(BaseThrottle):
    def allow_request(self, request, view) -> bool:
        agent = getattr(request, "kave_agent", None)
        kave_budget(agent=agent)(lambda: None)()
        return True

    def wait(self):
        return None
