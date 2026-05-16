from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnvironmentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENVIRONMENT_TYPE_UNSPECIFIED: _ClassVar[EnvironmentType]
    ENVIRONMENT_TYPE_DEV: _ClassVar[EnvironmentType]
    ENVIRONMENT_TYPE_STAGING: _ClassVar[EnvironmentType]
    ENVIRONMENT_TYPE_PROD: _ClassVar[EnvironmentType]
    ENVIRONMENT_TYPE_CUSTOM: _ClassVar[EnvironmentType]

class TrustMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRUST_MODE_UNSPECIFIED: _ClassVar[TrustMode]
    TRUST_MODE_STRICT: _ClassVar[TrustMode]
    TRUST_MODE_PERMISSIVE: _ClassVar[TrustMode]
ENVIRONMENT_TYPE_UNSPECIFIED: EnvironmentType
ENVIRONMENT_TYPE_DEV: EnvironmentType
ENVIRONMENT_TYPE_STAGING: EnvironmentType
ENVIRONMENT_TYPE_PROD: EnvironmentType
ENVIRONMENT_TYPE_CUSTOM: EnvironmentType
TRUST_MODE_UNSPECIFIED: TrustMode
TRUST_MODE_STRICT: TrustMode
TRUST_MODE_PERMISSIVE: TrustMode

class Environment(_message.Message):
    __slots__ = ("id", "project_id", "name", "slug", "type", "trust_mode", "created_at_ms", "updated_at_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TRUST_MODE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    name: str
    slug: str
    type: EnvironmentType
    trust_mode: TrustMode
    created_at_ms: int
    updated_at_ms: int
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., name: _Optional[str] = ..., slug: _Optional[str] = ..., type: _Optional[_Union[EnvironmentType, str]] = ..., trust_mode: _Optional[_Union[TrustMode, str]] = ..., created_at_ms: _Optional[int] = ..., updated_at_ms: _Optional[int] = ...) -> None: ...
