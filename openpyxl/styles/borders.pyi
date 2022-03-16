from openpyxl.styles.colors import Color
from typing import (
    Iterator,
    Optional,
    Tuple,
    Union,
)

BORDER_NONE = None
BORDER_DASHDOT = 'dashDot'
BORDER_DASHDOTDOT = 'dashDotDot'
BORDER_DASHED = 'dashed'
BORDER_DOTTED = 'dotted'
BORDER_DOUBLE = 'double'
BORDER_HAIR = 'hair'
BORDER_MEDIUM = 'medium'
BORDER_MEDIUMDASHDOT = 'mediumDashDot'
BORDER_MEDIUMDASHDOTDOT = 'mediumDashDotDot'
BORDER_MEDIUMDASHED = 'mediumDashed'
BORDER_SLANTDASHDOT = 'slantDashDot'
BORDER_THICK = 'thick'
BORDER_THIN = 'thin'

class Border:
    def __init__(
        self,
        left: Side = ...,
        right: Side = ...,
        top: Side = ...,
        bottom: Side = ...,
        diagonal: Side = ...,
        diagonal_direction: None = ...,
        vertical: None = ...,
        horizontal: None = ...,
        diagonalUp: Union[str, bool] = ...,
        diagonalDown: Union[str, bool] = ...,
        outline: bool = ...,
        start: None = ...,
        end: None = ...,
    ) -> None: ...
    def __iter__(self) -> Iterator[Tuple[str, str]]: ...

class Side:
    def __init__(
        self,
        style: Optional[str] = ...,
        color: Optional[Union[Color, str]] = ...,
        border_style: Optional[str] = ...,
    ) -> None: ...
