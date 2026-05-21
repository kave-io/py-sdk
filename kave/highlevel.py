from __future__ import annotations

from contextlib import asynccontextmanager
from typing import Any, AsyncIterator, Iterator

from google.protobuf.empty_pb2 import Empty

from kave.control.v1 import control_pb2, credential_pb2, rbac_pb2
from kave.control.v1 import budget_pb2
from kave.errors import is_not_found, wrap_error
from kave.runtime.v1 import runtime_pb2, span_pb2

DEFAULT_PAGE_SIZE = 100


def _same_amount(a: Any, b: Any) -> bool:
    if a is None or b is None:
        return a is b
    return getattr(a, "currency", "") == getattr(b, "currency", "") and getattr(a, "decimal", "") == getattr(b, "decimal", "")


def _same_budget(existing: Any, desired: budget_pb2.CreateBudgetRequest) -> bool:
    return (
        existing is not None
        and existing.period == desired.period
        and _same_amount(existing.hard_cap, desired.hard_cap)
        and _same_amount(existing.soft_cap, desired.soft_cap)
    )


class WithSpan:
    def __init__(self, client: Any, request: runtime_pb2.OpenSpanRequest) -> None:
        self.client = client
        self.request = request
        self.span = None

    def __enter__(self) -> Any:
        self.span = self.client.open_span(self.request)
        return self.span

    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: Any) -> bool:
        if self.span is None:
            return False
        end = span_pb2.SpanEnd()
        if exc is not None:
            end.error = str(exc)
        self.client.close_span(runtime_pb2.CloseSpanRequest(span_id=self.span.id, end=end))
        return False


class SyncHighLevelMixin:
    def ensure_organization(self, req: control_pb2.CreateOrganizationRequest):
        for org in self._list_all_organizations():
            if org.slug == req.slug or org.name == req.name:
                return org
        return self.control.CreateOrganization(req)

    def ensure_project(self, req: control_pb2.CreateProjectRequest):
        for project in self._list_all_projects(req.org_id):
            if project.slug == req.slug or project.name == req.name:
                return project
        return self.control.CreateProject(req)

    def ensure_environment(self, req: control_pb2.CreateEnvironmentRequest):
        for env in self._list_all_environments(req.project_id):
            if env.slug == req.slug or env.name == req.name:
                return env
        return self.control.CreateEnvironment(req)

    def ensure_agent(self, req: control_pb2.CreateAgentRequest):
        for agent in self._list_all_agents(req.env_id):
            if agent.name == req.name:
                return agent
        return self.control.CreateAgent(req)

    def ensure_policy(self, req: control_pb2.CreatePolicyRequest):
        for policy in self._list_all_policies(req.env_id):
            if policy.name == req.name:
                return policy
        return self.control.CreatePolicy(req)

    def ensure_budget(self, req: budget_pb2.CreateBudgetRequest):
        try:
            current = self.control.GetBudget(budget_pb2.GetBudgetRequest(agent_id=req.agent_id))
            if _same_budget(current, req):
                return current
            self.control.DeleteBudget(budget_pb2.DeleteBudgetRequest(agent_id=req.agent_id))
        except Exception as err:
            if not is_not_found(err):
                raise wrap_error(err) from err
        return self.control.CreateBudget(req)

    def ensure_credential(self, req: control_pb2.CreateCredentialRequest):
        resp = self.control.ListCredentials(
            control_pb2.ListCredentialsRequest(
                filter=credential_pb2.CredentialFilter(
                    env_id=req.env_id,
                    connector_type=req.connector_type,
                    label=req.label,
                ),
                limit=1,
            )
        )
        if resp.credentials:
            return resp.credentials[0]
        return self.control.CreateCredential(req)

    def ensure_rbac_binding(self, req: rbac_pb2.CreateBindingRequest):
        resp = self.rbac.ListBindings(Empty())
        for binding in resp.bindings:
            if binding.role_id == req.role_id and binding.subject == req.subject and binding.scope == req.scope:
                return binding
        return self.rbac.CreateBinding(req)

    def create_agent_token(self, req: control_pb2.CreateTokenRequest):
        return self.control.CreateToken(req)

    def create_run(self, req: runtime_pb2.CreateRunRequest):
        return self.runtime.CreateRun(req)

    def update_run(self, req: runtime_pb2.UpdateRunRequest):
        return self.runtime.UpdateRun(req)

    def create_action(self, req: runtime_pb2.CreateActionRequest):
        return self.runtime.CreateAction(req)

    def open_span(self, req: runtime_pb2.OpenSpanRequest):
        return self.runtime.OpenSpan(req)

    def close_span(self, req: runtime_pb2.CloseSpanRequest):
        return self.runtime.CloseSpan(req)

    def with_span(self, req: runtime_pb2.OpenSpanRequest) -> WithSpan:
        return WithSpan(self, req)

    def _list_all_organizations(self):
        cursor = ""
        while True:
            resp = self.control.ListOrganizations(control_pb2.ListOrganizationsRequest(limit=DEFAULT_PAGE_SIZE, cursor=cursor))
            yield from resp.organizations
            cursor = resp.next_cursor
            if not cursor:
                return

    def _list_all_projects(self, org_id: str):
        if not org_id:
            raise ValueError("org_id is required")
        cursor = ""
        while True:
            resp = self.control.ListProjects(control_pb2.ListProjectsRequest(org_id=org_id, limit=DEFAULT_PAGE_SIZE, cursor=cursor))
            yield from resp.projects
            cursor = resp.next_cursor
            if not cursor:
                return

    def _list_all_environments(self, project_id: str):
        if not project_id:
            raise ValueError("project_id is required")
        cursor = ""
        while True:
            resp = self.control.ListEnvironments(control_pb2.ListEnvironmentsRequest(project_id=project_id, limit=DEFAULT_PAGE_SIZE, cursor=cursor))
            yield from resp.environments
            cursor = resp.next_cursor
            if not cursor:
                return

    def _list_all_agents(self, env_id: str):
        if not env_id:
            raise ValueError("env_id is required")
        cursor = ""
        while True:
            resp = self.control.ListAgents(control_pb2.ListAgentsRequest(env_id=env_id, limit=DEFAULT_PAGE_SIZE, cursor=cursor))
            yield from resp.agents
            cursor = resp.next_cursor
            if not cursor:
                return

    def _list_all_policies(self, env_id: str):
        if not env_id:
            raise ValueError("env_id is required")
        cursor = ""
        while True:
            resp = self.control.ListPolicies(control_pb2.ListPoliciesRequest(env_id=env_id, limit=DEFAULT_PAGE_SIZE, cursor=cursor))
            yield from resp.policies
            cursor = resp.next_cursor
            if not cursor:
                return


class AsyncHighLevelMixin:
    async def ensure_organization(self, req: control_pb2.CreateOrganizationRequest):
        async for org in self._list_all_organizations():
            if org.slug == req.slug or org.name == req.name:
                return org
        return await self.control.CreateOrganization(req)

    async def ensure_project(self, req: control_pb2.CreateProjectRequest):
        async for project in self._list_all_projects(req.org_id):
            if project.slug == req.slug or project.name == req.name:
                return project
        return await self.control.CreateProject(req)

    async def ensure_environment(self, req: control_pb2.CreateEnvironmentRequest):
        async for env in self._list_all_environments(req.project_id):
            if env.slug == req.slug or env.name == req.name:
                return env
        return await self.control.CreateEnvironment(req)

    async def ensure_agent(self, req: control_pb2.CreateAgentRequest):
        async for agent in self._list_all_agents(req.env_id):
            if agent.name == req.name:
                return agent
        return await self.control.CreateAgent(req)

    async def ensure_policy(self, req: control_pb2.CreatePolicyRequest):
        async for policy in self._list_all_policies(req.env_id):
            if policy.name == req.name:
                return policy
        return await self.control.CreatePolicy(req)

    async def ensure_budget(self, req: budget_pb2.CreateBudgetRequest):
        try:
            current = await self.control.GetBudget(budget_pb2.GetBudgetRequest(agent_id=req.agent_id))
            if _same_budget(current, req):
                return current
            await self.control.DeleteBudget(budget_pb2.DeleteBudgetRequest(agent_id=req.agent_id))
        except Exception as err:
            if not is_not_found(err):
                raise wrap_error(err) from err
        return await self.control.CreateBudget(req)

    async def ensure_credential(self, req: control_pb2.CreateCredentialRequest):
        resp = await self.control.ListCredentials(
            control_pb2.ListCredentialsRequest(
                filter=credential_pb2.CredentialFilter(
                    env_id=req.env_id,
                    connector_type=req.connector_type,
                    label=req.label,
                ),
                limit=1,
            )
        )
        if resp.credentials:
            return resp.credentials[0]
        return await self.control.CreateCredential(req)

    async def ensure_rbac_binding(self, req: rbac_pb2.CreateBindingRequest):
        resp = await self.rbac.ListBindings(Empty())
        for binding in resp.bindings:
            if binding.role_id == req.role_id and binding.subject == req.subject and binding.scope == req.scope:
                return binding
        return await self.rbac.CreateBinding(req)

    async def create_agent_token(self, req: control_pb2.CreateTokenRequest):
        return await self.control.CreateToken(req)

    async def create_run(self, req: runtime_pb2.CreateRunRequest):
        return await self.runtime.CreateRun(req)

    async def update_run(self, req: runtime_pb2.UpdateRunRequest):
        return await self.runtime.UpdateRun(req)

    async def create_action(self, req: runtime_pb2.CreateActionRequest):
        return await self.runtime.CreateAction(req)

    async def open_span(self, req: runtime_pb2.OpenSpanRequest):
        return await self.runtime.OpenSpan(req)

    async def close_span(self, req: runtime_pb2.CloseSpanRequest):
        return await self.runtime.CloseSpan(req)

    @asynccontextmanager
    async def with_span(self, req: runtime_pb2.OpenSpanRequest) -> AsyncIterator[Any]:
        span = await self.open_span(req)
        try:
            yield span
        except Exception as exc:
            await self.close_span(runtime_pb2.CloseSpanRequest(span_id=span.id, end=span_pb2.SpanEnd(error=str(exc))))
            raise
        else:
            await self.close_span(runtime_pb2.CloseSpanRequest(span_id=span.id, end=span_pb2.SpanEnd()))

    async def _list_all_organizations(self):
        cursor = ""
        while True:
            resp = await self.control.ListOrganizations(control_pb2.ListOrganizationsRequest(limit=DEFAULT_PAGE_SIZE, cursor=cursor))
            for org in resp.organizations:
                yield org
            cursor = resp.next_cursor
            if not cursor:
                return

    async def _list_all_projects(self, org_id: str):
        if not org_id:
            raise ValueError("org_id is required")
        cursor = ""
        while True:
            resp = await self.control.ListProjects(control_pb2.ListProjectsRequest(org_id=org_id, limit=DEFAULT_PAGE_SIZE, cursor=cursor))
            for project in resp.projects:
                yield project
            cursor = resp.next_cursor
            if not cursor:
                return

    async def _list_all_environments(self, project_id: str):
        if not project_id:
            raise ValueError("project_id is required")
        cursor = ""
        while True:
            resp = await self.control.ListEnvironments(control_pb2.ListEnvironmentsRequest(project_id=project_id, limit=DEFAULT_PAGE_SIZE, cursor=cursor))
            for env in resp.environments:
                yield env
            cursor = resp.next_cursor
            if not cursor:
                return

    async def _list_all_agents(self, env_id: str):
        if not env_id:
            raise ValueError("env_id is required")
        cursor = ""
        while True:
            resp = await self.control.ListAgents(control_pb2.ListAgentsRequest(env_id=env_id, limit=DEFAULT_PAGE_SIZE, cursor=cursor))
            for agent in resp.agents:
                yield agent
            cursor = resp.next_cursor
            if not cursor:
                return

    async def _list_all_policies(self, env_id: str):
        if not env_id:
            raise ValueError("env_id is required")
        cursor = ""
        while True:
            resp = await self.control.ListPolicies(control_pb2.ListPoliciesRequest(env_id=env_id, limit=DEFAULT_PAGE_SIZE, cursor=cursor))
            for policy in resp.policies:
                yield policy
            cursor = resp.next_cursor
            if not cursor:
                return
