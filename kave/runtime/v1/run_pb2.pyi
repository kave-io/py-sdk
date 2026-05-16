from google.protobuf import struct_pb2 as _struct_pb2
from kave.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRIGGER_TYPE_UNSPECIFIED: _ClassVar[TriggerType]
    TRIGGER_TYPE_API: _ClassVar[TriggerType]
    TRIGGER_TYPE_SCHEDULE: _ClassVar[TriggerType]
    TRIGGER_TYPE_WEBHOOK: _ClassVar[TriggerType]
    TRIGGER_TYPE_MANUAL: _ClassVar[TriggerType]

class RunStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RUN_STATUS_UNSPECIFIED: _ClassVar[RunStatus]
    RUN_STATUS_ACTIVE: _ClassVar[RunStatus]
    RUN_STATUS_COMPLETED: _ClassVar[RunStatus]
    RUN_STATUS_FAILED: _ClassVar[RunStatus]
    RUN_STATUS_CANCELLED: _ClassVar[RunStatus]
    RUN_STATUS_TIMED_OUT: _ClassVar[RunStatus]
    RUN_STATUS_BLOCKED: _ClassVar[RunStatus]
TRIGGER_TYPE_UNSPECIFIED: TriggerType
TRIGGER_TYPE_API: TriggerType
TRIGGER_TYPE_SCHEDULE: TriggerType
TRIGGER_TYPE_WEBHOOK: TriggerType
TRIGGER_TYPE_MANUAL: TriggerType
RUN_STATUS_UNSPECIFIED: RunStatus
RUN_STATUS_ACTIVE: RunStatus
RUN_STATUS_COMPLETED: RunStatus
RUN_STATUS_FAILED: RunStatus
RUN_STATUS_CANCELLED: RunStatus
RUN_STATUS_TIMED_OUT: RunStatus
RUN_STATUS_BLOCKED: RunStatus

class RunRecord(_message.Message):
    __slots__ = ("id", "project_id", "env_id", "agent_id", "policy_id", "name", "status", "budget_cap", "spent", "metadata", "error_message", "trigger_type", "trigger_id", "correlation_id", "session_id", "idempotency_key", "started_at_ms", "ended_at_ms", "created_at_ms", "updated_at_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BUDGET_CAP_FIELD_NUMBER: _ClassVar[int]
    SPENT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_ID_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    env_id: str
    agent_id: str
    policy_id: str
    name: str
    status: RunStatus
    budget_cap: _common_pb2.Amount
    spent: _common_pb2.Amount
    metadata: _struct_pb2.Struct
    error_message: str
    trigger_type: TriggerType
    trigger_id: str
    correlation_id: str
    session_id: str
    idempotency_key: str
    started_at_ms: int
    ended_at_ms: int
    created_at_ms: int
    updated_at_ms: int
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., env_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., policy_id: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[RunStatus, str]] = ..., budget_cap: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., spent: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., error_message: _Optional[str] = ..., trigger_type: _Optional[_Union[TriggerType, str]] = ..., trigger_id: _Optional[str] = ..., correlation_id: _Optional[str] = ..., session_id: _Optional[str] = ..., idempotency_key: _Optional[str] = ..., started_at_ms: _Optional[int] = ..., ended_at_ms: _Optional[int] = ..., created_at_ms: _Optional[int] = ..., updated_at_ms: _Optional[int] = ...) -> None: ...

class RunUpdate(_message.Message):
    __slots__ = ("status", "spent", "error_message", "ended_at_ms", "metadata")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SPENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    status: RunStatus
    spent: _common_pb2.Amount
    error_message: str
    ended_at_ms: int
    metadata: _struct_pb2.Struct
    def __init__(self, status: _Optional[_Union[RunStatus, str]] = ..., spent: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., error_message: _Optional[str] = ..., ended_at_ms: _Optional[int] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class RunFilter(_message.Message):
    __slots__ = ("project_id", "env_id", "agent_id", "status", "from_ms", "to_ms")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FROM_MS_FIELD_NUMBER: _ClassVar[int]
    TO_MS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    env_id: str
    agent_id: str
    status: RunStatus
    from_ms: int
    to_ms: int
    def __init__(self, project_id: _Optional[str] = ..., env_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., status: _Optional[_Union[RunStatus, str]] = ..., from_ms: _Optional[int] = ..., to_ms: _Optional[int] = ...) -> None: ...
