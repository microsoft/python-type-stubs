import datetime
from io import BufferedIOBase, RawIOBase, TextIOBase, TextIOWrapper
from mmap import mmap
import numpy as np
from numpy import typing as npt
import sys
from os import PathLike
from pathlib import Path
from typing import (
    Any,
    AnyStr,
    Callable,
    Collection,
    Dict,
    Hashable,
    IO,
    List,
    Mapping,
    NewType,
    Optional,
    Sequence,
    Type,
    TypeVar,
    Union,
)

from pandas.core.generic import NDFrame
from pandas._libs.tslibs import Period, Timedelta as Timedelta, Timestamp as Timestamp
from pandas.core.arrays import ExtensionArray
from pandas.core.series import Series
from pandas.core.frame import DataFrame
from pandas.core.indexes.base import Index

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

ArrayLike = Union[ExtensionArray, np.ndarray]
AnyArrayLike = Union[Index, Series]
PythonScalar = Union[str, int, float, bool, complex]
DatetimeLikeScalar = TypeVar("DatetimeLikeScalar", Period, Timestamp, Timedelta)
PandasScalar = Union[bytes, datetime.date, datetime.datetime, datetime.timedelta]
# Scalar = Union[PythonScalar, PandasScalar]
# Dtype: Any

# filenames and file-like-objects
Buffer = Union[IO[AnyStr], RawIOBase, BufferedIOBase, TextIOBase, TextIOWrapper, mmap]
FileOrBuffer = Union[str, Buffer[AnyStr]]
FilePathOrBuffer = Union["PathLike[str]", FileOrBuffer[AnyStr]]

FrameOrSeries = TypeVar("FrameOrSeries", bound=NDFrame)
FrameOrSeriesUnion = Union[DataFrame, Series]
Axis = Union[str, int]
Label = Optional[Hashable]
Level = Union[Label, int]
Ordered = Optional[bool]
JSONSerializable = Union[PythonScalar, List, Dict]
Axes = Collection
Renamer = Union[Mapping[Label, Any], Callable[[Label], Label]]
T = TypeVar("T")
FuncType = Callable[..., Any]
F = TypeVar("F", bound=FuncType)

AggFuncTypeBase = Union[Callable, str]
AggFuncTypeDict = Dict[Hashable, Union[AggFuncTypeBase, List[AggFuncTypeBase]]]
AggFuncType = Union[
    AggFuncTypeBase,
    List[AggFuncTypeBase],
    AggFuncTypeDict,
]

num = Union[int, float]
SeriesAxisType = Union[str, int, Literal["index", 0]]  # Restricted subset of _AxisType for series
AxisType = Union[str, int, Literal["columns", "index", 0, 1]]
Dtype = TypeVar("Dtype", bool, int, float, object)
DtypeNp = TypeVar("DtypeNp", bound=np.dtype)
KeysArgType = Any
ListLike = TypeVar("ListLike", Sequence, np.ndarray, "Series")
StrLike = Union[str, np.str_]
Scalar = Union[str, bytes, datetime.date, datetime.datetime, datetime.timedelta, bool, int, float, complex, Timestamp, Timedelta]
# Refine the next 3 in 3.9 to use the specialized type.
np_ndarray_int64 = npt.NDArray[np.int64]
np_ndarray_bool = npt.NDArray[np.bool_]
np_ndarray_str = npt.NDArray[np.str_]
IndexType = Union[slice, np_ndarray_int64, Index[int], List[int], Series[int]]
MaskType = Union[Series[bool], np_ndarray_bool, Sequence[bool]]
# Scratch types for generics
S1 = TypeVar(
    "S1",
    str,
    bytes,
    datetime.date,
    datetime.datetime,
    datetime.timedelta,
    bool,
    int,
    float,
    complex,
    Timestamp,
    Timedelta,
    np.datetime64,
)
T1 = TypeVar("T1", str, int)
T2 = TypeVar("T2", str, int)

# Interval closed type

IntervalClosedType = Literal["left", "right", "both", "neither"]

DateTimeErrorChoices = Literal["ignore", "raise", "coerce"]
