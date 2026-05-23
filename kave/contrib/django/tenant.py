from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from decimal import Decimal
from typing import Any

from google.protobuf.struct_pb2 import Struct

from kave.common.v1 import common_pb2
from kave.contrib.django.client import RuntimeContext, get_client
from kave.contrib.django.settings import KaveDjangoSettings, load_settings
from kave.control.v1 import budget_pb2, control_pb2, environment_pb2, policy_pb2
from kave.runtime.v1 import run_pb2, runtime_pb2

_SAFE_CHARS = re.compile(r"[^a-z0-9-]+")


def _slug(value: str) -> str:
    out = value.strip().lower().replace("_", "-").replace(" ", "-")
    out = _SAFE_CHARS.sub("-", out)
    out = out.strip("-")
    return out or "unknown"


def agent_name_for_user(user_key: str, prefix: str = "user", max_len: int = 63) -> str:
    base = f"{_slug(prefix)}-{_slug(user_key)}"
    if len(base) <= max_len:
        return base
    digest = hashlib.sha1(user_key.encode("utf-8")).hexdigest()[:10]
    head = base[: max_len - 11].rstrip("-")
    return f"{head}-{digest}"


def _amount(decimal_value: str, currency: str) -> common_pb2.Amount:
    return common_pb2.Amount(decimal=str(decimal_value), currency=currency)


def _to_decimal(raw: str) -> Decimal:
    return Decimal(str(raw))


@dataclass(frozen=True)
class UserAgentContext:
    user_key: str
    agent_name: str
    runtime: RuntimeContext


class UserAgentManager:
    def __init__(self, *, client: Any | None = None, settings: KaveDjangoSettings | None = None) -> None:
        self.client = client or get_client()
        self.settings = settings or load_settings()

    def ensure_user_agent(
        self,
        user_key: str,
        *,
        hard_cap: str | None = None,
        soft_cap: str | None = None,
        currency: str | None = None,
        period: int = policy_pb2.BUDGET_PERIOD_MONTHLY,
    ) -> UserAgentContext:
        scope = self._resolve_scope()
        policy = self.client.ensure_policy(
            control_pb2.CreatePolicyRequest(
                env_id=scope["env"].id,
                name=self.settings.user_policy_name,
                description=self.settings.user_policy_description,
                mode=policy_pb2.POLICY_MODE_ENFORCE,
            )
        )
        agent_name = agent_name_for_user(user_key, prefix=self.settings.user_agent_prefix)
        agent = self.client.ensure_agent(
            control_pb2.CreateAgentRequest(
                env_id=scope["env"].id,
                name=agent_name,
                description=f"Isolated runtime agent for user {user_key}",
                policy_id=policy.id,
            )
        )
        money = currency or self.settings.currency
        self.client.ensure_budget(
            budget_pb2.CreateBudgetRequest(
                agent_id=agent.id,
                hard_cap=_amount(hard_cap or self.settings.monthly_hard_cap, money),
                soft_cap=_amount(soft_cap or self.settings.monthly_soft_cap, money),
                period=period,
            )
        )
        return UserAgentContext(
            user_key=str(user_key),
            agent_name=agent_name,
            runtime=RuntimeContext(
                project_id=scope["project"].id,
                env_id=scope["env"].id,
                agent_id=agent.id,
                policy_id=policy.id,
            ),
        )

    def set_user_budget(
        self,
        user_key: str,
        *,
        hard_cap: str,
        soft_cap: str | None = None,
        currency: str | None = None,
        period: int = policy_pb2.BUDGET_PERIOD_MONTHLY,
    ):
        ctx = self.ensure_user_agent(user_key, currency=currency, period=period)
        money = currency or self.settings.currency
        return self.client.ensure_budget(
            budget_pb2.CreateBudgetRequest(
                agent_id=ctx.runtime.agent_id,
                hard_cap=_amount(hard_cap, money),
                soft_cap=_amount(soft_cap if soft_cap is not None else hard_cap, money),
                period=period,
            )
        )

    def top_up_user_budget(
        self,
        user_key: str,
        *,
        hard_cap_delta: str,
        soft_cap_delta: str | None = None,
        currency: str | None = None,
    ):
        ctx = self.ensure_user_agent(user_key, currency=currency)
        money = currency or self.settings.currency
        current = self.client.control.GetBudget(budget_pb2.GetBudgetRequest(agent_id=ctx.runtime.agent_id))
        hard = _to_decimal(current.hard_cap.decimal) + _to_decimal(hard_cap_delta)
        soft_base = _to_decimal(current.soft_cap.decimal if current.HasField("soft_cap") else current.hard_cap.decimal)
        soft = soft_base + _to_decimal(soft_cap_delta or hard_cap_delta)
        return self.client.ensure_budget(
            budget_pb2.CreateBudgetRequest(
                agent_id=ctx.runtime.agent_id,
                hard_cap=_amount(str(hard), money),
                soft_cap=_amount(str(soft), money),
                period=current.period,
            )
        )

    def report_usage(
        self,
        user_key: str,
        *,
        spent_decimal: str,
        currency: str | None = None,
        run_name: str = "django.request",
        correlation_id: str | None = None,
        status: int = run_pb2.RUN_STATUS_COMPLETED,
        metadata: dict[str, Any] | None = None,
    ):
        ctx = self.ensure_user_agent(user_key, currency=currency)
        run = self.client.create_run(
            runtime_pb2.CreateRunRequest(
                project_id=ctx.runtime.project_id,
                env_id=ctx.runtime.env_id,
                agent_id=ctx.runtime.agent_id,
                policy_id=ctx.runtime.policy_id,
                name=run_name,
                trigger_type=run_pb2.TRIGGER_TYPE_API,
                correlation_id=correlation_id or "",
            )
        )
        run_meta = Struct()
        if metadata:
            run_meta.update(metadata)
        run_meta.update({"user_key": str(user_key), "agent_name": ctx.agent_name})
        return self.client.update_run(
            runtime_pb2.UpdateRunRequest(
                id=run.id,
                update=run_pb2.RunUpdate(
                    status=status,
                    spent=_amount(spent_decimal, currency or self.settings.currency),
                    metadata=run_meta,
                ),
            )
        )

    def encode_span_attrs(self, payload: dict[str, Any]) -> bytes:
        return json.dumps(payload, separators=(",", ":"), ensure_ascii=True).encode("utf-8")

    def _resolve_scope(self) -> dict[str, Any]:
        org = next(
            (item for item in self.client.iter_organizations() if item.slug == self.settings.org_slug or item.name == self.settings.org_slug),
            None,
        )
        if org is None:
            org = self.client.ensure_organization(
                control_pb2.CreateOrganizationRequest(name=self.settings.org_slug, slug=self.settings.org_slug)
            )
        project = next(
            (item for item in self.client.iter_projects(org.id) if item.slug == self.settings.project_slug or item.name == self.settings.project_slug),
            None,
        )
        if project is None:
            project = self.client.ensure_project(
                control_pb2.CreateProjectRequest(org_id=org.id, name=self.settings.project_slug, slug=self.settings.project_slug)
            )
        env = next(
            (item for item in self.client.iter_environments(project.id) if item.slug == self.settings.environment or item.name == self.settings.environment),
            None,
        )
        if env is None:
            env = self.client.ensure_environment(
                control_pb2.CreateEnvironmentRequest(
                    project_id=project.id,
                    name=self.settings.environment,
                    slug=self.settings.environment,
                    type=environment_pb2.ENVIRONMENT_TYPE_DEV,
                )
            )
        return {"org": org, "project": project, "env": env}
