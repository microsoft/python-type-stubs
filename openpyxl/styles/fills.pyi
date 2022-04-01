from lxml.etree import _Element
from openpyxl.styles.colors import ColorDescriptor, Color
from typing import (
    Iterator,
    List,
    Optional,
    Tuple,
    Union,
)
from openpyxl.descriptors import (
    Float,
    Set,
    Alias,
    NoneSet,
    Sequence,
    Integer,
    MinMax,
)

FILL_NONE = "none"
FILL_SOLID = "solid"
FILL_PATTERN_DARKDOWN = "darkDown"
FILL_PATTERN_DARKGRAY = "darkGray"
FILL_PATTERN_DARKGRID = "darkGrid"
FILL_PATTERN_DARKHORIZONTAL = "darkHorizontal"
FILL_PATTERN_DARKTRELLIS = "darkTrellis"
FILL_PATTERN_DARKUP = "darkUp"
FILL_PATTERN_DARKVERTICAL = "darkVertical"
FILL_PATTERN_GRAY0625 = "gray0625"
FILL_PATTERN_GRAY125 = "gray125"
FILL_PATTERN_LIGHTDOWN = "lightDown"
FILL_PATTERN_LIGHTGRAY = "lightGray"
FILL_PATTERN_LIGHTGRID = "lightGrid"
FILL_PATTERN_LIGHTHORIZONTAL = "lightHorizontal"
FILL_PATTERN_LIGHTTRELLIS = "lightTrellis"
FILL_PATTERN_LIGHTUP = "lightUp"
FILL_PATTERN_LIGHTVERTICAL = "lightVertical"
FILL_PATTERN_MEDIUMGRAY = "mediumGray"

fills = (
    FILL_SOLID,
    FILL_PATTERN_DARKDOWN,
    FILL_PATTERN_DARKGRAY,
    FILL_PATTERN_DARKGRID,
    FILL_PATTERN_DARKHORIZONTAL,
    FILL_PATTERN_DARKTRELLIS,
    FILL_PATTERN_DARKUP,
    FILL_PATTERN_DARKVERTICAL,
    FILL_PATTERN_GRAY0625,
    FILL_PATTERN_GRAY125,
    FILL_PATTERN_LIGHTDOWN,
    FILL_PATTERN_LIGHTGRAY,
    FILL_PATTERN_LIGHTGRID,
    FILL_PATTERN_LIGHTHORIZONTAL,
    FILL_PATTERN_LIGHTTRELLIS,
    FILL_PATTERN_LIGHTUP,
    FILL_PATTERN_LIGHTVERTICAL,
    FILL_PATTERN_MEDIUMGRAY,
)

def _assign_position(
    values: Union[List[Color], List[Stop], Tuple, List[Union[Stop, str]], List[str]]
) -> List[Stop]: ...

class Fill:
    @classmethod
    def from_tree(cls, el: _Element) -> Optional[Union[GradientFill, PatternFill]]: ...

class GradientFill:
    def __init__(
        self,
        type: str = ...,
        degree: Union[str, int] = ...,
        left: Union[str, int] = ...,
        right: Union[str, int] = ...,
        top: Union[str, int] = ...,
        bottom: Union[str, int] = ...,
        stop: Union[List[Stop], Tuple] = ...,
    ) -> None: ...
    def __iter__(self) -> Iterator[Tuple[str, str]]: ...
    def to_tree(
        self, tagname: None = ..., namespace: None = ..., idx: None = ...
    ) -> _Element: ...

class PatternFill:
    tagname = "patternFill"

    __elements__ = ("fgColor", "bgColor")

    patternType = NoneSet(values=fills)
    fill_type = Alias("patternType")
    fgColor = ColorDescriptor()
    start_color = Alias("fgColor")
    bgColor = ColorDescriptor()
    end_color = Alias("bgColor")
    def __init__(
        self,
        patternType: Optional[str] = ...,
        fgColor: Union[str, Color] = ...,
        bgColor: Union[str, Color] = ...,
        fill_type: Optional[str] = ...,
        start_color: Optional[Union[str, Color]] = ...,
        end_color: Optional[Union[str, Color]] = ...,
    ) -> None:
        if fill_type is not None:
            patternType = fill_type
        self.patternType = patternType
        if start_color is not None:
            fgColor = start_color
        self.fgColor = fgColor
        if end_color is not None:
            bgColor = end_color
        self.bgColor = bgColor
    @classmethod
    def _from_tree(cls, el: _Element) -> PatternFill: ...
    def to_tree(self, tagname: Optional[str] = ..., idx: None = ...) -> _Element: ...

class Stop:
    def __init__(
        self, color: Union[str, Color], position: Optional[Union[float, str, int]]
    ) -> None: ...

class StopList:
    def __set__(self, obj: GradientFill, values: Union[List[Stop], Tuple]) -> None: ...
