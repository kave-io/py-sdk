from google.protobuf import struct_pb2 as _struct_pb2
from kave.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PolicyMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POLICY_MODE_UNSPECIFIED: _ClassVar[PolicyMode]
    POLICY_MODE_ENFORCE: _ClassVar[PolicyMode]
    POLICY_MODE_SHADOW: _ClassVar[PolicyMode]

class PolicyStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POLICY_STATUS_UNSPECIFIED: _ClassVar[PolicyStatus]
    POLICY_STATUS_ACTIVE: _ClassVar[PolicyStatus]
    POLICY_STATUS_ARCHIVED: _ClassVar[PolicyStatus]

class BudgetPeriod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BUDGET_PERIOD_UNSPECIFIED: _ClassVar[BudgetPeriod]
    BUDGET_PERIOD_RUN: _ClassVar[BudgetPeriod]
    BUDGET_PERIOD_DAILY: _ClassVar[BudgetPeriod]
    BUDGET_PERIOD_MONTHLY: _ClassVar[BudgetPeriod]

class BudgetBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BUDGET_BEHAVIOR_UNSPECIFIED: _ClassVar[BudgetBehavior]
    BUDGET_BEHAVIOR_BLOCK: _ClassVar[BudgetBehavior]
    BUDGET_BEHAVIOR_WARN: _ClassVar[BudgetBehavior]
POLICY_MODE_UNSPECIFIED: PolicyMode
POLICY_MODE_ENFORCE: PolicyMode
POLICY_MODE_SHADOW: PolicyMode
POLICY_STATUS_UNSPECIFIED: PolicyStatus
POLICY_STATUS_ACTIVE: PolicyStatus
POLICY_STATUS_ARCHIVED: PolicyStatus
BUDGET_PERIOD_UNSPECIFIED: BudgetPeriod
BUDGET_PERIOD_RUN: BudgetPeriod
BUDGET_PERIOD_DAILY: BudgetPeriod
BUDGET_PERIOD_MONTHLY: BudgetPeriod
BUDGET_BEHAVIOR_UNSPECIFIED: BudgetBehavior
BUDGET_BEHAVIOR_BLOCK: BudgetBehavior
BUDGET_BEHAVIOR_WARN: BudgetBehavior

class PolicyRecord(_message.Message):
    __slots__ = ("id", "project_id", "env_id", "name", "description", "allowed_types", "allowed_connectors", "allowed_methods", "budget_cap", "budget_period", "budget_behavior", "trace_input", "trace_output", "retention_days", "config", "version", "mode", "status", "created_by", "updated_by", "created_at_ms", "updated_at_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_TYPES_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_CONNECTORS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_METHODS_FIELD_NUMBER: _ClassVar[int]
    BUDGET_CAP_FIELD_NUMBER: _ClassVar[int]
    BUDGET_PERIOD_FIELD_NUMBER: _ClassVar[int]
    BUDGET_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    TRACE_INPUT_FIELD_NUMBER: _ClassVar[int]
    TRACE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    env_id: str
    name: str
    description: str
    allowed_types: _containers.RepeatedScalarFieldContainer[str]
    allowed_connectors: _containers.RepeatedScalarFieldContainer[str]
    allowed_methods: _containers.RepeatedScalarFieldContainer[str]
    budget_cap: _common_pb2.Amount
    budget_period: BudgetPeriod
    budget_behavior: BudgetBehavior
    trace_input: bool
    trace_output: bool
    retention_days: int
    config: _struct_pb2.Struct
    version: int
    mode: PolicyMode
    status: PolicyStatus
    created_by: str
    updated_by: str
    created_at_ms: int
    updated_at_ms: int
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., env_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., allowed_types: _Optional[_Iterable[str]] = ..., allowed_connectors: _Optional[_Iterable[str]] = ..., allowed_methods: _Optional[_Iterable[str]] = ..., budget_cap: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., budget_period: _Optional[_Union[BudgetPeriod, str]] = ..., budget_behavior: _Optional[_Union[BudgetBehavior, str]] = ..., trace_input: bool = ..., trace_output: bool = ..., retention_days: _Optional[int] = ..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., version: _Optional[int] = ..., mode: _Optional[_Union[PolicyMode, str]] = ..., status: _Optional[_Union[PolicyStatus, str]] = ..., created_by: _Optional[str] = ..., updated_by: _Optional[str] = ..., created_at_ms: _Optional[int] = ..., updated_at_ms: _Optional[int] = ...) -> None: ...

class PolicyUpdate(_message.Message):
    __slots__ = ("description", "allowed_types", "allowed_connectors", "allowed_methods", "budget_cap", "clear_budget_cap", "budget_period", "budget_behavior", "trace_input", "trace_output", "retention_days", "config", "mode", "status", "updated_by")
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_TYPES_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_CONNECTORS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_METHODS_FIELD_NUMBER: _ClassVar[int]
    BUDGET_CAP_FIELD_NUMBER: _ClassVar[int]
    CLEAR_BUDGET_CAP_FIELD_NUMBER: _ClassVar[int]
    BUDGET_PERIOD_FIELD_NUMBER: _ClassVar[int]
    BUDGET_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    TRACE_INPUT_FIELD_NUMBER: _ClassVar[int]
    TRACE_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    description: str
    allowed_types: _containers.RepeatedScalarFieldContainer[str]
    allowed_connectors: _containers.RepeatedScalarFieldContainer[str]
    allowed_methods: _containers.RepeatedScalarFieldContainer[str]
    budget_cap: _common_pb2.Amount
    clear_budget_cap: bool
    budget_period: BudgetPeriod
    budget_behavior: BudgetBehavior
    trace_input: bool
    trace_output: bool
    retention_days: int
    config: _struct_pb2.Struct
    mode: PolicyMode
    status: PolicyStatus
    updated_by: str
    def __init__(self, description: _Optional[str] = ..., allowed_types: _Optional[_Iterable[str]] = ..., allowed_connectors: _Optional[_Iterable[str]] = ..., allowed_methods: _Optional[_Iterable[str]] = ..., budget_cap: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., clear_budget_cap: bool = ..., budget_period: _Optional[_Union[BudgetPeriod, str]] = ..., budget_behavior: _Optional[_Union[BudgetBehavior, str]] = ..., trace_input: bool = ..., trace_output: bool = ..., retention_days: _Optional[int] = ..., config: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., mode: _Optional[_Union[PolicyMode, str]] = ..., status: _Optional[_Union[PolicyStatus, str]] = ..., updated_by: _Optional[str] = ...) -> None: ...

class DeletePolicyRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ExportPolicyRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class PolicyYAML(_message.Message):
    __slots__ = ("yaml",)
    YAML_FIELD_NUMBER: _ClassVar[int]
    yaml: str
    def __init__(self, yaml: _Optional[str] = ...) -> None: ...

class ValidatePolicyRequest(_message.Message):
    __slots__ = ("yaml",)
    YAML_FIELD_NUMBER: _ClassVar[int]
    yaml: str
    def __init__(self, yaml: _Optional[str] = ...) -> None: ...

class ValidatePolicyResponse(_message.Message):
    __slots__ = ("ok", "issues")
    OK_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    issues: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ok: bool = ..., issues: _Optional[_Iterable[str]] = ...) -> None: ...
