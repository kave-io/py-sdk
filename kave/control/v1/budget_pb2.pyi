from kave.common.v1 import common_pb2 as _common_pb2
from kave.control.v1 import policy_pb2 as _policy_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Budget(_message.Message):
    __slots__ = ("id", "agent_id", "hard_cap", "soft_cap", "period", "created_at_ms", "updated_at_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    HARD_CAP_FIELD_NUMBER: _ClassVar[int]
    SOFT_CAP_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    agent_id: str
    hard_cap: _common_pb2.Amount
    soft_cap: _common_pb2.Amount
    period: _policy_pb2.BudgetPeriod
    created_at_ms: int
    updated_at_ms: int
    def __init__(self, id: _Optional[str] = ..., agent_id: _Optional[str] = ..., hard_cap: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., soft_cap: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., period: _Optional[_Union[_policy_pb2.BudgetPeriod, str]] = ..., created_at_ms: _Optional[int] = ..., updated_at_ms: _Optional[int] = ...) -> None: ...

class CreateBudgetRequest(_message.Message):
    __slots__ = ("agent_id", "hard_cap", "soft_cap", "period")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    HARD_CAP_FIELD_NUMBER: _ClassVar[int]
    SOFT_CAP_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    hard_cap: _common_pb2.Amount
    soft_cap: _common_pb2.Amount
    period: _policy_pb2.BudgetPeriod
    def __init__(self, agent_id: _Optional[str] = ..., hard_cap: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., soft_cap: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., period: _Optional[_Union[_policy_pb2.BudgetPeriod, str]] = ...) -> None: ...

class GetBudgetRequest(_message.Message):
    __slots__ = ("agent_id",)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    def __init__(self, agent_id: _Optional[str] = ...) -> None: ...

class DeleteBudgetRequest(_message.Message):
    __slots__ = ("agent_id",)
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    def __init__(self, agent_id: _Optional[str] = ...) -> None: ...
