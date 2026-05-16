from google.protobuf import struct_pb2 as _struct_pb2
from kave.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PriceSnapshot(_message.Message):
    __slots__ = ("version", "provider", "model", "match", "source", "input_per_million", "output_per_million", "cache_read_per_million", "cache_write_per_million", "reasoning_per_million", "audio_input_per_million", "audio_output_per_million", "image_unit_price", "per_request", "per_compute_ms", "per_gb_stored", "per_gb_transferred", "resolved_at_ms", "currency")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    INPUT_PER_MILLION_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PER_MILLION_FIELD_NUMBER: _ClassVar[int]
    CACHE_READ_PER_MILLION_FIELD_NUMBER: _ClassVar[int]
    CACHE_WRITE_PER_MILLION_FIELD_NUMBER: _ClassVar[int]
    REASONING_PER_MILLION_FIELD_NUMBER: _ClassVar[int]
    AUDIO_INPUT_PER_MILLION_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OUTPUT_PER_MILLION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_UNIT_PRICE_FIELD_NUMBER: _ClassVar[int]
    PER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PER_COMPUTE_MS_FIELD_NUMBER: _ClassVar[int]
    PER_GB_STORED_FIELD_NUMBER: _ClassVar[int]
    PER_GB_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    version: str
    provider: str
    model: str
    match: str
    source: str
    input_per_million: _common_pb2.Amount
    output_per_million: _common_pb2.Amount
    cache_read_per_million: _common_pb2.Amount
    cache_write_per_million: _common_pb2.Amount
    reasoning_per_million: _common_pb2.Amount
    audio_input_per_million: _common_pb2.Amount
    audio_output_per_million: _common_pb2.Amount
    image_unit_price: _common_pb2.Amount
    per_request: _common_pb2.Amount
    per_compute_ms: _common_pb2.Amount
    per_gb_stored: _common_pb2.Amount
    per_gb_transferred: _common_pb2.Amount
    resolved_at_ms: int
    currency: str
    def __init__(self, version: _Optional[str] = ..., provider: _Optional[str] = ..., model: _Optional[str] = ..., match: _Optional[str] = ..., source: _Optional[str] = ..., input_per_million: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., output_per_million: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., cache_read_per_million: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., cache_write_per_million: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., reasoning_per_million: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., audio_input_per_million: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., audio_output_per_million: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., image_unit_price: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., per_request: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., per_compute_ms: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., per_gb_stored: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., per_gb_transferred: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., resolved_at_ms: _Optional[int] = ..., currency: _Optional[str] = ...) -> None: ...

class PriceModel(_message.Message):
    __slots__ = ("provider", "match", "source", "input_per_million", "output_per_million", "cache_read_per_million", "cache_write_per_million", "reasoning_per_million", "audio_input_per_million", "audio_output_per_million", "image_unit_price", "per_request", "per_compute_ms", "per_gb_stored", "per_gb_transferred", "effective_from_ms", "effective_to_ms", "revision_note", "currency")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    INPUT_PER_MILLION_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PER_MILLION_FIELD_NUMBER: _ClassVar[int]
    CACHE_READ_PER_MILLION_FIELD_NUMBER: _ClassVar[int]
    CACHE_WRITE_PER_MILLION_FIELD_NUMBER: _ClassVar[int]
    REASONING_PER_MILLION_FIELD_NUMBER: _ClassVar[int]
    AUDIO_INPUT_PER_MILLION_FIELD_NUMBER: _ClassVar[int]
    AUDIO_OUTPUT_PER_MILLION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_UNIT_PRICE_FIELD_NUMBER: _ClassVar[int]
    PER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PER_COMPUTE_MS_FIELD_NUMBER: _ClassVar[int]
    PER_GB_STORED_FIELD_NUMBER: _ClassVar[int]
    PER_GB_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_FROM_MS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_TO_MS_FIELD_NUMBER: _ClassVar[int]
    REVISION_NOTE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    provider: str
    match: str
    source: str
    input_per_million: _common_pb2.Amount
    output_per_million: _common_pb2.Amount
    cache_read_per_million: _common_pb2.Amount
    cache_write_per_million: _common_pb2.Amount
    reasoning_per_million: _common_pb2.Amount
    audio_input_per_million: _common_pb2.Amount
    audio_output_per_million: _common_pb2.Amount
    image_unit_price: _common_pb2.Amount
    per_request: _common_pb2.Amount
    per_compute_ms: _common_pb2.Amount
    per_gb_stored: _common_pb2.Amount
    per_gb_transferred: _common_pb2.Amount
    effective_from_ms: int
    effective_to_ms: int
    revision_note: str
    currency: str
    def __init__(self, provider: _Optional[str] = ..., match: _Optional[str] = ..., source: _Optional[str] = ..., input_per_million: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., output_per_million: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., cache_read_per_million: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., cache_write_per_million: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., reasoning_per_million: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., audio_input_per_million: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., audio_output_per_million: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., image_unit_price: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., per_request: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., per_compute_ms: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., per_gb_stored: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., per_gb_transferred: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., effective_from_ms: _Optional[int] = ..., effective_to_ms: _Optional[int] = ..., revision_note: _Optional[str] = ..., currency: _Optional[str] = ...) -> None: ...

class PriceBook(_message.Message):
    __slots__ = ("version", "entries")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    version: str
    entries: _containers.RepeatedCompositeFieldContainer[PriceModel]
    def __init__(self, version: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[PriceModel, _Mapping]]] = ...) -> None: ...

class BudgetEntry(_message.Message):
    __slots__ = ("id", "project_id", "env_id", "policy_id", "agent_id", "run_id", "action_id", "span_id", "connector", "model", "input_tokens", "output_tokens", "cache_read_tokens", "cache_write_tokens", "reasoning_tokens", "audio_input_tokens", "audio_output_tokens", "image_units", "request_count", "compute_ms", "storage_bytes", "bandwidth_bytes", "cost", "price_snapshot", "usage_detail", "metadata", "created_at_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
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
    COST_FIELD_NUMBER: _ClassVar[int]
    PRICE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    USAGE_DETAIL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    env_id: str
    policy_id: str
    agent_id: str
    run_id: str
    action_id: str
    span_id: str
    connector: str
    model: str
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
    cost: _common_pb2.Amount
    price_snapshot: PriceSnapshot
    usage_detail: _struct_pb2.Struct
    metadata: _struct_pb2.Struct
    created_at_ms: int
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., env_id: _Optional[str] = ..., policy_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., run_id: _Optional[str] = ..., action_id: _Optional[str] = ..., span_id: _Optional[str] = ..., connector: _Optional[str] = ..., model: _Optional[str] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., cache_read_tokens: _Optional[int] = ..., cache_write_tokens: _Optional[int] = ..., reasoning_tokens: _Optional[int] = ..., audio_input_tokens: _Optional[int] = ..., audio_output_tokens: _Optional[int] = ..., image_units: _Optional[int] = ..., request_count: _Optional[int] = ..., compute_ms: _Optional[int] = ..., storage_bytes: _Optional[int] = ..., bandwidth_bytes: _Optional[int] = ..., cost: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., price_snapshot: _Optional[_Union[PriceSnapshot, _Mapping]] = ..., usage_detail: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_at_ms: _Optional[int] = ...) -> None: ...

class SpendFilter(_message.Message):
    __slots__ = ("project_id", "env_id", "policy_id", "agent_id", "connector", "model", "from_ms", "to_ms")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    FROM_MS_FIELD_NUMBER: _ClassVar[int]
    TO_MS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    env_id: str
    policy_id: str
    agent_id: str
    connector: str
    model: str
    from_ms: int
    to_ms: int
    def __init__(self, project_id: _Optional[str] = ..., env_id: _Optional[str] = ..., policy_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., connector: _Optional[str] = ..., model: _Optional[str] = ..., from_ms: _Optional[int] = ..., to_ms: _Optional[int] = ...) -> None: ...

class SpendReport(_message.Message):
    __slots__ = ("total", "by_project", "by_env", "by_policy", "by_agent", "by_connector", "by_model", "period_start_ms", "period_end_ms")
    class ByProjectEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.Amount
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ...) -> None: ...
    class ByEnvEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.Amount
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ...) -> None: ...
    class ByPolicyEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.Amount
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ...) -> None: ...
    class ByAgentEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.Amount
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ...) -> None: ...
    class ByConnectorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.Amount
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ...) -> None: ...
    class ByModelEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.Amount
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ...) -> None: ...
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    BY_PROJECT_FIELD_NUMBER: _ClassVar[int]
    BY_ENV_FIELD_NUMBER: _ClassVar[int]
    BY_POLICY_FIELD_NUMBER: _ClassVar[int]
    BY_AGENT_FIELD_NUMBER: _ClassVar[int]
    BY_CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    BY_MODEL_FIELD_NUMBER: _ClassVar[int]
    PERIOD_START_MS_FIELD_NUMBER: _ClassVar[int]
    PERIOD_END_MS_FIELD_NUMBER: _ClassVar[int]
    total: _common_pb2.Amount
    by_project: _containers.MessageMap[str, _common_pb2.Amount]
    by_env: _containers.MessageMap[str, _common_pb2.Amount]
    by_policy: _containers.MessageMap[str, _common_pb2.Amount]
    by_agent: _containers.MessageMap[str, _common_pb2.Amount]
    by_connector: _containers.MessageMap[str, _common_pb2.Amount]
    by_model: _containers.MessageMap[str, _common_pb2.Amount]
    period_start_ms: int
    period_end_ms: int
    def __init__(self, total: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., by_project: _Optional[_Mapping[str, _common_pb2.Amount]] = ..., by_env: _Optional[_Mapping[str, _common_pb2.Amount]] = ..., by_policy: _Optional[_Mapping[str, _common_pb2.Amount]] = ..., by_agent: _Optional[_Mapping[str, _common_pb2.Amount]] = ..., by_connector: _Optional[_Mapping[str, _common_pb2.Amount]] = ..., by_model: _Optional[_Mapping[str, _common_pb2.Amount]] = ..., period_start_ms: _Optional[int] = ..., period_end_ms: _Optional[int] = ...) -> None: ...
