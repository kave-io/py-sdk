from rest_framework.decorators import api_view
from rest_framework.response import Response

from kave.contrib.django.decorators import kave_span, kave_user_agent
from kave.contrib.django.tenant import UserAgentManager


@api_view(["POST"])
@kave_user_agent()
@kave_span("chat.completion", agent="maktab-chat")
def ask(request):
    if getattr(request, "kave_user_key", None):
        UserAgentManager().report_usage(request.kave_user_key, spent_decimal="0.01", correlation_id=request.kave_request_id)
    return Response({"answer": "route your LLM call through the Kave proxy here"})
