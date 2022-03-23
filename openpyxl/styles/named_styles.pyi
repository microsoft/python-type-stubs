from openpyxl.styles.alignment import Alignment
from openpyxl.styles.borders import Border
from openpyxl.styles.cell_style import (
    CellStyle,
    StyleArray,
)
from openpyxl.styles.fills import PatternFill
from openpyxl.styles.fonts import Font
from openpyxl.styles.protection import Protection
from openpyxl.workbook.workbook import Workbook
from typing import (
    Any,
    Iterator,
    List,
    Optional,
    Tuple,
    Union,
)

class NamedStyle:
    def __init__(
        self,
        name: str = ...,
        font: Font = ...,
        fill: PatternFill = ...,
        border: Border = ...,
        alignment: Alignment = ...,
        number_format: Optional[str] = ...,
        protection: Protection = ...,
        builtinId: Optional[Union[str, int]] = ...,
        hidden: Optional[Union[str, bool]] = ...,
        xfId: Optional[Union[str, int]] = ...,
    ) -> None: ...
    def __iter__(self) -> Iterator[Tuple[str, str]]: ...
    def __setattr__(self, attr: str, value: Any) -> None: ...
    def _recalculate(self) -> None: ...
    def _set_index(self, idx: int) -> None: ...
    def as_name(self) -> _NamedCellStyle: ...
    def as_tuple(self) -> StyleArray: ...
    def as_xf(self) -> CellStyle: ...
    def bind(self, wb: Workbook) -> None: ...
    @property
    def xfId(self) -> int: ...

class NamedStyleList:
    def __getitem__(self, key: Union[str, int]) -> NamedStyle: ...
    def append(self, style: Union[NamedStyle, int]) -> None: ...
    @property
    def names(self) -> List[str]: ...

class _NamedCellStyle:
    def __init__(
        self,
        name: Optional[str] = ...,
        xfId: Optional[Union[str, int]] = ...,
        builtinId: Optional[Union[str, int]] = ...,
        iLevel: None = ...,
        hidden: Optional[Union[str, bool]] = ...,
        customBuiltin: Optional[str] = ...,
        extLst: None = ...,
    ) -> None: ...

class _NamedCellStyleList:
    def __init__(
        self,
        count: Optional[str] = ...,
        cellStyle: Union[List[_NamedCellStyle], Tuple] = ...,
    ) -> None: ...
    @property
    def count(self) -> int: ...
    @property
    def names(self) -> NamedStyleList: ...
