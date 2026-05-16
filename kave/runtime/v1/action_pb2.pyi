from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTION_TYPE_UNSPECIFIED: _ClassVar[ActionType]
    ACTION_TYPE_LLM: _ClassVar[ActionType]
    ACTION_TYPE_TOOL: _ClassVar[ActionType]
    ACTION_TYPE_RETRIEVAL: _ClassVar[ActionType]
    ACTION_TYPE_MUTATION: _ClassVar[ActionType]
    ACTION_TYPE_API: _ClassVar[ActionType]

class ActionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTION_STATUS_UNSPECIFIED: _ClassVar[ActionStatus]
    ACTION_STATUS_PENDING: _ClassVar[ActionStatus]
    ACTION_STATUS_RUNNING: _ClassVar[ActionStatus]
    ACTION_STATUS_COMPLETED: _ClassVar[ActionStatus]
    ACTION_STATUS_FAILED: _ClassVar[ActionStatus]
    ACTION_STATUS_BLOCKED: _ClassVar[ActionStatus]
    ACTION_STATUS_RETRYING: _ClassVar[ActionStatus]

class ActionSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTION_SOURCE_UNSPECIFIED: _ClassVar[ActionSource]
    ACTION_SOURCE_INTERCEPTED: _ClassVar[ActionSource]
    ACTION_SOURCE_OBSERVED: _ClassVar[ActionSource]
ACTION_TYPE_UNSPECIFIED: ActionType
ACTION_TYPE_LLM: ActionType
ACTION_TYPE_TOOL: ActionType
ACTION_TYPE_RETRIEVAL: ActionType
ACTION_TYPE_MUTATION: ActionType
ACTION_TYPE_API: ActionType
ACTION_STATUS_UNSPECIFIED: ActionStatus
ACTION_STATUS_PENDING: ActionStatus
ACTION_STATUS_RUNNING: ActionStatus
ACTION_STATUS_COMPLETED: ActionStatus
ACTION_STATUS_FAILED: ActionStatus
ACTION_STATUS_BLOCKED: ActionStatus
ACTION_STATUS_RETRYING: ActionStatus
ACTION_SOURCE_UNSPECIFIED: ActionSource
ACTION_SOURCE_INTERCEPTED: ActionSource
ACTION_SOURCE_OBSERVED: ActionSource

class ActionRecord(_message.Message):
    __slots__ = ("id", "run_id", "agent_id", "project_id", "env_id", "parent_id", "action_type", "connector", "method", "input", "output", "error", "started_at_ms", "ended_at_ms", "depth", "seq", "status", "source", "metadata", "attempt", "max_attempts", "retry_reason", "provider_req_id", "external_id", "created_at_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    RETRY_REASON_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_REQ_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    run_id: str
    agent_id: str
    project_id: str
    env_id: str
    parent_id: str
    action_type: ActionType
    connector: str
    method: str
    input: bytes
    output: bytes
    error: str
    started_at_ms: int
    ended_at_ms: int
    depth: int
    seq: int
    status: ActionStatus
    source: ActionSource
    metadata: _struct_pb2.Struct
    attempt: int
    max_attempts: int
    retry_reason: str
    provider_req_id: str
    external_id: str
    created_at_ms: int
    def __init__(self, id: _Optional[str] = ..., run_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., project_id: _Optional[str] = ..., env_id: _Optional[str] = ..., parent_id: _Optional[str] = ..., action_type: _Optional[_Union[ActionType, str]] = ..., connector: _Optional[str] = ..., method: _Optional[str] = ..., input: _Optional[bytes] = ..., output: _Optional[bytes] = ..., error: _Optional[str] = ..., started_at_ms: _Optional[int] = ..., ended_at_ms: _Optional[int] = ..., depth: _Optional[int] = ..., seq: _Optional[int] = ..., status: _Optional[_Union[ActionStatus, str]] = ..., source: _Optional[_Union[ActionSource, str]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., attempt: _Optional[int] = ..., max_attempts: _Optional[int] = ..., retry_reason: _Optional[str] = ..., provider_req_id: _Optional[str] = ..., external_id: _Optional[str] = ..., created_at_ms: _Optional[int] = ...) -> None: ...

class ActionFilter(_message.Message):
    __slots__ = ("run_id", "agent_id", "action_type", "status", "source")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    agent_id: str
    action_type: ActionType
    status: ActionStatus
    source: ActionSource
    def __init__(self, run_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., action_type: _Optional[_Union[ActionType, str]] = ..., status: _Optional[_Union[ActionStatus, str]] = ..., source: _Optional[_Union[ActionSource, str]] = ...) -> None: ...
