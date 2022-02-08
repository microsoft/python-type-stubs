from __future__ import annotations
from collections import abc
import sys
from pandas._typing import FilePathOrBuffer as FilePathOrBuffer, Scalar
from pandas.core.frame import DataFrame as DataFrame
from typing import Any, Callable, List, Mapping, Optional, Sequence, Union, overload

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

@overload
def read_csv(
    reader: FilePathOrBuffer,
    *,
    sep: str = ...,
    delimiter: Optional[str] = ...,
    header: Union[int, Sequence[int], str, Literal["infer"]] = ...,
    names: Optional[Sequence[str]] = ...,
    index_col: Optional[Union[int, str, Sequence, str, Literal[False]]] = ...,
    usecols: Optional[Union[int, str, Sequence]] = ...,
    squeeze: bool = ...,
    prefix: Optional[str] = ...,
    mangle_dupe_cols: bool = ...,
    dtype: Optional[Union[str, Mapping[str, Any]]] = ...,
    engine: Optional[Union[str, Literal["c", "python"]]] = ...,
    converters: Optional[Mapping[Union[int, str], Callable]] = ...,
    true_values: Optional[Sequence[Scalar]] = ...,
    false_values: Optional[Sequence[Scalar]] = ...,
    skipinitialspace: bool = ...,
    skiprows: Optional[Union[Sequence, int, Callable]] = ...,
    skipfooter: int = ...,
    nrows: Optional[int] = ...,
    na_values=...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: Union[bool, List[int], List[str]] = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Optional[Callable] = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: Literal[True],
    chunksize: Optional[int] = ...,
    compression: Optional[Union[str, Literal["infer", "gzip", "bz2", "zip", "xz"]]] = ...,
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
) -> TextFileReader: ...
@overload
def read_csv(
    filepath: FilePathOrBuffer,
    *,
    sep: str = ...,
    delimiter: Optional[str] = ...,
    header: Optional[int | Sequence[int] | str | Literal["infer"]] = ...,
    names: Optional[Sequence[str]] = ...,
    index_col: Optional[Union[int, str, Sequence, Union[bool, Literal[False]]]] = ...,
    usecols: Optional[Union[int, str, Sequence]] = ...,
    squeeze: bool = ...,
    prefix: Optional[str] = ...,
    mangle_dupe_cols: bool = ...,
    dtype: Optional[Union[str, Mapping[str, Any]]] = ...,
    engine: Optional[Union[str, Literal["c", "python"]]] = ...,
    converters: Optional[Mapping[Union[int, str], Callable]] = ...,
    true_values: Optional[Sequence[Scalar]] = ...,
    false_values: Optional[Sequence[Scalar]] = ...,
    skipinitialspace: bool = ...,
    skiprows: Optional[Union[Sequence, int, Callable]] = ...,
    skipfooter: int = ...,
    nrows: Optional[int] = ...,
    na_values=...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: Union[bool, List[int], List[str]] = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Optional[Callable] = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: Literal[False],
    chunksize: int,
    compression: Optional[Union[str, Literal["infer", "gzip", "bz2", "zip", "xz"]]] = ...,
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
    on_bad_lines: Literal["error", "warn", "skip"] = "error",
    delim_whitespace: bool = ...,
    low_memory: bool = ...,
    memory_map: bool = ...,
    float_precision: Optional[str] = ...,
    storage_options: Optional[Dict[str, Any]] = ...,
) -> TextFileReader: ...
@overload
def read_csv(
    filepath: FilePathOrBuffer,
    *,
    sep: str = ...,
    delimiter: Optional[str] = ...,
    header: Optional[int | Sequence[int] | str | Literal["infer"]] = ...,
    names: Optional[Sequence[str]] = ...,
    index_col: Optional[Union[int, str, Sequence, Union[bool, Literal[False]]]] = ...,
    usecols: Optional[Union[int, str, Sequence]] = ...,
    squeeze: bool = ...,
    prefix: Optional[str] = ...,
    mangle_dupe_cols: bool = ...,
    dtype: Optional[Union[str, Mapping[str, Any]]] = ...,
    engine: Optional[Union[str, Literal["c", "python"]]] = ...,
    converters: Optional[Mapping[Union[int, str], Callable]] = ...,
    true_values: Optional[Sequence[Scalar]] = ...,
    false_values: Optional[Sequence[Scalar]] = ...,
    skipinitialspace: bool = ...,
    skiprows: Optional[Union[Sequence, int, Callable]] = ...,
    skipfooter: int = ...,
    nrows: Optional[int] = ...,
    na_values=...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: Union[bool, List[int], List[str]] = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Optional[Callable] = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: Literal[False] = ...,
    chunksize: None = ...,
    compression: Optional[Union[str, Literal["infer", "gzip", "bz2", "zip", "xz"]]] = ...,
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
    on_bad_lines: Literal["error", "warn", "skip"] = "error",
    delim_whitespace: bool = ...,
    low_memory: bool = ...,
    memory_map: bool = ...,
    float_precision: Optional[str] = ...,
    storage_options: Optional[Dict[str, Any]] = ...,
) -> DataFrame: ...
@overload
def read_csv(
    filepath: FilePathOrBuffer,
    *,
    sep: str = ...,
    delimiter: Optional[str] = ...,
    header: Optional[int | Sequence[int] | str | Literal["infer"]] = ...,
    names: Optional[Sequence[str]] = ...,
    index_col: Optional[Union[int, str, Sequence, Union[bool, Literal[False]]]] = ...,
    usecols: Optional[Union[int, str, Sequence]] = ...,
    squeeze: bool = ...,
    prefix: Optional[str] = ...,
    mangle_dupe_cols: bool = ...,
    dtype: Optional[Union[str, Mapping[str, Any]]] = ...,
    engine: Optional[Union[str, Literal["c", "python"]]] = ...,
    converters: Optional[Mapping[Union[int, str], Callable]] = ...,
    true_values: Optional[Sequence[Scalar]] = ...,
    false_values: Optional[Sequence[Scalar]] = ...,
    skipinitialspace: bool = ...,
    skiprows: Optional[Union[Sequence, int, Callable]] = ...,
    skipfooter: int = ...,
    nrows: Optional[int] = ...,
    na_values=...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: Union[bool, List[int], List[str]] = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Optional[Callable] = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: bool = ...,
    chunksize: int = ...,
    compression: Optional[Union[str, Literal["infer", "gzip", "bz2", "zip", "xz"]]] = ...,
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
    on_bad_lines: Literal["error", "warn", "skip"] = "error",
    delim_whitespace: bool = ...,
    low_memory: bool = ...,
    memory_map: bool = ...,
    float_precision: Optional[str] = ...,
    storage_options: Optional[Dict[str, Any]] = ...,
) -> TextFileReader: ...
@overload
def read_csv(
    filepath: FilePathOrBuffer,
    sep: str = ...,
    delimiter: Optional[str] = ...,
    header: Optional[int | Sequence[int] | str | Literal["infer"]] = ...,
    names: Optional[Sequence[str]] = ...,
    index_col: Optional[Union[int, str, Sequence, Union[bool, Literal[False]]]] = ...,
    usecols: Optional[Union[int, str, Sequence]] = ...,
    squeeze: bool = ...,
    prefix: Optional[str] = ...,
    mangle_dupe_cols: bool = ...,
    dtype: Optional[Union[str, Mapping[str, Any]]] = ...,
    engine: Optional[Union[str, Literal["c", "python"]]] = ...,
    converters: Optional[Mapping[Union[int, str], Callable]] = ...,
    true_values: Optional[Sequence[Scalar]] = ...,
    false_values: Optional[Sequence[Scalar]] = ...,
    skipinitialspace: bool = ...,
    skiprows: Optional[Union[Sequence, int, Callable]] = ...,
    skipfooter: int = ...,
    nrows: Optional[int] = ...,
    na_values=...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: Union[bool, List[int], List[str]] = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Optional[Callable] = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: bool = ...,
    chunksize: int = ...,
    compression: Optional[Union[str, Literal["infer", "gzip", "bz2", "zip", "xz"]]] = ...,
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
    on_bad_lines: Literal["error", "warn", "skip"] = "error",
    delim_whitespace: bool = ...,
    low_memory: bool = ...,
    memory_map: bool = ...,
    float_precision: Optional[str] = ...,
    storage_options: Optional[Dict[str, Any]] = ...,
) -> DataFrame: ...
@overload
def read_table(
    reader: FilePathOrBuffer,
    *,
    sep: str = ...,
    delimiter: Optional[str] = ...,
    header: Union[int, Sequence[int], str, Literal["infer"]] = ...,
    names: Optional[Sequence[str]] = ...,
    index_col: Optional[Union[int, str, Sequence, bool, Literal[False]]] = ...,
    usecols: Optional[Union[int, str, Sequence]] = ...,
    squeeze: bool = ...,
    prefix: Optional[str] = ...,
    mangle_dupe_cols: bool = ...,
    dtype: Optional[Union[str, Mapping[str, Any]]] = ...,
    engine: Optional[Union[str, Literal["c", "python"]]] = ...,
    converters: Optional[Mapping[Union[int, str], Callable]] = ...,
    true_values: Optional[Sequence[Scalar]] = ...,
    false_values: Optional[Sequence[Scalar]] = ...,
    skipinitialspace: bool = ...,
    skiprows: Optional[Union[Sequence, int, Callable]] = ...,
    skipfooter: int = ...,
    nrows: Optional[int] = ...,
    na_values=...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: Union[bool, List[int], List[str]] = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Optional[Callable] = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: bool = ...,
    chunksize: Optional[int] = ...,
    compression: Optional[Union[str, Literal["infer", "gzip", "bz2", "zip", "xz"]]] = ...,
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
) -> TextFileReader: ...
@overload
def read_table(
    filepath: FilePathOrBuffer,
    *,
    sep: str = ...,
    delimiter: Optional[str] = ...,
    header: Optional[int | Sequence[int] | str | Literal["infer"]] = ...,
    names: Optional[Sequence[str]] = ...,
    index_col: Optional[Union[int, str, Sequence, bool, Literal[False]]] = ...,
    usecols: Optional[Union[int, str, Sequence]] = ...,
    squeeze: bool = ...,
    prefix: Optional[str] = ...,
    mangle_dupe_cols: bool = ...,
    dtype: Optional[Union[str, Mapping[str, Any]]] = ...,
    engine: Optional[Union[str, Literal["c", "python"]]] = ...,
    converters: Optional[Mapping[Union[int, str], Callable]] = ...,
    true_values: Optional[Sequence[Scalar]] = ...,
    false_values: Optional[Sequence[Scalar]] = ...,
    skipinitialspace: bool = ...,
    skiprows: Optional[Union[Sequence, int, Callable]] = ...,
    skipfooter: int = ...,
    nrows: Optional[int] = ...,
    na_values=...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: Union[bool, List[int], List[str]] = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Optional[Callable] = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: Literal[False],
    chunksize: int,
    compression: Optional[Union[str, Literal["infer", "gzip", "bz2", "zip", "xz"]]] = ...,
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
) -> TextFileReader: ...
@overload
def read_table(
    filepath: FilePathOrBuffer,
    *,
    sep: str = ...,
    delimiter: Optional[str] = ...,
    header: Optional[int | Sequence[int] | str | Literal["infer"]] = ...,
    names: Optional[Sequence[str]] = ...,
    index_col: Optional[Union[int, str, Sequence, bool, Literal[False]]] = ...,
    usecols: Optional[Union[int, str, Sequence]] = ...,
    squeeze: bool = ...,
    prefix: Optional[str] = ...,
    mangle_dupe_cols: bool = ...,
    dtype: Optional[Union[str, Mapping[str, Any]]] = ...,
    engine: Optional[Union[str, Literal["c", "python"]]] = ...,
    converters: Optional[Mapping[Union[int, str], Callable]] = ...,
    true_values: Optional[Sequence[Scalar]] = ...,
    false_values: Optional[Sequence[Scalar]] = ...,
    skipinitialspace: bool = ...,
    skiprows: Optional[Union[Sequence, int, Callable]] = ...,
    skipfooter: int = ...,
    nrows: Optional[int] = ...,
    na_values=...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: Union[bool, List[int], List[str]] = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Optional[Callable] = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: Literal[False] = ...,
    chunksize: None = ...,
    compression: Optional[Union[str, Literal["infer", "gzip", "bz2", "zip", "xz"]]] = ...,
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
    filepath: FilePathOrBuffer,
    *,
    sep: str = ...,
    delimiter: Optional[str] = ...,
    header: Union[int, Sequence[int], str, Literal["infer"]] = ...,
    names: Optional[Sequence[str]] = ...,
    index_col: Optional[Union[int, str, Sequence, bool, Literal[False]]] = ...,
    usecols: Optional[Union[int, str, Sequence]] = ...,
    squeeze: bool = ...,
    prefix: Optional[str] = ...,
    mangle_dupe_cols: bool = ...,
    dtype: Optional[Union[str, Mapping[str, Any]]] = ...,
    engine: Optional[Union[str, Literal["c", "python"]]] = ...,
    converters: Optional[Mapping[Union[int, str], Callable]] = ...,
    true_values: Optional[Sequence[Scalar]] = ...,
    false_values: Optional[Sequence[Scalar]] = ...,
    skipinitialspace: bool = ...,
    skiprows: Optional[Union[Sequence, int, Callable]] = ...,
    skipfooter: int = ...,
    nrows: Optional[int] = ...,
    na_values=...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: Union[bool, List[int], List[str]] = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Optional[Callable] = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: bool = ...,
    chunksize: int = ...,
    compression: Optional[Union[str, Literal["infer", "gzip", "bz2", "zip", "xz"]]] = ...,
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
) -> TextFileReader: ...
@overload
def read_table(
    filepath: FilePathOrBuffer,
    sep: str = ...,
    delimiter: Optional[str] = ...,
    header: Union[int, Sequence[int], str, Literal["infer"]] = ...,
    names: Optional[Sequence[str]] = ...,
    index_col: Optional[Union[int, str, Sequence, bool, Literal[False]]] = ...,
    usecols: Optional[Union[int, str, Sequence]] = ...,
    squeeze: bool = ...,
    prefix: Optional[str] = ...,
    mangle_dupe_cols: bool = ...,
    dtype: Optional[Union[str, Mapping[str, Any]]] = ...,
    engine: Optional[Union[str, Literal["c", "python"]]] = ...,
    converters: Optional[Mapping[Union[int, str], Callable]] = ...,
    true_values: Optional[Sequence[Scalar]] = ...,
    false_values: Optional[Sequence[Scalar]] = ...,
    skipinitialspace: bool = ...,
    skiprows: Optional[Union[Sequence, int, Callable]] = ...,
    skipfooter: int = ...,
    nrows: Optional[int] = ...,
    na_values=...,
    keep_default_na: bool = ...,
    na_filter: bool = ...,
    verbose: bool = ...,
    skip_blank_lines: bool = ...,
    parse_dates: Union[bool, List[int], List[str]] = ...,
    infer_datetime_format: bool = ...,
    keep_date_col: bool = ...,
    date_parser: Optional[Callable] = ...,
    dayfirst: bool = ...,
    cache_dates: bool = ...,
    iterator: bool = ...,
    chunksize: int = ...,
    compression: Optional[Union[str, Literal["infer", "gzip", "bz2", "zip", "xz"]]] = ...,
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
) -> TextFileReader: ...
def read_fwf(filepath_or_buffer: FilePathOrBuffer, colspecs=..., widths=..., infer_nrows=..., **kwds): ...

class TextFileReader(abc.Iterator):
    f = ...
    orig_options = ...
    engine = ...
    chunksize = ...
    nrows = ...
    squeeze = ...
    def __init__(self, f, engine=..., **kwds) -> None: ...
    def close(self) -> None: ...
    def __next__(self): ...
    def read(self, nrows=...): ...
    def get_chunk(self, size=...): ...

class ParserBase:
    names = ...
    orig_names = ...
    prefix = ...
    index_col = ...
    unnamed_cols = ...
    index_names = ...
    col_names = ...
    parse_dates = ...
    date_parser = ...
    dayfirst = ...
    keep_date_col = ...
    na_values = ...
    na_fvalues = ...
    na_filter = ...
    keep_default_na = ...
    true_values = ...
    false_values = ...
    mangle_dupe_cols = ...
    infer_datetime_format = ...
    cache_dates = ...
    header = ...
    handles = ...
    def __init__(self, kwds) -> None: ...
    def close(self) -> None: ...

class CParserWrapper(ParserBase):
    kwds = ...
    unnamed_cols = ...
    names = ...
    orig_names = ...
    index_names = ...
    def __init__(self, src, **kwds) -> None: ...
    def close(self) -> None: ...
    def set_error_bad_lines(self, status) -> None: ...
    def read(self, nrows=...): ...

def TextParser(*args, **kwds): ...
def count_empty_vals(vals): ...

class PythonParser(ParserBase):
    data = ...
    buf = ...
    pos: int = ...
    line_pos: int = ...
    encoding = ...
    compression = ...
    memory_map = ...
    skiprows = ...
    skipfunc = ...
    skipfooter = ...
    delimiter = ...
    quotechar = ...
    escapechar = ...
    doublequote = ...
    skipinitialspace = ...
    lineterminator = ...
    quoting = ...
    skip_blank_lines = ...
    warn_bad_lines = ...
    error_bad_lines = ...
    names_passed = ...
    has_index_names: bool = ...
    verbose = ...
    converters = ...
    dtype = ...
    thousands = ...
    decimal = ...
    comment = ...
    num_original_columns = ...
    columns = ...
    orig_names = ...
    index_names = ...
    nonnum = ...
    def __init__(self, f, **kwds): ...
    def read(self, rows=...): ...
    def get_chunk(self, size=...): ...

class FixedWidthReader(abc.Iterator):
    f = ...
    buffer = ...
    delimiter = ...
    comment = ...
    colspecs = ...
    def __init__(self, f, colspecs, delimiter, comment, skiprows=..., infer_nrows: int = ...) -> None: ...
    def get_rows(self, infer_nrows, skiprows=...): ...
    def detect_colspecs(self, infer_nrows: int = ..., skiprows=...): ...
    def __next__(self): ...

class FixedWidthFieldParser(PythonParser):
    colspecs = ...
    infer_nrows = ...
    def __init__(self, f, **kwds) -> None: ...
