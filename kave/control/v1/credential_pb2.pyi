from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CredentialSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CREDENTIAL_SOURCE_UNSPECIFIED: _ClassVar[CredentialSource]
    CREDENTIAL_SOURCE_ENCRYPTED: _ClassVar[CredentialSource]
    CREDENTIAL_SOURCE_VAULT_REF: _ClassVar[CredentialSource]
    CREDENTIAL_SOURCE_OAUTH: _ClassVar[CredentialSource]
    CREDENTIAL_SOURCE_STS: _ClassVar[CredentialSource]
    CREDENTIAL_SOURCE_PASSTHROUGH: _ClassVar[CredentialSource]

class CredentialStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CREDENTIAL_STATUS_UNSPECIFIED: _ClassVar[CredentialStatus]
    CREDENTIAL_STATUS_ACTIVE: _ClassVar[CredentialStatus]
    CREDENTIAL_STATUS_REVOKED: _ClassVar[CredentialStatus]
    CREDENTIAL_STATUS_EXPIRED: _ClassVar[CredentialStatus]
    CREDENTIAL_STATUS_PENDING_ROTATION: _ClassVar[CredentialStatus]
CREDENTIAL_SOURCE_UNSPECIFIED: CredentialSource
CREDENTIAL_SOURCE_ENCRYPTED: CredentialSource
CREDENTIAL_SOURCE_VAULT_REF: CredentialSource
CREDENTIAL_SOURCE_OAUTH: CredentialSource
CREDENTIAL_SOURCE_STS: CredentialSource
CREDENTIAL_SOURCE_PASSTHROUGH: CredentialSource
CREDENTIAL_STATUS_UNSPECIFIED: CredentialStatus
CREDENTIAL_STATUS_ACTIVE: CredentialStatus
CREDENTIAL_STATUS_REVOKED: CredentialStatus
CREDENTIAL_STATUS_EXPIRED: CredentialStatus
CREDENTIAL_STATUS_PENDING_ROTATION: CredentialStatus

class ConnectorCredential(_message.Message):
    __slots__ = ("id", "project_id", "env_id", "connector_type", "account_id", "label", "description", "source_type", "encrypted_blob", "key_hash", "wrapping_key_id", "secret_ref", "secret_version", "status", "version", "expires_at_ms", "rotated_at_ms", "rotated_by", "last_used_at_ms", "last_validated_at_ms", "created_by", "created_at_ms", "updated_at_ms", "revoked_at_ms", "revoked_by", "revoke_reason")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_BLOB_FIELD_NUMBER: _ClassVar[int]
    KEY_HASH_FIELD_NUMBER: _ClassVar[int]
    WRAPPING_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_REF_FIELD_NUMBER: _ClassVar[int]
    SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_MS_FIELD_NUMBER: _ClassVar[int]
    ROTATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    ROTATED_BY_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    LAST_VALIDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    REVOKED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    REVOKED_BY_FIELD_NUMBER: _ClassVar[int]
    REVOKE_REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    env_id: str
    connector_type: str
    account_id: str
    label: str
    description: str
    source_type: CredentialSource
    encrypted_blob: bytes
    key_hash: str
    wrapping_key_id: str
    secret_ref: str
    secret_version: str
    status: CredentialStatus
    version: int
    expires_at_ms: int
    rotated_at_ms: int
    rotated_by: str
    last_used_at_ms: int
    last_validated_at_ms: int
    created_by: str
    created_at_ms: int
    updated_at_ms: int
    revoked_at_ms: int
    revoked_by: str
    revoke_reason: str
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., env_id: _Optional[str] = ..., connector_type: _Optional[str] = ..., account_id: _Optional[str] = ..., label: _Optional[str] = ..., description: _Optional[str] = ..., source_type: _Optional[_Union[CredentialSource, str]] = ..., encrypted_blob: _Optional[bytes] = ..., key_hash: _Optional[str] = ..., wrapping_key_id: _Optional[str] = ..., secret_ref: _Optional[str] = ..., secret_version: _Optional[str] = ..., status: _Optional[_Union[CredentialStatus, str]] = ..., version: _Optional[int] = ..., expires_at_ms: _Optional[int] = ..., rotated_at_ms: _Optional[int] = ..., rotated_by: _Optional[str] = ..., last_used_at_ms: _Optional[int] = ..., last_validated_at_ms: _Optional[int] = ..., created_by: _Optional[str] = ..., created_at_ms: _Optional[int] = ..., updated_at_ms: _Optional[int] = ..., revoked_at_ms: _Optional[int] = ..., revoked_by: _Optional[str] = ..., revoke_reason: _Optional[str] = ...) -> None: ...

class CredentialUpdate(_message.Message):
    __slots__ = ("label", "description", "account_id")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    label: str
    description: str
    account_id: str
    def __init__(self, label: _Optional[str] = ..., description: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class CredentialFilter(_message.Message):
    __slots__ = ("env_id", "connector_type", "account_id", "label", "status")
    ENV_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    env_id: str
    connector_type: str
    account_id: str
    label: str
    status: CredentialStatus
    def __init__(self, env_id: _Optional[str] = ..., connector_type: _Optional[str] = ..., account_id: _Optional[str] = ..., label: _Optional[str] = ..., status: _Optional[_Union[CredentialStatus, str]] = ...) -> None: ...
