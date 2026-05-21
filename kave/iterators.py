from __future__ import annotations

from typing import Any, AsyncIterator, Callable, Iterator, TypeVar

from kave.control.v1 import control_pb2
from kave.runtime.v1 import runtime_pb2

T = TypeVar("T")
DEFAULT_PAGE_SIZE = 100


def _paginate_sync(list_fn: Callable[[Any], Any], request: Any, item_attr: str, page_size: int = DEFAULT_PAGE_SIZE) -> Iterator[Any]:
    if getattr(request, "limit", 0) == 0:
        request.limit = page_size
    while True:
        resp = list_fn(request)
        yield from getattr(resp, item_attr)
        request.cursor = resp.next_cursor
        if not request.cursor:
            return


async def _paginate_async(list_fn: Callable[[Any], Any], request: Any, item_attr: str, page_size: int = DEFAULT_PAGE_SIZE) -> AsyncIterator[Any]:
    if getattr(request, "limit", 0) == 0:
        request.limit = page_size
    while True:
        resp = await list_fn(request)
        for item in getattr(resp, item_attr):
            yield item
        request.cursor = resp.next_cursor
        if not request.cursor:
            return


class SyncIteratorMixin:
    def iter_organizations(self):
        return _paginate_sync(self.control.ListOrganizations, control_pb2.ListOrganizationsRequest(), "organizations")

    def iter_projects(self, org_id: str):
        return _paginate_sync(self.control.ListProjects, control_pb2.ListProjectsRequest(org_id=org_id), "projects")

    def iter_environments(self, project_id: str):
        return _paginate_sync(self.control.ListEnvironments, control_pb2.ListEnvironmentsRequest(project_id=project_id), "environments")

    def iter_agents(self, env_id: str):
        return _paginate_sync(self.control.ListAgents, control_pb2.ListAgentsRequest(env_id=env_id), "agents")

    def iter_policies(self, env_id: str):
        return _paginate_sync(self.control.ListPolicies, control_pb2.ListPoliciesRequest(env_id=env_id), "policies")

    def iter_tokens(self, agent_id: str):
        return _paginate_sync(self.control.ListTokens, control_pb2.ListTokensRequest(agent_id=agent_id), "tokens")

    def iter_credentials(self, request: control_pb2.ListCredentialsRequest):
        copied = control_pb2.ListCredentialsRequest()
        copied.CopyFrom(request)
        return _paginate_sync(self.control.ListCredentials, copied, "credentials")

    def iter_runs(self, request: runtime_pb2.ListRunsRequest):
        copied = runtime_pb2.ListRunsRequest()
        copied.CopyFrom(request)
        return _paginate_sync(self.runtime.ListRuns, copied, "runs")

    def iter_actions(self, request: runtime_pb2.ListActionsRequest):
        copied = runtime_pb2.ListActionsRequest()
        copied.CopyFrom(request)
        return _paginate_sync(self.runtime.ListActions, copied, "actions")


class AsyncIteratorMixin:
    def aiter_organizations(self):
        return _paginate_async(self.control.ListOrganizations, control_pb2.ListOrganizationsRequest(), "organizations")

    def aiter_projects(self, org_id: str):
        return _paginate_async(self.control.ListProjects, control_pb2.ListProjectsRequest(org_id=org_id), "projects")

    def aiter_environments(self, project_id: str):
        return _paginate_async(self.control.ListEnvironments, control_pb2.ListEnvironmentsRequest(project_id=project_id), "environments")

    def aiter_agents(self, env_id: str):
        return _paginate_async(self.control.ListAgents, control_pb2.ListAgentsRequest(env_id=env_id), "agents")

    def aiter_policies(self, env_id: str):
        return _paginate_async(self.control.ListPolicies, control_pb2.ListPoliciesRequest(env_id=env_id), "policies")

    def aiter_tokens(self, agent_id: str):
        return _paginate_async(self.control.ListTokens, control_pb2.ListTokensRequest(agent_id=agent_id), "tokens")

    def aiter_credentials(self, request: control_pb2.ListCredentialsRequest):
        copied = control_pb2.ListCredentialsRequest()
        copied.CopyFrom(request)
        return _paginate_async(self.control.ListCredentials, copied, "credentials")

    def aiter_runs(self, request: runtime_pb2.ListRunsRequest):
        copied = runtime_pb2.ListRunsRequest()
        copied.CopyFrom(request)
        return _paginate_async(self.runtime.ListRuns, copied, "runs")

    def aiter_actions(self, request: runtime_pb2.ListActionsRequest):
        copied = runtime_pb2.ListActionsRequest()
        copied.CopyFrom(request)
        return _paginate_async(self.runtime.ListActions, copied, "actions")
