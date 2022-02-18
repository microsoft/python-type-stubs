from __future__ import annotations
import sys
from typing import Generic, overload, Union, Protocol, TypeVar, Any
from _typing import Timedelta, Timestamp
import datetime

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

OrderableScalarT = TypeVar("OrderableScalarT", int, float)
OrderableTimesT = TypeVar("OrderableTimesT", datetime.date, datetime.datetime, datetime.timedelta, Timestamp, Timedelta)
OrderableDTimesT = TypeVar("OrderableDTimesT", datetime.date, datetime.datetime, datetime.timedelta)
OrderablePTimesT = TypeVar("OrderablePTimesT", Timestamp, Timedelta)
OrderableT = TypeVar("OrderableT", int, float, datetime.date, datetime.datetime, datetime.timedelta, Timestamp, Timedelta)

OrderableScalar = Union[int, float]
OrderableTimes = Union[datetime.date, datetime.datetime, datetime.timedelta, Timestamp, Timedelta]
Orderable = Union[int, float, datetime.date, datetime.datetime, datetime.timedelta, Timestamp, Timedelta]

class IntervalMixinProtocol(Protocol): ...

class _LengthDescriptor:
    @overload
    def __get__(self, instance: Interval[float], owner: Any) -> float: ...
    @overload
    def __get__(self, instance: Interval[int], owner: Any) -> int: ...
    @overload
    def __get__(self, instance: Interval[OrderablePTimesT], owner: Any) -> Timedelta: ...
    @overload
    def __get__(self, instance: Interval[OrderableDTimesT], owner: Any) -> datetime.timedelta: ...

class IntervalMixin:
    @property
    def closed_left(self: IntervalMixinProtocol) -> bool: ...
    @property
    def closed_right(self: IntervalMixinProtocol) -> bool: ...
    @property
    def open_left(self: IntervalMixinProtocol) -> bool: ...
    @property
    def open_right(self: IntervalMixinProtocol) -> bool: ...
    @property
    def mid(self: IntervalMixinProtocol) -> float: ...
    @property
    def is_empty(self: IntervalMixinProtocol) -> bool: ...

class Interval(IntervalMixin, Generic[OrderableT]):
    @overload
    def left(self: Interval[OrderableScalarT]) -> OrderableScalar: ...
    @overload
    def left(self: Interval[OrderableTimesT]) -> OrderableTimes: ...
    @property
    @overload
    def left(self: Interval[OrderableT]) -> Orderable: ...
    @overload
    def right(self: Interval[OrderableScalarT]) -> OrderableScalar: ...
    @overload
    def right(self: Interval[OrderableTimesT]) -> OrderableTimes: ...
    @property
    @overload
    def right(self: Interval[OrderableT]) -> Orderable: ...
    @property
    def closed(self) -> str: ...
    @overload
    def __new__(
        cls,
        left: Timestamp,
        right: Timestamp,
        closed: Union[str, Literal["left", "right", "both", "neither"]] = ...,
    ) -> Interval[Timestamp]: ...
    @overload
    def __new__(
        cls,
        left: Timedelta,
        right: Timedelta,
        closed: Union[str, Literal["left", "right", "both", "neither"]] = ...,
    ) -> Interval[Timedelta]: ...
    @overload
    def __new__(
        cls,
        left: datetime.date,
        right: datetime.date,
        closed: Union[str, Literal["left", "right", "both", "neither"]] = ...,
    ) -> Interval[datetime.date]: ...
    @overload
    def __new__(
        cls,
        left: datetime.datetime,
        right: datetime.datetime,
        closed: Union[str, Literal["left", "right", "both", "neither"]] = ...,
    ) -> Interval[datetime.datetime]: ...
    @overload
    def __new__(
        cls,
        left: datetime.timedelta,
        right: datetime.timedelta,
        closed: Union[str, Literal["left", "right", "both", "neither"]] = ...,
    ) -> Interval[datetime.timedelta]: ...
    @overload
    def __new__(
        cls,
        left: int,
        right: int,
        closed: Union[str, Literal["left", "right", "both", "neither"]] = ...,
    ) -> Interval[int]: ...
    @overload
    def __new__(
        cls,
        left: float,
        right: float,
        closed: Union[str, Literal["left", "right", "both", "neither"]] = ...,
    ) -> Interval[float]: ...
    length: _LengthDescriptor
    def __hash__(self) -> int: ...
    def __contains__(self, key: Orderable) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __add__(self: Interval[OrderableT], y: float) -> Interval[OrderableT]: ...
    def __sub__(self: Interval[OrderableT], y: float) -> Interval[OrderableT]: ...
    def __mul__(self: Interval[OrderableT], y: float) -> Interval[OrderableT]: ...
    def __truediv__(self: Interval[OrderableT], y: float) -> Interval[OrderableT]: ...
    def __floordiv__(self: Interval[OrderableT], y: float) -> Interval[OrderableT]: ...
    def overlaps(self: Interval[OrderableT], other: Interval[OrderableT]) -> bool: ...
