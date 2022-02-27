from __future__ import annotations
import numpy as np
import sys
from datetime import datetime, timedelta, tzinfo
from .timestamps import Timestamp
from pandas.tseries.offsets import DateOffset
from typing import Any, Literal, Optional, Set, Type, Union

nat_strings: Set[str] = ...
iNaT: int = ...

class _NaT(datetime):

    __array_priority__: int = ...
    def __richcmp__(self, other: object, op: int) -> bool: ...
    def __add__(self, other) -> _NaT: ...
    def __pos__(self) -> _NaT: ...
    def __neg__(self) -> _NaT: ...
    def __truediv__(self, other) -> _NaT: ...
    def __floordiv__(self, other) -> _NaT: ...
    def __mul__(self, other) -> _NaT: ...
    @property
    def asm8(self) -> np.datetime64: ...
    def to_datetime64(self) -> np.datetime64: ...
    def to_numpy(self, dtype: Any, copy: bool = ...) -> np.datetime64: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> _NaT: ...
    def __long__(self) -> _NaT: ...
    @property
    def is_leap_year(self) -> bool: ...
    @property
    def is_month_start(self) -> bool: ...
    @property
    def is_quarter_start(self) -> bool: ...
    @property
    def is_year_start(self) -> bool: ...
    @property
    def is_month_end(self) -> bool: ...
    @property
    def is_quarter_end(self) -> bool: ...
    @property
    def is_year_end(self) -> bool: ...

class NaTType(_NaT):
    def __new__(cls) -> NaTType: ...
    def __reduce__(self) -> Any: ...
    def __rdiv__(self, other) -> _NaT: ...
    def __rtruediv__(self, other) -> _NaT: ...
    def __rfloordiv__(self, other) -> _NaT: ...
    def __rmul__(self, other) -> _NaT: ...
    @property
    def year(self) -> float: ...  # type: ignore[override]
    @property
    def quarter(self) -> float: ...
    @property
    def month(self) -> float: ...  # type: ignore[override]
    @property
    def day(self) -> float: ...  # type: ignore[override]
    @property
    def hour(self) -> float: ...  # type: ignore[override]
    @property
    def minute(self) -> float: ...  # type: ignore[override]
    @property
    def second(self) -> float: ...  # type: ignore[override]
    @property
    def millisecond(self) -> float: ...
    @property
    def microsecond(self) -> float: ...  # type: ignore[override]
    @property
    def nanosecond(self) -> float: ...
    @property
    def week(self) -> float: ...
    @property
    def dayofyear(self) -> float: ...
    @property
    def weekofyear(self) -> float: ...
    @property
    def days_in_month(self) -> float: ...
    @property
    def daysinmonth(self) -> float: ...
    @property
    def dayofweek(self) -> float: ...
    @property
    def days(self) -> float: ...
    @property
    def seconds(self) -> float: ...
    @property
    def microseconds(self) -> float: ...
    @property
    def nanoseconds(self) -> float: ...
    @property
    def qyear(self) -> float: ...
    @property
    def weekday(self) -> float: ...  # type: ignore[override]
    @property
    def isoweekday(self) -> float: ...  # type: ignore[override]
    @property
    def total_seconds(self) -> float: ...
    def month_name(self, locale: Optional[str] = ...) -> str: ...
    def day_name(self, locale: Optional[str] = ...) -> str: ...
    def date(self) -> NaTType: ...
    def dst(self) -> None: ...
    def tzname(self) -> None: ...
    def utcoffset(self) -> None: ...
    def timestamp(self) -> float: ...
    def to_pydatetime(self) -> datetime: ...
    @classmethod
    def now(cls, tz: Optional[tzinfo] = ...) -> NaTType: ...
    @classmethod
    def today(cls) -> NaTType: ...
    def round(
        self,
        freq: str,
        ambiguous: Union[bool, str, Literal["raise", "NaT"]] = ...,
        nonexistent: Union[str, Literal["raise", "shift_forward", "shift_backward", "NaT"], timedelta] = ...,
    ) -> Timestamp: ...
    def floor(
        self,
        freq: str,
        ambiguous: Union[bool, str, Literal["raise", "NaT"]] = ...,
        nonexistent: Union[str, Literal["raise", "shift_forward", "shift_backward", "NaT"], timedelta] = ...,
    ) -> Timestamp: ...
    def ceil(
        self,
        freq: str,
        ambiguous: Union[bool, str, Literal["raise", "NaT"]] = ...,
        nonexistent: Union[str, Literal["raise", "shift_forward", "shift_backward", "NaT"], timedelta] = ...,
    ) -> Timestamp: ...
    def tz_convert(self, tz: Any) -> Timestamp: ...
    def tz_localizel(
        self,
        tz: Any,
        ambiguous: Union[bool, str, Literal["raise", "NaT"]] = ...,
        nonexistent: Union[str, Literal["raise", "shift_forward", "shift_backward", "NaT"], timedelta] = ...,
    ) -> Timestamp: ...
    def replace(  # type: ignore[override]
        self,
        year: Optional[int] = ...,
        month: Optional[int] = ...,
        day: Optional[int] = ...,
        hour: Optional[int] = ...,
        minute: Optional[int] = ...,
        second: Optional[int] = ...,
        microsecond: Optional[int] = ...,
        nanosecond: Optional[int] = ...,
        tzinfo: Any = ...,
        fold: int = ...,
    ) -> Timestamp: ...

NaT: NaTType = ...

def checknull_with_nat(val: object) -> bool: ...
def is_null_datetimelike(val: object, inat_is_null: bool = ...) -> bool: ...
