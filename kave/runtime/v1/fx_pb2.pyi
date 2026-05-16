from kave.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListCurrenciesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCurrenciesResponse(_message.Message):
    __slots__ = ("currencies",)
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[Currency]
    def __init__(self, currencies: _Optional[_Iterable[_Union[Currency, _Mapping]]] = ...) -> None: ...

class Currency(_message.Message):
    __slots__ = ("code", "name", "symbol", "fetched_at_ms")
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    FETCHED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    code: str
    name: str
    symbol: str
    fetched_at_ms: int
    def __init__(self, code: _Optional[str] = ..., name: _Optional[str] = ..., symbol: _Optional[str] = ..., fetched_at_ms: _Optional[int] = ...) -> None: ...

class ListRatesRequest(_message.Message):
    __slots__ = ("base", "quotes")
    BASE_FIELD_NUMBER: _ClassVar[int]
    QUOTES_FIELD_NUMBER: _ClassVar[int]
    base: str
    quotes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base: _Optional[str] = ..., quotes: _Optional[_Iterable[str]] = ...) -> None: ...

class ListRatesResponse(_message.Message):
    __slots__ = ("rates",)
    RATES_FIELD_NUMBER: _ClassVar[int]
    rates: _containers.RepeatedCompositeFieldContainer[RateSnapshot]
    def __init__(self, rates: _Optional[_Iterable[_Union[RateSnapshot, _Mapping]]] = ...) -> None: ...

class RateSnapshot(_message.Message):
    __slots__ = ("base", "quote", "rate_micro", "captured_at_unix_ms", "source")
    BASE_FIELD_NUMBER: _ClassVar[int]
    QUOTE_FIELD_NUMBER: _ClassVar[int]
    RATE_MICRO_FIELD_NUMBER: _ClassVar[int]
    CAPTURED_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    base: str
    quote: str
    rate_micro: int
    captured_at_unix_ms: int
    source: str
    def __init__(self, base: _Optional[str] = ..., quote: _Optional[str] = ..., rate_micro: _Optional[int] = ..., captured_at_unix_ms: _Optional[int] = ..., source: _Optional[str] = ...) -> None: ...

class ConvertRequest(_message.Message):
    __slots__ = ("amount", "to_currency", "snapshot")
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TO_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    amount: _common_pb2.Amount
    to_currency: str
    snapshot: RateSnapshot
    def __init__(self, amount: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., to_currency: _Optional[str] = ..., snapshot: _Optional[_Union[RateSnapshot, _Mapping]] = ...) -> None: ...

class ConvertResponse(_message.Message):
    __slots__ = ("input", "output", "snapshot")
    INPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    input: _common_pb2.Amount
    output: _common_pb2.Amount
    snapshot: RateSnapshot
    def __init__(self, input: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., output: _Optional[_Union[_common_pb2.Amount, _Mapping]] = ..., snapshot: _Optional[_Union[RateSnapshot, _Mapping]] = ...) -> None: ...

class RefreshRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RefreshResponse(_message.Message):
    __slots__ = ("status", "refreshed_at_ms", "error_message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REFRESHED_AT_MS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: str
    refreshed_at_ms: int
    error_message: str
    def __init__(self, status: _Optional[str] = ..., refreshed_at_ms: _Optional[int] = ..., error_message: _Optional[str] = ...) -> None: ...
