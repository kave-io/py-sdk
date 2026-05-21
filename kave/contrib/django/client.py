from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

from kave import SyncClient
from kave.control.v1 import control_pb2
from kave.contrib.django.settings import load_settings

_client: SyncClient | None = None


@dataclass(frozen=True)
class RuntimeContext:
    project_id: str
    env_id: str
    agent_id: str
    policy_id: str = ""


def get_client() -> SyncClient:
    global _client
    if _client is None:
        cfg = load_settings()
        _client = SyncClient(addr=cfg.addr, token=cfg.token, tls=cfg.tls)
    return _client


def reset_client() -> None:
    global _client
    if _client is not None:
        _client.close()
    _client = None
    resolve_runtime_context.cache_clear()


@lru_cache(maxsize=128)
def resolve_runtime_context(agent: str | None = None) -> RuntimeContext:
    cfg = load_settings()
    client = get_client()
    agent_name = agent or cfg.default_agent

    org = next((item for item in client.iter_organizations() if item.slug == cfg.org_slug or item.name == cfg.org_slug), None)
    if org is None:
        raise RuntimeError(f"Kave organization not found: {cfg.org_slug}")
    project = next((item for item in client.iter_projects(org.id) if item.slug == cfg.project_slug or item.name == cfg.project_slug), None)
    if project is None:
        raise RuntimeError(f"Kave project not found: {cfg.project_slug}")
    env = next((item for item in client.iter_environments(project.id) if item.slug == cfg.environment or item.name == cfg.environment), None)
    if env is None:
        raise RuntimeError(f"Kave environment not found: {cfg.environment}")
    kave_agent = next((item for item in client.iter_agents(env.id) if item.name == agent_name), None)
    if kave_agent is None:
        raise RuntimeError(f"Kave agent not found: {agent_name}")
    return RuntimeContext(project_id=project.id, env_id=env.id, agent_id=kave_agent.id, policy_id=kave_agent.policy_id)


def issue_agent_token(agent: str | None = None, name: str = "django-runtime") -> str:
    ctx = resolve_runtime_context(agent)
    resp = get_client().create_agent_token(control_pb2.CreateTokenRequest(agent_id=ctx.agent_id, name=name))
    return resp.raw_token
