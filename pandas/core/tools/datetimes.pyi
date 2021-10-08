from datetime import datetime as datetime
from numpy import datetime64 as datetime64

from pandas._typing import ArrayLike as ArrayLike
from pandas.core.dtypes.generic import ABCSeries as ABCSeries
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex
from pandas.core.frame import Series as Series, DataFrame as DataFrame
from pandas._libs.tslibs import Timestamp
from typing import Optional, TypeVar, Union, overload

ArrayConvertible = Union[list, tuple, ArrayLike, ABCSeries]
Scalar = Union[int, float, str, Timestamp]
DatetimeScalar = TypeVar('DatetimeScalar', Scalar, datetime)
DatetimeScalarOrArrayConvertible = Union[DatetimeScalar, list, tuple, ArrayLike, Series]

def should_cache(arg: ArrayConvertible, unique_share: float=..., check_count: Optional[int]=...) -> bool: ...

@overload
def to_datetime(
    arg: DataFrame,
    errors: str = ...,
    dayfirst: bool = ...,
    yearfirst: bool = ...,
    utc: Optional[bool] = ...,
    format: Optional[str] = ...,
    exact: bool = ...,
    unit: Optional[str] = ...,
    infer_datetime_format: bool = ...,
    origin: Scalar = ...,
    cache: bool = ...) -> Series[datetime64]: ...
@overload
def to_datetime(
    arg: DatetimeScalar,
    errors: str = ...,
    dayfirst: bool = ...,
    yearfirst: bool = ...,
    utc: Optional[bool] = ...,
    format: Optional[str] = ...,
    exact: bool = ...,
    unit: Optional[str] = ...,
    infer_datetime_format: bool = ...,
    origin: Scalar = ...,
    cache: bool = ...) -> datetime: ...
@overload
def to_datetime(
    arg: Union[list, tuple, ArrayLike],
    errors: str = ...,
    dayfirst: bool = ...,
    yearfirst: bool = ...,
    utc: Optional[bool] = ...,
    format: Optional[str] = ...,
    exact: bool = ...,
    unit: Optional[str] = ...,
    infer_datetime_format: bool = ...,
    origin: Scalar = ...,
    cache: bool = ...) -> DatetimeIndex: ...

def to_time(arg, format = ..., infer_time_format: bool = ..., errors: str = ...): ...
