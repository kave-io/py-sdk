from google.protobuf import empty_pb2 as _empty_pb2
from kave.control.v1 import org_pb2 as _org_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterRequest(_message.Message):
    __slots__ = ("email", "name", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    name: str
    password: str
    def __init__(self, email: _Optional[str] = ..., name: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class LogoutRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class ChangePasswordRequest(_message.Message):
    __slots__ = ("old_password", "new_password")
    OLD_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    old_password: str
    new_password: str
    def __init__(self, old_password: _Optional[str] = ..., new_password: _Optional[str] = ...) -> None: ...

class AuthResponse(_message.Message):
    __slots__ = ("token", "user")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    token: str
    user: _org_pb2.User
    def __init__(self, token: _Optional[str] = ..., user: _Optional[_Union[_org_pb2.User, _Mapping]] = ...) -> None: ...

class RevokeSessionRequest(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    def __init__(self, session_id: _Optional[str] = ...) -> None: ...

class ListSessionsResponse(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[Session]
    def __init__(self, sessions: _Optional[_Iterable[_Union[Session, _Mapping]]] = ...) -> None: ...

class Session(_message.Message):
    __slots__ = ("id", "user_id", "created_at", "expires_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    created_at: int
    expires_at: int
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., created_at: _Optional[int] = ..., expires_at: _Optional[int] = ...) -> None: ...

class CreateAPITokenRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateAPITokenResponse(_message.Message):
    __slots__ = ("token", "raw_token")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    RAW_TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: APIToken
    raw_token: str
    def __init__(self, token: _Optional[_Union[APIToken, _Mapping]] = ..., raw_token: _Optional[str] = ...) -> None: ...

class ListAPITokensResponse(_message.Message):
    __slots__ = ("tokens",)
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedCompositeFieldContainer[APIToken]
    def __init__(self, tokens: _Optional[_Iterable[_Union[APIToken, _Mapping]]] = ...) -> None: ...

class APIToken(_message.Message):
    __slots__ = ("id", "name", "created_at", "last_used_at", "expires_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    created_at: int
    last_used_at: int
    expires_at: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., created_at: _Optional[int] = ..., last_used_at: _Optional[int] = ..., expires_at: _Optional[int] = ...) -> None: ...

class RevokeAPITokenRequest(_message.Message):
    __slots__ = ("token_id",)
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    token_id: str
    def __init__(self, token_id: _Optional[str] = ...) -> None: ...

class CreateAgentTokenRequest(_message.Message):
    __slots__ = ("agent_id", "name")
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    name: str
    def __init__(self, agent_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CreateAgentTokenResponse(_message.Message):
    __slots__ = ("token", "raw_token")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    RAW_TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: AgentTokenInfo
    raw_token: str
    def __init__(self, token: _Optional[_Union[AgentTokenInfo, _Mapping]] = ..., raw_token: _Optional[str] = ...) -> None: ...

class ListAgentTokensResponse(_message.Message):
    __slots__ = ("tokens",)
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedCompositeFieldContainer[AgentTokenInfo]
    def __init__(self, tokens: _Optional[_Iterable[_Union[AgentTokenInfo, _Mapping]]] = ...) -> None: ...

class AgentTokenInfo(_message.Message):
    __slots__ = ("id", "agent_id", "name", "created_at", "last_used_at", "expires_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    agent_id: str
    name: str
    created_at: int
    last_used_at: int
    expires_at: int
    def __init__(self, id: _Optional[str] = ..., agent_id: _Optional[str] = ..., name: _Optional[str] = ..., created_at: _Optional[int] = ..., last_used_at: _Optional[int] = ..., expires_at: _Optional[int] = ...) -> None: ...

class RevokeAgentTokenRequest(_message.Message):
    __slots__ = ("token_id",)
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    token_id: str
    def __init__(self, token_id: _Optional[str] = ...) -> None: ...
