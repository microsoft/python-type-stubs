import datetime
import re
from openpyxl.styles.cell_style import StyleArray
from openpyxl.worksheet._write_only import WriteOnlyWorksheet
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.styles import numbers
from openpyxl.styles.styleable import StyleableObject
from typing import Any, Optional, Union, Callable, Tuple, Dict
from openpyxl.compat import NUMERIC_TYPES

TIME_TYPES = (datetime.datetime, datetime.date, datetime.time, datetime.timedelta)
TIME_FORMATS = {
    datetime.datetime: numbers.FORMAT_DATE_DATETIME,
    datetime.date: numbers.FORMAT_DATE_YYYYMMDD2,
    datetime.time: numbers.FORMAT_DATE_TIME6,
    datetime.timedelta: numbers.FORMAT_DATE_TIMEDELTA,
}

STRING_TYPES = (str, bytes)
KNOWN_TYPES = NUMERIC_TYPES + TIME_TYPES + STRING_TYPES + (bool, type(None))

ILLEGAL_CHARACTERS_RE = re.compile(r"[\000-\010]|[\013-\014]|[\016-\037]")
ERROR_CODES = ("#NULL!", "#DIV/0!", "#VALUE!", "#REF!", "#NAME?", "#NUM!", "#N/A")

ERROR_CODES = ERROR_CODES

TYPE_STRING: str = "s"
TYPE_FORMULA: str = "f"
TYPE_NUMERIC: str = "n"
TYPE_BOOL: str = "b"
TYPE_NULL: str = "n"
TYPE_INLINE: str = "inlineStr"
TYPE_ERROR: str = "e"
TYPE_FORMULA_CACHE_STRING: str = "str"

VALID_TYPES: Tuple[str, ...] = (
    TYPE_STRING,
    TYPE_FORMULA,
    TYPE_NUMERIC,
    TYPE_BOOL,
    TYPE_NULL,
    TYPE_INLINE,
    TYPE_ERROR,
    TYPE_FORMULA_CACHE_STRING,
)

_TYPES: Dict[Callable, str] = {int: "n", float: "n", str: "s", bool: "b"}

def WriteOnlyCell(
    ws: Optional[WriteOnlyWorksheet] = ..., value: Optional[Union[str, int]] = ...
) -> Cell:
    return Cell(worksheet=ws, column=1, row=1, value=value)

def get_time_format(t: Any) -> Optional[str]: ...
def get_type(t: Any, value: Any) -> Optional[str]: ...

class Cell(StyleableObject):
    def __init__(
        self,
        worksheet: Optional[Union[Worksheet, WriteOnlyWorksheet]],
        row: Optional[Union[str, int]] = ...,
        column: Optional[int] = ...,
        value: Optional[Union[datetime.date, str, int]] = ...,
        style_array: Optional[StyleArray] = ...,
    ) -> None:
        super(Cell, self).__init__(worksheet, style_array)
        self.row = row
        """Row number of this cell (1-based)"""
        self.column = column
        """Column number of this cell (1-based)"""
        # _value is the stored value, while value is the displayed value
        self._value = None
        self._hyperlink = None
        self.data_type = "n"
        if value is not None:
            self.value = value
        self._comment = None
    def __repr__(self) -> str: ...
    def _bind_value(self, value: Any) -> None: ...
    def check_string(self, value: Union[str, bytes]) -> str: ...
    @property
    def col_idx(self) -> int: ...
    @property
    def column_letter(self) -> str: ...
    @property
    def coordinate(self) -> str: ...
    @property
    def encoding(self) -> str: ...
    @property
    def is_date(self) -> bool: ...
    def offset(self, row: int = ..., column: int = ...) -> Cell: ...

class MergedCell(StyleableObject):
    __slots__ = ("row", "column")

    _value = None
    data_type = "n"
    comment = None
    hyperlink = None
    def __init__(
        self,
        worksheet: Worksheet,
        row: Optional[int] = ...,
        column: Optional[int] = ...,
    ) -> None:
        super(MergedCell, self).__init__(worksheet)
        self.row = row
        self.column = column
    def __repr__(self) -> str: ...
    coordinate = Cell.coordinate
    _comment = comment
    value = _value
