# Kave Django

Add `kave.contrib.django` to `INSTALLED_APPS`, configure the `KAVE` setting,
and run `python manage.py kave_reconcile` on deploy.

```python
KAVE = {
    "ADDR": env("KAVE_ADDR", default="kave:19090"),
    "TOKEN": env("KAVE_TOKEN", default=None),
    "DEFAULT_AGENT": "maktab-chat",
    "PROJECT_SLUG": "maktab",
    "ENVIRONMENT": env("KAVE_ENV", default="development"),
    "USER_AGENT_PREFIX": "user",
    "USER_POLICY_NAME": "django-user-default",
}
```

Use `@kave_span("chat.completion", agent="maktab-chat")` around synchronous
view or service functions that should create Kave spans.

Per-user isolation and cap lifecycle:

```python
from kave.contrib.django.tenant import UserAgentManager

manager = UserAgentManager()
ctx = manager.ensure_user_agent("user_42")
manager.top_up_user_budget("user_42", hard_cap_delta="5.00")
manager.report_usage("user_42", spent_decimal="0.12", correlation_id="req_123")
```
