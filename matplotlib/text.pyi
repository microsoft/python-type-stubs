from pathlib import Path
from typing import Any, Callable, Literal, Optional, Tuple, Union

from matplotlib.artist import Artist
from matplotlib.backend_bases import RendererBase
from matplotlib.colors import _ColorLike
from matplotlib.font_manager import FontProperties
from matplotlib.transforms import Bbox, Transform


class Text(Artist):
    def __init__(
        self,
        x: float = ...,
        y: float = ...,
        text: str = ...,
        color: Optional[_ColorLike] = ...,
        verticalalignment: Literal['center', 'top', 'bottom', 'baseline', 'center_baseline'] = ...,
        horizontalalignment: Literal['center', 'right', 'left'] = ...,
        multialignment: Literal['center', 'right', 'left'] = ...,
        fontproperties: Optional[Union[str, Path, FontProperties]] = ...,
        rotation: Optional[Union[float, Literal['vertical', 'horizontal']]] = ...,
        linespacing: Optional[float] = ...,
        rotation_mode: Optional[Literal['default', 'anchor']] = ...,
        usetex: Optional[bool] = ...,
        wrap: bool = ...,
        **kwargs: Any
    ) -> None: ...
    
    def __getattr__(self, name: str) -> Any: ...  # incomplete


class _AnnotationBase:
    def __getattr__(self, name: str) -> Any: ...  # incomplete


class Annotation(Text, _AnnotationBase):
    def __init__(
        self,
        text: str,
        xy: Tuple[float, float],
        xytext: Optional[str] = ...,
        xycoords: Union[str, Artist, Transform, Callable[[RendererBase], Union[Bbox, Transform]], Tuple[float, float]] = ...,
        **kwargs: Any
    ) -> None: ...

    def __getattr__(self, name: str) -> Any: ...  # incomplete

class OffsetFrom:
    def __getattr__(self, name: str) -> Any: ...  # incomplete


def get_rotation(rotation: Optional[Union[float, Literal['horizontal', 'vertical']]]) -> float: ...
