from __future__ import annotations

import uuid

from kave.contrib.django.settings import load_settings


class KaveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        cfg = load_settings()
        request.kave_request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
        request.kave_agent = request.headers.get("X-Kave-Agent") or cfg.default_agent
        response = self.get_response(request)
        response["X-Request-ID"] = request.kave_request_id
        return response
