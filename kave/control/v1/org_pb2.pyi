from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MembershipRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEMBERSHIP_ROLE_UNSPECIFIED: _ClassVar[MembershipRole]
    MEMBERSHIP_ROLE_ADMIN: _ClassVar[MembershipRole]
    MEMBERSHIP_ROLE_DEV: _ClassVar[MembershipRole]
    MEMBERSHIP_ROLE_VIEWER: _ClassVar[MembershipRole]
    MEMBERSHIP_ROLE_BILLING: _ClassVar[MembershipRole]

class UserStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_STATUS_UNSPECIFIED: _ClassVar[UserStatus]
    USER_STATUS_ACTIVE: _ClassVar[UserStatus]
    USER_STATUS_SUSPENDED: _ClassVar[UserStatus]

class PlanTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLAN_TIER_UNSPECIFIED: _ClassVar[PlanTier]
    PLAN_TIER_FREE: _ClassVar[PlanTier]
    PLAN_TIER_TEAM: _ClassVar[PlanTier]
    PLAN_TIER_ENTERPRISE: _ClassVar[PlanTier]
MEMBERSHIP_ROLE_UNSPECIFIED: MembershipRole
MEMBERSHIP_ROLE_ADMIN: MembershipRole
MEMBERSHIP_ROLE_DEV: MembershipRole
MEMBERSHIP_ROLE_VIEWER: MembershipRole
MEMBERSHIP_ROLE_BILLING: MembershipRole
USER_STATUS_UNSPECIFIED: UserStatus
USER_STATUS_ACTIVE: UserStatus
USER_STATUS_SUSPENDED: UserStatus
PLAN_TIER_UNSPECIFIED: PlanTier
PLAN_TIER_FREE: PlanTier
PLAN_TIER_TEAM: PlanTier
PLAN_TIER_ENTERPRISE: PlanTier

class Organization(_message.Message):
    __slots__ = ("id", "name", "slug", "plan", "created_at_ms", "updated_at_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    PLAN_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    slug: str
    plan: PlanTier
    created_at_ms: int
    updated_at_ms: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., slug: _Optional[str] = ..., plan: _Optional[_Union[PlanTier, str]] = ..., created_at_ms: _Optional[int] = ..., updated_at_ms: _Optional[int] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("id", "org_id", "email", "name", "password_hash", "status", "last_login_at_ms", "created_at_ms", "updated_at_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_HASH_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_LOGIN_AT_MS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    email: str
    name: str
    password_hash: str
    status: UserStatus
    last_login_at_ms: int
    created_at_ms: int
    updated_at_ms: int
    def __init__(self, id: _Optional[str] = ..., org_id: _Optional[str] = ..., email: _Optional[str] = ..., name: _Optional[str] = ..., password_hash: _Optional[str] = ..., status: _Optional[_Union[UserStatus, str]] = ..., last_login_at_ms: _Optional[int] = ..., created_at_ms: _Optional[int] = ..., updated_at_ms: _Optional[int] = ...) -> None: ...

class Membership(_message.Message):
    __slots__ = ("id", "org_id", "user_id", "role", "invited_by", "created_at_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    INVITED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    user_id: str
    role: MembershipRole
    invited_by: str
    created_at_ms: int
    def __init__(self, id: _Optional[str] = ..., org_id: _Optional[str] = ..., user_id: _Optional[str] = ..., role: _Optional[_Union[MembershipRole, str]] = ..., invited_by: _Optional[str] = ..., created_at_ms: _Optional[int] = ...) -> None: ...
