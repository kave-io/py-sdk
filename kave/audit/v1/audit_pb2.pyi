from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuditActorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AUDIT_ACTOR_TYPE_UNSPECIFIED: _ClassVar[AuditActorType]
    AUDIT_ACTOR_TYPE_USER: _ClassVar[AuditActorType]
    AUDIT_ACTOR_TYPE_API_KEY: _ClassVar[AuditActorType]
    AUDIT_ACTOR_TYPE_SYSTEM: _ClassVar[AuditActorType]
AUDIT_ACTOR_TYPE_UNSPECIFIED: AuditActorType
AUDIT_ACTOR_TYPE_USER: AuditActorType
AUDIT_ACTOR_TYPE_API_KEY: AuditActorType
AUDIT_ACTOR_TYPE_SYSTEM: AuditActorType

class AuditLog(_message.Message):
    __slots__ = ("id", "org_id", "project_id", "env_id", "actor_id", "actor_type", "event", "resource_type", "resource_id", "diff_before", "diff_after", "ip", "created_at_ms", "provenance")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    DIFF_BEFORE_FIELD_NUMBER: _ClassVar[int]
    DIFF_AFTER_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    project_id: str
    env_id: str
    actor_id: str
    actor_type: AuditActorType
    event: str
    resource_type: str
    resource_id: str
    diff_before: bytes
    diff_after: bytes
    ip: str
    created_at_ms: int
    provenance: bytes
    def __init__(self, id: _Optional[str] = ..., org_id: _Optional[str] = ..., project_id: _Optional[str] = ..., env_id: _Optional[str] = ..., actor_id: _Optional[str] = ..., actor_type: _Optional[_Union[AuditActorType, str]] = ..., event: _Optional[str] = ..., resource_type: _Optional[str] = ..., resource_id: _Optional[str] = ..., diff_before: _Optional[bytes] = ..., diff_after: _Optional[bytes] = ..., ip: _Optional[str] = ..., created_at_ms: _Optional[int] = ..., provenance: _Optional[bytes] = ...) -> None: ...

class AppendAuditInput(_message.Message):
    __slots__ = ("org_id", "project_id", "env_id", "actor_id", "actor_type", "event", "resource_type", "resource_id", "diff_before", "diff_after", "ip", "provenance")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    DIFF_BEFORE_FIELD_NUMBER: _ClassVar[int]
    DIFF_AFTER_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    project_id: str
    env_id: str
    actor_id: str
    actor_type: AuditActorType
    event: str
    resource_type: str
    resource_id: str
    diff_before: bytes
    diff_after: bytes
    ip: str
    provenance: bytes
    def __init__(self, org_id: _Optional[str] = ..., project_id: _Optional[str] = ..., env_id: _Optional[str] = ..., actor_id: _Optional[str] = ..., actor_type: _Optional[_Union[AuditActorType, str]] = ..., event: _Optional[str] = ..., resource_type: _Optional[str] = ..., resource_id: _Optional[str] = ..., diff_before: _Optional[bytes] = ..., diff_after: _Optional[bytes] = ..., ip: _Optional[str] = ..., provenance: _Optional[bytes] = ...) -> None: ...

class AuditFilter(_message.Message):
    __slots__ = ("org_id", "project_id", "env_id", "actor_id", "resource_type", "resource_id", "event", "from_ms", "to_ms")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    FROM_MS_FIELD_NUMBER: _ClassVar[int]
    TO_MS_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    project_id: str
    env_id: str
    actor_id: str
    resource_type: str
    resource_id: str
    event: str
    from_ms: int
    to_ms: int
    def __init__(self, org_id: _Optional[str] = ..., project_id: _Optional[str] = ..., env_id: _Optional[str] = ..., actor_id: _Optional[str] = ..., resource_type: _Optional[str] = ..., resource_id: _Optional[str] = ..., event: _Optional[str] = ..., from_ms: _Optional[int] = ..., to_ms: _Optional[int] = ...) -> None: ...

class AppendAuditRequest(_message.Message):
    __slots__ = ("entry",)
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: AppendAuditInput
    def __init__(self, entry: _Optional[_Union[AppendAuditInput, _Mapping]] = ...) -> None: ...

class QueryAuditsRequest(_message.Message):
    __slots__ = ("filter", "limit", "page_token")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    filter: AuditFilter
    limit: int
    page_token: str
    def __init__(self, filter: _Optional[_Union[AuditFilter, _Mapping]] = ..., limit: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class QueryAuditsResponse(_message.Message):
    __slots__ = ("entries", "next_page_token")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[AuditLog]
    next_page_token: str
    def __init__(self, entries: _Optional[_Iterable[_Union[AuditLog, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
