from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRoleRequest(_message.Message):
    __slots__ = ("name", "permissions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    permissions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., permissions: _Optional[_Iterable[str]] = ...) -> None: ...

class GetRoleRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListRolesResponse(_message.Message):
    __slots__ = ("roles",)
    ROLES_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedCompositeFieldContainer[Role]
    def __init__(self, roles: _Optional[_Iterable[_Union[Role, _Mapping]]] = ...) -> None: ...

class DeleteRoleRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ("id", "name", "permissions", "created_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    permissions: _containers.RepeatedScalarFieldContainer[str]
    created_at: int
    updated_at: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., permissions: _Optional[_Iterable[str]] = ..., created_at: _Optional[int] = ..., updated_at: _Optional[int] = ...) -> None: ...

class CreateBindingRequest(_message.Message):
    __slots__ = ("role_id", "subject", "scope")
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    role_id: str
    subject: str
    scope: str
    def __init__(self, role_id: _Optional[str] = ..., subject: _Optional[str] = ..., scope: _Optional[str] = ...) -> None: ...

class ListBindingsResponse(_message.Message):
    __slots__ = ("bindings",)
    BINDINGS_FIELD_NUMBER: _ClassVar[int]
    bindings: _containers.RepeatedCompositeFieldContainer[Binding]
    def __init__(self, bindings: _Optional[_Iterable[_Union[Binding, _Mapping]]] = ...) -> None: ...

class DeleteBindingRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class Binding(_message.Message):
    __slots__ = ("id", "role_id", "subject", "scope", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    role_id: str
    subject: str
    scope: str
    created_at: int
    def __init__(self, id: _Optional[str] = ..., role_id: _Optional[str] = ..., subject: _Optional[str] = ..., scope: _Optional[str] = ..., created_at: _Optional[int] = ...) -> None: ...

class TestPermissionRequest(_message.Message):
    __slots__ = ("subject", "action", "resource")
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    subject: str
    action: str
    resource: str
    def __init__(self, subject: _Optional[str] = ..., action: _Optional[str] = ..., resource: _Optional[str] = ...) -> None: ...

class TestPermissionResponse(_message.Message):
    __slots__ = ("allowed", "reason")
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    allowed: bool
    reason: str
    def __init__(self, allowed: bool = ..., reason: _Optional[str] = ...) -> None: ...
