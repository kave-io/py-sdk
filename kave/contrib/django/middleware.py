from __future__ import annotations

import uuid

from kave.contrib.django.settings import load_settings
from kave.contrib.django.tenant import agent_name_for_user


def _resolve_user_key(request) -> str | None:
    explicit = request.headers.get("X-Kave-User") or request.headers.get("X-User-ID")
    if explicit:
        return str(explicit)
    user = getattr(request, "user", None)
    if user is None or not getattr(user, "is_authenticated", False):
        return None
    for key in ("pk", "id", "uuid", "username", "email"):
        value = getattr(user, key, None)
        if value:
            return str(value)
    return None


class KaveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        cfg = load_settings()
        request.kave_request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
        request.kave_user_key = _resolve_user_key(request)
        if request.headers.get("X-Kave-Agent"):
            request.kave_agent = request.headers["X-Kave-Agent"]
        elif request.kave_user_key:
            request.kave_agent = agent_name_for_user(request.kave_user_key, prefix=cfg.user_agent_prefix)
        else:
            request.kave_agent = cfg.default_agent
        response = self.get_response(request)
        response["X-Request-ID"] = request.kave_request_id
        if request.kave_user_key:
            response["X-Kave-User"] = request.kave_user_key
            response["X-Kave-Agent"] = request.kave_agent
        return response
