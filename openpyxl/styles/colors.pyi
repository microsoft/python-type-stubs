from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.drawing.colors import SystemColor
from typing import (
    Iterator,
    List,
    Optional,
    Tuple,
    Union,
)
import re

# Default Color Index as per 18.8.27 of ECMA Part 4
COLOR_INDEX = (
    "00000000",
    "00FFFFFF",
    "00FF0000",
    "0000FF00",
    "000000FF",  # 0-4
    "00FFFF00",
    "00FF00FF",
    "0000FFFF",
    "00000000",
    "00FFFFFF",  # 5-9
    "00FF0000",
    "0000FF00",
    "000000FF",
    "00FFFF00",
    "00FF00FF",  # 10-14
    "0000FFFF",
    "00800000",
    "00008000",
    "00000080",
    "00808000",  # 15-19
    "00800080",
    "00008080",
    "00C0C0C0",
    "00808080",
    "009999FF",  # 20-24
    "00993366",
    "00FFFFCC",
    "00CCFFFF",
    "00660066",
    "00FF8080",  # 25-29
    "000066CC",
    "00CCCCFF",
    "00000080",
    "00FF00FF",
    "00FFFF00",  # 30-34
    "0000FFFF",
    "00800080",
    "00800000",
    "00008080",
    "000000FF",  # 35-39
    "0000CCFF",
    "00CCFFFF",
    "00CCFFCC",
    "00FFFF99",
    "0099CCFF",  # 40-44
    "00FF99CC",
    "00CC99FF",
    "00FFCC99",
    "003366FF",
    "0033CCCC",  # 45-49
    "0099CC00",
    "00FFCC00",
    "00FF9900",
    "00FF6600",
    "00666699",  # 50-54
    "00969696",
    "00003366",
    "00339966",
    "00003300",
    "00333300",  # 55-59
    "00993300",
    "00993366",
    "00333399",
    "00333333",  # 60-63
)

BLACK = COLOR_INDEX[0]
WHITE = COLOR_INDEX[1]
BLUE = COLOR_INDEX[4]

aRGB_REGEX = re.compile("^([A-Fa-f0-9]{8}|[A-Fa-f0-9]{6})$")

class Color:
    def __add__(self, other: Union[Color, int]) -> Color: ...
    def __init__(
        self,
        rgb: str = ...,
        indexed: Union[None, str, int] = ...,
        auto: Union[None, str, bool, int] = ...,
        theme: Union[None, str, int] = ...,
        tint: Union[float, str] = ...,
        index: None = ...,
        type: str = ...,
    ) -> None: ...
    def __iter__(self) -> Iterator[Tuple[str, str]]: ...
    @property
    def index(self) -> int: ...

class ColorDescriptor:
    def __set__(
        self, instance: Serialisable, value: Union[None, str, Color]
    ) -> None: ...

class ColorList:
    def __bool__(self) -> bool: ...
    def __init__(
        self,
        indexedColors: Union[
            Tuple[str, str],
            List[str],
            Tuple,
            List[RgbColor],
            Tuple[
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
            ],
        ] = ...,
        mruColors: Union[List[Color], Tuple] = ...,
    ) -> None: ...
    @property
    def index(self) -> List[str]: ...

class RGB:
    def __set__(
        self,
        instance: Union[Color, SystemColor, RgbColor],
        value: Optional[Union[str, int]],
    ) -> None: ...

class RgbColor:
    def __init__(self, rgb: Optional[str] = ...) -> None: ...
