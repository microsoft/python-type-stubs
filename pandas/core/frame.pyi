import datetime
import numpy.ma as np
import matplotlib
import sys
from pandas._config import get_option as get_option
from pandas._libs import lib as lib
from pandas._typing import Axes as Axes, Axis as Axis, Dtype as Dtype, FilePathOrBuffer as FilePathOrBuffer, Level as Level, Renamer as Renamer
from pandas._typing import _str, _bool, num, _SeriesAxisType, _AxisType, _DType, _DTypeNp, _StrLike, _Path_or_Buf, _LevelType, _Scalar, _IndexType, _MaskType, _np_ndarray_bool, _np_ndarray_int64, _np_ndarray_str
from pandas.compat import PY37 as PY37
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core import algorithms as algorithms, nanops as nanops, ops as ops
from pandas.core.accessor import CachedAccessor as CachedAccessor
from pandas.core.arrays import Categorical as Categorical, ExtensionArray as ExtensionArray
from pandas.core.arrays.sparse import SparseFrameAccessor as SparseFrameAccessor
from pandas.core.dtypes.cast import cast_scalar_to_array as cast_scalar_to_array, coerce_to_dtypes as coerce_to_dtypes, find_common_type as find_common_type, infer_dtype_from_scalar as infer_dtype_from_scalar, invalidate_string_dtypes as invalidate_string_dtypes, maybe_cast_to_datetime as maybe_cast_to_datetime, maybe_convert_platform as maybe_convert_platform, maybe_downcast_to_dtype as maybe_downcast_to_dtype, maybe_infer_to_datetimelike as maybe_infer_to_datetimelike, maybe_upcast as maybe_upcast, maybe_upcast_putmask as maybe_upcast_putmask
from pandas.core.dtypes.common import ensure_float64 as ensure_float64, ensure_int64 as ensure_int64, ensure_platform_int as ensure_platform_int, infer_dtype_from_object as infer_dtype_from_object, is_bool_dtype as is_bool_dtype, is_dict_like as is_dict_like, is_dtype_equal as is_dtype_equal, is_extension_array_dtype as is_extension_array_dtype, is_float_dtype as is_float_dtype, is_hashable as is_hashable, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_iterator as is_iterator, is_list_like as is_list_like, is_named_tuple as is_named_tuple, is_object_dtype as is_object_dtype, is_scalar as is_scalar, is_sequence as is_sequence, needs_i8_conversion as needs_i8_conversion
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCIndexClass as ABCIndexClass, ABCMultiIndex as ABCMultiIndex, ABCSeries as ABCSeries
from pandas.core.dtypes.missing import isna as isna, notna as notna
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.groupby import generic as groupby_generic, DataFrameGroupBy as DataFrameGroupBy
from pandas.core.indexes.api import Index as Index, ensure_index as ensure_index, ensure_index_from_sequences as ensure_index_from_sequences
from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex
from pandas.core.indexes.multi import maybe_droplevels as maybe_droplevels
from pandas.core.indexes.period import PeriodIndex as PeriodIndex
from pandas.core.indexing import check_bool_indexer as check_bool_indexer, convert_to_index_sliceable as convert_to_index_sliceable
from pandas.core.internals import BlockManager as BlockManager
from pandas.core.internals.construction import arrays_to_mgr as arrays_to_mgr, get_names_from_index as get_names_from_index, init_dict as init_dict, init_ndarray as init_ndarray, masked_rec_array_to_mgr as masked_rec_array_to_mgr, reorder_arrays as reorder_arrays, sanitize_index as sanitize_index, to_arrays as to_arrays
from pandas.core.ops.missing import dispatch_fill_zeros as dispatch_fill_zeros
from pandas.core.series import Series as Series
from pandas.io.common import get_filepath_or_buffer as get_filepath_or_buffer
from pandas.io.formats import console as console, format as fmt
from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.io.formats.style import Styler as Styler
from pandas.util._decorators import Appender as Appender, Substitution as Substitution, deprecate_kwarg as deprecate_kwarg, rewrite_axis_style_signature as rewrite_axis_style_signature
from pandas.util._validators import validate_axis_style_args as validate_axis_style_args, validate_bool_kwarg as validate_bool_kwarg, validate_percentile as validate_percentile
from typing import Any, Callable, Dict, Hashable, IO, Iterable, Iterator, List, Mapping, Optional, Sequence, Tuple, Type, TypeVar, Union, overload

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

import numpy as _np
import datetime as _dt
from pathlib import Path


class _iLocIndexerFrame:
    @overload
    def __getitem__(self, idx: Tuple[int, int]) -> _DType: ...
    @overload
    def __getitem__(self, idx: Union[_IndexType, slice, Tuple[_IndexType, _IndexType]]) -> DataFrame: ...
    @overload
    def __getitem__(self, idx: Union[int, Tuple[_IndexType, int, Tuple[int, _IndexType]]]) -> Series[_DType]: ...
    def __setitem__(
        self,
        idx: Union[
            int,
            _IndexType,
            Tuple[int, int],
            Tuple[_IndexType, int],
            Tuple[_IndexType, _IndexType],
            Tuple[int, _IndexType],
        ],
        value: Union[float, Series[_DType], DataFrame],
    ) -> None: ...


class _LocIndexerFrame:
    @overload
    def __getitem__(self, idx: Union[int, slice, _MaskType],) -> DataFrame: ...
    @overload
    def __getitem__(self, idx: _StrLike,) -> Series[_DType]: ...
    @overload
    def __getitem__(self, idx: Tuple[_StrLike, _StrLike],) -> float: ...
    @overload
    def __getitem__(self, idx: Tuple[Union[_MaskType, List[str]], Union[_MaskType, List[str]]],) -> DataFrame: ...
    def __setitem__(
        self,
        idx: Union[_MaskType, _StrLike, Tuple[Union[_MaskType, List[str]], Union[_MaskType, List[str]]],],
        value: Union[float, _np.ndarray, Series[_DType], DataFrame],
    ) -> None: ...


class DataFrame(NDFrame):
    _ListLike = Union[
        _np.ndarray, List[_DType], Dict[_str, _np.ndarray], Sequence, Index, Series[_DType],
    ]

    def __init__(
        self,
        data: Optional[Union[_ListLike, DataFrame, Dict[_str, Any]]] = ...,
        index: Optional[_ListLike] = ...,
        columns: Optional[_ListLike] = ...,
        dtype: Any = ...,
        copy: bool = ...,
    ): ...

    def __init__(self, data: Any=..., index: Optional[Axes]=..., columns: Optional[Axes]=..., dtype: Optional[Dtype]=..., copy: bool=...) -> None: ...
    @property
    def axes(self) -> List[Index]: ...
    @property
    def shape(self) -> Tuple[int, int]: ...
    def to_string(self, buf: Optional[FilePathOrBuffer[_str]]=..., columns: Optional[Sequence[str]]=..., col_space: Optional[int]=..., header: Union[bool, Sequence[str]]=..., index: bool=..., na_rep: str=..., formatters: Optional[fmt.formatters_type]=..., float_format: Optional[fmt.float_format_type]=..., sparsify: Optional[bool]=..., index_names: bool=..., justify: Optional[str]=..., max_rows: Optional[int]=..., min_rows: Optional[int]=..., max_cols: Optional[int]=..., show_dimensions: bool=..., decimal: str=..., line_width: Optional[int]=..., max_colwidth: Optional[int]=..., encoding: Optional[str]=...) -> Optional[str]: ...
    @property
    def style(self) -> Styler: ...
    def items(self) -> Iterable[Tuple[Optional[Hashable], Series]]: ...
    def iteritems(self) -> Iterable[Tuple[Optional[Hashable], Series]]: ...
    def iterrows(self) -> Iterable[Tuple[Optional[Hashable], Series]]: ...
    def itertuples(self, index: bool = ..., name: str = ...): ...
    def __len__(self) -> int: ...
    @overload
    def dot(self, other: DataFrame) -> DataFrame: ...
    @overload
    def dot(self, other: Series[_DType]) -> Series[_DType]: ...
    def __matmul__(self, other: Any): ...
    def __rmatmul__(self, other: Any): ...
    @classmethod
    def from_dict(cls: Any, data: Any, orient: Any=..., dtype: Any=..., columns: Any=...) -> DataFrame: ...
    @overload
    def to_numpy(self) -> _np.ndarray: ...
    @overload
    def to_numpy(self, dtype: Optional[Type[_DTypeNp]]) -> _np.ndarray: ...
    @overload
    def to_dict(self) -> Dict[_str, Any]: ...
    @overload
    def to_dict(
        self, orient: Literal["dict", "list", "series", "split", "records", "index"] = ..., into: Hashable = ...,
    ) -> List[Dict[_str, Any]]: ...
    def to_gbq(self, destination_table: Any, project_id: Any=..., chunksize: Any=..., reauth: Any=..., if_exists: Any=..., auth_local_webserver: Any=..., table_schema: Any=..., location: Any=..., progress_bar: Any=..., credentials: Any=...) -> None: ...
    @classmethod
    def from_records(cls: Any, data: Any, index: Any=..., exclude: Any=..., columns: Any=..., coerce_float: Any=..., nrows: Any=...) -> DataFrame: ...
    def to_records(
        self,
        index: _bool = ...,
        column_dtypes: Optional[Union[_str, Dict]] = ...,
        index_dtypes: Optional[Union[_str, Dict]] = ...,
    ) -> np.recarray: ...
    def to_stata(
        self,
        path: _Path_or_Buf,
        convert_dates: Optional[Dict] = ...,
        write_index: _bool = ...,
        byteorder: Optional[Literal["<", ">", "little", "big"]] = ...,
        time_stamp: Optional[Any] = ...,
        data_label: Optional[_str] = ...,
        variable_labels: Optional[Dict] = ...,
        version: int = ...,
        convert_strl: Optional[List[_str]] = ...,
    ) -> None: ...
    def to_feather(self, path: _str) -> None: ...
    @overload
    def to_markdown(self, buf: Optional[_Path_or_Buf], mode: Optional[_str] = ..., **kwargs) -> None: ...
    @overload
    def to_markdown(self, mode: Optional[_str] = ..., **kwargs) -> _str: ...
    def to_parquet(
        self,
        path: _str,
        engine: Literal["auto", "pyarrow", "fastparquet"] = ...,
        compression: Literal["snappy", "gzip", "brotli"] = ...,
        index: Optional[_bool] = ...,
        partition_cols: Optional[List] = ...,
        **kwargs
    ) -> None: ...
    @overload
    def to_html(
        self,
        buf: Optional[_Path_or_Buf],
        columns: Optional[Sequence[_str]] = ...,
        col_space: Optional[Union[_str, int]] = ...,
        header: _bool = ...,
        index: _bool = ...,
        na_rep: _str = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        justify: Optional[_str] = ...,
        max_rows: Optional[int] = ...,
        max_cols: Optional[int] = ...,
        show_dimensions: _bool = ...,
        decimal: _str = ...,
        bold_rows: _bool = ...,
        classes: Optional[Union[_str, List, Tuple]] = ...,
        escape: _bool = ...,
        notebook: _bool = ...,
        border: Optional[int] = ...,
        table_id: Optional[_str] = ...,
        render_links: _bool = ...,
        encoding: Optional[_str] = ...,
    ) -> None: ...
    @overload
    def to_html(
        self,
        columns: Optional[Sequence[_str]] = ...,
        col_space: Optional[Union[_str, int]] = ...,
        header: _bool = ...,
        index: _bool = ...,
        na_rep: _str = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        justify: Optional[_str] = ...,
        max_rows: Optional[int] = ...,
        max_cols: Optional[int] = ...,
        show_dimensions: _bool = ...,
        decimal: _str = ...,
        bold_rows: _bool = ...,
        classes: Optional[Union[_str, List, Tuple]] = ...,
        escape: _bool = ...,
        notebook: _bool = ...,
        border: Optional[int] = ...,
        table_id: Optional[_str] = ...,
        render_links: _bool = ...,
        encoding: Optional[_str] = ...,
    ) -> _str: ...
    def info(self, verbose: Any=..., buf: Any=..., max_cols: Any=..., memory_usage: Any=..., null_counts: Any=...) -> None: ...
    def memory_usage(self, index: _bool = ..., deep: _bool = ...) -> Series[_DType]: ...
    def transpose(self, *args: Any, copy: bool=...) -> DataFrame: ...
    @property
    def T(self) -> DataFrame: ...
    @overload
    def __getitem__(self, idx: _str) -> Series[_DType]: ...
    @overload
    def __getitem__(self, rows: slice) -> DataFrame: ...
    @overload
    def __getitem__(
        self, idx: Union[Series[_bool], DataFrame, List[_str], Index[_str], np.ndarray],
    ) -> DataFrame: ...
    def __setitem__(self, key: Any, value: Any): ...
    def query(self, expr: _str, inplace: _bool = ..., **kwargs) -> DataFrame: ...
    def eval(self, expr: _str, inplace: _bool = ..., **kwargs) -> Any: ...
    def select_dtypes(
        self, include: Optional[Union[_str, List[_str]]] = ..., exclude: Optional[Union[_str, List[_str]]] = ...,
    ) -> DataFrame: ...
    def insert(self, loc: int, column: Any, value: Union[int, _ListLike], allow_duplicates: _bool = ...,) -> None: ...
    def assign(self, **kwargs) -> DataFrame: ...
    def lookup(self, row_labels: Sequence, col_labels: Sequence) -> np.ndarray: ...
    def align(
        self,
        other: Union[DataFrame, Series[_DType]],
        join: Literal["inner", "outer", "left", "right"] = ...,
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        copy: _bool = ...,
        fill_value: Optional[Any] = ...,
        method: Optional[Literal["backfill", "bfill", "pad", "ffill"]] = ...,
        limit: Optional[int] = ...,
        fill_axis: _AxisType = ...,
        broadcast_axis: Optional[_AxisType] = ...,
    ) -> DataFrame: ...
    def reindex(
        self,
        labels: Optional[List] = ...,
        index: Optional[Any] = ...,
        columns: Optional[Any] = ...,
        axis: Optional[_AxisType] = ...,
        method: Optional[Literal["backfill", "bfill", "pad", "ffill", "nearest"]] = ...,
        copy: _bool = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Any = ...,
        limit: Optional[int] = ...,
        tolerance: Optional[Any] = ...,
    ) -> DataFrame: ...
    def drop(
        self,
        labels: Optional[Union[_str, List]] = ...,
        axis: _AxisType = ...,
        index: Optional[Union[List[_str], List[int], Index]] = ...,
        columns: Optional[Union[_str, List]] = ...,
        level: Optional[_LevelType] = ...,
        inplace: _bool = ...,
        errors: Literal["ignore", "raise"] = ...,
    ) -> DataFrame: ...
    # looks like rename is missing an index arg?
    @overload
    def rename(
        self,
        mapper: Optional[Callable],
        axis: Optional[_AxisType] = ...,
        copy: _bool = ...,
        inplace: _bool = ...,
        level: Optional[_LevelType] = ...,
        errors: Literal["ignore", "raise"] = ...,
    ) -> DataFrame: ...
    @overload
    def rename(
        self,
        columns: Optional[Dict[_str, _str]],
        axis: Optional[_AxisType] = ...,
        copy: _bool = ...,
        inplace: _bool = ...,
        level: Optional[_LevelType] = ...,
        errors: Literal["ignore", "raise"] = ...,
    ) -> DataFrame: ...
    @overload
    def fillna(
        self,
        value: Optional[Union[_Scalar, Dict, Series, DataFrame]] = ...,
        method: Optional[Literal["backfill", "bfill", "ffill", "pad"]] = ...,
        axis: Optional[_AxisType] = ...,
        inplace: Optional[Literal[False]] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
    ) -> DataFrame: ...
    @overload
    def fillna(
        self,
        value: Optional[Union[_Scalar, Dict, Series, DataFrame]] = ...,
        method: Optional[Literal["backfill", "bfill", "ffill", "pad"]] = ...,
        axis: Optional[_AxisType] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def replace(
        self,
        to_replace: Optional[Any] = ...,
        value: Optional[Any] = ...,
        limit: Optional[int] = ...,
        regex: Any = ...,
        method: _str = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def replace(
        self,
        to_replace: Optional[Any] = ...,
        value: Optional[Any] = ...,
        inplace: Optional[Literal[False]] = ...,
        limit: Optional[int] = ...,
        regex: Any = ...,
        method: _str = ...,
    ) -> DataFrame: ...
    def shift(
        self,
        periods: int = ...,
        freq: Optional[Any] = ...,
        axis: _AxisType = ...,
        fill_value: Optional[Hashable] = ...,
    ) -> DataFrame: ...
    @overload
    def set_index(
        self,
        keys: List,
        drop: _bool = ...,
        append: _bool = ...,
        verify_integrity: _bool = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def set_index(
        self,
        keys: List,
        drop: _bool = ...,
        append: _bool = ...,
        inplace: Optional[Literal[True]] = ...,
        verify_integrity: _bool = ...,
    ) -> DataFrame: ...
    @overload
    def reset_index(
        self,
        level: _LevelType = ...,
        drop: _bool = ...,
        col_level: Union[int, _str] = ...,
        col_fill: Hashable = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def reset_index(
        self,
        level: _LevelType = ...,
        drop: _bool = ...,
        inplace: Optional[Literal[False]] = ...,
        col_level: Union[int, _str] = ...,
        col_fill: Hashable = ...,
    ) -> DataFrame: ...
    def isna(self) -> DataFrame: ...
    def isnull(self) -> DataFrame: ...
    def notna(self) -> DataFrame: ...
    def notnull(self) -> DataFrame: ...
    @overload
    def dropna(
        self,
        axis: _AxisType = ...,
        how: Literal["any", "all"] = ...,
        thresh: Optional[int] = ...,
        subset: Optional[List] = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def dropna(
        self,
        axis: _AxisType = ...,
        how: Literal["any", "all"] = ...,
        thresh: Optional[int] = ...,
        subset: Optional[List] = ...,
        inplace: Optional[Literal[False]] = ...,
    ) -> DataFrame: ...
    def drop_duplicates(
        self,
        subset: Optional[Any] = ...,
        keep: Union[Literal["first", "last"], _bool] = ...,
        inplace: _bool = ...,
        ignore_index: _bool = ...,
    ) -> DataFrame: ...
    def duplicated(
        self,
        subset: Optional[Union[Hashable, Sequence[Hashable]]] = ...,
        keep: Union[Literal["first", "last"], _bool] = ...,
    ) -> Series[_DType]: ...
    @overload
    def sort_values(
        self,
        by: List[_str],
        axis: _AxisType = ...,
        ascending: _bool = ...,
        kind: Literal["quicksort", "mergesort", "heapsort"] = ...,
        na_position: Literal["first", "last"] = ...,
        ignore_index: _bool = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def sort_values(
        self,
        by: List[_str],
        axis: _AxisType = ...,
        ascending: _bool = ...,
        inplace: Optional[Literal[False]] = ...,
        kind: Literal["quicksort", "mergesort", "heapsort"] = ...,
        na_position: Literal["first", "last"] = ...,
        ignore_index: _bool = ...,
    ) -> DataFrame: ...
    @overload
    def sort_index(
        self,
        axis: _AxisType = ...,
        level: Optional[_LevelType] = ...,
        ascending: _bool = ...,
        kind: Literal["quicksort", "mergesort", "heapsort"] = ...,
        na_position: Literal["first", "last"] = ...,
        sort_remaining: _bool = ...,
        ignore_index: _bool = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def sort_index(
        self,
        axis: _AxisType = ...,
        level: Optional[_LevelType] = ...,
        ascending: _bool = ...,
        inplace: Optional[Literal[False]] = ...,
        kind: Literal["quicksort", "mergesort", "heapsort"] = ...,
        na_position: Literal["first", "last"] = ...,
        sort_remaining: _bool = ...,
        ignore_index: _bool = ...,
    ) -> DataFrame: ...
    def nlargest(
        self, n: int, columns: Union[_str, List[_str]], keep: Literal["first", "last", "all"] = ...,
    ) -> DataFrame: ...
    def nsmallest(
        self, n: int, columns: Union[_str, List[_str]], keep: Literal["first", "last", "all"] = ...,
    ) -> DataFrame: ...
    def swaplevel(self, i: _LevelType = ..., j: _LevelType = ..., axis: _AxisType = ...) -> DataFrame: ...
    def reorder_levels(self, order: List, axis: _AxisType = ...) -> DataFrame: ...
    def combine(
        self, other: DataFrame, func: Callable, fill_value: Optional[Any] = ..., overwrite: _bool = ...,
    ) -> DataFrame: ...
    def combine_first(self, other: DataFrame) -> DataFrame: ...
    def update(
        self,
        other: Union[DataFrame, Series[_DType]],
        join: Literal["left"] = ...,
        overwrite: _bool = ...,
        filter_func: Optional[Callable] = ...,
        errors: Literal["raise", "ignore"] = ...,
    ) -> None: ...
    def groupby(
        self,
        by: Optional[Union[List[_str], _str]],
        axis: _AxisType = ...,
        level: Optional[_LevelType] = ...,
        as_index: _bool = ...,
        sort: _bool = ...,
        group_keys: _bool = ...,
        squeeze: _bool = ...,
        observed: _bool = ...,
    ) -> DataFrameGroupBy: ...
    def pivot(
        self, index: Optional[Any] = ..., columns: Optional[Any] = ..., values: Optional[Any] = ...,
    ) -> DataFrame: ...
    def pivot_table(
        self,
        values: Optional[Any] = ...,
        index: Optional[Any] = ...,
        columns: Optional[Any] = ...,
        aggfunc: Any = ...,
        fill_value: Optional[Any] = ...,
        margins: _bool = ...,
        dropna: _bool = ...,
        margins_name: _str = ...,
        observed: _bool = ...,
    ) -> DataFrame: ...
    def stack(self, level: _LevelType = ..., dropna: _bool = ...) -> Union[DataFrame, Series[_DType]]: ...
    def explode(self, column: Union[str, Tuple]) -> DataFrame: ...
    def unstack(
        self, level: _LevelType = ..., fill_value: Optional[Union[int, _str, Dict]] = ...,
    ) -> Union[DataFrame, Series[_DType]]: ...
    def melt(
        self,
        id_vars: Optional[Any] = ...,
        value_vars: Optional[Any] = ...,
        var_name: Optional[Any] = ...,
        value_name: Any = ...,
        col_level: Optional[Union[int, _str]] = ...,
    ) -> DataFrame: ...
    def diff(self, periods: int = ..., axis: _AxisType = ...) -> DataFrame: ...
    @overload
    def agg(self, func: Union[Callable, _str], axis: _AxisType = ..., **kwargs) -> Series[_DType]: ...
    @overload
    def agg(self, func: Union[List[Callable], Dict[_str, Callable]], axis: _AxisType = ..., **kwargs) -> DataFrame: ...
    @overload
    def aggregate(self, func: Union[Callable, _str], axis: _AxisType = ..., **kwargs) -> Series[_DType]: ...
    @overload
    def aggregate(
        self, func: Union[List[Callable], Dict[_str, Callable]], axis: _AxisType = ..., **kwargs
    ) -> DataFrame: ...
    def transform(self, func: Callable, axis: _AxisType = ..., *args, **kwargs) -> DataFrame: ...
    @overload
    def apply(self, f: Callable[..., int]) -> Series[_DType]: ...
    @overload
    def apply(
        self, f: Callable, axis: _AxisType = ..., raw: _bool = ..., result_type: Optional[_str] = ...,
    ) -> DataFrame: ...
    def applymap(self, func: Callable) -> DataFrame: ...
    def append(
        self,
        other: Union[DataFrame, Series[_DType], Dict[_str, Any]],
        ignore_index: _bool = ...,
        verify_integrity: _bool = ...,
        sort: _bool = ...,
    ) -> DataFrame: ...
    def join(
        self,
        other: Union[DataFrame, Series[_DType], List[DataFrame]],
        on: Optional[Union[_str, List[_str]]] = ...,
        how: Literal["left", "right", "outer", "inner"] = ...,
        lsuffix: _str = ...,
        rsuffix: _str = ...,
        sort: _bool = ...,
    ) -> DataFrame: ...
    def merge(
        self,
        right: Union[DataFrame, Series[_DType]],
        how: Literal["left", "right", "inner", "outer"] = ...,
        on: Optional[Union[_LevelType, List[_LevelType]]] = ...,
        left_on: Optional[Union[_LevelType, List[_LevelType]]] = ...,
        right_on: Optional[Union[_LevelType, List[_LevelType]]] = ...,
        left_index: _bool = ...,
        right_index: _bool = ...,
        sort: _bool = ...,
        suffixes: Tuple[_str, _str] = ...,
        copy: _bool = ...,
        indicator: Union[_bool, _str] = ...,
        validate: Optional[_str] = ...,
    ) -> DataFrame: ...
    def round(self, decimals: Union[int, Dict, Series[_DType]] = ..., *args, **kwargs) -> DataFrame: ...
    def corr(self, method: Literal["pearson", "kendall", "spearman"] = ..., min_periods: int = ...,) -> DataFrame: ...
    def cov(self, min_periods: Optional[int] = ...) -> DataFrame: ...
    def corrwith(
        self,
        other: Union[DataFrame, Series[_DType]],
        axis: Optional[_AxisType] = ...,
        drop: _bool = ...,
        method: Literal["pearson", "kendall", "spearman"] = ...,
    ) -> Series: ...
    @overload
    def count(self, axis: _AxisType = ..., numeric_only: _bool = ..., *, level: _LevelType) -> DataFrame: ...
    @overload
    def count(self, axis: _AxisType = ..., level: None = ..., numeric_only: _bool = ...) -> Series[_DType]: ...
    def nunique(self, axis: _AxisType = ..., dropna=True) -> Series[_DType]: ...
    def idxmax(self, axis: _AxisType, skipna: _bool = ...) -> Series[_DType]: ...
    def idxmin(self, axis: _AxisType, skipna: _bool = ...) -> Series[_DType]: ...
    @overload
    def mode(
        self, axis: _AxisType = ..., skipna: _bool = ..., numeric_only: _bool = ..., *, level: _LevelType, **kwargs
    ) -> DataFrame: ...
    @overload
    def mode(
        self, axis: _AxisType = ..., skipna: _bool = ..., level: None = ..., numeric_only: _bool = ..., **kwargs
    ) -> Series[_DType]: ...
    @overload
    def quantile(
        self,
        q: float = ...,
        axis: _AxisType = ...,
        numeric_only: _bool = ...,
        interpolation: Literal["linear", "lower", "higher", "midpoint", "nearest"] = ...,
    ) -> Series: ...
    @overload
    def quantile(
        self,
        q: List = ...,
        axis: _AxisType = ...,
        numeric_only: _bool = ...,
        interpolation: Literal["linear", "lower", "higher", "midpoint", "nearest"] = ...,
    ) -> DataFrame: ...
    def to_timestamp(
        self,
        freq: Optional[Any] = ...,
        how: Literal["start", "end", "s", "e"] = ...,
        axis: _AxisType = ...,
        copy: _bool = ...,
    ) -> DataFrame: ...
    def to_period(self, freq: Optional[_str] = ..., axis: _AxisType = ..., copy: _bool = ...) -> DataFrame: ...
    def isin(self, values: Union[Iterable, Series[_DType], DataFrame, Dict]) -> DataFrame: ...
    def plot(self, kind: _str, yerr: DataFrame, **kwargs) -> matplotlib.axes.Axes: ...
    def hist(
        data,
        column: Optional[Union[_str, List[_str]]] = ...,
        by: Optional[Union[_str, _ListLike]] = ...,
        grid: _bool = ...,
        xlabelsize: Optional[int] = ...,
        xrot: Optional[float] = ...,
        ylabelsize: Optional[int] = ...,
        yrot: Optional[float] = ...,
        ax: Optional[matplotlib.axes.Axes] = ...,
        sharex: _bool = ...,
        sharey: _bool = ...,
        figsize: Optional[Tuple[float, float]] = ...,
        layout: Optional[Tuple[int, int]] = ...,
        bins: Union[int, List] = ...,
        backend: Optional[_str] = ...,
        **kwargs
    ) -> Any: ...
    def boxplot(
        self,
        column: Optional[Union[_str, List[_str]]] = ...,
        by: Optional[Union[_str, _ListLike]] = ...,
        ax: Optional[matplotlib.axes.Axes] = ...,
        fontsize: Optional[Union[float, _str]] = ...,
        rot: int = ...,
        grid: _bool = ...,
        figsize: Optional[Tuple[float, float]] = ...,
        layout: Optional[Tuple[int, int]] = ...,
        return_type: Optional[Literal["axes", "dict", "both"]] = ...,
        backend: Optional[_str] = ...,
        **kwargs
    ) -> Any: ...
    sparse: Any = ...

    # The rest of these are remnants from the 
    # stubs shipped at preview. They may belong in 
    # base classes, or stubgen just failed to generate
    # these.

    Name: _str
    #
    # dunder methods
    def __add__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __and__(self, other: Union[num, _ListLike, DataFrame], axis: _SeriesAxisType = ...) -> DataFrame: ...
    def __delitem__(self, key: _str) -> None: ...
    def __div__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __eq__(self, other: Union[float, Series[_DType], DataFrame]) -> DataFrame: ...  # type: ignore
    def __exp__(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: _AxisType = ...,
        level: _LevelType = ...,
        fill_value: Union[None, float] = ...,
    ) -> DataFrame: ...
    def __floordiv__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...

    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def __le__(self, other: float) -> DataFrame: ...
    def __lt__(self, other: float) -> DataFrame: ...
    def __ge__(self, other: float) -> DataFrame: ...
    def __gt__(self, other: float) -> DataFrame: ...
    def __mod__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __mul__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __pow__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __ne__(self, other: Union[float, Series[_DType], DataFrame]) -> DataFrame: ...  # type: ignore
    def __or__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __radd__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rand__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rdiv__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rfloordiv__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rmod__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rmul__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rnatmul__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __ror__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rpow__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rsub__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rtruediv__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __rxor__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __truediv__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __mul__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __sub__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __xor__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    # properties
    @property
    def at(self) -> Any: ...  # Not sure what to do with this yet; look at source
    @property
    def bool(self) -> _bool: ...
    @property
    def columns(self) -> Index[_str]: ...
    @columns.setter  # setter needs to be right next to getter; otherwise mypy complains
    def columns(self, cols: Union[List[_str], Index[_str]]) -> None: ...
    @property
    def dtypes(self) -> Series[_DType]: ...
    @property
    def empty(self) -> _bool: ...
    @property
    def iat(self) -> Any: ...  # Not sure what to do with this yet; look at source
    @property
    def iloc(self) -> _iLocIndexerFrame: ...
    @property
    def index(self) -> Index[int]: ...
    @index.setter
    def index(self, idx: Index) -> None: ...
    @property
    def loc(self) -> _LocIndexerFrame: ...
    @property
    def ndim(self) -> int: ...
    @property
    def size(self) -> int: ...
    @property
    def str(self) -> _str: ...
    # this function is deprecated:
    @property
    def values(self) -> _np.ndarray: ...
    # methods
    def abs(self) -> DataFrame: ...
    def add(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def add_prefix(self, prefix: _str) -> DataFrame: ...
    def add_suffix(self, suffix: _str) -> DataFrame: ...
    @overload
    def all(
        self, axis: _AxisType = ..., bool_only: Optional[_bool] = ..., skipna: _bool = ..., level: None = ..., **kwargs
    ) -> Series[_DType]: ...
    @overload
    def all(
        self,
        axis: _AxisType = ...,
        bool_only: Optional[_bool] = ...,
        skipna: _bool = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def any(
        self, axis: _AxisType = ..., bool_only: Optional[_bool] = ..., skipna: _bool = ..., level: None = ..., **kwargs
    ) -> Series[_DType]: ...
    @overload
    def any(
        self, axis: _AxisType = ..., bool_only: _bool = ..., skipna: _bool = ..., *, level: _LevelType, **kwargs
    ) -> DataFrame: ...
    def asof(self, where: Any, subset: Optional[Union[_str, List[_str]]] = ...) -> DataFrame: ...
    def asfreq(
        self,
        freq: Any,
        method: Optional[Literal["backfill", "bfill", "pad", "ffill"]] = ...,
        how: Optional[Literal["start", "end"]] = ...,
        normalize: _bool = ...,
        fill_value: Optional[_Scalar] = ...,
    ) -> DataFrame: ...
    def astype(self, dtype: Union[_str, Dict[_str, _str]], copy: _bool = ..., errors: _str = ...,) -> DataFrame: ...
    def at_time(
        self, time: Union[_str, datetime.time], asof: _bool = ..., axis: Optional[_AxisType] = ...,
    ) -> DataFrame: ...
    def between_time(
        self,
        start_time: Union[_str, datetime.time],
        end_time: Union[_str, datetime.time],
        include_start: _bool = ...,
        include_end: _bool = ...,
        axis: Optional[_AxisType] = ...,
    ) -> DataFrame: ...
    @overload
    def bfill(
        self,
        value: Optional[Union[float, Dict, Series[_DType], DataFrame]] = ...,
        axis: Optional[_AxisType] = ...,
        inplace: Optional[Literal[False]] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
    ) -> DataFrame: ...
    @overload
    def bfill(
        self,
        value: Optional[Union[float, Dict, Series[_DType], DataFrame]] = ...,
        axis: Optional[_AxisType] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    def clip(
        self,
        lower: Optional[float] = ...,
        upper: Optional[float] = ...,
        axis: Optional[_AxisType] = ...,
        inplace: _bool = ...,
        *args,
        **kwargs
    ) -> DataFrame: ...
    def convert_dtypes(
        self,
        infer_objects: _bool = ...,
        convert_string: _bool = ...,
        convert_integer: _bool = ...,
        convert__boolean: _bool = ...,
    ) -> DataFrame: ...
    def copy(self, deep: _bool = ...) -> DataFrame: ...
    def cummax(self, axis: Optional[_AxisType] = ..., skipna: _bool = ..., *args, **kwargs) -> DataFrame: ...
    def cummin(self, axis: Optional[_AxisType] = ..., skipna: _bool = ..., *args, **kwargs) -> DataFrame: ...
    def cumprod(self, axis: Optional[_AxisType] = ..., skipna: _bool = ..., *args, **kwargs) -> DataFrame: ...
    def cumsum(self, axis: Optional[_AxisType] = ..., skipna: _bool = ..., *args, **kwargs) -> DataFrame: ...
    def describe(
        self,
        percentiles: Optional[List[float]] = ...,
        include: Optional[Union[Literal["all"], List[_DType]]] = ...,
        exclude: Optional[List[_DType]] = ...,
    ) -> DataFrame: ...
    def div(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def divide(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def droplevel(self, level: _LevelType = ..., axis: _AxisType = ...) -> DataFrame: ...
    def eq(self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ...) -> DataFrame: ...
    def equals(self, other: Union[Series[_DType], DataFrame]) -> _bool: ...
    def ewm(
        self,
        com: Optional[float] = ...,
        span: Optional[float] = ...,
        halflife: Optional[float] = ...,
        alpha: Optional[float] = ...,
        min_periods: int = ...,
        adjust: _bool = ...,
        ignore_na: _bool = ...,
        axis: _AxisType = ...,
    ) -> DataFrame: ...
    def exp(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def expanding(self, min_periods: int = ..., center: _bool = ..., axis: _AxisType = ...) -> Any: ...  # for now
    @overload
    def ffill(
        self,
        value: Optional[Union[_Scalar, Dict, Series[_DType], DataFrame]] = ...,
        axis: Optional[_AxisType] = ...,
        inplace: Optional[Literal[False]] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
    ) -> DataFrame: ...
    @overload
    def ffill(
        self,
        value: Optional[Union[_Scalar, Dict, Series, DataFrame]] = ...,
        axis: Optional[_AxisType] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    def filter(
        self,
        items: Optional[List] = ...,
        like: Optional[_str] = ...,
        regex: Optional[_str] = ...,
        axis: Optional[_AxisType] = ...,
    ) -> DataFrame: ...
    def first(self, offset: Any) -> DataFrame: ...
    def first_valid_index(self) -> _Scalar: ...
    def floordiv(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    # def from_dict
    # def from_records
    def fulldiv(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def ge(self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ...) -> DataFrame: ...
    # def get
    def gt(self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ...) -> DataFrame: ...
    def head(self, n: int = ...) -> DataFrame: ...
    def infer_objects(self) -> DataFrame: ...
    # def info
    @overload
    def interpolate(
        self,
        method: _str = ...,
        axis: _AxisType = ...,
        limit: Optional[int] = ...,
        limit_direction: Literal["forward", "backward", "both"] = ...,
        limit_area: Optional[Literal["inside", "outside"]] = ...,
        downcast: Optional[Literal["infer"]] = ...,
        *,
        inplace: Literal[True],
        **kwargs
    ) -> None: ...
    @overload
    def interpolate(
        self,
        method: _str = ...,
        axis: _AxisType = ...,
        limit: Optional[int] = ...,
        inplace: Optional[Literal[False]] = ...,
        limit_direction: Literal["forward", "backward", "both"] = ...,
        limit_area: Optional[Literal["inside", "outside"]] = ...,
        downcast: Optional[Literal["infer"]] = ...,
        **kwargs
    ) -> DataFrame: ...
    def keys(self) -> Index: ...
    @overload
    def kurt(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def kurt(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def kurtosis(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def kurtosis(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    def last(self, offset: Any) -> DataFrame: ...
    def last_valid_index(self) -> _Scalar: ...
    def le(self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ...) -> DataFrame: ...
    def lt(self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ...) -> DataFrame: ...
    @overload
    def mad(
        self, axis: Optional[_AxisType] = ..., skipna: Optional[_bool] = ..., level: None = ...,
    ) -> Series[_DType]: ...
    @overload
    def mad(
        self, axis: Optional[_AxisType] = ..., skipna: Optional[_bool] = ..., *, level: _LevelType, **kwargs
    ) -> DataFrame: ...
    def mask(
        self,
        cond: Union[Series[_DType], DataFrame, _np.ndarray],
        other: Any = ...,
        inplace: _bool = ...,
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        errors: _str = ...,
        try_cast: _bool = ...,
    ) -> DataFrame: ...
    @overload
    def max(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def max(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def mean(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def mean(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def median(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def median(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def min(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def min(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    def mod(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def mul(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def multiply(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def ne(self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ...) -> DataFrame: ...
    def pct_change(
        self,
        periods: int = ...,
        fill_method: _str = ...,
        limit: Optional[int] = ...,
        freq: Optional[Any] = ...,
        **kwargs
    ) -> DataFrame: ...
    def pipe(self, func: Callable, *args, **kwargs) -> Any: ...
    def pop(self, item: _str) -> Series[_DType]: ...
    def pow(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    @overload
    def prod(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def prod(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs
    ) -> Series: ...
    def product(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: _bool = ...,
        level: Optional[_LevelType] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs
    ) -> DataFrame: ...
    def radd(
        self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rank(
        self,
        axis: _AxisType = ...,
        method: Literal["average", "min", "max", "first", "dense"] = ...,
        numeric_only: Optional[_bool] = ...,
        na_option: Literal["keep", "top", "bottom"] = ...,
        ascending: _bool = ...,
        pct: _bool = ...,
    ) -> DataFrame: ...
    def rdiv(
        self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def reindex_like(
        self,
        other: DataFrame,
        method: Optional[Literal["backfill", "bfill", "pad", "ffill", "nearest"]] = ...,
        copy: _bool = ...,
        limit: Optional[int] = ...,
        tolerance: Optional[Any] = ...,
    ) -> DataFrame: ...
    @overload
    def rename_axis(
        self,
        mapper: Optional[Any] = ...,
        index: Optional[_IndexType] = ...,
        columns: Optional[Any] = ...,
        axis: Optional[_AxisType] = ...,
        copy: _bool = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def rename_axis(
        self,
        mapper: Optional[Any] = ...,
        index: Optional[_IndexType] = ...,
        columns: Optional[Any] = ...,
        axis: Optional[_AxisType] = ...,
        copy: _bool = ...,
        inplace: Optional[Literal[False]] = ...,
    ) -> DataFrame: ...
    def resample(
        self,
        rule: Any,
        axis: _AxisType = ...,
        closed: Optional[_str] = ...,
        label: Optional[_str] = ...,
        convention: Literal["start", "end", "s", "e"] = ...,
        kind: Optional[Literal["timestamp", "period"]] = ...,
        loffset: Optional[Any] = ...,
        base: int = ...,
        on: Optional[_str] = ...,
        level: Optional[_LevelType] = ...,
    ) -> Any: ...
    def rfloordiv(
        self,
        other: Any,
        axis: _AxisType = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[Union[float, None]] = ...,
    ) -> DataFrame: ...
    def rmod(
        self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rmul(
        self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rolling(
        self,
        window: Any,
        min_periods: Optional[int] = ...,
        center: _bool = ...,
        win_type: Optional[_str] = ...,
        on: Optional[_str] = ...,
        axis: _AxisType = ...,
        closed: Optional[_str] = ...,
    ) -> Any: ...  # For now
    def rpow(
        self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rsub(
        self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rtruediv(
        self, other: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    # sample is missing a weights arg
    @overload
    def sample(
        self,
        frac: Optional[float],
        random_state: Optional[int] = ...,
        replace: _bool = ...,
        axis: Optional[_AxisType] = ...,
    ) -> DataFrame: ...
    @overload
    def sample(
        self,
        n: Optional[int],
        random_state: Optional[int] = ...,
        replace: _bool = ...,
        axis: Optional[_AxisType] = ...,
    ) -> DataFrame: ...

    @overload
    def sem(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def sem(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    @overload
    def set_axis(self, labels: List, inplace: Literal[True], axis: _AxisType = ...) -> None: ...
    @overload
    def set_axis(self, labels: List, axis: _AxisType = ..., inplace: Optional[Literal[False]] = ...,) -> DataFrame: ...
    @overload
    def skew(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def skew(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    def slice_shift(self, periods: int = ..., axis: _AxisType = ...) -> DataFrame: ...
    def squeeze(self, axis: Optional[_AxisType] = ...) -> Any: ...
    @overload
    def std(
        self,
        axis: _AxisType = ...,
        skipna: _bool = ...,
        ddof: int = ...,
        numeric_only: _bool = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def std(
        self,
        axis: _AxisType = ...,
        skipna: _bool = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: _bool = ...,
        **kwargs
    ) -> Series[_DType]: ...
    def sub(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def subtract(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    @overload
    def sum(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def sum(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs
    ) -> Series[_DType]: ...
    def swapaxes(self, axis1: _AxisType, axis2: _AxisType, copy: _bool = ...) -> DataFrame: ...
    def tail(self, n: int = ...) -> DataFrame: ...
    def take(self, indices: List, axis: _AxisType = ..., is_copy: Optional[_bool] = ..., **kwargs) -> DataFrame: ...
    def transform(self, func: Union[List[Callable], Dict[_str, Callable]], axis: _AxisType = ...,) -> DataFrame: ...
    def transpose(self, *args, copy: _bool = ...) -> DataFrame: ...
    T = transpose
    def tshift(self, periods: int = ..., freq: Any = ..., axis: _AxisType = ...) -> DataFrame: ...
    def to_clipboard(self, excel: _bool = ..., sep: Optional[_str] = ..., **kwargs) -> None: ...
    @overload
    def to_csv(
        self,
        path_or_buf: Optional[_Path_or_Buf],
        sep: _str = ...,
        na_rep: _str = ...,
        float_format: Optional[_str] = ...,
        columns: Optional[Sequence[Hashable]] = ...,
        header: Union[_bool, List[_str]] = ...,
        index: _bool = ...,
        index_label: Optional[Union[_bool, _str, Sequence[Hashable]]] = ...,
        mode: _str = ...,
        encoding: Optional[_str] = ...,
        compression: Union[_str, Mapping[_str, _str]] = ...,
        quoting: Optional[int] = ...,
        quotechar: _str = ...,
        line_terminator: Optional[_str] = ...,
        chunksize: Optional[int] = ...,
        date_format: Optional[_str] = ...,
        doublequote: _bool = ...,
        escapechar: Optional[_str] = ...,
        decimal: _str = ...,
    ) -> None: ...
    @overload
    def to_csv(
        self,
        sep: _str = ...,
        na_rep: _str = ...,
        float_format: Optional[_str] = ...,
        columns: Optional[Sequence[Hashable]] = ...,
        header: Union[_bool, List[_str]] = ...,
        index: _bool = ...,
        index_label: Optional[Union[_bool, _str, Sequence[Hashable]]] = ...,
        mode: _str = ...,
        encoding: Optional[_str] = ...,
        compression: Union[_str, Mapping[_str, _str]] = ...,
        quoting: Optional[int] = ...,
        quotechar: _str = ...,
        line_terminator: Optional[_str] = ...,
        chunksize: Optional[int] = ...,
        date_format: Optional[_str] = ...,
        doublequote: _bool = ...,
        escapechar: Optional[_str] = ...,
        decimal: _str = ...,
    ) -> _str: ...
    def to_excel(
        self,
        excel_writer: Any,
        sheet_name: _str = ...,
        na_rep: _str = ...,
        float_format: Optional[_str] = ...,
        columns: Optional[Union[_str, Sequence[_str]]] = ...,
        header: _bool = ...,
        index: _bool = ...,
        index_label: Optional[Union[_str, Sequence[_str]]] = ...,
        startrow: int = ...,
        startcol: int = ...,
        engine: Optional[_str] = ...,
        merge_cells: _bool = ...,
        encoding: Optional[_str] = ...,
        inf_rep: _str = ...,
        verbose: _bool = ...,
        freeze_panes: Optional[Tuple[int, int]] = ...,
    ) -> None: ...
    def to_hdf(
        self,
        path_or_buf: _Path_or_Buf,
        key: _str,
        mode: _str = ...,
        complevel: Optional[int] = ...,
        complib: Optional[_str] = ...,
        append: _bool = ...,
        format: Optional[_str] = ...,
        index: _bool = ...,
        min_itemsize: Optional[Union[int, Dict[_str, int]]] = ...,
        nan_rep: Optional[Any] = ...,
        dropna: Optional[_bool] = ...,
        data_columns: Optional[List[_str]] = ...,
        errors: _str = ...,
        encoding: _str = ...,
    ) -> None: ...
    @overload
    def to_json(
        self,
        path_or_buf: Optional[_Path_or_Buf],
        orient: Optional[Literal["split", "records", "index", "columns", "values", "table"]] = ...,
        date_format: Optional[Literal["epoch", "iso"]] = ...,
        double_precision: int = ...,
        force_ascii: _bool = ...,
        date_unit: Literal["s", "ms", "us", "ns"] = ...,
        default_handler: Optional[Callable[[Any], Union[_str, int, float, _bool, List, Dict]]] = ...,
        lines: _bool = ...,
        compression: Literal["infer", "gzip", "bz2", "zip", "xz"] = ...,
        index: _bool = ...,
        indent: Optional[int] = ...,
    ) -> None: ...
    @overload
    def to_json(
        self,
        orient: Optional[Literal["split", "records", "index", "columns", "values", "table"]] = ...,
        date_format: Optional[Literal["epoch", "iso"]] = ...,
        double_precision: int = ...,
        force_ascii: _bool = ...,
        date_unit: Literal["s", "ms", "us", "ns"] = ...,
        default_handler: Optional[Callable[[Any], Union[_str, int, float, _bool, List, Dict]]] = ...,
        lines: _bool = ...,
        compression: Literal["infer", "gzip", "bz2", "zip", "xz"] = ...,
        index: _bool = ...,
        indent: Optional[int] = ...,
    ) -> _str: ...
    @overload
    def to_latex(
        self,
        buf: Optional[_Path_or_Buf],
        columns: Optional[List[_str]] = ...,
        col_space: Optional[int] = ...,
        header: _bool = ...,
        index: _bool = ...,
        na_rep: _str = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        bold_rows: _bool = ...,
        column_format: Optional[_str] = ...,
        longtable: Optional[_bool] = ...,
        escape: Optional[_bool] = ...,
        encoding: Optional[_str] = ...,
        decimal: _str = ...,
        multicolumn: Optional[_bool] = ...,
        multicolumn_format: Optional[_str] = ...,
        multirow: Optional[_bool] = ...,
        caption: Optional[_str] = ...,
        label: Optional[_str] = ...,
    ) -> None: ...
    @overload
    def to_latex(
        self,
        columns: Optional[List[_str]] = ...,
        col_space: Optional[int] = ...,
        header: _bool = ...,
        index: _bool = ...,
        na_rep: _str = ...,
        formatters: Optional[Any] = ...,
        float_format: Optional[Any] = ...,
        sparsify: Optional[_bool] = ...,
        index_names: _bool = ...,
        bold_rows: _bool = ...,
        column_format: Optional[_str] = ...,
        longtable: Optional[_bool] = ...,
        escape: Optional[_bool] = ...,
        encoding: Optional[_str] = ...,
        decimal: _str = ...,
        multicolumn: Optional[_bool] = ...,
        multicolumn_format: Optional[_str] = ...,
        multirow: Optional[_bool] = ...,
        caption: Optional[_str] = ...,
        label: Optional[_str] = ...,
    ) -> _str: ...
    def to_pickle(
        self, path: _str, compression: Literal["infer", "gzip", "bz2", "zip", "xz"] = ..., protocol: int = ...,
    ) -> None: ...
    def to_sql(
        self,
        name: _str,
        con: Any,
        schema: Optional[_str] = ...,
        if_exists: _str = ...,
        index: _bool = ...,
        index_label: Optional[Union[_str, Sequence[_str]]] = ...,
        chunksize: Optional[int] = ...,
        dtype: Optional[Union[Dict, _Scalar]] = ...,
        method: Optional[Union[_str, Callable]] = ...,
    ) -> None: ...
    @overload
    def to_string(
        self,
        buf: Optional[_Path_or_Buf],
        columns: Optional[Sequence[_str]] = ...,
        col_space: Optional[int] = ...,
        header: Union[_bool, Sequence[_str]] = ...,
        index: _bool = ...,
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
        columns: Optional[Sequence[_str]] = ...,
        col_space: Optional[int] = ...,
        header: Union[_bool, Sequence[_str]] = ...,
        index: _bool = ...,
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
    def to_xarray(self) -> Any: ...
    def truediv(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def truncate(
        self,
        before: Optional[Union[datetime.date, _str, int]] = ...,
        after: Optional[Union[datetime.date, _str, int]] = ...,
        axis: Optional[_AxisType] = ...,
        copy: _bool = ...,
    ) -> DataFrame: ...
    # def tshift
    def tz_convert(
        self, tz: Any, axis: _AxisType = ..., level: Optional[_LevelType] = ..., copy: _bool = ...,
    ) -> DataFrame: ...
    def tz_localize(
        self,
        tz: Any,
        axis: _AxisType = ...,
        level: Optional[_LevelType] = ...,
        copy: _bool = ...,
        ambiguous: Any = ...,
        nonexistent: _str = ...,
    ) -> DataFrame: ...
    def unique(self) -> DataFrame: ...
    @overload
    def var(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: _LevelType,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def var(
        self,
        axis: Optional[_AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[_DType]: ...
    def where(
        self,
        cond: Union[Series[_DType], DataFrame, _np.ndarray],
        other: Any = ...,
        inplace: _bool = ...,
        axis: Optional[_AxisType] = ...,
        level: Optional[_LevelType] = ...,
        errors: _str = ...,
        try_cast: _bool = ...,
    ) -> DataFrame: ...
    def xs(
        self,
        key: Union[_str, Tuple[_str]],
        axis: _AxisType = ...,
        level: Optional[_LevelType] = ...,
        drop_level: _bool = ...,
    ) -> DataFrame: ... 