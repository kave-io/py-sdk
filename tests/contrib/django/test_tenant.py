from __future__ import annotations

from types import SimpleNamespace

from kave.common.v1 import common_pb2
from kave.contrib.django.settings import KaveDjangoSettings
from kave.contrib.django.tenant import UserAgentManager, agent_name_for_user
from kave.control.v1 import budget_pb2


def test_agent_name_for_user_is_stable_and_bounded():
    name = agent_name_for_user("USER_ABC_123", prefix="Tenant User")
    assert name.startswith("tenant-user-user-abc-123")
    assert len(name) <= 63


class _FakeClient:
    def __init__(self):
        self._budget = budget_pb2.Budget(
            agent_id="agent_1",
            hard_cap=common_pb2.Amount(decimal="10.00", currency="USD"),
            soft_cap=common_pb2.Amount(decimal="8.00", currency="USD"),
            period=1,
        )
        self.control = SimpleNamespace(GetBudget=self._get_budget)

    def _get_budget(self, req):
        assert req.agent_id == "agent_1"
        return self._budget

    def ensure_budget(self, req):
        self._budget = budget_pb2.Budget(
            agent_id=req.agent_id,
            hard_cap=req.hard_cap,
            soft_cap=req.soft_cap,
            period=req.period,
        )
        return self._budget


def test_top_up_user_budget_adds_to_existing_budget():
    client = _FakeClient()
    settings = KaveDjangoSettings()
    manager = UserAgentManager(client=client, settings=settings)
    manager.ensure_user_agent = lambda *_args, **_kwargs: SimpleNamespace(runtime=SimpleNamespace(agent_id="agent_1"))  # type: ignore[method-assign]

    updated = manager.top_up_user_budget("user_1", hard_cap_delta="2.50", soft_cap_delta="1.25")

    assert updated.hard_cap.decimal == "12.50"
    assert updated.soft_cap.decimal == "9.25"
