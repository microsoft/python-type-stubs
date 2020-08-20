from typing import Tuple, Callable, Optional, Union, overload, Type

# Most useful stuff
from . import constants as constants
from . import surface as surface
from . import rect as rect
from . import color as color
from . import event as event
from . import bufferproxy as bufferproxy
from . import draw as draw
from . import display as display
from . import font as font
from . import image as image
from . import key as key
from . import mixer as mixer
from . import mouse as mouse
from . import time as time
from . import version as version

# Advanced stuff
from . import cursors as cursors
from . import joystick as joystick
from . import mask as mask
from . import sprite as sprite
from . import transform as transform
from . import pixelarray as pixelarray
from . import pixelcopy as pixelcopy
from . import sndarray as sndarray
from . import surfarray as surfarray
from . import math as math
from . import fastevent as fastevent

# Other
from . import scrap as scrap

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
@overload
def encode_file_path(obj: Union[str, bytes], etype: Optional[Type[Exception]] = ...) -> bytes: ...
def encode_file_path(obj: object, etype: Optional[Type[Exception]] = ...) -> bytes: ...
def register_quit(callable: Callable[[], None]) -> None: ...

# def __getattr__(name) -> Any: ...  # don't error on missing stubs
