from google.protobuf import struct_pb2 as _struct_pb2
from kave.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGENT_STATUS_UNSPECIFIED: _ClassVar[AgentStatus]
    AGENT_STATUS_ACTIVE: _ClassVar[AgentStatus]
    AGENT_STATUS_DISABLED: _ClassVar[AgentStatus]
AGENT_STATUS_UNSPECIFIED: AgentStatus
AGENT_STATUS_ACTIVE: AgentStatus
AGENT_STATUS_DISABLED: AgentStatus

class Agent(_message.Message):
    __slots__ = ("id", "project_id", "env_id", "name", "description", "policy_id", "monthly_budget", "status", "metadata", "created_by", "updated_by", "deleted_at_ms", "created_at_ms", "updated_at_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_BUDGET_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    env_id: str
    name: str
    description: str
    policy_id: str
    monthly_budget: _common_pb2.Amount
    status: AgentStatus
    metadata: _struct_pb2.Struct
    created_by: str
    updated_by: str
    deleted_at_ms: int
    created_at_ms: int
    updated_at_ms: int
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., env_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., policy_id: _Optional[str] = ..., monthly_budget: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., status: _Optional[_Union[AgentStatus, str]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_by: _Optional[str] = ..., updated_by: _Optional[str] = ..., deleted_at_ms: _Optional[int] = ..., created_at_ms: _Optional[int] = ..., updated_at_ms: _Optional[int] = ...) -> None: ...

class AgentUpdate(_message.Message):
    __slots__ = ("description", "policy_id", "monthly_budget", "status", "metadata", "updated_by")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_BUDGET_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    description: str
    policy_id: str
    monthly_budget: _common_pb2.Amount
    status: AgentStatus
    metadata: _struct_pb2.Struct
    updated_by: str
    def __init__(self, description: _Optional[str] = ..., policy_id: _Optional[str] = ..., monthly_budget: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., status: _Optional[_Union[AgentStatus, str]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., updated_by: _Optional[str] = ...) -> None: ...
