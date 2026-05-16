from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DaemonStatusResponse(_message.Message):
    __slots__ = ("pid", "version", "started_at", "uptime", "status")
    class StatusEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    pid: str
    version: str
    started_at: int
    uptime: str
    status: _containers.ScalarMap[str, str]
    def __init__(self, pid: _Optional[str] = ..., version: _Optional[str] = ..., started_at: _Optional[int] = ..., uptime: _Optional[str] = ..., status: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DoctorReportResponse(_message.Message):
    __slots__ = ("checks",)
    CHECKS_FIELD_NUMBER: _ClassVar[int]
    checks: _containers.RepeatedCompositeFieldContainer[DoctorCheck]
    def __init__(self, checks: _Optional[_Iterable[_Union[DoctorCheck, _Mapping]]] = ...) -> None: ...

class DoctorCheck(_message.Message):
    __slots__ = ("name", "status", "message", "detail")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    name: str
    status: str
    message: str
    detail: str
    def __init__(self, name: _Optional[str] = ..., status: _Optional[str] = ..., message: _Optional[str] = ..., detail: _Optional[str] = ...) -> None: ...

class ConfigViewResponse(_message.Message):
    __slots__ = ("raw",)
    RAW_FIELD_NUMBER: _ClassVar[int]
    raw: str
    def __init__(self, raw: _Optional[str] = ...) -> None: ...

class ConfigDiffResponse(_message.Message):
    __slots__ = ("diff",)
    DIFF_FIELD_NUMBER: _ClassVar[int]
    diff: str
    def __init__(self, diff: _Optional[str] = ...) -> None: ...

class ConfigPathsResponse(_message.Message):
    __slots__ = ("config_dir", "config_file", "data_dir", "log_file", "pid_file")
    CONFIG_DIR_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    DATA_DIR_FIELD_NUMBER: _ClassVar[int]
    LOG_FILE_FIELD_NUMBER: _ClassVar[int]
    PID_FILE_FIELD_NUMBER: _ClassVar[int]
    config_dir: str
    config_file: str
    data_dir: str
    log_file: str
    pid_file: str
    def __init__(self, config_dir: _Optional[str] = ..., config_file: _Optional[str] = ..., data_dir: _Optional[str] = ..., log_file: _Optional[str] = ..., pid_file: _Optional[str] = ...) -> None: ...

class ApplyRequest(_message.Message):
    __slots__ = ("prune",)
    PRUNE_FIELD_NUMBER: _ClassVar[int]
    prune: bool
    def __init__(self, prune: bool = ...) -> None: ...

class ApplyPlanResponse(_message.Message):
    __slots__ = ("changes",)
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[PlannedChange]
    def __init__(self, changes: _Optional[_Iterable[_Union[PlannedChange, _Mapping]]] = ...) -> None: ...

class PlannedChange(_message.Message):
    __slots__ = ("resource_type", "resource_id", "action", "summary")
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    resource_type: str
    resource_id: str
    action: str
    summary: str
    def __init__(self, resource_type: _Optional[str] = ..., resource_id: _Optional[str] = ..., action: _Optional[str] = ..., summary: _Optional[str] = ...) -> None: ...

class ApplyReportResponse(_message.Message):
    __slots__ = ("created", "updated", "deleted", "summary", "errors")
    CREATED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    created: int
    updated: int
    deleted: int
    summary: str
    errors: _containers.RepeatedCompositeFieldContainer[ApplyError]
    def __init__(self, created: _Optional[int] = ..., updated: _Optional[int] = ..., deleted: _Optional[int] = ..., summary: _Optional[str] = ..., errors: _Optional[_Iterable[_Union[ApplyError, _Mapping]]] = ...) -> None: ...

class ApplyError(_message.Message):
    __slots__ = ("resource_id", "message")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    message: str
    def __init__(self, resource_id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class ConfigReloadReportResponse(_message.Message):
    __slots__ = ("success", "message", "resources_loaded")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_LOADED_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    resources_loaded: int
    def __init__(self, success: bool = ..., message: _Optional[str] = ..., resources_loaded: _Optional[int] = ...) -> None: ...

class AdminStoreReportResponse(_message.Message):
    __slots__ = ("database_url", "tables_count", "total_size", "tables")
    class TablesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: StoreTableInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[StoreTableInfo, _Mapping]] = ...) -> None: ...
    DATABASE_URL_FIELD_NUMBER: _ClassVar[int]
    TABLES_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    database_url: str
    tables_count: int
    total_size: str
    tables: _containers.MessageMap[str, StoreTableInfo]
    def __init__(self, database_url: _Optional[str] = ..., tables_count: _Optional[int] = ..., total_size: _Optional[str] = ..., tables: _Optional[_Mapping[str, StoreTableInfo]] = ...) -> None: ...

class StoreTableInfo(_message.Message):
    __slots__ = ("row_count", "approx_size")
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    APPROX_SIZE_FIELD_NUMBER: _ClassVar[int]
    row_count: int
    approx_size: str
    def __init__(self, row_count: _Optional[int] = ..., approx_size: _Optional[str] = ...) -> None: ...
