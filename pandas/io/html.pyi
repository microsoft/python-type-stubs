from pandas._typing import FilePathOrBuffer as FilePathOrBuffer
from pandas.compat._optional import import_optional_dependency as import_optional_dependency
from pandas.core.construction import create_series_with_explicit_dtype as create_series_with_explicit_dtype
from pandas.core.dtypes.common import is_list_like as is_list_like
from pandas.core.frame import DataFrame as DataFrame
from pandas.errors import AbstractMethodError as AbstractMethodError, EmptyDataError as EmptyDataError
from pandas.io.common import is_url as is_url, urlopen as urlopen, validate_header_arg as validate_header_arg
from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.io.parsers import TextParser as TextParser
from typing import Any, Callable, Iterable, List, Mapping, Optional, Sequence, Union

class _HtmlFrameParser:
    io: Any = ...
    match: Any = ...
    attrs: Any = ...
    encoding: Any = ...
    displayed_only: Any = ...
    def __init__(self, io: Any, match: Any, attrs: Any, encoding: Any, displayed_only: Any) -> None: ...
    def parse_tables(self) -> Any: ...

class _BeautifulSoupHtml5LibFrameParser(_HtmlFrameParser):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class _LxmlFrameParser(_HtmlFrameParser):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

def read_html(
    io: FilePathOrBuffer,
    match: str = ...,
    flavor: Optional[str] = ...,
    header: Optional[Union[int, Sequence[int]]] = ...,
    index_col: Optional[Union[int, Sequence[Any]]] = ...,
    skiprows: Optional[Union[int, Sequence[Any], slice]] = ...,
    attrs: Optional[Mapping[str, str]] = ...,
    parse_dates: bool = ...,
    thousands: str = ...,
    encoding: Optional[str] = ...,
    decimal: str = ...,
    converters: Optional[Mapping[Union[int, str], Callable]] = ...,
    na_values: Optional[Iterable[Any]] = ...,
    keep_default_na: bool = ...,
    displayed_only: bool = ...,
) -> List[DataFrame]: ...
