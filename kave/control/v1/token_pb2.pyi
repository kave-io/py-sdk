from kave.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentToken(_message.Message):
    __slots__ = ("id", "agent_id", "project_id", "name", "description", "token_prefix", "hash", "issued_for", "issued_by", "connectors", "methods", "budget_cap", "scopes", "not_before_ms", "expires_at_ms", "last_used_at_ms", "revoked_at_ms", "revoked_by", "revoke_reason", "created_at_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TOKEN_PREFIX_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    ISSUED_FOR_FIELD_NUMBER: _ClassVar[int]
    ISSUED_BY_FIELD_NUMBER: _ClassVar[int]
    CONNECTORS_FIELD_NUMBER: _ClassVar[int]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    BUDGET_CAP_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    NOT_BEFORE_MS_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_MS_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    REVOKED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    REVOKED_BY_FIELD_NUMBER: _ClassVar[int]
    REVOKE_REASON_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    agent_id: str
    project_id: str
    name: str
    description: str
    token_prefix: str
    hash: str
    issued_for: str
    issued_by: str
    connectors: _containers.RepeatedScalarFieldContainer[str]
    methods: _containers.RepeatedScalarFieldContainer[str]
    budget_cap: _common_pb2.Amount
    scopes: _containers.RepeatedScalarFieldContainer[str]
    not_before_ms: int
    expires_at_ms: int
    last_used_at_ms: int
    revoked_at_ms: int
    revoked_by: str
    revoke_reason: str
    created_at_ms: int
    def __init__(self, id: _Optional[str] = ..., agent_id: _Optional[str] = ..., project_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., token_prefix: _Optional[str] = ..., hash: _Optional[str] = ..., issued_for: _Optional[str] = ..., issued_by: _Optional[str] = ..., connectors: _Optional[_Iterable[str]] = ..., methods: _Optional[_Iterable[str]] = ..., budget_cap: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., scopes: _Optional[_Iterable[str]] = ..., not_before_ms: _Optional[int] = ..., expires_at_ms: _Optional[int] = ..., last_used_at_ms: _Optional[int] = ..., revoked_at_ms: _Optional[int] = ..., revoked_by: _Optional[str] = ..., revoke_reason: _Optional[str] = ..., created_at_ms: _Optional[int] = ...) -> None: ...

class AgentTokenUpdate(_message.Message):
    __slots__ = ("revoked_at_ms", "revoked_by", "revoke_reason")
    REVOKED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    REVOKED_BY_FIELD_NUMBER: _ClassVar[int]
    REVOKE_REASON_FIELD_NUMBER: _ClassVar[int]
    revoked_at_ms: int
    revoked_by: str
    revoke_reason: str
    def __init__(self, revoked_at_ms: _Optional[int] = ..., revoked_by: _Optional[str] = ..., revoke_reason: _Optional[str] = ...) -> None: ...
