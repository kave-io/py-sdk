from kave.common.v1 import common_pb2 as _common_pb2
from kave.runtime.v1 import action_pb2 as _action_pb2
from kave.runtime.v1 import cost_pb2 as _cost_pb2
from kave.runtime.v1 import fx_pb2 as _fx_pb2
from kave.runtime.v1 import run_pb2 as _run_pb2
from kave.runtime.v1 import span_pb2 as _span_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRunRequest(_message.Message):
    __slots__ = ("project_id", "env_id", "agent_id", "policy_id", "name", "trigger_type", "trigger_id", "correlation_id", "session_id", "idempotency_key")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_ID_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    env_id: str
    agent_id: str
    policy_id: str
    name: str
    trigger_type: _run_pb2.TriggerType
    trigger_id: str
    correlation_id: str
    session_id: str
    idempotency_key: str
    def __init__(self, project_id: _Optional[str] = ..., env_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., policy_id: _Optional[str] = ..., name: _Optional[str] = ..., trigger_type: _Optional[_Union[_run_pb2.TriggerType, str]] = ..., trigger_id: _Optional[str] = ..., correlation_id: _Optional[str] = ..., session_id: _Optional[str] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class GetRunRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListRunsRequest(_message.Message):
    __slots__ = ("filter", "limit", "cursor")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    filter: _run_pb2.RunFilter
    limit: int
    cursor: str
    def __init__(self, filter: _Optional[_Union[_run_pb2.RunFilter, _Mapping]] = ..., limit: _Optional[int] = ..., cursor: _Optional[str] = ...) -> None: ...

class ListRunsResponse(_message.Message):
    __slots__ = ("runs", "next_cursor")
    RUNS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[_run_pb2.RunRecord]
    next_cursor: str
    def __init__(self, runs: _Optional[_Iterable[_Union[_run_pb2.RunRecord, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class UpdateRunRequest(_message.Message):
    __slots__ = ("id", "update")
    ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    update: _run_pb2.RunUpdate
    def __init__(self, id: _Optional[str] = ..., update: _Optional[_Union[_run_pb2.RunUpdate, _Mapping]] = ...) -> None: ...

class CancelRunRequest(_message.Message):
    __slots__ = ("id", "reason")
    ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    reason: str
    def __init__(self, id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class WatchRunsRequest(_message.Message):
    __slots__ = ("env_id", "agent_id", "statuses")
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    env_id: str
    agent_id: str
    statuses: _containers.RepeatedScalarFieldContainer[_run_pb2.RunStatus]
    def __init__(self, env_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., statuses: _Optional[_Iterable[_Union[_run_pb2.RunStatus, str]]] = ...) -> None: ...

class CreateActionRequest(_message.Message):
    __slots__ = ("run_id", "agent_id", "project_id", "env_id", "action_type", "connector", "method")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    agent_id: str
    project_id: str
    env_id: str
    action_type: _action_pb2.ActionType
    connector: str
    method: str
    def __init__(self, run_id: _Optional[str] = ..., agent_id: _Optional[str] = ..., project_id: _Optional[str] = ..., env_id: _Optional[str] = ..., action_type: _Optional[_Union[_action_pb2.ActionType, str]] = ..., connector: _Optional[str] = ..., method: _Optional[str] = ...) -> None: ...

class GetActionRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListActionsRequest(_message.Message):
    __slots__ = ("filter", "limit", "cursor")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    filter: _action_pb2.ActionFilter
    limit: int
    cursor: str
    def __init__(self, filter: _Optional[_Union[_action_pb2.ActionFilter, _Mapping]] = ..., limit: _Optional[int] = ..., cursor: _Optional[str] = ...) -> None: ...

class ListActionsResponse(_message.Message):
    __slots__ = ("actions", "next_cursor")
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[_action_pb2.ActionRecord]
    next_cursor: str
    def __init__(self, actions: _Optional[_Iterable[_Union[_action_pb2.ActionRecord, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class OpenSpanRequest(_message.Message):
    __slots__ = ("span",)
    SPAN_FIELD_NUMBER: _ClassVar[int]
    span: _span_pb2.SpanInput
    def __init__(self, span: _Optional[_Union[_span_pb2.SpanInput, _Mapping]] = ...) -> None: ...

class CloseSpanRequest(_message.Message):
    __slots__ = ("span_id", "end")
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    span_id: str
    end: _span_pb2.SpanEnd
    def __init__(self, span_id: _Optional[str] = ..., end: _Optional[_Union[_span_pb2.SpanEnd, _Mapping]] = ...) -> None: ...

class GetSpanRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class QuerySpansRequest(_message.Message):
    __slots__ = ("filter", "limit", "cursor")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    filter: _span_pb2.SpanFilter
    limit: int
    cursor: str
    def __init__(self, filter: _Optional[_Union[_span_pb2.SpanFilter, _Mapping]] = ..., limit: _Optional[int] = ..., cursor: _Optional[str] = ...) -> None: ...

class QuerySpansResponse(_message.Message):
    __slots__ = ("spans", "next_cursor")
    SPANS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    spans: _containers.RepeatedCompositeFieldContainer[_span_pb2.SpanRow]
    next_cursor: str
    def __init__(self, spans: _Optional[_Iterable[_Union[_span_pb2.SpanRow, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class WatchEventsRequest(_message.Message):
    __slots__ = ("env_id", "project_id", "kind")
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    env_id: str
    project_id: str
    kind: str
    def __init__(self, env_id: _Optional[str] = ..., project_id: _Optional[str] = ..., kind: _Optional[str] = ...) -> None: ...

class RuntimeEvent(_message.Message):
    __slots__ = ("kind", "at", "data")
    KIND_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    kind: str
    at: int
    data: bytes
    def __init__(self, kind: _Optional[str] = ..., at: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class WatchLogsRequest(_message.Message):
    __slots__ = ("level",)
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    level: str
    def __init__(self, level: _Optional[str] = ...) -> None: ...

class LogLine(_message.Message):
    __slots__ = ("at", "level", "message", "context")
    class ContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AT_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    at: int
    level: str
    message: str
    context: _containers.ScalarMap[str, str]
    def __init__(self, at: _Optional[int] = ..., level: _Optional[str] = ..., message: _Optional[str] = ..., context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class TailTracesRequest(_message.Message):
    __slots__ = ("project_id", "env_id", "run_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    env_id: str
    run_id: str
    def __init__(self, project_id: _Optional[str] = ..., env_id: _Optional[str] = ..., run_id: _Optional[str] = ...) -> None: ...

class TraceEvent(_message.Message):
    __slots__ = ("kind", "at", "data")
    KIND_FIELD_NUMBER: _ClassVar[int]
    AT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    kind: str
    at: int
    data: bytes
    def __init__(self, kind: _Optional[str] = ..., at: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class StreamSpansRequest(_message.Message):
    __slots__ = ("project_id", "env_id", "run_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    env_id: str
    run_id: str
    def __init__(self, project_id: _Optional[str] = ..., env_id: _Optional[str] = ..., run_id: _Optional[str] = ...) -> None: ...

class SpanEvent(_message.Message):
    __slots__ = ("at", "span")
    AT_FIELD_NUMBER: _ClassVar[int]
    SPAN_FIELD_NUMBER: _ClassVar[int]
    at: int
    span: _span_pb2.SpanRow
    def __init__(self, at: _Optional[int] = ..., span: _Optional[_Union[_span_pb2.SpanRow, _Mapping]] = ...) -> None: ...

class ExportTraceRequest(_message.Message):
    __slots__ = ("trace_id", "format")
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    trace_id: str
    format: str
    def __init__(self, trace_id: _Optional[str] = ..., format: _Optional[str] = ...) -> None: ...

class ExportTraceResponse(_message.Message):
    __slots__ = ("data", "content_type")
    DATA_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    content_type: str
    def __init__(self, data: _Optional[bytes] = ..., content_type: _Optional[str] = ...) -> None: ...

class IngestTracesRequest(_message.Message):
    __slots__ = ("data", "format")
    DATA_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    format: str
    def __init__(self, data: _Optional[bytes] = ..., format: _Optional[str] = ...) -> None: ...

class IngestTracesResponse(_message.Message):
    __slots__ = ("accepted",)
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    accepted: int
    def __init__(self, accepted: _Optional[int] = ...) -> None: ...

class GetPriceBookRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSpendReportRequest(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: _cost_pb2.SpendFilter
    def __init__(self, filter: _Optional[_Union[_cost_pb2.SpendFilter, _Mapping]] = ...) -> None: ...

class GetDashboardOverviewRequest(_message.Message):
    __slots__ = ("project_id", "env_id", "from_ms", "to_ms", "recent_limit")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_MS_FIELD_NUMBER: _ClassVar[int]
    TO_MS_FIELD_NUMBER: _ClassVar[int]
    RECENT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    env_id: str
    from_ms: int
    to_ms: int
    recent_limit: int
    def __init__(self, project_id: _Optional[str] = ..., env_id: _Optional[str] = ..., from_ms: _Optional[int] = ..., to_ms: _Optional[int] = ..., recent_limit: _Optional[int] = ...) -> None: ...

class DashboardOverview(_message.Message):
    __slots__ = ("total_runs", "active_runs", "blocked_runs", "failed_runs", "avg_latency_ms", "total_input_tokens", "total_output_tokens", "spend", "recent_runs", "recent_attention_runs", "top_agents")
    TOTAL_RUNS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_RUNS_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_RUNS_FIELD_NUMBER: _ClassVar[int]
    FAILED_RUNS_FIELD_NUMBER: _ClassVar[int]
    AVG_LATENCY_MS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    SPEND_FIELD_NUMBER: _ClassVar[int]
    RECENT_RUNS_FIELD_NUMBER: _ClassVar[int]
    RECENT_ATTENTION_RUNS_FIELD_NUMBER: _ClassVar[int]
    TOP_AGENTS_FIELD_NUMBER: _ClassVar[int]
    total_runs: int
    active_runs: int
    blocked_runs: int
    failed_runs: int
    avg_latency_ms: int
    total_input_tokens: int
    total_output_tokens: int
    spend: _cost_pb2.SpendReport
    recent_runs: _containers.RepeatedCompositeFieldContainer[_run_pb2.RunRecord]
    recent_attention_runs: _containers.RepeatedCompositeFieldContainer[_run_pb2.RunRecord]
    top_agents: _containers.RepeatedCompositeFieldContainer[DashboardAgentSpend]
    def __init__(self, total_runs: _Optional[int] = ..., active_runs: _Optional[int] = ..., blocked_runs: _Optional[int] = ..., failed_runs: _Optional[int] = ..., avg_latency_ms: _Optional[int] = ..., total_input_tokens: _Optional[int] = ..., total_output_tokens: _Optional[int] = ..., spend: _Optional[_Union[_cost_pb2.SpendReport, _Mapping]] = ..., recent_runs: _Optional[_Iterable[_Union[_run_pb2.RunRecord, _Mapping]]] = ..., recent_attention_runs: _Optional[_Iterable[_Union[_run_pb2.RunRecord, _Mapping]]] = ..., top_agents: _Optional[_Iterable[_Union[DashboardAgentSpend, _Mapping]]] = ...) -> None: ...

class DashboardAgentSpend(_message.Message):
    __slots__ = ("agent_id", "agent_name", "spend", "run_count")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_NAME_FIELD_NUMBER: _ClassVar[int]
    SPEND_FIELD_NUMBER: _ClassVar[int]
    RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    agent_name: str
    spend: _common_pb2.Amount
    run_count: int
    def __init__(self, agent_id: _Optional[str] = ..., agent_name: _Optional[str] = ..., spend: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., run_count: _Optional[int] = ...) -> None: ...

class GetTraceGraphRequest(_message.Message):
    __slots__ = ("run_id", "trace_id", "limit")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    trace_id: str
    limit: int
    def __init__(self, run_id: _Optional[str] = ..., trace_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class TraceGraph(_message.Message):
    __slots__ = ("run", "spans", "nodes", "edges", "total_duration_ms", "total_cost", "total_input_tokens", "total_output_tokens")
    RUN_FIELD_NUMBER: _ClassVar[int]
    SPANS_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    EDGES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    run: _run_pb2.RunRecord
    spans: _containers.RepeatedCompositeFieldContainer[_span_pb2.SpanRow]
    nodes: _containers.RepeatedCompositeFieldContainer[TraceGraphNode]
    edges: _containers.RepeatedCompositeFieldContainer[TraceGraphEdge]
    total_duration_ms: int
    total_cost: _common_pb2.Amount
    total_input_tokens: int
    total_output_tokens: int
    def __init__(self, run: _Optional[_Union[_run_pb2.RunRecord, _Mapping]] = ..., spans: _Optional[_Iterable[_Union[_span_pb2.SpanRow, _Mapping]]] = ..., nodes: _Optional[_Iterable[_Union[TraceGraphNode, _Mapping]]] = ..., edges: _Optional[_Iterable[_Union[TraceGraphEdge, _Mapping]]] = ..., total_duration_ms: _Optional[int] = ..., total_cost: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., total_input_tokens: _Optional[int] = ..., total_output_tokens: _Optional[int] = ...) -> None: ...

class TraceGraphNode(_message.Message):
    __slots__ = ("span_id", "parent_span_id", "name", "connector", "model", "has_error", "depth", "offset_ms", "duration_ms", "cost", "input_tokens", "output_tokens")
    SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    HAS_ERROR_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    span_id: str
    parent_span_id: str
    name: str
    connector: str
    model: str
    has_error: bool
    depth: int
    offset_ms: int
    duration_ms: int
    cost: _common_pb2.Amount
    input_tokens: int
    output_tokens: int
    def __init__(self, span_id: _Optional[str] = ..., parent_span_id: _Optional[str] = ..., name: _Optional[str] = ..., connector: _Optional[str] = ..., model: _Optional[str] = ..., has_error: bool = ..., depth: _Optional[int] = ..., offset_ms: _Optional[int] = ..., duration_ms: _Optional[int] = ..., cost: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ...) -> None: ...

class TraceGraphEdge(_message.Message):
    __slots__ = ("parent_span_id", "child_span_id")
    PARENT_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_SPAN_ID_FIELD_NUMBER: _ClassVar[int]
    parent_span_id: str
    child_span_id: str
    def __init__(self, parent_span_id: _Optional[str] = ..., child_span_id: _Optional[str] = ...) -> None: ...
