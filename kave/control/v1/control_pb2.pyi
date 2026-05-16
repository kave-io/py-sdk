from google.protobuf import empty_pb2 as _empty_pb2
from kave.control.v1 import agent_pb2 as _agent_pb2
from kave.control.v1 import auth_pb2 as _auth_pb2
from kave.control.v1 import budget_pb2 as _budget_pb2
from kave.control.v1 import credential_pb2 as _credential_pb2
from kave.control.v1 import daemon_pb2 as _daemon_pb2
from kave.control.v1 import environment_pb2 as _environment_pb2
from kave.control.v1 import org_pb2 as _org_pb2
from kave.control.v1 import policy_pb2 as _policy_pb2
from kave.control.v1 import project_pb2 as _project_pb2
from kave.control.v1 import rbac_pb2 as _rbac_pb2
from kave.control.v1 import token_pb2 as _token_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateOrganizationRequest(_message.Message):
    __slots__ = ("name", "slug")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ...) -> None: ...

class GetOrganizationRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListOrganizationsRequest(_message.Message):
    __slots__ = ("limit", "cursor")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    limit: int
    cursor: str
    def __init__(self, limit: _Optional[int] = ..., cursor: _Optional[str] = ...) -> None: ...

class ListOrganizationsResponse(_message.Message):
    __slots__ = ("organizations", "next_cursor")
    ORGANIZATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    organizations: _containers.RepeatedCompositeFieldContainer[_org_pb2.Organization]
    next_cursor: str
    def __init__(self, organizations: _Optional[_Iterable[_Union[_org_pb2.Organization, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class CreateProjectRequest(_message.Message):
    __slots__ = ("org_id", "name", "slug")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    name: str
    slug: str
    def __init__(self, org_id: _Optional[str] = ..., name: _Optional[str] = ..., slug: _Optional[str] = ...) -> None: ...

class GetProjectRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListProjectsRequest(_message.Message):
    __slots__ = ("org_id", "limit", "cursor")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    limit: int
    cursor: str
    def __init__(self, org_id: _Optional[str] = ..., limit: _Optional[int] = ..., cursor: _Optional[str] = ...) -> None: ...

class ListProjectsResponse(_message.Message):
    __slots__ = ("projects", "next_cursor")
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.RepeatedCompositeFieldContainer[_project_pb2.Project]
    next_cursor: str
    def __init__(self, projects: _Optional[_Iterable[_Union[_project_pb2.Project, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class CreateEnvironmentRequest(_message.Message):
    __slots__ = ("project_id", "name", "slug", "type")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    name: str
    slug: str
    type: _environment_pb2.EnvironmentType
    def __init__(self, project_id: _Optional[str] = ..., name: _Optional[str] = ..., slug: _Optional[str] = ..., type: _Optional[_Union[_environment_pb2.EnvironmentType, str]] = ...) -> None: ...

class GetEnvironmentRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListEnvironmentsRequest(_message.Message):
    __slots__ = ("project_id", "limit", "cursor")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    limit: int
    cursor: str
    def __init__(self, project_id: _Optional[str] = ..., limit: _Optional[int] = ..., cursor: _Optional[str] = ...) -> None: ...

class ListEnvironmentsResponse(_message.Message):
    __slots__ = ("environments", "next_cursor")
    ENVIRONMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    environments: _containers.RepeatedCompositeFieldContainer[_environment_pb2.Environment]
    next_cursor: str
    def __init__(self, environments: _Optional[_Iterable[_Union[_environment_pb2.Environment, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class CreateAgentRequest(_message.Message):
    __slots__ = ("env_id", "name", "description", "policy_id")
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    env_id: str
    name: str
    description: str
    policy_id: str
    def __init__(self, env_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., policy_id: _Optional[str] = ...) -> None: ...

class GetAgentRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListAgentsRequest(_message.Message):
    __slots__ = ("env_id", "limit", "cursor")
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    env_id: str
    limit: int
    cursor: str
    def __init__(self, env_id: _Optional[str] = ..., limit: _Optional[int] = ..., cursor: _Optional[str] = ...) -> None: ...

class ListAgentsResponse(_message.Message):
    __slots__ = ("agents", "next_cursor")
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    agents: _containers.RepeatedCompositeFieldContainer[_agent_pb2.Agent]
    next_cursor: str
    def __init__(self, agents: _Optional[_Iterable[_Union[_agent_pb2.Agent, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class UpdateAgentRequest(_message.Message):
    __slots__ = ("id", "update")
    ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    update: _agent_pb2.AgentUpdate
    def __init__(self, id: _Optional[str] = ..., update: _Optional[_Union[_agent_pb2.AgentUpdate, _Mapping]] = ...) -> None: ...

class DeleteAgentRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RestoreAgentRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CreatePolicyRequest(_message.Message):
    __slots__ = ("env_id", "name", "description", "mode")
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    env_id: str
    name: str
    description: str
    mode: _policy_pb2.PolicyMode
    def __init__(self, env_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., mode: _Optional[_Union[_policy_pb2.PolicyMode, str]] = ...) -> None: ...

class GetPolicyRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListPoliciesRequest(_message.Message):
    __slots__ = ("env_id", "limit", "cursor")
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    env_id: str
    limit: int
    cursor: str
    def __init__(self, env_id: _Optional[str] = ..., limit: _Optional[int] = ..., cursor: _Optional[str] = ...) -> None: ...

class ListPoliciesResponse(_message.Message):
    __slots__ = ("policies", "next_cursor")
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    policies: _containers.RepeatedCompositeFieldContainer[_policy_pb2.PolicyRecord]
    next_cursor: str
    def __init__(self, policies: _Optional[_Iterable[_Union[_policy_pb2.PolicyRecord, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class UpdatePolicyRequest(_message.Message):
    __slots__ = ("id", "update")
    ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    update: _policy_pb2.PolicyUpdate
    def __init__(self, id: _Optional[str] = ..., update: _Optional[_Union[_policy_pb2.PolicyUpdate, _Mapping]] = ...) -> None: ...

class CreateTokenRequest(_message.Message):
    __slots__ = ("agent_id", "name")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    name: str
    def __init__(self, agent_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CreateTokenResponse(_message.Message):
    __slots__ = ("token", "raw_token")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    RAW_TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: _token_pb2.AgentToken
    raw_token: str
    def __init__(self, token: _Optional[_Union[_token_pb2.AgentToken, _Mapping]] = ..., raw_token: _Optional[str] = ...) -> None: ...

class GetTokenRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListTokensRequest(_message.Message):
    __slots__ = ("agent_id", "limit", "cursor")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    limit: int
    cursor: str
    def __init__(self, agent_id: _Optional[str] = ..., limit: _Optional[int] = ..., cursor: _Optional[str] = ...) -> None: ...

class ListTokensResponse(_message.Message):
    __slots__ = ("tokens", "next_cursor")
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedCompositeFieldContainer[_token_pb2.AgentToken]
    next_cursor: str
    def __init__(self, tokens: _Optional[_Iterable[_Union[_token_pb2.AgentToken, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class RevokeTokenRequest(_message.Message):
    __slots__ = ("id", "reason")
    ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    reason: str
    def __init__(self, id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class CreateCredentialRequest(_message.Message):
    __slots__ = ("env_id", "connector_type", "label", "encrypted_blob")
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_BLOB_FIELD_NUMBER: _ClassVar[int]
    env_id: str
    connector_type: str
    label: str
    encrypted_blob: bytes
    def __init__(self, env_id: _Optional[str] = ..., connector_type: _Optional[str] = ..., label: _Optional[str] = ..., encrypted_blob: _Optional[bytes] = ...) -> None: ...

class GetCredentialRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListCredentialsRequest(_message.Message):
    __slots__ = ("filter", "limit", "cursor")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    filter: _credential_pb2.CredentialFilter
    limit: int
    cursor: str
    def __init__(self, filter: _Optional[_Union[_credential_pb2.CredentialFilter, _Mapping]] = ..., limit: _Optional[int] = ..., cursor: _Optional[str] = ...) -> None: ...

class ListCredentialsResponse(_message.Message):
    __slots__ = ("credentials", "next_cursor")
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    credentials: _containers.RepeatedCompositeFieldContainer[_credential_pb2.ConnectorCredential]
    next_cursor: str
    def __init__(self, credentials: _Optional[_Iterable[_Union[_credential_pb2.ConnectorCredential, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class UpdateCredentialRequest(_message.Message):
    __slots__ = ("id", "update")
    ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    update: _credential_pb2.CredentialUpdate
    def __init__(self, id: _Optional[str] = ..., update: _Optional[_Union[_credential_pb2.CredentialUpdate, _Mapping]] = ...) -> None: ...

class RotateCredentialRequest(_message.Message):
    __slots__ = ("id", "new_encrypted_blob")
    ID_FIELD_NUMBER: _ClassVar[int]
    NEW_ENCRYPTED_BLOB_FIELD_NUMBER: _ClassVar[int]
    id: str
    new_encrypted_blob: bytes
    def __init__(self, id: _Optional[str] = ..., new_encrypted_blob: _Optional[bytes] = ...) -> None: ...

class RevokeCredentialRequest(_message.Message):
    __slots__ = ("id", "reason")
    ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    reason: str
    def __init__(self, id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class DeleteCredentialRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
