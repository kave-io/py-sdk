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
}
```

Use `@kave_span("chat.completion", agent="maktab-chat")` around synchronous
view or service functions that should create Kave spans.
