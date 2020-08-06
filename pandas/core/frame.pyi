import datetime
import numpy as np
from matplotlib.axes import Axes as PlotAxes
import sys
#from pandas._config import get_option as get_option
#from pandas._libs import lib as lib
from pandas._typing import Axes as Axes, Axis as Axis, FilePathOrBuffer as FilePathOrBuffer, Level as Level, Renamer as Renamer
from pandas._typing import num, SeriesAxisType, AxisType, DType, DTypeNp, StrLike, Scalar, IndexType, MaskType, np_ndarray_bool, np_ndarray_int64, np_ndarray_str
#from pandas.compat import PY37 as PY37
#from pandas.compat._optional import import_optional_dependency as import_optional_dependency
#from pandas.core import algorithms as algorithms, nanops as nanops, ops as ops
#from pandas.core.accessor import CachedAccessor as CachedAccessor
#from pandas.core.arrays import Categorical as Categorical, ExtensionArray as ExtensionArray
#from pandas.core.arrays.sparse import SparseFrameAccessor as SparseFrameAccessor
#from pandas.core.dtypes.cast import (
#    cast_scalar_to_array as cast_scalar_to_array,
    #coerce_toDTypes as coerce_toDTypes,
#    find_common_type as find_common_type,
    #inferDType_from_scalar as inferDType_from_scalar,
    #invalidate_stringDTypes as invalidate_stringDTypes,
    #maybe_cast_to_datetime as maybe_cast_to_datetime,
#    maybe_convert_platform as maybe_convert_platform,
    #maybe_downcast_toDType as maybe_downcast_toDType,
#    maybe_infer_to_datetimelike as maybe_infer_to_datetimelike,
#    maybe_upcast as maybe_upcast,
#   maybe_upcast_putmask as maybe_upcast_putmask)
#from pandas.core.dtypes.common import (
#    ensure_float64 as ensure_float64,
#    ensure_int64 as ensure_int64,
#    ensure_platform_int as ensure_platform_int,
    #inferDType_from_object as inferDType_from_object,
    #is_boolDType as is_boolDType,
#    is_dict_like as is_dict_like,
    #isDType_equal as isDType_equal,
    #is_extension_arrayDType as is_extension_arrayDType,
    #is_floatDType as is_floatDType,
#    is_hashable as is_hashable,
#    is_integer as is_integer,
    #is_integerDType as is_integerDType,
#    is_iterator as is_iterator,
#    is_list_like as is_list_like,
#    is_named_tuple as is_named_tuple,
    #is_objectDType as is_objectDType,
#    is_scalar as is_scalar,
#    is_sequence as is_sequence,
#    needs_i8_conversion as needs_i8_conversion)
#from pandas.core.dtypes.generic import (
#    ABCDataFrame as ABCDataFrame,
##    ABCIndexClass as ABCIndexClass,
#    ABCMultiIndex as ABCMultiIndex,
#    ABCSeries as ABCSeries)
#from pandas.core.dtypes.missing import isna as isna, notna as notna
from pandas.core.generic import NDFrame as NDFrame
#from pandas.core.groupby import generic as groupby_generic, DataFrameGroupBy as DataFrameGroupBy
from pandas.core.groupby import DataFrameGroupBy as DataFrameGroupBy
from pandas.core.indexes.api import Index as Index
#, ensure_index as ensure_index, ensure_index_from_sequences as ensure_index_from_sequences
#from pandas.core.indexes.datetimes import DatetimeIndex as DatetimeIndex
#from pandas.core.indexes.multi import maybe_droplevels as maybe_droplevels
#from pandas.core.indexes.period import PeriodIndex as PeriodIndex
#from pandas.core.indexing import check_bool_indexer as check_bool_indexer, convert_to_index_sliceable as convert_to_index_sliceable
#from pandas.core.internals import BlockManager as BlockManager
#from pandas.core.internals.construction import arrays_to_mgr as arrays_to_mgr, get_names_from_index as get_names_from_index, init_dict as init_dict, init_ndarray as init_ndarray, masked_rec_array_to_mgr as masked_rec_array_to_mgr, reorder_arrays as reorder_arrays, sanitize_index as sanitize_index, to_arrays as to_arrays
#from pandas.core.ops.missing import dispatch_fill_zeros as dispatch_fill_zeros
from pandas.core.series import Series as Series
#from pandas.io.common import get_filepath_or_buffer as get_filepath_or_buffer
from pandas.io.formats import console as console, format as fmt
#from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.io.formats.style import Styler as Styler
#from pandas.util._decorators import Appender as Appender, Substitution as Substitution, deprecate_kwarg as deprecate_kwarg, rewrite_axis_style_signature as rewrite_axis_style_signature
#from pandas.util._validators import validate_axis_style_args as validate_axis_style_args, validate_bool_kwarg as validate_bool_kwarg, validate_percentile as validate_percentile
from typing import Any, Callable, Dict, Hashable, Iterable, Iterator, List, Mapping, Optional, Sequence, Tuple, Type, Union, overload

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

import numpy as _np
import datetime as _dt


_str = str
_bool = bool


class _iLocIndexerFrame:
    @overload
    def __getitem__(self, idx: Tuple[int, int]) -> DType: ...
    @overload
    def __getitem__(self, idx: Union[IndexType, slice, Tuple[IndexType, IndexType]]) -> DataFrame: ...
    @overload
    def __getitem__(self, idx: Union[int, Tuple[IndexType, int, Tuple[int, IndexType]]]) -> Series[DType]: ...
    def __setitem__(
        self,
        idx: Union[
            int,
            IndexType,
            Tuple[int, int],
            Tuple[IndexType, int],
            Tuple[IndexType, IndexType],
            Tuple[int, IndexType],
        ],
        value: Union[float, Series[DType], DataFrame],
    ) -> None: ...


class _LocIndexerFrame:
    @overload
    def __getitem__(self, idx: Union[int, slice, MaskType],) -> DataFrame: ...
    @overload
    def __getitem__(self, idx: StrLike,) -> Series[DType]: ...
    @overload
    def __getitem__(self, idx: Tuple[StrLike, StrLike],) -> float: ...
    @overload
    def __getitem__(self, idx: Tuple[Union[MaskType, List[str]], Union[MaskType, List[str]]],) -> DataFrame: ...
    def __setitem__(
        self,
        idx: Union[MaskType, StrLike, Tuple[Union[MaskType, List[str]], Union[MaskType, List[str]]],],
        value: Union[float, _np.ndarray, Series[DType], DataFrame],
    ) -> None: ...


class DataFrame(NDFrame):
    _ListLike = Union[
        np.ndarray, List[DType], Dict[_str, _np.ndarray], Sequence, Index, Series[DType],
    ]

    def __init__(
        self,
        data: Optional[Union[_ListLike, DataFrame, Dict[_str, Any]]] = ...,
        index: Optional[_ListLike] = ...,
        columns: Optional[_ListLike] = ...,
        dtype: Any = ...,
        copy: bool = ...,
    ): ...

    def __init__(self, data: Any=..., index: Optional[Axes]=..., columns: Optional[Axes]=..., dtype: Optional[DType]=..., copy: bool=...) -> None: ...
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
    def dot(self, other: Series[DType]) -> Series[DType]: ...
    def __matmul__(self, other: Any): ...
    def __rmatmul__(self, other: Any): ...
    @classmethod
    def from_dict(cls: Any, data: Any, orient: Any=..., dtype: Any=..., columns: Any=...) -> DataFrame: ...
    @overload
    def to_numpy(self) -> _np.ndarray: ...
    @overload
    def to_numpy(self, dtype: Optional[Type[DTypeNp]]) -> _np.ndarray: ...
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
        columnDTypes: Optional[Union[_str, Dict]] = ...,
        indexDTypes: Optional[Union[_str, Dict]] = ...,
    ) -> np.recarray: ...
    def to_stata(
        self,
        path: FilePathOrBuffer,
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
    def to_markdown(self, buf: Optional[FilePathOrBuffer], mode: Optional[_str] = ..., **kwargs) -> None: ...
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
        buf: Optional[FilePathOrBuffer],
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
    def memory_usage(self, index: _bool = ..., deep: _bool = ...) -> Series[DType]: ...
    def transpose(self, *args: Any, copy: bool=...) -> DataFrame: ...
    @property
    def T(self) -> DataFrame: ...
    @overload
    def __getitem__(self, idx: _str) -> Series[DType]: ...
    @overload
    def __getitem__(self, rows: slice) -> DataFrame: ...
    @overload
    def __getitem__(
        self, idx: Union[Series[_bool], DataFrame, List[_str], Index[_str], np.ndarray],
    ) -> DataFrame: ...
    def __setitem__(self, key: Any, value: Any): ...
    def query(self, expr: _str, inplace: _bool = ..., **kwargs) -> DataFrame: ...
    def eval(self, expr: _str, inplace: _bool = ..., **kwargs) -> Any: ...
    def selectDTypes(
        self, include: Optional[Union[_str, List[_str]]] = ..., exclude: Optional[Union[_str, List[_str]]] = ...,
    ) -> DataFrame: ...
    def insert(self, loc: int, column: Any, value: Union[int, _ListLike], allow_duplicates: _bool = ...,) -> None: ...
    def assign(self, **kwargs) -> DataFrame: ...
    def lookup(self, row_labels: Sequence, col_labels: Sequence) -> np.ndarray: ...
    def align(
        self,
        other: Union[DataFrame, Series[DType]],
        join: Literal["inner", "outer", "left", "right"] = ...,
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        copy: _bool = ...,
        fill_value: Optional[Any] = ...,
        method: Optional[Literal["backfill", "bfill", "pad", "ffill"]] = ...,
        limit: Optional[int] = ...,
        fill_axis: AxisType = ...,
        broadcast_axis: Optional[AxisType] = ...,
    ) -> DataFrame: ...
    def reindex(
        self,
        labels: Optional[List] = ...,
        index: Optional[Any] = ...,
        columns: Optional[Any] = ...,
        axis: Optional[AxisType] = ...,
        method: Optional[Literal["backfill", "bfill", "pad", "ffill", "nearest"]] = ...,
        copy: _bool = ...,
        level: Optional[Level] = ...,
        fill_value: Any = ...,
        limit: Optional[int] = ...,
        tolerance: Optional[Any] = ...,
    ) -> DataFrame: ...
    def drop(
        self,
        labels: Optional[Union[_str, List]] = ...,
        axis: AxisType = ...,
        index: Optional[Union[List[_str], List[int], Index]] = ...,
        columns: Optional[Union[_str, List]] = ...,
        level: Optional[Level] = ...,
        inplace: _bool = ...,
        errors: Literal["ignore", "raise"] = ...,
    ) -> DataFrame: ...
    # looks like rename is missing an index arg?
    @overload
    def rename(
        self,
        mapper: Optional[Callable],
        axis: Optional[AxisType] = ...,
        copy: _bool = ...,
        inplace: _bool = ...,
        level: Optional[Level] = ...,
        errors: Literal["ignore", "raise"] = ...,
    ) -> DataFrame: ...
    @overload
    def rename(
        self,
        columns: Optional[Dict[_str, _str]],
        axis: Optional[AxisType] = ...,
        copy: _bool = ...,
        inplace: _bool = ...,
        level: Optional[Level] = ...,
        errors: Literal["ignore", "raise"] = ...,
    ) -> DataFrame: ...
    @overload
    def fillna(
        self,
        value: Optional[Union[Scalar, Dict, Series, DataFrame]] = ...,
        method: Optional[Literal["backfill", "bfill", "ffill", "pad"]] = ...,
        axis: Optional[AxisType] = ...,
        inplace: Optional[Literal[False]] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
    ) -> DataFrame: ...
    @overload
    def fillna(
        self,
        value: Optional[Union[Scalar, Dict, Series, DataFrame]] = ...,
        method: Optional[Literal["backfill", "bfill", "ffill", "pad"]] = ...,
        axis: Optional[AxisType] = ...,
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
        axis: AxisType = ...,
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
        level: Level = ...,
        drop: _bool = ...,
        col_level: Union[int, _str] = ...,
        col_fill: Hashable = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def reset_index(
        self,
        level: Level = ...,
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
        axis: AxisType = ...,
        how: Literal["any", "all"] = ...,
        thresh: Optional[int] = ...,
        subset: Optional[List] = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def dropna(
        self,
        axis: AxisType = ...,
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
    ) -> Series[DType]: ...
    @overload
    def sort_values(
        self,
        by: List[_str],
        axis: AxisType = ...,
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
        axis: AxisType = ...,
        ascending: _bool = ...,
        inplace: Optional[Literal[False]] = ...,
        kind: Literal["quicksort", "mergesort", "heapsort"] = ...,
        na_position: Literal["first", "last"] = ...,
        ignore_index: _bool = ...,
    ) -> DataFrame: ...
    @overload
    def sort_index(
        self,
        axis: AxisType = ...,
        level: Optional[Level] = ...,
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
        axis: AxisType = ...,
        level: Optional[Level] = ...,
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
    def swaplevel(self, i: Level = ..., j: Level = ..., axis: AxisType = ...) -> DataFrame: ...
    def reorder_levels(self, order: List, axis: AxisType = ...) -> DataFrame: ...
    def combine(
        self, other: DataFrame, func: Callable, fill_value: Optional[Any] = ..., overwrite: _bool = ...,
    ) -> DataFrame: ...
    def combine_first(self, other: DataFrame) -> DataFrame: ...
    def update(
        self,
        other: Union[DataFrame, Series[DType]],
        join: Literal["left"] = ...,
        overwrite: _bool = ...,
        filter_func: Optional[Callable] = ...,
        errors: Literal["raise", "ignore"] = ...,
    ) -> None: ...
    def groupby(
        self,
        by: Optional[Union[List[_str], _str]],
        axis: AxisType = ...,
        level: Optional[Level] = ...,
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
    def stack(self, level: Level = ..., dropna: _bool = ...) -> Union[DataFrame, Series[DType]]: ...
    def explode(self, column: Union[str, Tuple]) -> DataFrame: ...
    def unstack(
        self, level: Level = ..., fill_value: Optional[Union[int, _str, Dict]] = ...,
    ) -> Union[DataFrame, Series[DType]]: ...
    def melt(
        self,
        id_vars: Optional[Any] = ...,
        value_vars: Optional[Any] = ...,
        var_name: Optional[Any] = ...,
        value_name: Any = ...,
        col_level: Optional[Union[int, _str]] = ...,
    ) -> DataFrame: ...
    def diff(self, periods: int = ..., axis: AxisType = ...) -> DataFrame: ...
    @overload
    def agg(self, func: Union[Callable, _str], axis: AxisType = ..., **kwargs) -> Series[DType]: ...
    @overload
    def agg(self, func: Union[List[Callable], Dict[_str, Callable]], axis: AxisType = ..., **kwargs) -> DataFrame: ...
    @overload
    def aggregate(self, func: Union[Callable, _str], axis: AxisType = ..., **kwargs) -> Series[DType]: ...
    @overload
    def aggregate(
        self, func: Union[List[Callable], Dict[_str, Callable]], axis: AxisType = ..., **kwargs
    ) -> DataFrame: ...
    def transform(self, func: Callable, axis: AxisType = ..., *args, **kwargs) -> DataFrame: ...
    @overload
    def apply(self, f: Callable[..., int]) -> Series[DType]: ...
    @overload
    def apply(
        self, f: Callable, axis: AxisType = ..., raw: _bool = ..., result_type: Optional[_str] = ...,
    ) -> DataFrame: ...
    def applymap(self, func: Callable) -> DataFrame: ...
    def append(
        self,
        other: Union[DataFrame, Series[DType], Dict[_str, Any]],
        ignore_index: _bool = ...,
        verify_integrity: _bool = ...,
        sort: _bool = ...,
    ) -> DataFrame: ...
    def join(
        self,
        other: Union[DataFrame, Series[DType], List[DataFrame]],
        on: Optional[Union[_str, List[_str]]] = ...,
        how: Literal["left", "right", "outer", "inner"] = ...,
        lsuffix: _str = ...,
        rsuffix: _str = ...,
        sort: _bool = ...,
    ) -> DataFrame: ...
    def merge(
        self,
        right: Union[DataFrame, Series[DType]],
        how: Literal["left", "right", "inner", "outer"] = ...,
        on: Optional[Union[Level, List[Level]]] = ...,
        left_on: Optional[Union[Level, List[Level]]] = ...,
        right_on: Optional[Union[Level, List[Level]]] = ...,
        left_index: _bool = ...,
        right_index: _bool = ...,
        sort: _bool = ...,
        suffixes: Tuple[_str, _str] = ...,
        copy: _bool = ...,
        indicator: Union[_bool, _str] = ...,
        validate: Optional[_str] = ...,
    ) -> DataFrame: ...
    def round(self, decimals: Union[int, Dict, Series[DType]] = ..., *args, **kwargs) -> DataFrame: ...
    def corr(self, method: Literal["pearson", "kendall", "spearman"] = ..., min_periods: int = ...,) -> DataFrame: ...
    def cov(self, min_periods: Optional[int] = ...) -> DataFrame: ...
    def corrwith(
        self,
        other: Union[DataFrame, Series[DType]],
        axis: Optional[AxisType] = ...,
        drop: _bool = ...,
        method: Literal["pearson", "kendall", "spearman"] = ...,
    ) -> Series: ...
    @overload
    def count(self, axis: AxisType = ..., numeric_only: _bool = ..., *, level: Level) -> DataFrame: ...
    @overload
    def count(self, axis: AxisType = ..., level: None = ..., numeric_only: _bool = ...) -> Series[DType]: ...
    def nunique(self, axis: AxisType = ..., dropna=True) -> Series[DType]: ...
    def idxmax(self, axis: AxisType, skipna: _bool = ...) -> Series[DType]: ...
    def idxmin(self, axis: AxisType, skipna: _bool = ...) -> Series[DType]: ...
    @overload
    def mode(
        self, axis: AxisType = ..., skipna: _bool = ..., numeric_only: _bool = ..., *, level: Level, **kwargs
    ) -> DataFrame: ...
    @overload
    def mode(
        self, axis: AxisType = ..., skipna: _bool = ..., level: None = ..., numeric_only: _bool = ..., **kwargs
    ) -> Series[DType]: ...
    @overload
    def quantile(
        self,
        q: float = ...,
        axis: AxisType = ...,
        numeric_only: _bool = ...,
        interpolation: Literal["linear", "lower", "higher", "midpoint", "nearest"] = ...,
    ) -> Series: ...
    @overload
    def quantile(
        self,
        q: List = ...,
        axis: AxisType = ...,
        numeric_only: _bool = ...,
        interpolation: Literal["linear", "lower", "higher", "midpoint", "nearest"] = ...,
    ) -> DataFrame: ...
    def to_timestamp(
        self,
        freq: Optional[Any] = ...,
        how: Literal["start", "end", "s", "e"] = ...,
        axis: AxisType = ...,
        copy: _bool = ...,
    ) -> DataFrame: ...
    def to_period(self, freq: Optional[_str] = ..., axis: AxisType = ..., copy: _bool = ...) -> DataFrame: ...
    def isin(self, values: Union[Iterable, Series[DType], DataFrame, Dict]) -> DataFrame: ...
    def plot(self, kind: _str, yerr: DataFrame, **kwargs) -> PlotAxes: ...
    def hist(
        data,
        column: Optional[Union[_str, List[_str]]] = ...,
        by: Optional[Union[_str, _ListLike]] = ...,
        grid: _bool = ...,
        xlabelsize: Optional[int] = ...,
        xrot: Optional[float] = ...,
        ylabelsize: Optional[int] = ...,
        yrot: Optional[float] = ...,
        ax: Optional[PlotAxes] = ...,
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
        ax: Optional[PlotAxes] = ...,
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
    def __and__(self, other: Union[num, _ListLike, DataFrame], axis: SeriesAxisType = ...) -> DataFrame: ...
    def __delitem__(self, key: _str) -> None: ...
    def __div__(self, other: Union[num, _ListLike, DataFrame]) -> DataFrame: ...
    def __eq__(self, other: Union[float, Series[DType], DataFrame]) -> DataFrame: ...  # type: ignore
    def __exp__(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: AxisType = ...,
        level: Level = ...,
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
    def __ne__(self, other: Union[float, Series[DType], DataFrame]) -> DataFrame: ...  # type: ignore
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
    def dtypes(self) -> Series[DType]: ...
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
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def add_prefix(self, prefix: _str) -> DataFrame: ...
    def add_suffix(self, suffix: _str) -> DataFrame: ...
    @overload
    def all(
        self, axis: AxisType = ..., bool_only: Optional[_bool] = ..., skipna: _bool = ..., level: None = ..., **kwargs
    ) -> Series[DType]: ...
    @overload
    def all(
        self,
        axis: AxisType = ...,
        bool_only: Optional[_bool] = ...,
        skipna: _bool = ...,
        *,
        level: Level,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def any(
        self, axis: AxisType = ..., bool_only: Optional[_bool] = ..., skipna: _bool = ..., level: None = ..., **kwargs
    ) -> Series[DType]: ...
    @overload
    def any(
        self, axis: AxisType = ..., bool_only: _bool = ..., skipna: _bool = ..., *, level: Level, **kwargs
    ) -> DataFrame: ...
    def asof(self, where: Any, subset: Optional[Union[_str, List[_str]]] = ...) -> DataFrame: ...
    def asfreq(
        self,
        freq: Any,
        method: Optional[Literal["backfill", "bfill", "pad", "ffill"]] = ...,
        how: Optional[Literal["start", "end"]] = ...,
        normalize: _bool = ...,
        fill_value: Optional[Scalar] = ...,
    ) -> DataFrame: ...
    def astype(self, dtype: Union[_str, Dict[_str, _str]], copy: _bool = ..., errors: _str = ...,) -> DataFrame: ...
    def at_time(
        self, time: Union[_str, datetime.time], asof: _bool = ..., axis: Optional[AxisType] = ...,
    ) -> DataFrame: ...
    def between_time(
        self,
        start_time: Union[_str, datetime.time],
        end_time: Union[_str, datetime.time],
        include_start: _bool = ...,
        include_end: _bool = ...,
        axis: Optional[AxisType] = ...,
    ) -> DataFrame: ...
    @overload
    def bfill(
        self,
        value: Optional[Union[float, Dict, Series[DType], DataFrame]] = ...,
        axis: Optional[AxisType] = ...,
        inplace: Optional[Literal[False]] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
    ) -> DataFrame: ...
    @overload
    def bfill(
        self,
        value: Optional[Union[float, Dict, Series[DType], DataFrame]] = ...,
        axis: Optional[AxisType] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    def clip(
        self,
        lower: Optional[float] = ...,
        upper: Optional[float] = ...,
        axis: Optional[AxisType] = ...,
        inplace: _bool = ...,
        *args,
        **kwargs
    ) -> DataFrame: ...
    def convertDTypes(
        self,
        infer_objects: _bool = ...,
        convert_string: _bool = ...,
        convert_integer: _bool = ...,
        convert__boolean: _bool = ...,
    ) -> DataFrame: ...
    def copy(self, deep: _bool = ...) -> DataFrame: ...
    def cummax(self, axis: Optional[AxisType] = ..., skipna: _bool = ..., *args, **kwargs) -> DataFrame: ...
    def cummin(self, axis: Optional[AxisType] = ..., skipna: _bool = ..., *args, **kwargs) -> DataFrame: ...
    def cumprod(self, axis: Optional[AxisType] = ..., skipna: _bool = ..., *args, **kwargs) -> DataFrame: ...
    def cumsum(self, axis: Optional[AxisType] = ..., skipna: _bool = ..., *args, **kwargs) -> DataFrame: ...
    def describe(
        self,
        percentiles: Optional[List[float]] = ...,
        include: Optional[Union[Literal["all"], List[DType]]] = ...,
        exclude: Optional[List[DType]] = ...,
    ) -> DataFrame: ...
    def div(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def divide(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def droplevel(self, level: Level = ..., axis: AxisType = ...) -> DataFrame: ...
    def eq(self, other: Any, axis: AxisType = ..., level: Optional[Level] = ...) -> DataFrame: ...
    def equals(self, other: Union[Series[DType], DataFrame]) -> _bool: ...
    def ewm(
        self,
        com: Optional[float] = ...,
        span: Optional[float] = ...,
        halflife: Optional[float] = ...,
        alpha: Optional[float] = ...,
        min_periods: int = ...,
        adjust: _bool = ...,
        ignore_na: _bool = ...,
        axis: AxisType = ...,
    ) -> DataFrame: ...
    def exp(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def expanding(self, min_periods: int = ..., center: _bool = ..., axis: AxisType = ...) -> Any: ...  # for now
    @overload
    def ffill(
        self,
        value: Optional[Union[Scalar, Dict, Series[DType], DataFrame]] = ...,
        axis: Optional[AxisType] = ...,
        inplace: Optional[Literal[False]] = ...,
        limit: int = ...,
        downcast: Optional[Dict] = ...,
    ) -> DataFrame: ...
    @overload
    def ffill(
        self,
        value: Optional[Union[Scalar, Dict, Series, DataFrame]] = ...,
        axis: Optional[AxisType] = ...,
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
        axis: Optional[AxisType] = ...,
    ) -> DataFrame: ...
    def first(self, offset: Any) -> DataFrame: ...
    def first_valid_index(self) -> Scalar: ...
    def floordiv(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    # def from_dict
    # def from_records
    def fulldiv(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def ge(self, other: Any, axis: AxisType = ..., level: Optional[Level] = ...) -> DataFrame: ...
    # def get
    def gt(self, other: Any, axis: AxisType = ..., level: Optional[Level] = ...) -> DataFrame: ...
    def head(self, n: int = ...) -> DataFrame: ...
    def infer_objects(self) -> DataFrame: ...
    # def info
    @overload
    def interpolate(
        self,
        method: _str = ...,
        axis: AxisType = ...,
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
        axis: AxisType = ...,
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
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def kurt(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[DType]: ...
    @overload
    def kurtosis(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def kurtosis(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[DType]: ...
    def last(self, offset: Any) -> DataFrame: ...
    def last_valid_index(self) -> Scalar: ...
    def le(self, other: Any, axis: AxisType = ..., level: Optional[Level] = ...) -> DataFrame: ...
    def lt(self, other: Any, axis: AxisType = ..., level: Optional[Level] = ...) -> DataFrame: ...
    @overload
    def mad(
        self, axis: Optional[AxisType] = ..., skipna: Optional[_bool] = ..., level: None = ...,
    ) -> Series[DType]: ...
    @overload
    def mad(
        self, axis: Optional[AxisType] = ..., skipna: Optional[_bool] = ..., *, level: Level, **kwargs
    ) -> DataFrame: ...
    def mask(
        self,
        cond: Union[Series[DType], DataFrame, _np.ndarray],
        other: Any = ...,
        inplace: _bool = ...,
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        errors: _str = ...,
        try_cast: _bool = ...,
    ) -> DataFrame: ...
    @overload
    def max(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def max(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[DType]: ...
    @overload
    def mean(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def mean(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[DType]: ...
    @overload
    def median(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def median(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[DType]: ...
    @overload
    def min(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def min(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[DType]: ...
    def mod(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def mul(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def multiply(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def ne(self, other: Any, axis: AxisType = ..., level: Optional[Level] = ...) -> DataFrame: ...
    def pct_change(
        self,
        periods: int = ...,
        fill_method: _str = ...,
        limit: Optional[int] = ...,
        freq: Optional[Any] = ...,
        **kwargs
    ) -> DataFrame: ...
    def pipe(self, func: Callable, *args, **kwargs) -> Any: ...
    def pop(self, item: _str) -> Series[DType]: ...
    def pow(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    @overload
    def prod(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        *,
        level: Level,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def prod(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs
    ) -> Series: ...
    def product(
        self,
        axis: Optional[AxisType] = ...,
        skipna: _bool = ...,
        level: Optional[Level] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs
    ) -> DataFrame: ...
    def radd(
        self, other: Any, axis: AxisType = ..., level: Optional[Level] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rank(
        self,
        axis: AxisType = ...,
        method: Literal["average", "min", "max", "first", "dense"] = ...,
        numeric_only: Optional[_bool] = ...,
        na_option: Literal["keep", "top", "bottom"] = ...,
        ascending: _bool = ...,
        pct: _bool = ...,
    ) -> DataFrame: ...
    def rdiv(
        self, other: Any, axis: AxisType = ..., level: Optional[Level] = ..., fill_value: Optional[float] = ...,
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
        index: Optional[IndexType] = ...,
        columns: Optional[Any] = ...,
        axis: Optional[AxisType] = ...,
        copy: _bool = ...,
        *,
        inplace: Literal[True]
    ) -> None: ...
    @overload
    def rename_axis(
        self,
        mapper: Optional[Any] = ...,
        index: Optional[IndexType] = ...,
        columns: Optional[Any] = ...,
        axis: Optional[AxisType] = ...,
        copy: _bool = ...,
        inplace: Optional[Literal[False]] = ...,
    ) -> DataFrame: ...
    def resample(
        self,
        rule: Any,
        axis: AxisType = ...,
        closed: Optional[_str] = ...,
        label: Optional[_str] = ...,
        convention: Literal["start", "end", "s", "e"] = ...,
        kind: Optional[Literal["timestamp", "period"]] = ...,
        loffset: Optional[Any] = ...,
        base: int = ...,
        on: Optional[_str] = ...,
        level: Optional[Level] = ...,
    ) -> Any: ...
    def rfloordiv(
        self,
        other: Any,
        axis: AxisType = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[Union[float, None]] = ...,
    ) -> DataFrame: ...
    def rmod(
        self, other: Any, axis: AxisType = ..., level: Optional[Level] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rmul(
        self, other: Any, axis: AxisType = ..., level: Optional[Level] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rolling(
        self,
        window: Any,
        min_periods: Optional[int] = ...,
        center: _bool = ...,
        win_type: Optional[_str] = ...,
        on: Optional[_str] = ...,
        axis: AxisType = ...,
        closed: Optional[_str] = ...,
    ) -> Any: ...  # For now
    def rpow(
        self, other: Any, axis: AxisType = ..., level: Optional[Level] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rsub(
        self, other: Any, axis: AxisType = ..., level: Optional[Level] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def rtruediv(
        self, other: Any, axis: AxisType = ..., level: Optional[Level] = ..., fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    # sample is missing a weights arg
    @overload
    def sample(
        self,
        frac: Optional[float],
        random_state: Optional[int] = ...,
        replace: _bool = ...,
        axis: Optional[AxisType] = ...,
    ) -> DataFrame: ...
    @overload
    def sample(
        self,
        n: Optional[int],
        random_state: Optional[int] = ...,
        replace: _bool = ...,
        axis: Optional[AxisType] = ...,
    ) -> DataFrame: ...

    @overload
    def sem(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def sem(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[DType]: ...
    @overload
    def set_axis(self, labels: List, inplace: Literal[True], axis: AxisType = ...) -> None: ...
    @overload
    def set_axis(self, labels: List, axis: AxisType = ..., inplace: Optional[Literal[False]] = ...,) -> DataFrame: ...
    @overload
    def skew(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def skew(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[DType]: ...
    def slice_shift(self, periods: int = ..., axis: AxisType = ...) -> DataFrame: ...
    def squeeze(self, axis: Optional[AxisType] = ...) -> Any: ...
    @overload
    def std(
        self,
        axis: AxisType = ...,
        skipna: _bool = ...,
        ddof: int = ...,
        numeric_only: _bool = ...,
        *,
        level: Level,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def std(
        self,
        axis: AxisType = ...,
        skipna: _bool = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: _bool = ...,
        **kwargs
    ) -> Series[DType]: ...
    def sub(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def subtract(
        self,
        other: Union[num, _ListLike, DataFrame],
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    @overload
    def sum(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        *,
        level: Level,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def sum(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        numeric_only: Optional[_bool] = ...,
        min_count: int = ...,
        **kwargs
    ) -> Series[DType]: ...
    def swapaxes(self, axis1: AxisType, axis2: AxisType, copy: _bool = ...) -> DataFrame: ...
    def tail(self, n: int = ...) -> DataFrame: ...
    def take(self, indices: List, axis: AxisType = ..., is_copy: Optional[_bool] = ..., **kwargs) -> DataFrame: ...
    def transform(self, func: Union[List[Callable], Dict[_str, Callable]], axis: AxisType = ...,) -> DataFrame: ...
    def transpose(self, *args, copy: _bool = ...) -> DataFrame: ...
    T = transpose
    def tshift(self, periods: int = ..., freq: Any = ..., axis: AxisType = ...) -> DataFrame: ...
    def to_clipboard(self, excel: _bool = ..., sep: Optional[_str] = ..., **kwargs) -> None: ...
    @overload
    def to_csv(
        self,
        path_or_buf: Optional[FilePathOrBuffer],
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
        path_or_buf: FilePathOrBuffer,
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
        path_or_buf: Optional[FilePathOrBuffer],
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
        buf: Optional[FilePathOrBuffer],
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
        dtype: Optional[Union[Dict, Scalar]] = ...,
        method: Optional[Union[_str, Callable]] = ...,
    ) -> None: ...
    @overload
    def to_string(
        self,
        buf: Optional[FilePathOrBuffer],
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
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        fill_value: Optional[float] = ...,
    ) -> DataFrame: ...
    def truncate(
        self,
        before: Optional[Union[datetime.date, _str, int]] = ...,
        after: Optional[Union[datetime.date, _str, int]] = ...,
        axis: Optional[AxisType] = ...,
        copy: _bool = ...,
    ) -> DataFrame: ...
    # def tshift
    def tz_convert(
        self, tz: Any, axis: AxisType = ..., level: Optional[Level] = ..., copy: _bool = ...,
    ) -> DataFrame: ...
    def tz_localize(
        self,
        tz: Any,
        axis: AxisType = ...,
        level: Optional[Level] = ...,
        copy: _bool = ...,
        ambiguous: Any = ...,
        nonexistent: _str = ...,
    ) -> DataFrame: ...
    def unique(self) -> DataFrame: ...
    @overload
    def var(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        *,
        level: Level,
        **kwargs
    ) -> DataFrame: ...
    @overload
    def var(
        self,
        axis: Optional[AxisType] = ...,
        skipna: Optional[_bool] = ...,
        level: None = ...,
        ddof: int = ...,
        numeric_only: Optional[_bool] = ...,
        **kwargs
    ) -> Series[DType]: ...
    def where(
        self,
        cond: Union[Series[DType], DataFrame, _np.ndarray],
        other: Any = ...,
        inplace: _bool = ...,
        axis: Optional[AxisType] = ...,
        level: Optional[Level] = ...,
        errors: _str = ...,
        try_cast: _bool = ...,
    ) -> DataFrame: ...
    def xs(
        self,
        key: Union[_str, Tuple[_str]],
        axis: AxisType = ...,
        level: Optional[Level] = ...,
        drop_level: _bool = ...,
    ) -> DataFrame: ... 