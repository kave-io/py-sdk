from __future__ import annotations

from enum import StrEnum
from typing import Any

import grpc


class Code(StrEnum):
    UNKNOWN = "Unknown"
    CANCELED = "Canceled"
    INVALID_ARGUMENT = "InvalidArgument"
    DEADLINE_EXCEEDED = "DeadlineExceeded"
    NOT_FOUND = "NotFound"
    ALREADY_EXISTS = "AlreadyExists"
    PERMISSION_DENIED = "PermissionDenied"
    UNAUTHENTICATED = "Unauthenticated"
    UNAVAILABLE = "Unavailable"


class KaveError(Exception):
    def __init__(self, code: Code, message: str = "", cause: BaseException | None = None) -> None:
        self.code = code
        self.message = message or str(code)
        self.__cause__ = cause
        super().__init__(self.message)


def wrap_error(err: BaseException | None) -> KaveError | None:
    if err is None:
        return None
    if isinstance(err, KaveError):
        return err
    return KaveError(_code_of(err), _message_of(err), err)


def _message_of(err: BaseException) -> str:
    details = getattr(err, "details", None)
    if callable(details):
        try:
            value = details()
            if value:
                return str(value)
        except Exception:
            pass
    return str(err)


def _code_of(err: BaseException) -> Code:
    if isinstance(err, KaveError):
        return err.code
    if isinstance(err, grpc.RpcError):
        try:
            return _code_from_grpc(err.code())
        except Exception:
            return Code.UNKNOWN
    return Code.UNKNOWN


def _code_from_grpc(code: Any) -> Code:
    if code == grpc.StatusCode.CANCELLED:
        return Code.CANCELED
    if code == grpc.StatusCode.INVALID_ARGUMENT:
        return Code.INVALID_ARGUMENT
    if code == grpc.StatusCode.DEADLINE_EXCEEDED:
        return Code.DEADLINE_EXCEEDED
    if code == grpc.StatusCode.NOT_FOUND:
        return Code.NOT_FOUND
    if code == grpc.StatusCode.ALREADY_EXISTS:
        return Code.ALREADY_EXISTS
    if code == grpc.StatusCode.PERMISSION_DENIED:
        return Code.PERMISSION_DENIED
    if code == grpc.StatusCode.UNAUTHENTICATED:
        return Code.UNAUTHENTICATED
    if code == grpc.StatusCode.UNAVAILABLE:
        return Code.UNAVAILABLE
    return Code.UNKNOWN


def is_not_found(err: BaseException) -> bool:
    return _code_of(err) == Code.NOT_FOUND


def is_already_exists(err: BaseException) -> bool:
    return _code_of(err) == Code.ALREADY_EXISTS


def is_permission_denied(err: BaseException) -> bool:
    return _code_of(err) == Code.PERMISSION_DENIED


def is_unauthenticated(err: BaseException) -> bool:
    return _code_of(err) == Code.UNAUTHENTICATED


def is_invalid_argument(err: BaseException) -> bool:
    return _code_of(err) == Code.INVALID_ARGUMENT


def is_unavailable(err: BaseException) -> bool:
    return _code_of(err) == Code.UNAVAILABLE


def is_canceled(err: BaseException) -> bool:
    return _code_of(err) == Code.CANCELED


def is_deadline_exceeded(err: BaseException) -> bool:
    return _code_of(err) == Code.DEADLINE_EXCEEDED
