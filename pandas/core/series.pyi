from __future__ import annotations

import numpy as np
import datetime as dt
import matplotlib
from pathlib import Path
import sys
from pandas._typing import _str, _bool, num, _SeriesAxisType, _AxisType, _DType, _DTypeNp, _StrLike, _Path_or_Buf, _LevelType, _Scalar, _MaskType, _np_ndarray_bool, _np_ndarray_int64, _np_ndarray_str
from pandas.core import base, generic
from pandas.core.arrays import ExtensionArray
from pandas.core.groupby import generic as groupby_generic
from typing import Any, Callable, Dict, Generic, Hashable, IO, Iterable, List, Mapping, NewType, Optional, Sequence, Tuple, Type, TypeVar, Union, overload
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


class _iLocIndexerSeries(Generic[_DType]):
    # get item
    @overload
    def __getitem__(self, idx: int) -> _DType: ...
    @overload
    def __getitem__(self, idx: Index) -> Series[_DType]: ...
    # set item
    @overload
    def __setitem__(self, idx: int, value: _DType) -> None: ...
    @overload
    def __setitem__(self, idx: Index, value: Union[_DType, Series[_DType]]) -> None: ...


class _LocIndexerSeries(Generic[_DType]):
    @overload
    def __getitem__(self, idx: _MaskType,) -> Series[_DType]: ...
    @overload
    def __getitem__(self, idx: Union[int, str],) -> _DType: ...
    @overload
    def __getitem__(self, idx: List[str],) -> Series[_DType]: ...
    @overload
    def __setitem__(self, idx: _MaskType, value: Union[_DType, np.ndarray, Series[_DType]],) -> None: ...
    @overload
    def __setitem__(self, idx: str, value: _DType,) -> None: ...
    @overload
    def __setitem__(self, idx: List[str], value: Union[_DType, np.ndarray, Series[_DType]],) -> None: ...


class Series(base.IndexOpsMixin, generic.NDFrame, Generic[_DType]):

    _ListLike = Union[np.ndarray, List[_DType], Dict[_str, np.ndarray], Sequence, Index]
    def __init__(
        self,
        data: Optional[Union[_ListLike[_DType], Series[_DType], Dict[int, _DType], Dict[_str, _DType]]] = ...,
        index: Union[_str, int, Series, List] = ...,
        dtype: Any = ...,
        name: _str = ...,
        copy: bool = ...,
    ): ...

    hasnans: Any = ...
    def div(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[float]: ...
    def rdiv(
        self,
        other: Union[Series[_DType], _Scalar],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    def __init__(self, data: Optional[Any] = ..., index: Optional[Any] = ..., dtype: Optional[Any] = ..., name: Optional[Any] = ..., copy: bool = ..., fastpath: bool = ...) -> None: ...
    @property
    def dtype(self): ...
    @property
    def dtypes(self): ...
    @property
    def name(self) -> Optional[Hashable]: ...
    @name.setter
    def name(self, value: Optional[Hashable]) -> None: ...
    @property
    def values(self): ...
    @property
    def array(self) -> ExtensionArray: ...
    def ravel(self, order: str = ...): ...
    def __len__(self) -> int: ...
    def view(self, dtype: Optional[Any] = ...): ...
    def __array_ufunc__(self, ufunc: Callable, method: str, *inputs: Any, **kwargs: Any) -> Any: ...
    def __array__(self, dtype: Any=...) -> np.ndarray: ...
    __float__: Any = ...
    __long__: Any = ...
    __int__: Any = ...
    @property
    def axes(self) -> List: ...
    def take(self, indices: Sequence, axis: _SeriesAxisType = ..., is_copy: _bool = ..., **kwargs) -> Series[_DType]: ...
    @overload
    def __getitem__(self, idx: Union[List[_str], Index[int], Series[_DType], slice]) -> Series: ...
    @overload
    def __getitem__(self, idx: Union[int, _str]) -> _DType: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def repeat(self, repeats: Union[int, List[int]], axis: Optional[_SeriesAxisType] = ...) -> Series[_DType]: ...
    @property
    def index(self) -> Index: ...
    def reset_index(
        self, level: Optional[_LevelType] = ..., drop: _bool = ..., name: Optional[object] = ..., inplace: _bool = ...,
    ) -> Series[_DType]: ...
    @overload
    def to_string(
        self,
        buf: Optional[_Path_or_Buf],
        na_rep: _str = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        justify: Optional[_str] = ...,
        max_rows: Optional[int] = ...,
        min_rows: Optional[int] = ...,
        max_cols: Optional[int] = ...,
        show_dimensions: _bool = ...,
        decimal: _str = ...,
        line_width: Optional[int] = ...,
        max_colwidth: Optional[int] = ...,
        encoding: Optional[_str] = ...,
    ) -> None: ...
    @overload
    def to_string(
        self,
        na_rep: _str = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        justify: Optional[_str] = ...,
        max_rows: Optional[int] = ...,
        min_rows: Optional[int] = ...,
        max_cols: Optional[int] = ...,
        show_dimensions: _bool = ...,
        decimal: _str = ...,
        line_width: Optional[int] = ...,
        max_colwidth: Optional[int] = ...,
        encoding: Optional[_str] = ...,
    ) -> _str: ...
    @overload
    def to_markdown(self, buf: Optional[_Path_or_Buf], mode: Optional[_str] = ..., **kwargs) -> None: ...
    @overload
    def to_markdown(self, mode: Optional[_str] = ...,) -> _str: ...
    def items(self) -> Iterable[Tuple[Union[int, _str], _DType]]: ...
    def iteritems(self) -> Iterable[Tuple[Union[int, _str], _DType]]: ...
    def keys(self) -> List: ...
    def to_dict(self, into: Hashable = ...) -> Dict[_str, Any]: ...
    def to_frame(self, name: Optional[object] = ...) -> DataFrame: ...
    def groupby(
        self,
        by: Optional[Any] = ...,
        axis: _SeriesAxisType = ...,
        level: Optional[_LevelType] = ...,
        as_index: _bool = ...,
        sort: _bool = ...,
        group_keys: _bool = ...,
        squeeze: _bool = ...,
        observed: _bool = ...,
    ) -> groupby_generic.SeriesGroupBy: ...
    @overload
    def count(self, level: None = ...) -> int: ...
    @overload
    def count(self, level: _LevelType) -> Series[_DType]: ...
    def mode(self, dropna: Any) -> Series[_DType]: ...
    def unique(self) -> np.ndarray: ...
    def drop_duplicates(self, keep: Literal["first", "last", False] = ..., inplace: _bool = ...) -> Series[_DType]: ...
    def duplicated(self, keep: Literal["first", "last", False] = ...) -> Series[_bool]: ...
    def idxmax(self, axis: _SeriesAxisType = ..., skipna: _bool = ..., *args, **kwargs) -> Union[int, _str]: ...
    def idxmin(self, axis: _SeriesAxisType = ..., skipna: _bool = ..., *args, **kwargs) -> Union[int, _str]: ...
    def round(self, decimals: int = ..., *args, **kwargs) -> Series[_DType]: ...
    @overload
    def quantile(
        self, q: float = ..., interpolation: Literal["linear", "lower", "higher", "midpoint", "nearest"] = ...,
    ) -> float: ...
    @overload
    def quantile(
        self, q: _ListLike = ..., interpolation: Literal["linear", "lower", "higher", "midpoint", "nearest"] = ...,
    ) -> Series[_DType]: ...
    def corr(
        self, other: Series[_DType], method: Literal["pearson", "kendall", "spearman"] = ..., min_periods: int = ...,
    ) -> float: ...
    def cov(self, other: Series[_DType], min_periods: Optional[int] = ...) -> float: ...
    def diff(self, periods: int = ...) -> Series[_DType]: ...
    def autocorr(self, lag: int = ...) -> float: ...
    @overload
    def dot(self, other: Union[DataFrame, Series[_DType]]) -> Series[_DType]: ...
    @overload
    def dot(self, other: _ListLike) -> np.ndarray: ...
    def __matmul__(self, other: Any): ...
    def __rmatmul__(self, other: Any): ...
    @overload
    def searchsorted(
        self, value: _ListLike, side: Literal["left", "right"] = ..., sorter: Optional[_ListLike] = ...,
    ) -> List[int]: ...
    @overload
    def searchsorted(
        self, value: _Scalar, side: Literal["left", "right"] = ..., sorter: Optional[_ListLike] = ...,
    ) -> int: ...
    def append(
        self,
        to_append: Union[Series[Any], Sequence[Series[Any]]],
        ignore_index: _bool = ...,
        verify_integrity: _bool = ...,
    ) -> Series[_DType]: ...
    def combine(
        self, other: Series[_DType], func: Callable, fill_value: Optional[_Scalar] = ...
    ) -> Series[_DType]: ...
    def combine_first(self, other: Series[_DType]) -> Series[_DType]: ...
    def update(self, other: Series[_DType]) -> None: ...
    def sort_values(
        self,
        axis: _SeriesAxisType = ...,
        ascending: _bool = ...,
        inplace: _bool = ...,
        kind: Literal["quicksort", "heapsort", "mergesort"] = ...,
        na_position: Literal["first", "last"] = ...,
        ignore_index: _bool = ...,
    ) -> Series[_DType]: ...
    def sort_index(
        self,
        axis: _SeriesAxisType = ...,
        level: Optional[_LevelType] = ...,
        ascending: _bool = ...,
        inplace: _bool = ...,
        kind: Literal["quicksort", "heapsort", "mergesort"] = ...,
        na_position: Literal["first", "last"] = ...,
        sort_remaining: _bool = ...,
        ignore_index: _bool = ...,
    ) -> Series[_DType]: ...
    def argsort(
        self,
        axis: _SeriesAxisType = ...,
        kind: Literal["mergesort", "quicksort", "heapsort"] = ...,
        order: None = ...,
    ) -> Series[int]: ...
    def nlargest(self, n: int = ..., keep: Literal["first", "last", "all"] = ...) -> Series[_DType]: ...
    def nsmallest(self, n: int = ..., keep: Literal["first", "last", "all"] = ...) -> Series[_DType]: ...
    def swaplevel(self, i: _LevelType = ..., j: _LevelType = ..., copy: _bool = ...) -> Series[_DType]: ...
    def reorder_levels(self, order: List) -> Series[_DType]: ...
    def explode(self) -> Series[_DType]: ...
    def unstack(self, level: _LevelType = ..., fill_value: Optional[Union[int, _str, Dict]] = ...,) -> DataFrame: ...
    def map(self, arg: Any, na_action: Optional[Literal["ignore"]] = ...) -> Series[_DType]: ...
    def aggregate(
        self,
        func: Union[Callable, _str, List[Union[Callable, _str]], Dict[_SeriesAxisType, Union[Callable, _str]],],
        axis: _SeriesAxisType = ...,
        *args,
        **kwargs
    ) -> None: ...
    def agg(
        self,
        func: Union[Callable, _str, List[Union[Callable, _str]], Dict[_SeriesAxisType, Union[Callable, _str]],],
        axis: _SeriesAxisType = ...,
        *args,
        **kwargs
    ) -> None: ...
    def transform(
        self, func: Union[List[Callable], Dict[_str, Callable]], axis: _SeriesAxisType = ..., *args, **kwargs
    ) -> Series[_DType]: ...
    def apply(
        self, func: Callable, convert_dtype: _bool = ..., args: Tuple = ..., **kwds
    ) -> Union[Series, DataFrame]: ...
    def align(
        self,
        other: Union[DataFrame, Series[Any]],
        join: Literal["inner", "outer", "left", "right"] = ...,
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        copy: _bool = ...,
        fill_value: Optional[Any] = ...,
        method: Optional[Literal["backfill", "bfill", "pad", "ffill"]] = ...,
        limit: Optional[int] = ...,
        fill_axis: _SeriesAxisType = ...,
        broadcast_axis: Optional[_SeriesAxisType] = ...,
    ) -> Tuple[Series, Series]: ...
    def rename(
        self,
        index: Optional[Any] = ...,
        *,
        axis: Optional[_SeriesAxisType] = ...,
        copy: _bool = ...,
        inplace: _bool = ...,
        level: Optional[_LevelType] = ...,
        errors: Literal["raise", "ignore"] = ...
    ) -> Series: ...
    def reindex_like(
        self,
        other: Series[_DType],
        method: Optional[Literal["backfill", "bfill", "pad", "ffill", "nearest"]] = ...,
        copy: _bool = ...,
        limit: Optional[int] = ...,
        tolerance: Optional[float] = ...,
    ) -> Series: ...
    def drop(
        self,
        labels: Optional[Union[_str, List]] = ...,
        axis: _SeriesAxisType = ...,
        index: Optional[Union[List[_str], List[int], Index]] = ...,
        columns: Optional[Union[_str, List]] = ...,
        level: Optional[_LevelType] = ...,
        inplace: _bool = ...,
        errors: Literal["ignore", "raise"] = ...,
    ) -> Series: ...
    @overload
    def fillna(
        self,
        value: Union[_DType, Dict, Series[_DType], DataFrame],
        method: Optional[Literal["backfill", "bfill", "pad", "ffill"]] = ...,
        axis: _SeriesAxisType = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True]
    ) -> Series[_DType]: ...
    @overload
    def fillna(
        self,
        value: Union[_DType, Dict, Series[_DType], DataFrame],
        method: Optional[Literal["backfill", "bfill", "pad", "ffill"]] = ...,
        axis: _SeriesAxisType = ...,
        inplace: Literal[False] = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
    ) -> None: ...
    def replace(
        self,
        to_replace: Optional[Union[str, List, Dict, Series[_DType], int, float]] = ...,
        value: Optional[Union[_Scalar, Dict, List, _str]] = ...,
        inplace: _bool = ...,
        limit: Optional[int] = ...,
        regex: Any = ...,
        method: Optional[Literal["pad", "ffill", "bfill"]] = ...,
    ) -> Series[_DType]: ...
    def shift(
        self,
        periods: int = ...,
        freq: Optional[Any] = ...,
        axis: _SeriesAxisType = ...,
        fill_value: Optional[object] = ...,
    ) -> Series[_DType]: ...
    def memory_usage(self, index: _bool = ..., deep: _bool = ...) -> int: ...
    def isin(self, values: Union[Iterable, Series[_DType], Dict]) -> Series[_bool]: ...
    def between(
        self, left: Union[_Scalar, Sequence], right: Union[_Scalar, Sequence], inclusive: _bool = ...,
    ) -> Series[_bool]: ...
    def isna(self) -> Series[_bool]: ...
    def isnull(self) -> Series[_bool]: ...
    def notna(self) -> Series[_bool]: ...
    def notnull(self) -> Series[_bool]: ...
    def dropna(
        self, axis: _SeriesAxisType = ..., inplace: _bool = ..., how: Optional[_str] = ...,
    ) -> Series[_DType]: ...
    def to_timestamp(
        self, freq: Optional[Any] = ..., how: Literal["start", "end", "s", "e"] = ..., copy: _bool = ...,
    ) -> Series[_DType]: ...
    def to_period(self, freq: Optional[_str] = ..., copy: _bool = ...) -> DataFrame: ...
    def str(self) -> _str: ...
    @property
    def dt(self) -> Series: ...
    cat: Any = ...
    def plot(self, **kwargs) -> Union[matplotlib.axes.Axes, np.ndarray]: ...
    sparse: Any = ...
    def hist(
        self,
        by: Optional[object] = ...,
        ax: Optional[matplotlib.axes.Axes] = ...,
        grid: _bool = ...,
        xlabelsize: Optional[int] = ...,
        xrot: Optional[float] = ...,
        ylabelsize: Optional[int] = ...,
        yrot: Optional[float] = ...,
        figsize: Optional[Tuple[float, float]] = ...,
        bins: Union[int, Sequence] = ...,
        backend: Optional[_str] = ...,
        **kwargs
    ) -> matplotlib.axes.SubplotBase: ...
    def swapaxes(self, axis1: _SeriesAxisType, axis2: _SeriesAxisType, copy: _bool = ...) -> Series[_DType]: ...
    def droplevel(self, level: _LevelType, axis: _SeriesAxisType = ...) -> DataFrame: ...
    def pop(self, item: _str) -> Series[_DType]: ...
    def squeeze(self, axis: Optional[_SeriesAxisType] = ...) -> _Scalar: ...
    def __abs__(self) -> Series[_DType]: ...
    def add_prefix(self, prefix: _str) -> Series[_DType]: ...
    def add_suffix(self, suffix: _str) -> Series[_DType]: ...
    def reindex(self, index: Optional[_ListLike] = ..., **kwargs) -> Series[_DType]: ...
    def filter(
        self,
        items: Optional[_ListLike] = ...,
        like: Optional[_str] = ...,
        regex: Optional[_str] = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> Series[_DType]: ...
    def head(self, n: int = ...) -> Series[_DType]: ...
    def tail(self, n: int = ...) -> Series[_DType]: ...
    def sample(
        self,
        n: Optional[int] = ...,
        frac: Optional[float] = ...,
        replace: _bool = ...,
        weights: Optional[Union[_str, _ListLike, np.ndarray]] = ...,
        random_state: Optional[int] = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> Series[_DType]: ...
    @property
    def dtype(self) -> _DType: ...
    @property
    def dtypes(self) -> _DType: ...
    def astype(
        self,
        dtype: Union[Type[_str], Type[int], Type[float]],
        copy: _bool = ...,
        errors: Literal["raise", "ignore"] = ...,
    ) -> Series: ...
    def copy(self, deep: _bool = ...) -> Series[_DType]: ...
    def infer_objects(self) -> Series[_DType]: ...
    def convert_dtypes(
        self,
        infer_objects: _bool = ...,
        convert_string: _bool = ...,
        convert_integer: _bool = ...,
        convert_boolean: _bool = ...,
    ) -> Series[_DType]: ...
    @overload
    def ffill(
        self,
        value: Union[_DType, Dict, Series[_DType], DataFrame],
        axis: _SeriesAxisType,
        inplace: Literal[True],
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
    ) -> Series[_DType]: ...
    @overload
    def ffill(
        self,
        value: Union[_DType, Dict, Series[_DType], DataFrame],
        inplace: Literal[True],
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
    ) -> Series[_DType]: ...
    @overload
    def ffill(
        self,
        value: Union[_DType, Dict, Series[_DType], DataFrame],
        axis: _SeriesAxisType = ...,
        inplace: Literal[False] = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
    ) -> None: ...
    @overload
    def bfill(
        self,
        value: Union[_DType, Dict, Series[_DType], DataFrame],
        axis: _SeriesAxisType = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True]
    ) -> Series[_DType]: ...
    @overload
    def bfill(
        self,
        value: Union[_DType, Dict, Series[_DType], DataFrame],
        axis: _SeriesAxisType = ...,
        inplace: Literal[False] = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
    ) -> None: ...
    def interpolate(
        self,
        method: Literal[
            "linear",
            "time",
            "index",
            "values",
            "pad",
            "nearest",
            "slinear",
            "quadratic",
            "cubic",
            "spline",
            "barycentric",
            "polynomial",
            "krogh",
            "pecewise_polynomial",
            "spline",
            "pchip",
            "akima",
            "from_derivatives",
        ] = ...,
        axis: Optional[_SeriesAxisType] = ...,
        limit: Optional[int] = ...,
        inplace: _bool = ...,
        limit_direction: Optional[Literal["forward", "backward", "both"]] = ...,
        limit_area: Optional[Literal["inside", "outside"]] = ...,
        downcast: Optional[Literal["infer"]] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    def asof(
        self, where: Union[_Scalar, Sequence[_Scalar]], subset: Optional[Union[_str, Sequence[_str]]] = ...,
    ) -> Union[_Scalar, Series[_DType]]: ...
    def notnull(self) -> Series[_bool]: ...
    def clip(
        self,
        lower: Optional[float] = ...,
        upper: Optional[float] = ...,
        axis: Optional[_SeriesAxisType] = ...,
        inplace: _bool = ...,
        *args,
        **kwargs
    ) -> Series[_DType]: ...
    def asfreq(
        self,
        freq: Any,
        method: Optional[Literal["backfill", "bfill", "pad", "ffill"]] = ...,
        how: Optional[Literal["start", "end"]] = ...,
        normalize: _bool = ...,
        fill_value: Optional[_Scalar] = ...,
    ) -> Series[_DType]: ...
    def at_time(
        self, time: Union[_str, dt.time], asof: _bool = ..., axis: Optional[_SeriesAxisType] = ...,
    ) -> Series[_DType]: ...
    def between_time(
        self,
        start_time: Union[_str, dt.time],
        end_time: Union[_str, dt.time],
        include_start: _bool = ...,
        include_end: _bool = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> Series[_DType]: ...
    # Next one should return a 'Resampler' object
    def resample(
        self,
        rule: Any,
        axis: _SeriesAxisType = ...,
        closed: Optional[_str] = ...,
        label: Optional[_str] = ...,
        convention: Literal["start", "end", "s", "e"] = ...,
        kind: Optional[Literal["timestamp", "period"]] = ...,
        loffset: Optional[Any] = ...,
        base: int = ...,
        on: Optional[str] = ...,
        level: Optional[_LevelType] = ...,
    ) -> Any: ...
    def first(self, offset: Any) -> Series[_DType]: ...
    def last(self, offset: Any) -> Series[_DType]: ...
    def rank(
        self,
        axis: _SeriesAxisType = ...,
        method: Literal["average", "min", "max", "first", "dense"] = ...,
        numeric_only: Optional[_bool] = ...,
        na_option: Literal["keep", "top", "bottom"] = ...,
        ascending: _bool = ...,
        pct: _bool = ...,
    ) -> Series: ...
    def where(
        self,
        cond: Union[Series[_DType], Series[_DType], np.ndarray],
        other: Any = ...,
        inplace: _bool = ...,
        axis: Optional[_SeriesAxisType] = ...,
        level: Optional[_LevelType] = ...,
        errors: _str = ...,
        try_cast: _bool = ...,
    ) -> Series[_DType]: ...
    def mask(
        self,
        cond: Union[Series[_DType], np.ndarray, Callable],
        other: Union[_Scalar, Series[_DType], DataFrame, Callable] = ...,
        inplace: _bool = ...,
        axis: Optional[_SeriesAxisType] = ...,
        level: Optional[_LevelType] = ...,
        errors: Literal["raise", "ignore"] = ...,
        try_cast: _bool = ...,
    ) -> Series[_DType]: ...
    def slice_shift(self, periods: int = ..., axis: _SeriesAxisType = ...) -> Series[_DType]: ...
    def tshift(self, periods: int = ..., freq: Any = ..., axis: _SeriesAxisType = ...) -> Series[_DType]: ...
    def truncate(
        self,
        before: Optional[Union[dt.date, _str, int]] = ...,
        after: Optional[Union[dt.date, _str, int]] = ...,
        axis: Optional[_SeriesAxisType] = ...,
        copy: _bool = ...,
    ) -> Series[_DType]: ...
    def tz_convert(
        self, tz: Any, axis: _SeriesAxisType = ..., level: Optional[_LevelType] = ..., copy: _bool = ...,
    ) -> Series[_DType]: ...
    def tz_localize(
        self,
        tz: Any,
        axis: _SeriesAxisType = ...,
        level: Optional[_LevelType] = ...,
        copy: _bool = ...,
        ambiguous: Any = ...,
        nonexistent: _str = ...,
    ) -> Series[_DType]: ...
    def abs(self) -> Series[_DType]: ...
    def describe(
        self,
        percentiles: Optional[List[float]] = ...,
        include: Optional[Union[Literal["all"], List[_DType]]] = ...,
        exclude: Optional[List[_DType]] = ...,
    ) -> Series[_DType]: ...
    def pct_change(
        self,
        periods: int = ...,
        fill_method: _str = ...,
        limit: Optional[int] = ...,
        freq: Optional[Any] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    def first_valid_index(self) -> _Scalar: ...
    def last_valid_index(self) -> _Scalar: ...
    def value_counts(
        self,
        normalize: _bool = ...,
        sort: _bool = ...,
        ascending: _bool = ...,
        bins: Optional[int] = ...,
        dropna: _bool = ...,
    ) -> Series[_DType]: ...
    def transpose(self, *args, **kwargs) -> Series[_DType]: ...
    @property
    def T(self) -> Series[_DType]: ...

    # The rest of these were left over from the old 
    # stubs we shipped in preview. They may belong in 
    # the base classes in some cases; I expect stubgen
    # just failed to generate these so I couldn't match 
    # them up.

    def __add__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __and__(self, other: Union[_ListLike, Series[_DType]]) -> Series[_bool]: ...
    # def __array__(self, dtype: Optional[_bool] = ...) -> _np_ndarray
    def __div__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __eq__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_bool]: ...
    def __floordiv__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[int]: ...
    def __ge__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_bool]: ...
    def __gt__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_bool]: ...
    # def __iadd__(self, other: _DType) -> Series[_DType]: ...
    # def __iand__(self, other: _DType) -> Series[_bool]: ...
    # def __idiv__(self, other: _DType) -> Series[_DType]: ...
    # def __ifloordiv__(self, other: _DType) -> Series[_DType]: ...
    # def __imod__(self, other: _DType) -> Series[_DType]: ...
    # def __imul__(self, other: _DType) -> Series[_DType]: ...
    # def __ior__(self, other: _DType) -> Series[_bool]: ...
    # def __ipow__(self, other: _DType) -> Series[_DType]: ...
    # def __isub__(self, other: _DType) -> Series[_DType]: ...
    # def __itruediv__(self, other: _DType) -> Series[_DType]: ...
    # def __itruediv__(self, other: Any) -> None: ...
    # def __ixor__(self, other: _DType) -> Series[_bool]: ...
    def __le__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_bool]: ...
    def __lt__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_bool]: ...
    def __mul__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __mod__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __ne__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_bool]: ...
    def __pow__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __or__(self, other: Union[_ListLike, Series[_DType]]) -> Series[_bool]: ...
    def __radd__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __rand__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_bool]: ...
    def __rdiv__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __rdivmod__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __rfloordiv__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __rmod__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __rmul__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __rnatmul__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __rpow__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __ror__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_bool]: ...
    def __rsub__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __rtruediv__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __rxor__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_bool]: ...
    def __sub__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __truediv__(self, other: Union[num, _ListLike, Series[_DType]]) -> Series[_DType]: ...
    def __xor__(self, other: Union[_ListLike, Series[_DType]]) -> Series: ...
    # properties
    # @property
    # def array(self) -> _npndarray
    @property
    def at(self) -> _LocIndexerSeries[_DType]: ...

    # @property
    # def cat(self) -> ?
    @property
    def hasnans(self) -> bool: ...
    @property
    def iat(self) -> _iLocIndexerSeries[_DType]: ...
    @property
    def iloc(self) -> _iLocIndexerSeries[_DType]: ...
    @property
    def loc(self) -> _LocIndexerSeries[_DType]: ...

    # Methods
    def add(
        self,
        other: Union[Series[_DType], _Scalar],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: Literal[0] = ...,
    ) -> Series[_DType]: ...
    def all(
        self,
        axis: _SeriesAxisType = ...,
        bool_only: Optional[_bool] = ...,
        skipna: _bool = ...,
        level: Optional[_LevelType] = ...,
        **kwargs
    ) -> _bool: ...
    def any(
        self,
        axis: _SeriesAxisType = ...,
        bool_only: Optional[_bool] = ...,
        skipna: _bool = ...,
        level: Optional[_LevelType] = ...,
        **kwargs
    ) -> _bool: ...
    def cummax(
        self, axis: Optional[_SeriesAxisType] = ..., skipna: _bool = ..., *args, **kwargs
    ) -> Series[_DType]: ...
    def cummin(
        self, axis: Optional[_SeriesAxisType] = ..., skipna: _bool = ..., *args, **kwargs
    ) -> Series[_DType]: ...
    def cumprod(
        self, axis: Optional[_SeriesAxisType] = ..., skipna: _bool = ..., *args, **kwargs
    ) -> Series[_DType]: ...
    def cumsum(
        self, axis: Optional[_SeriesAxisType] = ..., skipna: _bool = ..., *args, **kwargs
    ) -> Series[_DType]: ...
    def divide(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[float]: ...
    def divmod(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    def eq(
        self,
        other: Union[_Scalar, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_bool]: ...
    def ewm(
        self,
        com: Optional[float] = ...,
        span: Optional[float] = ...,
        halflife: Optional[float] = ...,
        alpha: Optional[float] = ...,
        min_periods: int = ...,
        adjust: _bool = ...,
        ignore_na: _bool = ...,
        axis: _SeriesAxisType = ...,
    ) -> DataFrame: ...
    def expanding(self, min_periods: int = ..., center: _bool = ..., axis: _SeriesAxisType = ...) -> DataFrame: ...
    def floordiv(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> Series[int]: ...
    def ge(
        self,
        other: Union[_Scalar, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_bool]: ...
    def gt(
        self,
        other: Union[_Scalar, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_bool]: ...
    def item(self) -> _DType: ...
    @overload
    def kurt(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def kurt(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> _Scalar: ...
    @overload
    def kurtosis(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Optional[_LevelType],
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def kurtosis(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> _Scalar: ...
    def le(
        self,
        other: Union[_Scalar, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_bool]: ...
    def lt(
        self,
        other: Union[_Scalar, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_bool]: ...
    @overload
    def mad(
        self, axis: Optional[_SeriesAxisType] = ..., skipna: _bool = ..., *, level: Optional[_LevelType], **kwargs
    ) -> Series[_DType]: ...
    @overload
    def mad(
        self, axis: Optional[_SeriesAxisType] = ..., skipna: _bool = ..., level: None = ..., **kwargs
    ) -> _Scalar: ...
    @overload
    def max(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def max(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> _DType: ...
    @overload
    def mean(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def mean(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> _DType: ...
    @overload
    def median(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def median(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> _DType: ...
    @overload
    def min(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def min(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: _bool = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> _DType: ...
    def mod(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> Series[_DType]: ...
    def mul(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> Series[_DType]: ...
    def multiply(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> Series[_DType]: ...
    def ne(
        self,
        other: Union[_Scalar, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_bool]: ...
    def nunique(self, dropna: _bool = ...) -> int: ...
    def pow(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> Series[_DType]: ...
    @overload
    def prod(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def prod(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs
    ) -> _Scalar: ...
    @overload
    def product(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def product(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs
    ) -> _Scalar: ...
    def radd(
        self,
        other: Union[Series[_DType], _Scalar],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    def ravel(self, order: _str = ...) -> np.ndarray: ...
    def rdivmod(
        self,
        other: Union[Series[_DType], _Scalar],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    def rfloordiv(
        self,
        other: Any,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[Union[float, None]] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    def rmod(
        self,
        other: Union[Series[_DType], _Scalar],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    def rmul(
        self,
        other: Union[Series[_DType], _Scalar],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    # Next one should return a window class
    def rolling(
        self,
        window: Any,
        min_periods: Optional[int] = ...,
        center: _bool = ...,
        win_type: Optional[_str] = ...,
        on: Optional[_str] = ...,
        axis: _SeriesAxisType = ...,
        closed: Optional[_str] = ...,
    ) -> Any: ...
    def rpow(
        self,
        other: Union[Series[_DType], _Scalar],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    def rsub(
        self,
        other: Union[Series[_DType], _Scalar],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    def rtruediv(
        self,
        other: Any,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[Union[float, None]] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[_DType]: ...
    @overload
    def sem(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def sem(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> _Scalar: ...
    @overload
    def skew(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def skew(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> _Scalar: ...
    @overload
    def std(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[float]: ...
    @overload
    def std(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> float: ...
    def sub(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> float: ...
    def subtract(
        self,
        other: Union[num, _ListLike, Series[_DType]],
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[_SeriesAxisType] = ...,
    ) -> float: ...
    def sum(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: Optional[_LevelType] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs
    ) -> float: ...
    def to_list(self) -> List: ...
    def to_numpy(
        self, dtype: Optional[Type[_DTypeNp]] = ..., copy: _bool = ..., na_value: Any = ..., **kwargs
    ) -> np.ndarray: ...
    def to_records(
        self,
        index: _bool = ...,
        column_dtypes: Optional[Union[_str, Dict]] = ...,
        index_dtypes: Optional[Union[_str, Dict]] = ...,
    ) -> Any: ...
    def tolist(self) -> List: ...
    def truediv(
        self,
        other: Any,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[Union[float, None]] = ...,
        axis: _SeriesAxisType = ...,
    ) -> Series[float]: ...
    @overload
    def var(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def var(
        self,
        axis: Optional[_SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> _Scalar: ...
    def view(self, dtype: Optional[Any] = ...) -> Series[_DType]: ...


from pandas.core.index import Index
from pandas.core.frame import DataFrame