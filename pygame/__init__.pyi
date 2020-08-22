from typing import Callable, Optional, Tuple, Type, Union

from . import (
    bufferproxy as bufferproxy,
    color as color,
    constants as constants,
    cursors as cursors,
    display as display,
    draw as draw,
    event as event,
    fastevent as fastevent,
    font as font,
    image as image,
    joystick as joystick,
    key as key,
    mask as mask,
    math as math,
    mixer as mixer,
    mouse as mouse,
    pixelarray as pixelarray,
    pixelcopy as pixelcopy,
    rect as rect,
    scrap as scrap,
    sndarray as sndarray,
    sprite as sprite,
    surface as surface,
    surfarray as surfarray,
    time as time,
    transform as transform,
    version as version,
)

# This classes are auto imported with pygame, so I put their declaration here
class Rect(rect.Rect): ...
class Surface(surface.Surface): ...
class Color(color.Color): ...
class PixelArray(pixelarray.PixelArray): ...
class Vector2(math.Vector2): ...
class Vector3(math.Vector3): ...

def init() -> Tuple[int, int]: ...
def quit() -> None: ...
def get_init() -> bool: ...

class error(RuntimeError): ...

def get_error() -> str: ...
def set_error(error_msg: str) -> None: ...
def get_sdl_version() -> Tuple[int, int, int]: ...
def get_sdl_byteorder() -> int: ...
def encode_string(
    obj: Union[str, bytes], encoding: Optional[str] = ..., errors: Optional[str] = ..., etype: Optional[Type[Exception]] = ...,
) -> bytes: ...
def encode_file_path(obj: Union[str, bytes, object], etype: Optional[Type[Exception]] = ...) -> bytes: ...
def register_quit(callable: Callable[[], None]) -> None: ...

# def __getattr__(name) -> Any: ...  # don't error on missing stubs
