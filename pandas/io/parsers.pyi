from collections import abc
import sys
#from pandas._libs.parsers import STR_NA_VALUES as STR_NA_VALUES
#from pandas._libs.tslibs import parsing as parsing
from pandas._typing import FilePathOrBuffer as FilePathOrBuffer, Scalar
#from pandas.core import algorithms as algorithms
#from pandas.core.arrays import Categorical as Categorical
#from pandas.core.dtypes.cast import astype_nansafe as astype_nansafe
#from pandas.core.dtypes.common import ensure_object as ensure_object, ensure_str as ensure_str, is_bool_dtype as is_bool_dtype, is_categorical_dtype as is_categorical_dtype, is_dtype_equal as is_dtype_equal, is_extension_array_dtype as is_extension_array_dtype, is_file_like as is_file_like, is_float as is_float, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_list_like as is_list_like, is_object_dtype as is_object_dtype, is_scalar as is_scalar, is_string_dtype as is_string_dtype, pandas_dtype as pandas_dtype
#from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype
#from pandas.core.dtypes.missing import isna as isna
from pandas.core.frame import DataFrame as DataFrame
#from pandas.core.indexes.api import Index as Index, MultiIndex as MultiIndex, RangeIndex as RangeIndex
#from pandas.core.series import Series as Series
#from pandas.errors import AbstractMethodError as AbstractMethodError, EmptyDataError as EmptyDataError, ParserError as ParserError, ParserWarning as ParserWarning
#from pandas.io.common import get_filepath_or_buffer as get_filepath_or_buffer, get_handle as get_handle, infer_compression as infer_compression, validate_header_arg as validate_header_arg
#from pandas.io.date_converters import generic_parser as generic_parser
#from pandas.util._decorators import Appender as Appender
from typing import Any, Callable, IO, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

@overload
def read_csv(
    reader: IO,
    sep: str = ...,
    delimiter: Optional[str] = ...,
    header: Union[int, Sequence[int], Literal["infer"]] = ...,
    names: Optional[Sequence[str]] = ...,
    index_col: Optional[Union[int, str, Sequence, Literal[False]]] = ...,
    usecols: Optional[Union[int, str, Sequence]] = ...,
    squeeze: bool = ...,
    prefix: Optional[str] = ...,
    mangle_dupe_cols: bool = ...,
    dtype: Optional[Union[str, Mapping[str, Any]]] = ...,
    engine: Optional[Literal["c", "python"]] = ...,
    converters: Optional[Mapping[Union[int, str], Callable]] = ...,
    true_values: Optional[Sequence[Scalar]] = ...,
    false_values: Optional[Sequence[Scalar]] = ...,
    skipinitialspace: bool = ...,
    skiprows: Optional[Union[Sequence, int, Callable]] = ...,
    skipfooter: int = ...,
    nrows: Optional[int] = ...,
    na_values: Optional[Any] = ...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: bool = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Optional[Callable] = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: bool = ...,
    chunksize: Optional[int] = ...,
    compression: Optional[Literal["infer", "gzip", "bz2", "zip", "xz"]] = ...,
    thousands: Optional[str] = ...,
    decimal: Optional[str] = ...,
    lineterminator: Optional[str] = ...,
    quotechar: str = ...,
    quoting: int = ...,
    doublequote: bool = ...,
    escapechar: Optional[str] = ...,
    comment: Optional[str] = ...,
    encoding: Optional[str] = ...,
    dialect: Optional[str] = ...,
    error_bad_lines: bool = ...,
    warn_bad_lines: bool = ...,
    delim_whitespace: bool = ...,
    low_memory: bool = ...,
    memory_map: bool = ...,
    float_precision: Optional[str] = ...,
) -> TextParser: ...

@overload
def read_csv(
    filepath: FilePathOrBuffer,
    sep: str = ...,
    delimiter: Optional[str] = ...,
    header: Union[int, Sequence[int], Literal["infer"]] = ...,
    names: Optional[Sequence[str]] = ...,
    index_col: Optional[Union[int, str, Sequence, Literal[False]]] = ...,
    usecols: Optional[Union[int, str, Sequence]] = ...,
    squeeze: bool = ...,
    prefix: Optional[str] = ...,
    mangle_dupe_cols: bool = ...,
    dtype: Optional[Union[str, Mapping[str, Any]]] = ...,
    engine: Optional[Literal["c", "python"]] = ...,
    converters: Optional[Mapping[Union[int, str], Callable]] = ...,
    true_values: Optional[Sequence[Scalar]] = ...,
    false_values: Optional[Sequence[Scalar]] = ...,
    skipinitialspace: bool = ...,
    skiprows: Optional[Union[Sequence, int, Callable]] = ...,
    skipfooter: int = ...,
    nrows: Optional[int] = ...,
    na_values: Optional[Any] = ...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: bool = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Optional[Callable] = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: bool = ...,
    chunksize: Optional[int] = ...,
    compression: Optional[Literal["infer", "gzip", "bz2", "zip", "xz"]] = ...,
    thousands: Optional[str] = ...,
    decimal: Optional[str] = ...,
    lineterminator: Optional[str] = ...,
    quotechar: str = ...,
    quoting: int = ...,
    doublequote: bool = ...,
    escapechar: Optional[str] = ...,
    comment: Optional[str] = ...,
    encoding: Optional[str] = ...,
    dialect: Optional[str] = ...,
    error_bad_lines: bool = ...,
    warn_bad_lines: bool = ...,
    delim_whitespace: bool = ...,
    low_memory: bool = ...,
    memory_map: bool = ...,
    float_precision: Optional[str] = ...,
) -> DataFrame: ...

@overload
def read_table(
    reader: IO,
    sep: str = ...,
    delimiter: Optional[str] = ...,
    header: Union[int, Sequence[int], Literal["infer"]] = ...,
    names: Optional[Sequence[str]] = ...,
    index_col: Optional[Union[int, str, Sequence, Literal[False]]] = ...,
    usecols: Optional[Union[int, str, Sequence]] = ...,
    squeeze: bool = ...,
    prefix: Optional[str] = ...,
    mangle_dupe_cols: bool = ...,
    dtype: Optional[Union[str, Mapping[str, Any]]] = ...,
    engine: Optional[Literal["c", "python"]] = ...,
    converters: Optional[Mapping[Union[int, str], Callable]] = ...,
    true_values: Optional[Sequence[Scalar]] = ...,
    false_values: Optional[Sequence[Scalar]] = ...,
    skipinitialspace: bool = ...,
    skiprows: Optional[Union[Sequence, int, Callable]] = ...,
    skipfooter: int = ...,
    nrows: Optional[int] = ...,
    na_values: Optional[Any] = ...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: bool = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Optional[Callable] = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: bool = ...,
    chunksize: Optional[int] = ...,
    compression: Optional[Literal["infer", "gzip", "bz2", "zip", "xz"]] = ...,
    thousands: Optional[str] = ...,
    decimal: Optional[str] = ...,
    lineterminator: Optional[str] = ...,
    quotechar: str = ...,
    quoting: int = ...,
    doublequote: bool = ...,
    escapechar: Optional[str] = ...,
    comment: Optional[str] = ...,
    encoding: Optional[str] = ...,
    dialect: Optional[str] = ...,
    error_bad_lines: bool = ...,
    warn_bad_lines: bool = ...,
    delim_whitespace: bool = ...,
    low_memory: bool = ...,
    memory_map: bool = ...,
    float_precision: Optional[str] = ...,
) -> TextParser: ...

@overload
def read_table(
    filepath: FilePathOrBuffer,
    sep: str = ...,
    delimiter: Optional[str] = ...,
    header: Union[int, Sequence[int], Literal["infer"]] = ...,
    names: Optional[Sequence[str]] = ...,
    index_col: Optional[Union[int, str, Sequence, Literal[False]]] = ...,
    usecols: Optional[Union[int, str, Sequence]] = ...,
    squeeze: bool = ...,
    prefix: Optional[str] = ...,
    mangle_dupe_cols: bool = ...,
    dtype: Optional[Union[str, Mapping[str, Any]]] = ...,
    engine: Optional[Literal["c", "python"]] = ...,
    converters: Optional[Mapping[Union[int, str], Callable]] = ...,
    true_values: Optional[Sequence[Scalar]] = ...,
    false_values: Optional[Sequence[Scalar]] = ...,
    skipinitialspace: bool = ...,
    skiprows: Optional[Union[Sequence, int, Callable]] = ...,
    skipfooter: int = ...,
    nrows: Optional[int] = ...,
    na_values: Optional[Any] = ...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: bool = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Optional[Callable] = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: bool = ...,
    chunksize: Optional[int] = ...,
    compression: Optional[Literal["infer", "gzip", "bz2", "zip", "xz"]] = ...,
    thousands: Optional[str] = ...,
    decimal: Optional[str] = ...,
    lineterminator: Optional[str] = ...,
    quotechar: str = ...,
    quoting: int = ...,
    doublequote: bool = ...,
    escapechar: Optional[str] = ...,
    comment: Optional[str] = ...,
    encoding: Optional[str] = ...,
    dialect: Optional[str] = ...,
    error_bad_lines: bool = ...,
    warn_bad_lines: bool = ...,
    delim_whitespace: bool = ...,
    low_memory: bool = ...,
    memory_map: bool = ...,
    float_precision: Optional[str] = ...,
) -> DataFrame: ...

def read_fwf(filepath_or_buffer: FilePathOrBuffer, colspecs: Any=..., widths: Any=..., infer_nrows: Any=..., **kwds: Any) -> Any: ...

class TextFileReader(abc.Iterator):
    f: Any = ...
    orig_options: Any = ...
    engine: Any = ...
    chunksize: Any = ...
    nrows: Any = ...
    squeeze: Any = ...
    def __init__(self, f: Any, engine: Optional[Any] = ..., **kwds: Any) -> None: ...
    def close(self) -> None: ...
    def __next__(self): ...
    def read(self, nrows: Optional[Any] = ...): ...
    def get_chunk(self, size: Optional[Any] = ...): ...

class ParserBase:
    names: Any = ...
    orig_names: Any = ...
    prefix: Any = ...
    index_col: Any = ...
    unnamed_cols: Any = ...
    index_names: Any = ...
    col_names: Any = ...
    parse_dates: Any = ...
    date_parser: Any = ...
    dayfirst: Any = ...
    keep_date_col: Any = ...
    na_values: Any = ...
    na_fvalues: Any = ...
    na_filter: Any = ...
    keep_default_na: Any = ...
    true_values: Any = ...
    false_values: Any = ...
    mangle_dupe_cols: Any = ...
    infer_datetime_format: Any = ...
    cache_dates: Any = ...
    header: Any = ...
    handles: Any = ...
    def __init__(self, kwds: Any) -> None: ...
    def close(self) -> None: ...

class CParserWrapper(ParserBase):
    kwds: Any = ...
    unnamed_cols: Any = ...
    names: Any = ...
    orig_names: Any = ...
    index_names: Any = ...
    def __init__(self, src: Any, **kwds: Any) -> None: ...
    def close(self) -> None: ...
    def set_error_bad_lines(self, status: Any) -> None: ...
    def read(self, nrows: Optional[Any] = ...): ...

def TextParser(*args: Any, **kwds: Any): ...
def count_empty_vals(vals: Any): ...

class PythonParser(ParserBase):
    data: Any = ...
    buf: Any = ...
    pos: int = ...
    line_pos: int = ...
    encoding: Any = ...
    compression: Any = ...
    memory_map: Any = ...
    skiprows: Any = ...
    skipfunc: Any = ...
    skipfooter: Any = ...
    delimiter: Any = ...
    quotechar: Any = ...
    escapechar: Any = ...
    doublequote: Any = ...
    skipinitialspace: Any = ...
    lineterminator: Any = ...
    quoting: Any = ...
    skip_blank_lines: Any = ...
    warn_bad_lines: Any = ...
    error_bad_lines: Any = ...
    names_passed: Any = ...
    has_index_names: bool = ...
    verbose: Any = ...
    converters: Any = ...
    dtype: Any = ...
    thousands: Any = ...
    decimal: Any = ...
    comment: Any = ...
    num_original_columns: Any = ...
    columns: Any = ...
    orig_names: Any = ...
    index_names: Any = ...
    nonnum: Any = ...
    def __init__(self, f: Any, **kwds: Any): ...
    def read(self, rows: Optional[Any] = ...): ...
    def get_chunk(self, size: Optional[Any] = ...): ...

class FixedWidthReader(abc.Iterator):
    f: Any = ...
    buffer: Any = ...
    delimiter: Any = ...
    comment: Any = ...
    colspecs: Any = ...
    def __init__(self, f: Any, colspecs: Any, delimiter: Any, comment: Any, skiprows: Optional[Any] = ..., infer_nrows: int = ...) -> None: ...
    def get_rows(self, infer_nrows: Any, skiprows: Optional[Any] = ...): ...
    def detect_colspecs(self, infer_nrows: int = ..., skiprows: Optional[Any] = ...): ...
    def __next__(self): ...

class FixedWidthFieldParser(PythonParser):
    colspecs: Any = ...
    infer_nrows: Any = ...
    def __init__(self, f: Any, **kwds: Any) -> None: ...
