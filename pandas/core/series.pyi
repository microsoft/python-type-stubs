import numpy as np
from datetime import time, date
from matplotlib.axes import Axes as PlotAxes, SubplotBase as SubplotBase
import sys
from .base import IndexOpsMixin
from .generic import NDFrame
from .indexing import _iLocIndexer, _LocIndexer
from .frame import DataFrame
from pandas.core.arrays.base import ExtensionArray
from pandas.core.groupby import generic as groupby_generic
from pandas.core.indexes.base import Index
from pandas._typing import AxisType as AxisType, Dtype as Dtype, DtypeNp as DtypeNp, FilePathOrBuffer as FilePathOrBuffer, Level as Level, MaskType as MaskType, Scalar as Scalar, SeriesAxisType as SeriesAxisType, num as num
from typing import Any, Callable, Dict, Generic, Hashable, Iterable, List, Optional, Sequence, Tuple, Type, Union, overload
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

_bool = bool
_str = str

class _iLocIndexerSeries(_iLocIndexer, Generic[Dtype]):
    # get item
    @overload
    def __getitem__(self, idx: int) -> Dtype: ...
    @overload
    def __getitem__(self, idx: Index) -> Series[Dtype]: ...
    # set item
    @overload
    def __setitem__(self, idx: int, value: Dtype) -> None: ...
    @overload
    def __setitem__(self, idx: Index, value: Union[Dtype, Series[Dtype]]) -> None: ...


class _LocIndexerSeries(_LocIndexer, Generic[Dtype]):
    @overload
    def __getitem__(self, idx: MaskType,) -> Series[Dtype]: ...
    @overload
    def __getitem__(self, idx: Union[int, str],) -> Dtype: ...
    @overload
    def __getitem__(self, idx: List[str],) -> Series[Dtype]: ...
    @overload
    def __setitem__(self, idx: MaskType, value: Union[Dtype, np.ndarray, Series[Dtype]], ) -> None: ...
    @overload
    def __setitem__(self, idx: str, value: Dtype, ) -> None: ...
    @overload
    def __setitem__(self, idx: List[str], value: Union[Dtype, np.ndarray, Series[Dtype]], ) -> None: ...


class Series(IndexOpsMixin, NDFrame, Generic[Dtype]):

    _ListLike = Union[np.ndarray, List[Dtype], Dict[_str, np.ndarray], Sequence, Index]
    def __init__(
        self,
        data: Optional[Union[_ListLike, Series[Dtype], Dict[int, Dtype], Dict[_str, Dtype]]] = ...,
        index: Union[_str, int, Series, List] = ...,
        dtype = ...,
        name: _str = ...,
        copy: bool = ...,
        fastpath: bool = ...
    ): ...
    @property
    def hasnans(self) -> bool: ...
    def div(
        self,
        other: Union[num, _ListLike, Series[Dtype]],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: SeriesAxisType = ...,
    ) -> Series[float]: ...
    def rdiv(
        self,
        other: Union[Series[Dtype], Scalar],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: SeriesAxisType = ...,
    ) -> Series[Dtype]: ...
    @property
    def dtype(self) -> Dtype: ...
    @property
    def dtypes(self) -> Dtype: ...
    @property
    def name(self) -> Optional[Hashable]: ...
    @name.setter
    def name(self, value: Optional[Hashable]) -> None: ...
    @property
    def values(self): ...
    @property
    def array(self) -> ExtensionArray: ...
    def ravel(self, order: _str = ...) -> np.ndarray: ...
    def __len__(self) -> int: ...
    def view(self, dtype = ...) -> Series[Dtype]: ...
    def __array_ufunc__(self, ufunc: Callable, method: _str, *inputs, **kwargs) : ...
    def __array__(self, dtype=...) -> np.ndarray: ...
    def __float__(self) -> Series[np.float]: ...
    def __long__(self) -> Series[np.long]: ...
    def __int__(self) -> Series[np.int]: ...
    @property
    def axes(self) -> List: ...
    def take(self, indices: Sequence, axis: SeriesAxisType = ..., is_copy: _bool = ..., **kwargs) -> Series[Dtype]: ...
    @overload
    def __getitem__(self, idx: Union[List[_str], Index[int], Series[Dtype], slice]) -> Series: ...
    @overload
    def __getitem__(self, idx: Union[int, _str]) -> Dtype: ...
    def __setitem__(self, key, value) -> None: ...
    def repeat(self, repeats: Union[int, List[int]], axis: Optional[SeriesAxisType] = ...) -> Series[Dtype]: ...
    @property
    def index(self) -> Index: ...
    def reset_index(
        self, level: Optional[Level] = ..., drop: _bool = ..., name: Optional[object] = ..., inplace: _bool = ...,
    ) -> Series[Dtype]: ...
    @overload
    def to_string(
        self,
        buf: Optional[FilePathOrBuffer],
        na_rep: _str = ...,
        formatters = ...,
        float_format = ...,
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
        formatters = ...,
        float_format = ...,
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
    def to_markdown(self, buf: Optional[FilePathOrBuffer], mode: Optional[_str] = ..., **kwargs) -> None: ...
    @overload
    def to_markdown(self, mode: Optional[_str] = ...,) -> _str: ...
    def items(self) -> Iterable[Tuple[Union[int, _str], Dtype]]: ...
    def iteritems(self) -> Iterable[Tuple[Union[int, _str], Dtype]]: ...
    def keys(self) -> List: ...
    def to_dict(self, into: Hashable = ...) -> Dict[_str, Any]: ...
    def to_frame(self, name: Optional[object] = ...) -> DataFrame: ...
    def groupby(
        self,
        by = ...,
        axis: SeriesAxisType = ...,
        level: Optional[Level] = ...,
        as_index: _bool = ...,
        sort: _bool = ...,
        group_keys: _bool = ...,
        squeeze: _bool = ...,
        observed: _bool = ...,
    ) -> groupby_generic.SeriesGroupBy: ...
    @overload
    def count(self, level: None = ...) -> int: ...
    @overload
    def count(self, level: Level) -> Series[Dtype]: ...
    def mode(self, dropna) -> Series[Dtype]: ...
    def unique(self) -> np.ndarray: ...
    def drop_duplicates(self, keep: Literal["first", "last", False] = ..., inplace: _bool = ...) -> Series[Dtype]: ...
    def duplicated(self, keep: Literal["first", "last", False] = ...) -> Series[_bool]: ...
    def idxmax(self, axis: SeriesAxisType = ..., skipna: _bool = ..., *args, **kwargs) -> Union[int, _str]: ...
    def idxmin(self, axis: SeriesAxisType = ..., skipna: _bool = ..., *args, **kwargs) -> Union[int, _str]: ...
    def round(self, decimals: int = ..., *args, **kwargs) -> Series[Dtype]: ...
    @overload
    def quantile(
        self, q: float = ..., interpolation: Literal["linear", "lower", "higher", "midpoint", "nearest"] = ...,
    ) -> float: ...
    @overload
    def quantile(
        self, q: _ListLike = ..., interpolation: Literal["linear", "lower", "higher", "midpoint", "nearest"] = ...,
    ) -> Series[Dtype]: ...
    def corr(
        self, other: Series[Dtype], method: Literal["pearson", "kendall", "spearman"] = ..., min_periods: int = ...,
    ) -> float: ...
    def cov(self, other: Series[Dtype], min_periods: Optional[int] = ...) -> float: ...
    def diff(self, periods: int = ...) -> Series[Dtype]: ...
    def autocorr(self, lag: int = ...) -> float: ...
    @overload
    def dot(self, other: Union[DataFrame, Series[Dtype]]) -> Series[Dtype]: ...
    @overload
    def dot(self, other: _ListLike) -> np.ndarray: ...
    def __matmul__(self, other): ...
    def __rmatmul__(self, other): ...
    @overload
    def searchsorted(
        self, value: _ListLike, side: Literal["left", "right"] = ..., sorter: Optional[_ListLike] = ...,
    ) -> List[int]: ...
    @overload
    def searchsorted(
        self, value: Scalar, side: Literal["left", "right"] = ..., sorter: Optional[_ListLike] = ...,
    ) -> int: ...
    def append(
        self,
        to_append: Union[Series, Sequence[Series]],
        ignore_index: _bool = ...,
        verify_integrity: _bool = ...,
    ) -> Series[Dtype]: ...
    def combine(
        self, other: Series[Dtype], func: Callable, fill_value: Optional[Scalar] = ...
    ) -> Series[Dtype]: ...
    def combine_first(self, other: Series[Dtype]) -> Series[Dtype]: ...
    def update(self, other: Series[Dtype]) -> None: ...
    def sort_values(
        self,
        axis: SeriesAxisType = ...,
        ascending: _bool = ...,
        inplace: _bool = ...,
        kind: Literal["quicksort", "heapsort", "mergesort"] = ...,
        na_position: Literal["first", "last"] = ...,
        ignore_index: _bool = ...,
    ) -> Series[Dtype]: ...
    def sort_index(
        self,
        axis: SeriesAxisType = ...,
        level: Optional[Level] = ...,
        ascending: _bool = ...,
        inplace: _bool = ...,
        kind: Literal["quicksort", "heapsort", "mergesort"] = ...,
        na_position: Literal["first", "last"] = ...,
        sort_remaining: _bool = ...,
        ignore_index: _bool = ...,
    ) -> Series[Dtype]: ...
    def argsort(
        self,
        axis: SeriesAxisType = ...,
        kind: Literal["mergesort", "quicksort", "heapsort"] = ...,
        order: None = ...,
    ) -> Series[int]: ...
    def nlargest(self, n: int = ..., keep: Literal["first", "last", "all"] = ...) -> Series[Dtype]: ...
    def nsmallest(self, n: int = ..., keep: Literal["first", "last", "all"] = ...) -> Series[Dtype]: ...
    def swaplevel(self, i: Level = ..., j: Level = ..., copy: _bool = ...) -> Series[Dtype]: ...
    def reorder_levels(self, order: List) -> Series[Dtype]: ...
    def explode(self) -> Series[Dtype]: ...
    def unstack(self, level: Level = ..., fill_value: Optional[Union[int, _str, Dict]] = ...,) -> DataFrame: ...
    def map(self, arg, na_action: Optional[Literal["ignore"]] = ...) -> Series[Dtype]: ...
    def aggregate(
        self,
        func: Union[Callable, _str, List[Union[Callable, _str]], Dict[SeriesAxisType, Union[Callable, _str]],],
        axis: SeriesAxisType = ...,
        *args,
        **kwargs
    ) -> None: ...
    def agg(
        self,
        func: Union[Callable, _str, List[Union[Callable, _str]], Dict[SeriesAxisType, Union[Callable, _str]],],
        axis: SeriesAxisType = ...,
        *args,
        **kwargs
    ) -> None: ...
    def transform(
        self, func: Union[List[Callable], Dict[_str, Callable]], axis: SeriesAxisType = ..., *args, **kwargs
    ) -> Series[Dtype]: ...
    def apply(
        self, func: Callable, convertDType: _bool = ..., args: Tuple = ..., **kwds
    ) -> Union[Series, DataFrame]: ...
    def align(
        self,
        other: Union[DataFrame, Series],
        join: Literal["inner", "outer", "left", "right"] = ...,
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        copy: _bool = ...,
        fill_value = ...,
        method: Optional[Literal["backfill", "bfill", "pad", "ffill"]] = ...,
        limit: Optional[int] = ...,
        fill_axis: SeriesAxisType = ...,
        broadcast_axis: Optional[SeriesAxisType] = ...,
    ) -> Tuple[Series, Series]: ...
    def rename(
        self,
        index = ...,
        *,
        axis: Optional[SeriesAxisType] = ...,
        copy: _bool = ...,
        inplace: _bool = ...,
        level: Optional[Level] = ...,
        errors: Literal["raise", "ignore"] = ...
    ) -> Series: ...
    def reindex_like(
        self,
        other: Series[Dtype],
        method: Optional[Literal["backfill", "bfill", "pad", "ffill", "nearest"]] = ...,
        copy: _bool = ...,
        limit: Optional[int] = ...,
        tolerance: Optional[float] = ...,
    ) -> Series: ...
    def drop(
        self,
        labels: Optional[Union[_str, List]] = ...,
        axis: SeriesAxisType = ...,
        index: Optional[Union[List[_str], List[int], Index]] = ...,
        columns: Optional[Union[_str, List]] = ...,
        level: Optional[Level] = ...,
        inplace: _bool = ...,
        errors: Literal["ignore", "raise"] = ...,
    ) -> Series: ...
    @overload
    def fillna(
        self,
        value: Union[Dtype, Dict, Series[Dtype], DataFrame],
        method: Optional[Literal["backfill", "bfill", "pad", "ffill"]] = ...,
        axis: SeriesAxisType = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True]
    ) -> Series[Dtype]: ...
    @overload
    def fillna(
        self,
        value: Union[Dtype, Dict, Series[Dtype], DataFrame],
        method: Optional[Literal["backfill", "bfill", "pad", "ffill"]] = ...,
        axis: SeriesAxisType = ...,
        inplace: Literal[False] = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
    ) -> None: ...
    def replace(
        self,
        to_replace: Optional[Union[_str, List, Dict, Series[Dtype], int, float]] = ...,
        value: Optional[Union[Scalar, Dict, List, _str]] = ...,
        inplace: _bool = ...,
        limit: Optional[int] = ...,
        regex = ...,
        method: Optional[Literal["pad", "ffill", "bfill"]] = ...,
    ) -> Series[Dtype]: ...
    def shift(
        self,
        periods: int = ...,
        freq = ...,
        axis: SeriesAxisType = ...,
        fill_value: Optional[object] = ...,
    ) -> Series[Dtype]: ...
    def memory_usage(self, index: _bool = ..., deep: _bool = ...) -> int: ...
    def isin(self, values: Union[Iterable, Series[Dtype], Dict]) -> Series[_bool]: ...
    def between(
        self, left: Union[Scalar, Sequence], right: Union[Scalar, Sequence], inclusive: _bool = ...,
    ) -> Series[_bool]: ...
    def isna(self) -> Series[_bool]: ...
    def isnull(self) -> Series[_bool]: ...
    def notna(self) -> Series[_bool]: ...
    def notnull(self) -> Series[_bool]: ...
    def dropna(
        self, axis: SeriesAxisType = ..., inplace: _bool = ..., how: Optional[_str] = ...,
    ) -> Series[Dtype]: ...
    def to_timestamp(
        self, freq = ..., how: Literal["start", "end", "s", "e"] = ..., copy: _bool = ...,
    ) -> Series[Dtype]: ...
    def to_period(self, freq: Optional[_str] = ..., copy: _bool = ...) -> DataFrame: ...
    def str(self) -> _str: ...
    @property
    def dt(self) -> Series: ...
    cat = ...
    def plot(self, **kwargs) -> Union[PlotAxes, np.ndarray]: ...
    sparse = ...
    def hist(
        self,
        by: Optional[object] = ...,
        ax: Optional[PlotAxes] = ...,
        grid: _bool = ...,
        xlabelsize: Optional[int] = ...,
        xrot: Optional[float] = ...,
        ylabelsize: Optional[int] = ...,
        yrot: Optional[float] = ...,
        figsize: Optional[Tuple[float, float]] = ...,
        bins: Union[int, Sequence] = ...,
        backend: Optional[_str] = ...,
        **kwargs
    ) -> SubplotBase: ...
    def swapaxes(self, axis1: SeriesAxisType, axis2: SeriesAxisType, copy: _bool = ...) -> Series[Dtype]: ...
    def droplevel(self, level: Level, axis: SeriesAxisType = ...) -> DataFrame: ...
    def pop(self, item: _str) -> Series[Dtype]: ...
    def squeeze(self, axis: Optional[SeriesAxisType] = ...) -> Scalar: ...
    def __abs__(self) -> Series[Dtype]: ...
    def add_prefix(self, prefix: _str) -> Series[Dtype]: ...
    def add_suffix(self, suffix: _str) -> Series[Dtype]: ...
    def reindex(self, index: Optional[_ListLike] = ..., **kwargs) -> Series[Dtype]: ...
    def filter(
        self,
        items: Optional[_ListLike] = ...,
        like: Optional[_str] = ...,
        regex: Optional[_str] = ...,
        axis: Optional[SeriesAxisType] = ...,
    ) -> Series[Dtype]: ...
    def head(self, n: int = ...) -> Series[Dtype]: ...
    def tail(self, n: int = ...) -> Series[Dtype]: ...
    def sample(
        self,
        n: Optional[int] = ...,
        frac: Optional[float] = ...,
        replace: _bool = ...,
        weights: Optional[Union[_str, _ListLike, np.ndarray]] = ...,
        random_state: Optional[int] = ...,
        axis: Optional[SeriesAxisType] = ...,
    ) -> Series[Dtype]: ...
    def astype(
        self,
        dtype: Union[Dtype, _str],
        copy: _bool = ...,
        errors: Literal["raise", "ignore"] = ...,
    ) -> Series: ...
    def copy(self, deep: _bool = ...) -> Series[Dtype]: ...
    def infer_objects(self) -> Series[Dtype]: ...
    def convertDTypes(
        self,
        infer_objects: _bool = ...,
        convert_string: _bool = ...,
        convert_integer: _bool = ...,
        convert_boolean: _bool = ...,
    ) -> Series[Dtype]: ...
    @overload
    def ffill(
        self,
        value: Union[Dtype, Dict, Series[Dtype], DataFrame],
        axis: SeriesAxisType,
        inplace: Literal[True],
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
    ) -> Series[Dtype]: ...
    @overload
    def ffill(
        self,
        value: Union[Dtype, Dict, Series[Dtype], DataFrame],
        inplace: Literal[True],
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
    ) -> Series[Dtype]: ...
    @overload
    def ffill(
        self,
        value: Union[Dtype, Dict, Series[Dtype], DataFrame],
        axis: SeriesAxisType = ...,
        inplace: Literal[False] = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
    ) -> None: ...
    @overload
    def bfill(
        self,
        value: Union[Dtype, Dict, Series[Dtype], DataFrame],
        axis: SeriesAxisType = ...,
        limit: Optional[int] = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True]
    ) -> Series[Dtype]: ...
    @overload
    def bfill(
        self,
        value: Union[Dtype, Dict, Series[Dtype], DataFrame],
        axis: SeriesAxisType = ...,
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
        axis: Optional[SeriesAxisType] = ...,
        limit: Optional[int] = ...,
        inplace: _bool = ...,
        limit_direction: Optional[Literal["forward", "backward", "both"]] = ...,
        limit_area: Optional[Literal["inside", "outside"]] = ...,
        downcast: Optional[Literal["infer"]] = ...,
        **kwargs
    ) -> Series[Dtype]: ...
    def asof(
        self, where: Union[Scalar, Sequence[Scalar]], subset: Optional[Union[_str, Sequence[_str]]] = ...,
    ) -> Union[Scalar, Series[Dtype]]: ...
    def clip(
        self,
        lower: Optional[float] = ...,
        upper: Optional[float] = ...,
        axis: Optional[SeriesAxisType] = ...,
        inplace: _bool = ...,
        *args,
        **kwargs
    ) -> Series[Dtype]: ...
    def asfreq(
        self,
        freq,
        method: Optional[Literal["backfill", "bfill", "pad", "ffill"]] = ...,
        how: Optional[Literal["start", "end"]] = ...,
        normalize: _bool = ...,
        fill_value: Optional[Scalar] = ...,
    ) -> Series[Dtype]: ...
    def at_time(
        self, time: Union[_str, time], asof: _bool = ..., axis: Optional[SeriesAxisType] = ...,
    ) -> Series[Dtype]: ...
    def between_time(
        self,
        start_time: Union[_str, time],
        end_time: Union[_str, time],
        include_start: _bool = ...,
        include_end: _bool = ...,
        axis: Optional[SeriesAxisType] = ...,
    ) -> Series[Dtype]: ...
    # Next one should return a 'Resampler' object
    def resample(
        self,
        rule,
        axis: SeriesAxisType = ...,
        closed: Optional[_str] = ...,
        label: Optional[_str] = ...,
        convention: Literal["start", "end", "s", "e"] = ...,
        kind: Optional[Literal["timestamp", "period"]] = ...,
        loffset = ...,
        base: int = ...,
        on: Optional[_str] = ...,
        level: Optional[Level] = ...,
    ) : ...
    def first(self, offset) -> Series[Dtype]: ...
    def last(self, offset) -> Series[Dtype]: ...
    def rank(
        self,
        axis: SeriesAxisType = ...,
        method: Literal["average", "min", "max", "first", "dense"] = ...,
        numeric_only: Optional[_bool] = ...,
        na_option: Literal["keep", "top", "bottom"] = ...,
        ascending: _bool = ...,
        pct: _bool = ...,
    ) -> Series: ...
    def where(
        self,
        cond: Union[Series[Dtype], Series[Dtype], np.ndarray],
        other = ...,
        inplace: _bool = ...,
        axis: Optional[SeriesAxisType] = ...,
        level: Optional[Level] = ...,
        errors: _str = ...,
        try_cast: _bool = ...,
    ) -> Series[Dtype]: ...
    def mask(
        self,
        cond: Union[Series[Dtype], np.ndarray, Callable],
        other: Union[Scalar, Series[Dtype], DataFrame, Callable] = ...,
        inplace: _bool = ...,
        axis: Optional[SeriesAxisType] = ...,
        level: Optional[Level] = ...,
        errors: Literal["raise", "ignore"] = ...,
        try_cast: _bool = ...,
    ) -> Series[Dtype]: ...
    def slice_shift(self, periods: int = ..., axis: SeriesAxisType = ...) -> Series[Dtype]: ...
    def tshift(self, periods: int = ..., freq = ..., axis: SeriesAxisType = ...) -> Series[Dtype]: ...
    def truncate(
        self,
        before: Optional[Union[date, _str, int]] = ...,
        after: Optional[Union[date, _str, int]] = ...,
        axis: Optional[SeriesAxisType] = ...,
        copy: _bool = ...,
    ) -> Series[Dtype]: ...
    def tz_convert(
        self, tz, axis: SeriesAxisType = ..., level: Optional[Level] = ..., copy: _bool = ...,
    ) -> Series[Dtype]: ...
    def tz_localize(
        self,
        tz,
        axis: SeriesAxisType = ...,
        level: Optional[Level] = ...,
        copy: _bool = ...,
        ambiguous = ...,
        nonexistent: _str = ...,
    ) -> Series[Dtype]: ...
    def abs(self) -> Series[Dtype]: ...
    def describe(
        self,
        percentiles: Optional[List[float]] = ...,
        include: Optional[Union[Literal["all"], List[Dtype]]] = ...,
        exclude: Optional[List[Dtype]] = ...,
    ) -> Series[Dtype]: ...
    def pct_change(
        self,
        periods: int = ...,
        fill_method: _str = ...,
        limit: Optional[int] = ...,
        freq = ...,
        **kwargs
    ) -> Series[Dtype]: ...
    def first_valid_index(self) -> Scalar: ...
    def last_valid_index(self) -> Scalar: ...
    def value_counts(
        self,
        normalize: _bool = ...,
        sort: _bool = ...,
        ascending: _bool = ...,
        bins: Optional[int] = ...,
        dropna: _bool = ...,
    ) -> Series[Dtype]: ...
    def transpose(self, *args, **kwargs) -> Series[Dtype]: ...
    @property
    def T(self) -> Series[Dtype]: ...

    # The rest of these were left over from the old 
    # stubs we shipped in preview. They may belong in 
    # the base classes in some cases; I expect stubgen
    # just failed to generate these so I couldn't match 
    # them up.

    def __add__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[Dtype]: ...
    def __and__(self, other: Union[_ListLike, Series[Dtype]]) -> Series[_bool]: ...
    # def __array__(self, dtype: Optional[_bool] = ...) -> _np_ndarray
    def __div__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[Dtype]: ...
    def __eq__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[_bool]: ...
    def __floordiv__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[int]: ...
    def __ge__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[_bool]: ...
    def __gt__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[_bool]: ...
    # def __iadd__(self, other: Dtype) -> Series[Dtype]: ...
    # def __iand__(self, other: Dtype) -> Series[_bool]: ...
    # def __idiv__(self, other: Dtype) -> Series[Dtype]: ...
    # def __ifloordiv__(self, other: Dtype) -> Series[Dtype]: ...
    # def __imod__(self, other: Dtype) -> Series[Dtype]: ...
    # def __imul__(self, other: Dtype) -> Series[Dtype]: ...
    # def __ior__(self, other: Dtype) -> Series[_bool]: ...
    # def __ipow__(self, other: Dtype) -> Series[Dtype]: ...
    # def __isub__(self, other: Dtype) -> Series[Dtype]: ...
    # def __itruediv__(self, other: Dtype) -> Series[Dtype]: ...
    # def __itruediv__(self, other) -> None: ...
    # def __ixor__(self, other: Dtype) -> Series[_bool]: ...
    def __le__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[_bool]: ...
    def __lt__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[_bool]: ...
    def __mul__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[Dtype]: ...
    def __mod__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[Dtype]: ...
    def __ne__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[_bool]: ...
    def __pow__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[Dtype]: ...
    def __or__(self, other: Union[_ListLike, Series[Dtype]]) -> Series[_bool]: ...
    def __radd__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[Dtype]: ...
    def __rand__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[_bool]: ...
    def __rdiv__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[Dtype]: ...
    def __rdivmod__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[Dtype]: ...
    def __rfloordiv__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[Dtype]: ...
    def __rmod__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[Dtype]: ...
    def __rmul__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[Dtype]: ...
    def __rnatmul__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[Dtype]: ...
    def __rpow__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[Dtype]: ...
    def __ror__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[_bool]: ...
    def __rsub__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[Dtype]: ...
    def __rtruediv__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[Dtype]: ...
    def __rxor__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[_bool]: ...
    def __sub__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[Dtype]: ...
    def __truediv__(self, other: Union[num, _ListLike, Series[Dtype]]) -> Series[Dtype]: ...
    def __xor__(self, other: Union[_ListLike, Series[Dtype]]) -> Series: ...
    # properties
    # @property
    # def array(self) -> _npndarray
    @property
    def at(self) -> _LocIndexerSeries[Dtype]: ...

    # @property
    # def cat(self) -> ?

    @property
    def iat(self) -> _iLocIndexerSeries[Dtype]: ...
    @property
    def iloc(self) -> _iLocIndexerSeries[Dtype]: ...
    @property
    def loc(self) -> _LocIndexerSeries[Dtype]: ...

    # Methods
    def add(
        self,
        other: Union[Series[Dtype], Scalar],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: Literal[0] = ...,
    ) -> Series[Dtype]: ...
    def all(
        self,
        axis: SeriesAxisType = ...,
        bool_only: Optional[_bool] = ...,
        skipna: _bool = ...,
        level: Optional[Level] = ...,
        **kwargs
    ) -> _bool: ...
    def any(
        self,
        axis: SeriesAxisType = ...,
        bool_only: Optional[_bool] = ...,
        skipna: _bool = ...,
        level: Optional[Level] = ...,
        **kwargs
    ) -> _bool: ...
    def cummax(
        self, axis: Optional[SeriesAxisType] = ..., skipna: _bool = ..., *args, **kwargs
    ) -> Series[Dtype]: ...
    def cummin(
        self, axis: Optional[SeriesAxisType] = ..., skipna: _bool = ..., *args, **kwargs
    ) -> Series[Dtype]: ...
    def cumprod(
        self, axis: Optional[SeriesAxisType] = ..., skipna: _bool = ..., *args, **kwargs
    ) -> Series[Dtype]: ...
    def cumsum(
        self, axis: Optional[SeriesAxisType] = ..., skipna: _bool = ..., *args, **kwargs
    ) -> Series[Dtype]: ...
    def divide(
        self,
        other: Union[num, _ListLike, Series[Dtype]],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: SeriesAxisType = ...,
    ) -> Series[float]: ...
    def divmod(
        self,
        other: Union[num, _ListLike, Series[Dtype]],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: SeriesAxisType = ...,
    ) -> Series[Dtype]: ...
    def eq(
        self,
        other: Union[Scalar, Series[Dtype]],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: SeriesAxisType = ...,
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
        axis: SeriesAxisType = ...,
    ) -> DataFrame: ...
    def expanding(self, min_periods: int = ..., center: _bool = ..., axis: SeriesAxisType = ...) -> DataFrame: ...
    def floordiv(
        self,
        other: Union[num, _ListLike, Series[Dtype]],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[SeriesAxisType] = ...,
    ) -> Series[int]: ...
    def ge(
        self,
        other: Union[Scalar, Series[Dtype]],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: SeriesAxisType = ...,
    ) -> Series[_bool]: ...
    def gt(
        self,
        other: Union[Scalar, Series[Dtype]],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: SeriesAxisType = ...,
    ) -> Series[_bool]: ...
    def item(self) -> Dtype: ...
    @overload
    def kurt(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: _bool = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> Series[Dtype]: ...
    @overload
    def kurt(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: _bool = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Scalar: ...
    @overload
    def kurtosis(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: _bool = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Optional[Level],
        **kwargs
    ) -> Series[Dtype]: ...
    @overload
    def kurtosis(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: _bool = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Scalar: ...
    def le(
        self,
        other: Union[Scalar, Series[Dtype]],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: SeriesAxisType = ...,
    ) -> Series[_bool]: ...
    def lt(
        self,
        other: Union[Scalar, Series[Dtype]],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: SeriesAxisType = ...,
    ) -> Series[_bool]: ...
    @overload
    def mad(
        self, axis: Optional[SeriesAxisType] = ..., skipna: _bool = ..., *, level: Optional[Level], **kwargs
    ) -> Series[Dtype]: ...
    @overload
    def mad(
        self, axis: Optional[SeriesAxisType] = ..., skipna: _bool = ..., level: None = ..., **kwargs
    ) -> Scalar: ...
    @overload
    def max(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: _bool = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> Series[Dtype]: ...
    @overload
    def max(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: _bool = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Dtype: ...
    @overload
    def mean(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: _bool = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> Series[Dtype]: ...
    @overload
    def mean(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: _bool = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Dtype: ...
    @overload
    def median(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: _bool = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> Series[Dtype]: ...
    @overload
    def median(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: _bool = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Dtype: ...
    @overload
    def min(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: _bool = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> Series[Dtype]: ...
    @overload
    def min(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: _bool = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Dtype: ...
    def mod(
        self,
        other: Union[num, _ListLike, Series[Dtype]],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[SeriesAxisType] = ...,
    ) -> Series[Dtype]: ...
    def mul(
        self,
        other: Union[num, _ListLike, Series[Dtype]],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[SeriesAxisType] = ...,
    ) -> Series[Dtype]: ...
    def multiply(
        self,
        other: Union[num, _ListLike, Series[Dtype]],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[SeriesAxisType] = ...,
    ) -> Series[Dtype]: ...
    def ne(
        self,
        other: Union[Scalar, Series[Dtype]],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: SeriesAxisType = ...,
    ) -> Series[_bool]: ...
    def nunique(self, dropna: _bool = ...) -> int: ...
    def pow(
        self,
        other: Union[num, _ListLike, Series[Dtype]],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[SeriesAxisType] = ...,
    ) -> Series[Dtype]: ...
    @overload
    def prod(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        *,
        level: Level,
        **kwargs
    ) -> Series[Dtype]: ...
    @overload
    def prod(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs
    ) -> Scalar: ...
    @overload
    def product(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        *,
        level: Level,
        **kwargs
    ) -> Series[Dtype]: ...
    @overload
    def product(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs
    ) -> Scalar: ...
    def radd(
        self,
        other: Union[Series[Dtype], Scalar],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: SeriesAxisType = ...,
    ) -> Series[Dtype]: ...
    def rdivmod(
        self,
        other: Union[Series[Dtype], Scalar],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: SeriesAxisType = ...,
    ) -> Series[Dtype]: ...
    def rfloordiv(
        self,
        other,
        level: Optional[Level] = ...,
        fill_value: Optional[Union[float, None]] = ...,
        axis: SeriesAxisType = ...,
    ) -> Series[Dtype]: ...
    def rmod(
        self,
        other: Union[Series[Dtype], Scalar],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: SeriesAxisType = ...,
    ) -> Series[Dtype]: ...
    def rmul(
        self,
        other: Union[Series[Dtype], Scalar],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: SeriesAxisType = ...,
    ) -> Series[Dtype]: ...
    # Next one should return a window class
    def rolling(
        self,
        window,
        min_periods: Optional[int] = ...,
        center: _bool = ...,
        win_type: Optional[_str] = ...,
        on: Optional[_str] = ...,
        axis: SeriesAxisType = ...,
        closed: Optional[_str] = ...,
    ) : ...
    def rpow(
        self,
        other: Union[Series[Dtype], Scalar],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: SeriesAxisType = ...,
    ) -> Series[Dtype]: ...
    def rsub(
        self,
        other: Union[Series[Dtype], Scalar],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: SeriesAxisType = ...,
    ) -> Series[Dtype]: ...
    def rtruediv(
        self,
        other,
        level: Optional[Level] = ...,
        fill_value: Optional[Union[float, None]] = ...,
        axis: SeriesAxisType = ...,
    ) -> Series[Dtype]: ...
    @overload
    def sem(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> Series[Dtype]: ...
    @overload
    def sem(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Scalar: ...
    @overload
    def skew(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> Series[Dtype]: ...
    @overload
    def skew(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Scalar: ...
    @overload
    def std(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> Series[float]: ...
    @overload
    def std(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> float: ...
    def sub(
        self,
        other: Union[num, _ListLike, Series[Dtype]],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[SeriesAxisType] = ...,
    ) -> float: ...
    def subtract(
        self,
        other: Union[num, _ListLike, Series[Dtype]],
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
        axis: Optional[SeriesAxisType] = ...,
    ) -> float: ...
    def sum(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: Optional[Level] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs
    ) -> float: ...
    def to_list(self) -> List: ...
    def to_numpy(
        self, dtype: Optional[Type[DtypeNp]] = ..., copy: _bool = ..., na_value = ..., **kwargs
    ) -> np.ndarray: ...
    def to_records(
        self,
        index: _bool = ...,
        columnDTypes: Optional[Union[_str, Dict]] = ...,
        indexDTypes: Optional[Union[_str, Dict]] = ...,
    ) : ...
    def tolist(self) -> List: ...
    def truediv(
        self,
        other,
        level: Optional[Level] = ...,
        fill_value: Optional[Union[float, None]] = ...,
        axis: SeriesAxisType = ...,
    ) -> Series[float]: ...
    @overload
    def var(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> Series[Dtype]: ...
    @overload
    def var(
        self,
        axis: Optional[SeriesAxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Scalar: ...



