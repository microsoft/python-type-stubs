from datetime import datetime
#from pandas._libs import tslib as tslib
#from pandas._libs import tslibs as tslibs
#from pandas._libs.tslibs import Timestamp as Timestamp, conversion as conversion, parsing as parsing
#from pandas._libs.tslibs.parsing import DateParseError as DateParseError, parse_time_string as parse_time_string
#from pandas._libs.tslibs.strptime import array_strptime as array_strptime
from pandas._typing import ArrayLike as ArrayLike
#from pandas.arrays import IntegerArray as IntegerArray
#from pandas.core import algorithms as algorithms
#from pandas.core.algorithms import unique as unique
#from pandas.core.dtypes.common import ensure_object as ensure_object, is_datetime64_dtype as is_datetime64_dtype, is_datetime64_ns_dtype as is_datetime64_ns_dtype, is_datetime64tz_dtype as is_datetime64tz_dtype, is_float as is_float, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_numeric_dtype as is_numeric_dtype, is_scalar as is_scalar
#from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCDatetimeIndex as ABCDatetimeIndex, ABCIndex as ABCIndex, ABCIndexClass as ABCIndexClass
from pandas.core.dtypes.generic import ABCSeries as ABCSeries
#from pandas.core.dtypes.missing import notna as notna
from typing import Any, Optional, TypeVar, Union

ArrayConvertible = Union[list, tuple, ArrayLike, ABCSeries]
Scalar = Union[int, float, str]
DatetimeScalar = TypeVar('DatetimeScalar', Scalar, datetime)
DatetimeScalarOrArrayConvertible = Union[DatetimeScalar, list, tuple, ArrayLike, ABCSeries]

def should_cache(arg: ArrayConvertible, unique_share: float=..., check_count: Optional[int]=...) -> bool: ...
def to_datetime(arg: Any, errors: str = ..., dayfirst: bool = ..., yearfirst: bool = ..., utc: Optional[Any] = ..., format: Optional[Any] = ..., exact: bool = ..., unit: Optional[Any] = ..., infer_datetime_format: bool = ..., origin: str = ..., cache: bool = ...): ...
def to_time(arg: Any, format: Optional[Any] = ..., infer_time_format: bool = ..., errors: str = ...): ...
