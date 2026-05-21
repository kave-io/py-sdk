from __future__ import annotations

try:
    from django.conf import settings as django_settings
    from django.core.management.base import BaseCommand
except Exception:  # pragma: no cover
    BaseCommand = object  # type: ignore[misc,assignment]
    django_settings = None

from kave.common.v1 import common_pb2
from kave.control.v1 import budget_pb2, control_pb2, environment_pb2, policy_pb2
from kave.contrib.django.client import get_client, resolve_runtime_context
from kave.contrib.django.settings import load_settings


class Command(BaseCommand):
    help = "Reconcile Django application resources into Kave."

    def handle(self, *args, **options):
        cfg = load_settings()
        client = get_client()
        org = client.ensure_organization(control_pb2.CreateOrganizationRequest(name=cfg.org_slug, slug=cfg.org_slug))
        project = client.ensure_project(control_pb2.CreateProjectRequest(org_id=org.id, name=cfg.project_slug, slug=cfg.project_slug))
        env = client.ensure_environment(
            control_pb2.CreateEnvironmentRequest(
                project_id=project.id,
                name=cfg.environment,
                slug=cfg.environment,
                type=environment_pb2.ENVIRONMENT_TYPE_DEV,
            )
        )
        policy = client.ensure_policy(
            control_pb2.CreatePolicyRequest(
                env_id=env.id,
                name="maktab-default",
                description="Maktab default LLM policy",
                mode=policy_pb2.POLICY_MODE_ENFORCE,
            )
        )
        agent = client.ensure_agent(
            control_pb2.CreateAgentRequest(
                env_id=env.id,
                name=cfg.default_agent,
                description="Maktab chat backend",
                policy_id=policy.id,
            )
        )
        client.ensure_budget(
            budget_pb2.CreateBudgetRequest(
                agent_id=agent.id,
                hard_cap=common_pb2.Amount(decimal=cfg.monthly_hard_cap, currency=cfg.currency),
                soft_cap=common_pb2.Amount(decimal=cfg.monthly_soft_cap, currency=cfg.currency),
                period=policy_pb2.BUDGET_PERIOD_MONTHLY,
            )
        )
        api_key = getattr(django_settings, "GAPGPT_API_KEY", "") if django_settings is not None else ""
        if api_key:
            client.ensure_credential(
                control_pb2.CreateCredentialRequest(
                    env_id=env.id,
                    connector_type="openai",
                    label="gapgpt",
                    encrypted_blob=api_key.encode("utf-8"),
                )
            )
        resolve_runtime_context.cache_clear()
        self.stdout.write(self.style.SUCCESS("Kave resources reconciled"))
