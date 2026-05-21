import importlib.util

import pytest


pytestmark = pytest.mark.skipif(importlib.util.find_spec("django") is None, reason="django not installed")


def test_django_contrib_imports():
    from kave.contrib.django.decorators import kave_budget, kave_span

    assert callable(kave_span)
    assert callable(kave_budget)
