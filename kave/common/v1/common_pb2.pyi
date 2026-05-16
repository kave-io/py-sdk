from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Amount(_message.Message):
    __slots__ = ("decimal", "currency")
    DECIMAL_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    decimal: str
    currency: str
    def __init__(self, decimal: _Optional[str] = ..., currency: _Optional[str] = ...) -> None: ...
