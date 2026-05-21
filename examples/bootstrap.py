from kave import SyncClient
from kave.common.v1 import common_pb2
from kave.control.v1 import budget_pb2, control_pb2, environment_pb2, policy_pb2

with SyncClient("localhost:19090") as kave:
    org = kave.ensure_organization(control_pb2.CreateOrganizationRequest(name="Acme", slug="acme"))
    project = kave.ensure_project(control_pb2.CreateProjectRequest(org_id=org.id, name="Demo", slug="demo"))
    env = kave.ensure_environment(
        control_pb2.CreateEnvironmentRequest(
            project_id=project.id,
            name="development",
            slug="development",
            type=environment_pb2.ENVIRONMENT_TYPE_DEV,
        )
    )
    policy = kave.ensure_policy(
        control_pb2.CreatePolicyRequest(env_id=env.id, name="default", mode=policy_pb2.POLICY_MODE_ENFORCE)
    )
    agent = kave.ensure_agent(control_pb2.CreateAgentRequest(env_id=env.id, name="demo-agent", policy_id=policy.id))
    kave.ensure_budget(
        budget_pb2.CreateBudgetRequest(
            agent_id=agent.id,
            hard_cap=common_pb2.Amount(decimal="100.00", currency="USD"),
            soft_cap=common_pb2.Amount(decimal="80.00", currency="USD"),
            period=policy_pb2.BUDGET_PERIOD_MONTHLY,
        )
    )
    token = kave.create_agent_token(control_pb2.CreateTokenRequest(agent_id=agent.id, name="quickstart"))
    print(token.raw_token)
