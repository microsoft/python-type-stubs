from openpyxl.styles.borders import Border
from openpyxl.styles.fills import PatternFill
from openpyxl.styles.fonts import Font
from typing import (
    Optional,
    Tuple,
)

class DifferentialStyle:
    def __init__(
        self,
        font: Optional[Font] = ...,
        numFmt: None = ...,
        fill: Optional[PatternFill] = ...,
        alignment: None = ...,
        border: Optional[Border] = ...,
        protection: None = ...,
        extLst: None = ...,
    ) -> None: ...

class DifferentialStyleList:
    def __getitem__(self, idx: int) -> DifferentialStyle: ...
    def __init__(self, dxf: Tuple = ...) -> None: ...
    def add(self, dxf: DifferentialStyle) -> int: ...
    def append(self, dxf: DifferentialStyle) -> None: ...
