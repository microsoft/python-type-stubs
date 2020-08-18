from typing import Tuple, Optional, Union, Text, IO, Sequence, Any, overload

from pygame.surface import Surface
from pygame.color import Color
from pygame.rect import Rect

_ColorValue = Union[Color, Tuple[int, int, int], Sequence[int], int]

def get_error() -> str: ...
def get_version() -> Tuple[int, int, int]: ...
def init(cache_size: Optional[int] = 64, resolution: Optional[int] = 72) -> None: ...
def quit() -> None: ...
def get_init() -> bool: ...
def was_init() -> bool: ...
def get_cache_size() -> int: ...
def get_default_resolution() -> int: ...
def set_default_resolution(resolution: int) -> None: ...
@overload
def SysFont(
    name: str, size: int, bold: Optional[int] = False, italic: Optional[int] = False
) -> Font: ...  # todo: optionional int false?
@overload
def SysFont(
    name: Sequence[str], size: int, bold: Optional[int] = False, italic: Optional[int] = False
) -> Font: ...  # todo: optionional int false?
def get_default_font() -> str: ...

STYLE_NORMAL: int
STYLE_UNDERLINE: int
STYLE_OBLIQUE: int
STYLE_STRONG: int
STYLE_WIDE: int
STYLE_DEFAULT: int

class Font:
    name: str
    path: Text
    size: Union[float, Tuple[float, float]]
    height: int
    ascender: int
    descender: int
    style: int
    underline: bool
    strong: bool
    oblique: bool
    wide: bool
    strength: float
    underline_adjustment: float
    fixed_width: bool
    fixed_sizes: int
    scalable: bool
    use_bitmap_strikes: bool
    antialiased: bool
    kerning: bool
    vertical: bool
    rotation: int
    fgcolor: Color
    bgcolor: Color
    origin: bool
    pad: bool
    ucs4: bool
    resolution: int
    @overload
    def __init__(
        self,
        file: str,
        size: Optional[float] = 0,
        font_index: Optional[int] = 0,
        resolution: Optional[int] = 0,
        ucs4: Optional[int] = False,  # todo: optionional int false?
    ) -> None: ...
    @overload
    def __init__(
        self,
        file: IO,  # what should this be?
        size: Optional[float] = 0,
        font_index: Optional[int] = 0,
        resolution: Optional[int] = 0,
        ucs4: Optional[int] = False,
    ) -> None: ...
    def get_rect(
        self, text: str, style: Optional[int] = STYLE_DEFAULT, rotation: Optional[int] = 0, size: Optional[float] = 0,
    ) -> Rect: ...
    def get_metrics(self, text: str, size: Optional[float] = 0) -> Sequence[Tuple[int, int, int, int, float, float]]: ...
    def get_sized_ascender(self, size: float) -> int: ...
    def get_sized_descender(self, size: float) -> int: ...
    def get_sized_height(self, size: float) -> int: ...
    def get_sized_glyph_height(self, size: float) -> int: ...
    def get_sizes(self) -> Sequence[Tuple[int, int, int, float, float]]: ...
    def render(
        self,
        text: str,
        fgcolor: Optional[_ColorValue] = None,
        bgcolor: Optional[_ColorValue] = None,
        style: Optional[int] = STYLE_DEFAULT,
        rotation: Optional[int] = 0,
        size: Optional[float] = 0,
    ) -> Tuple[Surface, Rect]: ...
    def render_to(
        self,
        surf: Surface,
        dest: Tuple[int, int],
        text: str,
        fgcolor: Optional[_ColorValue] = None,
        bgcolor: Optional[_ColorValue] = None,
        style: Optional[int] = STYLE_DEFAULT,
        rotation: Optional[int] = 0,
        size: Optional[float] = 0,
    ) -> Rect: ...
    def render_to(
        self,
        surf: Surface,
        dest: Sequence[int],
        text: str,
        fgcolor: Optional[_ColorValue] = None,
        bgcolor: Optional[_ColorValue] = None,
        style: Optional[int] = STYLE_DEFAULT,
        rotation: Optional[int] = 0,
        size: Optional[float] = 0,
    ) -> Rect: ...
    def render_to(
        self,
        surf: Surface,
        dest: Rect,
        text: str,
        fgcolor: Optional[_ColorValue] = None,
        bgcolor: Optional[_ColorValue] = None,
        style: Optional[int] = STYLE_DEFAULT,
        rotation: Optional[int] = 0,
        size: Optional[float] = 0,
    ) -> Rect: ...
    def render_raw(
        self,
        text: str,
        style: Optional[int] = STYLE_DEFAULT,
        rotation: Optional[int] = 0,
        size: Optional[float] = 0,
        invert: Optional[bool] = False,
    ) -> Tuple[bytes, Tuple[int, int]]: ...
    @overload
    def render_raw_to(
        self,
        array: Any,  # Sequence[int] ?
        text: str,
        dest: Optional[Tuple[int, int]] = None,
        style: Optional[int] = STYLE_DEFAULT,
        rotation: Optional[int] = 0,
        size: Optional[float] = 0,
        invert: Optional[bool] = False,
    ) -> Rect: ...
    @overload
    def render_raw_to(
        self,
        array: Any,  # Sequence[int] ?
        text: str,
        dest: Optional[Sequence[int]] = None,
        style: Optional[int] = STYLE_DEFAULT,
        rotation: Optional[int] = 0,
        size: Optional[float] = 0,
        invert: Optional[bool] = False,
    ) -> Rect: ...

