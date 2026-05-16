from kave.common.v1 import common_pb2 as _common_pb2
from kave.runtime.v1 import cost_pb2 as _cost_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpanKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPAN_KIND_UNSPECIFIED: _ClassVar[SpanKind]
    SPAN_KIND_ACTION: _ClassVar[SpanKind]
    SPAN_KIND_OBSERVED_ACTION: _ClassVar[SpanKind]
    SPAN_KIND_IMPORT: _ClassVar[SpanKind]

class SpanSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPAN_SOURCE_UNSPECIFIED: _ClassVar[SpanSource]
    SPAN_SOURCE_INTERCEPT: _ClassVar[SpanSource]
    SPAN_SOURCE_REPORT: _ClassVar[SpanSource]
    SPAN_SOURCE_OTEL_IMPORT: _ClassVar[SpanSource]
SPAN_KIND_UNSPECIFIED: SpanKind
SPAN_KIND_ACTION: SpanKind
SPAN_KIND_OBSERVED_ACTION: SpanKind
SPAN_KIND_IMPORT: SpanKind
SPAN_SOURCE_UNSPECIFIED: SpanSource
SPAN_SOURCE_INTERCEPT: SpanSource
SPAN_SOURCE_REPORT: SpanSource
SPAN_SOURCE_OTEL_IMPORT: SpanSource

class ValidationMeta(_message.Message):
    __slots__ = ("valid", "violation_count", "enforcement_mode", "validator_name", "validator_version", "rule_version", "duration_ms", "retryable")
    VALID_FIELD_NUMBER: _ClassVar[int]
    VIOLATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENFORCEMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    RULE_VERSION_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    RETRYABLE_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    violation_count: int
    enforcement_mode: str
    validator_name: str
    validator_version: str
    rule_version: str
    duration_ms: int
    retryable: bool
    def __init__(self, valid: bool = ..., violation_count: _Optional[int] = ..., enforcement_mode: _Optional[str] = ..., validator_name: _Optional[str] = ..., validator_version: _Optional[str] = ..., rule_version: _Optional[str] = ..., duration_ms: _Optional[int] = ..., retryable: bool = ...) -> None: ...

class SpanInput(_message.Message):
    __slots__ = ("project_id", "env_id", "agent_id", "run_id", "action_id", "parent_id", "name", "kind", "source", "connector", "started_at_ms", "input", "trace_id", "root_span_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    env_id: str
    agent_id: str
    run_id: str
    action_id: str
    parent_id: str
    name: str
    kind: SpanKind
    source: SpanSource
    connector: str
    started_at_ms: int
    input: bytes
    trace_id: str
    root_span_id: str
    def __init__(self, project_id: _Optional[str] = ..., env_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., run_id: _Optional[str] = ..., action_id: _Optional[str] = ..., parent_id: _Optional[str] = ..., name: _Optional[str] = ..., kind: _Optional[_Union[SpanKind, str]] = ..., source: _Optional[_Union[SpanSource, str]] = ..., connector: _Optional[str] = ..., started_at_ms: _Optional[int] = ..., input: _Optional[bytes] = ..., trace_id: _Optional[str] = ..., root_span_id: _Optional[str] = ...) -> None: ...

class SpanRow(_message.Message):
    __slots__ = ("id", "project_id", "env_id", "agent_id", "run_id", "action_id", "parent_id", "name", "kind", "source", "connector", "started_at_ms", "ended_at_ms", "duration_ms", "input", "output", "attrs", "error", "input_tokens", "output_tokens", "cache_read_tokens", "cache_write_tokens", "reasoning_tokens", "audio_input_tokens", "audio_output_tokens", "image_units", "request_count", "compute_ms", "storage_bytes", "bandwidth_bytes", "model", "cost", "price_snapshot", "trace_id", "root_span_id", "validation_meta", "created_at_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    ATTRS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_READ_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_WRITE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    REASONING_TOKENS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_UNITS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_MS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_BYTES_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    PRICE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_META_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    env_id: str
    agent_id: str
    run_id: str
    action_id: str
    parent_id: str
    name: str
    kind: SpanKind
    source: SpanSource
    connector: str
    started_at_ms: int
    ended_at_ms: int
    duration_ms: int
    input: bytes
    output: bytes
    attrs: bytes
    error: str
    input_tokens: int
    output_tokens: int
    cache_read_tokens: int
    cache_write_tokens: int
    reasoning_tokens: int
    audio_input_tokens: int
    audio_output_tokens: int
    image_units: int
    request_count: int
    compute_ms: int
    storage_bytes: int
    bandwidth_bytes: int
    model: str
    cost: _common_pb2.Amount
    price_snapshot: _cost_pb2.PriceSnapshot
    trace_id: str
    root_span_id: str
    validation_meta: ValidationMeta
    created_at_ms: int
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., env_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., run_id: _Optional[str] = ..., action_id: _Optional[str] = ..., parent_id: _Optional[str] = ..., name: _Optional[str] = ..., kind: _Optional[_Union[SpanKind, str]] = ..., source: _Optional[_Union[SpanSource, str]] = ..., connector: _Optional[str] = ..., started_at_ms: _Optional[int] = ..., ended_at_ms: _Optional[int] = ..., duration_ms: _Optional[int] = ..., input: _Optional[bytes] = ..., output: _Optional[bytes] = ..., attrs: _Optional[bytes] = ..., error: _Optional[str] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., cache_read_tokens: _Optional[int] = ..., cache_write_tokens: _Optional[int] = ..., reasoning_tokens: _Optional[int] = ..., audio_input_tokens: _Optional[int] = ..., audio_output_tokens: _Optional[int] = ..., image_units: _Optional[int] = ..., request_count: _Optional[int] = ..., compute_ms: _Optional[int] = ..., storage_bytes: _Optional[int] = ..., bandwidth_bytes: _Optional[int] = ..., model: _Optional[str] = ..., cost: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., price_snapshot: _Optional[_Union[_cost_pb2.PriceSnapshot, _Mapping]] = ..., trace_id: _Optional[str] = ..., root_span_id: _Optional[str] = ..., validation_meta: _Optional[_Union[ValidationMeta, _Mapping]] = ..., created_at_ms: _Optional[int] = ...) -> None: ...

class SpanEnd(_message.Message):
    __slots__ = ("ended_at_ms", "duration_ms", "output", "attrs", "error", "input_tokens", "output_tokens", "cache_read_tokens", "cache_write_tokens", "reasoning_tokens", "audio_input_tokens", "audio_output_tokens", "image_units", "request_count", "compute_ms", "storage_bytes", "bandwidth_bytes", "model", "cost", "price_snapshot", "trace_id", "root_span_id", "validation_meta")
    ENDED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    ATTRS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_READ_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHE_WRITE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    REASONING_TOKENS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_UNITS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_COUNT_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_MS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_BYTES_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    PRICE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_META_FIELD_NUMBER: _ClassVar[int]
    ended_at_ms: int
    duration_ms: int
    output: bytes
    attrs: bytes
    error: str
    input_tokens: int
    output_tokens: int
    cache_read_tokens: int
    cache_write_tokens: int
    reasoning_tokens: int
    audio_input_tokens: int
    audio_output_tokens: int
    image_units: int
    request_count: int
    compute_ms: int
    storage_bytes: int
    bandwidth_bytes: int
    model: str
    cost: _common_pb2.Amount
    price_snapshot: _cost_pb2.PriceSnapshot
    trace_id: str
    root_span_id: str
    validation_meta: ValidationMeta
    def __init__(self, ended_at_ms: _Optional[int] = ..., duration_ms: _Optional[int] = ..., output: _Optional[bytes] = ..., attrs: _Optional[bytes] = ..., error: _Optional[str] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., cache_read_tokens: _Optional[int] = ..., cache_write_tokens: _Optional[int] = ..., reasoning_tokens: _Optional[int] = ..., audio_input_tokens: _Optional[int] = ..., audio_output_tokens: _Optional[int] = ..., image_units: _Optional[int] = ..., request_count: _Optional[int] = ..., compute_ms: _Optional[int] = ..., storage_bytes: _Optional[int] = ..., bandwidth_bytes: _Optional[int] = ..., model: _Optional[str] = ..., cost: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., price_snapshot: _Optional[_Union[_cost_pb2.PriceSnapshot, _Mapping]] = ..., trace_id: _Optional[str] = ..., root_span_id: _Optional[str] = ..., validation_meta: _Optional[_Union[ValidationMeta, _Mapping]] = ...) -> None: ...

class SpanFilter(_message.Message):
    __slots__ = ("run_id", "action_id", "from_ms", "to_ms", "has_error")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_MS_FIELD_NUMBER: _ClassVar[int]
    TO_MS_FIELD_NUMBER: _ClassVar[int]
    HAS_ERROR_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    action_id: str
    from_ms: int
    to_ms: int
    has_error: bool
    def __init__(self, run_id: _Optional[str] = ..., action_id: _Optional[str] = ..., from_ms: _Optional[int] = ..., to_ms: _Optional[int] = ..., has_error: bool = ...) -> None: ...
