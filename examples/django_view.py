from rest_framework.decorators import api_view
from rest_framework.response import Response

from kave.contrib.django.decorators import kave_span


@api_view(["POST"])
@kave_span("chat.completion", agent="maktab-chat")
def ask(request):
    return Response({"answer": "route your LLM call through the Kave proxy here"})
