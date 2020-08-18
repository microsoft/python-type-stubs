from typing import Any, Optional, Sequence, Tuple, Union, IO, Literal, overload

from pygame.surface import Surface
from pygame.bufferproxy import BufferProxy

_BufferStyle = Union[BufferProxy, bytes, bytearray, memoryview]
_to_string_format = Literal["p", "RGB", "RGBX", "RGBA", "ARGB", "RGBA_PREMULT", "ARGB_PREMULT"]
_from_buffer_format = Literal["p", "RGB", "BRG", "RGBX", "RGBA", "ARGB"]
_from_string_format = Literal["p", "RGB", "RGBX", "RGBA", "ARGB"]
@overload
def load(filename: str, namehint: Optional[str] = "") -> Surface: ...
@overload
def load(filename: Any, namehint: Optional[str] = "") -> Surface: ...  # todo: Any is IO
@overload
def save(surface: Surface, filename: str) -> None: ...
@overload
def save(surface: Surface, filename: Any) -> None: ...  # todo: Any is IO
def get_extended() -> bool: ...
def tostring(surface: Surface, format: _to_string_format, flipped: Optional[bool] = False) -> str: ...
@overload
def fromstring(string: str, size: Sequence[int], format: _from_string_format, flipped: Optional[bool] = False) -> Surface: ...
@overload
def fromstring(string: str, size: Tuple[int, int], format: _from_string_format, flipped: Optional[bool] = False) -> Surface: ...
@overload
def frombuffer(bytes: _BufferStyle, size: Sequence[int], format: _from_buffer_format) -> Surface: ...
@overload
def frombuffer(bytes: _BufferStyle, size: Tuple[int, int], format: _from_buffer_format) -> Surface: ...

