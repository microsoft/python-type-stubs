from typing import Tuple, Callable, Optional, overload, Type

# Most useful stuff
from .constants import *
import .surface
import .rect
import .color
import .event
import .bufferproxy
import .draw
import .display
import .font
import .image
import .key
import .mixer
import .mouse
import .time
import .version

# Advanced stuff
import .cursors
import .joystick
import .mask
import .sprite
import .transform
import .pixelarray
import .pixelcopy
import .sndarray
import .surfarray
import .math
import .fastevent

# Other
import pygame.scrap

# This classes are auto imported with pygame, so I put their declaration here
class Rect(pygame.rect.Rect): ...
class Surface(pygame.surface.Surface): ...
class Color(pygame.color.Color): ...
class PixelArray(pygame.pixelarray.PixelArray): ...
class Vector2(pygame.math.Vector2): ...
class Vector3(pygame.math.Vector3): ...

def init() -> Tuple[int, int]: ...
def quit() -> None: ...
def get_init() -> bool: ...

class error(RuntimeError): ...

def get_error() -> str: ...
def set_error(error_msg: str) -> None: ...
def get_sdl_version() -> Tuple[int, int, int]: ...
def get_sdl_byteorder() -> int: ...
@overload
def encode_string(
    obj: str,
    encoding: Optional[str] = "unicode_escape",
    errors: Optional[str] = "backslashreplace",
    etype: Optional[Type[Exception]] = UnicodeEncodeError,
) -> bytes: ...
@overload
def encode_string(
    obj: bytes,
    encoding: Optional[str] = "unicode_escape",
    errors: Optional[str] = "backslashreplace",
    etype: Optional[Type[Exception]] = UnicodeEncodeError,
) -> bytes: ...
@overload
def encode_file_path(obj: str, etype: Optional[Type[Exception]] = UnicodeEncodeError) -> bytes: ...
@overload
def encode_file_path(obj: bytes, etype: Optional[Type[Exception]] = UnicodeEncodeError) -> bytes: ...
@overload
def encode_file_path(obj: object, etype: Optional[Type[Exception]] = UnicodeEncodeError) -> bytes: ...
def register_quit(callable: Callable[[], None]) -> None: ...

# def __getattr__(name) -> Any: ...  # don't error on missing stubs
