from __future__ import annotations

import sys
from typing import (
    Any,
    Generic,
    Protocol,
    TypeVar,
    Union,
    overload,
)

import numpy as np

from pandas._typing import (
    Timedelta,
    Timestamp,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

VALID_CLOSED: frozenset

OrderableScalarT = TypeVar("OrderableScalarT", int, float)
OrderableTimesT = TypeVar("OrderableTimesT", Timestamp, Timedelta)
OrderableT = TypeVar("OrderableT", int, float, Timestamp, Timedelta)

class IntervalMixinProtocol(Protocol): ...

class _LengthDescriptor:
    @overload
    def __get__(self, instance: Interval[float], owner: Any) -> float: ...
    @overload
    def __get__(self, instance: Interval[int], owner: Any) -> int: ...
    @overload
    def __get__(self, instance: Interval[OrderableTimesT], owner: Any) -> Timedelta: ...

class _MidDescriptor:
    @overload
    def __get__(self, instance: Interval[OrderableScalarT], owner: Any) -> float: ...
    @overload
    def __get__(self, instance: Interval[Timedelta], owner: Any) -> Timedelta: ...
    @overload
    def __get__(self, instance: Interval[Timestamp], owner: Any) -> Timestamp: ...

class IntervalMixin(IntervalMixinProtocol):
    @property
    def closed_left(self) -> bool: ...
    @property
    def closed_right(self) -> bool: ...
    @property
    def open_left(self) -> bool: ...
    @property
    def open_right(self) -> bool: ...
    mid: _MidDescriptor
    length: _LengthDescriptor
    @property
    def is_empty(self) -> bool: ...
    def _check_closed_matches(self, other: IntervalMixin, name: str = ...): ...

class Interval(IntervalMixin, Generic[OrderableT]):
    @property
    def left(self: Interval[OrderableT]) -> OrderableT: ...
    @property
    def right(self: Interval[OrderableT]) -> OrderableT: ...
    @property
    def closed(self) -> str: ...
    def __init__(
        self,
        left: OrderableT,
        right: OrderableT,
        closed: Literal["left", "right", "both", "neither"] = ...,
    ): ...
    def __hash__(self) -> int: ...
    @overload
    def __contains__(self: Interval[OrderableTimesT], OrderableTimesT) -> bool: ...
    @overload
    def __contains__(self: Interval[int], key: Union[int, float]) -> bool: ...
    @overload
    def __contains__(self: Interval[float], key: Union[int, float]) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    @overload
    def __add__(self: Interval[OrderableTimesT], y: Timedelta) -> Interval[OrderableTimesT]: ...
    @overload
    def __add__(self: Interval[int], y: int) -> Interval[int]: ...
    @overload
    def __add__(self: Interval[int], y: float) -> Interval[float]: ...
    @overload
    def __add__(self: Interval[float], y: Union[int, float]) -> Interval[float]: ...
    @overload
    def __sub__(self: Interval[OrderableTimesT], y: Timedelta) -> Interval[OrderableTimesT]: ...
    @overload
    def __sub__(self: Interval[int], y: int) -> Interval[int]: ...
    @overload
    def __sub__(self: Interval[int], y: float) -> Interval[float]: ...
    @overload
    def __sub__(self: Interval[float], y: Union[int, float]) -> Interval[float]: ...
    @overload
    def __mul__(self: Interval[int], y: int) -> Interval[int]: ...
    @overload
    def __mul__(self: Interval[int], y: float) -> Interval[float]: ...
    @overload
    def __mul__(self: Interval[float], y: Union[int, float]) -> Interval[float]: ...
    @overload
    def __truediv__(self: Interval[int], y: int) -> Interval[int]: ...
    @overload
    def __truediv__(self: Interval[int], y: float) -> Interval[float]: ...
    @overload
    def __truediv__(self: Interval[float], y: Union[int, float]) -> Interval[float]: ...
    @overload
    def __floordiv__(self: Interval[int], y: int) -> Interval[int]: ...
    @overload
    def __floordiv__(self: Interval[int], y: float) -> Interval[float]: ...
    @overload
    def __floordiv__(self: Interval[float], y: Union[int, float]) -> Interval[float]: ...
    def overlaps(self: Interval[OrderableT], other: Interval[OrderableT]) -> bool: ...

def intervals_to_interval_bounds(intervals: np.ndarray, validate_closed: int = ...): ...

class IntervalTree(IntervalMixin):
    def __init__(
        self,
        left: np.ndarray,
        right: np.ndarray,
        closed: Literal["left", "right", "both", "neither"] = ...,
    ): ...
    def get_indexer(self, target) -> np.ndarray: ...
    def get_indexer_non_unique(self, target) -> np.ndarray: ...
    _na_count: int
    @property
    def is_overlapping(self) -> bool: ...
