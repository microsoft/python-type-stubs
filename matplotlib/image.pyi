# COMPLETE

from pathlib import Path
from typing import Any, BinaryIO, Collection, Dict, Literal, Optional, Tuple, Union

from PIL.Image import Image as PILImage

from matplotlib._typing import ArrayLike, ndarray
from matplotlib.artist import Artist
from matplotlib.axes._axes import Axes
from matplotlib.backend_bases import LocationEvent, MouseEvent, RendererBase
from matplotlib.cm import Colormap, ScalarMappable
from matplotlib.colors import Normalize
from matplotlib.figure import Figure
from matplotlib.transforms import Affine2D, Bbox

_PathOrIO = Union[str, Path, BinaryIO]

class _ImageBase(Artist, ScalarMappable):
    def __init__(
        self,
        ax: Axes,
        cmap: Optional[Union[str, Colormap]] = ...,
        norm: Optional[Normalize] = ...,
        interpolation: Optional[str] = ...,
        origin: Optional[Literal['upper', 'lower']] = ...,
        filternorm: bool = ...,
        filterrad: float = ...,
        resample: bool = ...,
        **kwargs: Any
    ) -> None: ...

    def get_size(self) -> Tuple[int, int]: ...
    def set_alpha(self, alpha: float) -> None: ...
    def changed(self) -> None: ...
    def make_image(self, renderer: RendererBase, magnification: float = ..., unsampled: bool = ...) -> Tuple[ndarray, Tuple[float, float], Affine2D]: ...
    def draw(self, renderer: RendererBase, *args: Any, **kwargs: Any) -> None: ...
    def contains(self, mouseevent: MouseEvent) -> Tuple[bool, Dict[Any, Any]]: ...
    def write_png(self, fname: _PathOrIO) -> None: ...
    def set_data(self, A: Union[ArrayLike, PILImage]) -> None: ...
    def set_array(self, A: ArrayLike) -> None: ...
    def get_interpolation(self) -> str: ...
    def set_interpolation(self, s: str) -> None: ...
    def can_composite(self) -> bool: ...
    def set_resample(self, v: Optional[bool]) -> None: ...
    def get_resample(self) -> bool: ...
    def set_filternorm(self, filternorm: bool) -> None: ...
    def get_filternorm(self) -> bool: ...
    def set_filterrad(self, filterrad: float) -> None: ...
    def get_filterrad(self) -> float: ...


class AxesImage(_ImageBase):
    def __init__(
        self,
        ax: Axes,
        cmap: Optional[Union[str, Colormap]] = ...,
        norm: Optional[Normalize] = ...,
        interpolation: Optional[str] = ...,
        origin: Optional[Literal['upper', 'lower']] = ...,
        extent: Optional[Tuple[float, float, float, float]] = ...,
        filternorm: bool = ...,
        filterrad: float = ...,
        resample: bool = ...,
        **kwargs: Any
    ) -> None: ...

    def format_cursor_data(self, data: ArrayLike) -> str: ...
    def get_cursor_data(self, event: LocationEvent) -> Optional[ndarray]: ...

    def set_extent(self, extent: Tuple[float, float, float, float]) -> None: ...
    def get_extent(self) -> Tuple[float, float, float, float]: ...
    def get_window_extent(self, renderer: Optional[RendererBase] = ...) -> Tuple[float, float, float, float]: ...

class NonUniformImage(AxesImage):
    def __init__(self, ax: Axes, *, interpolation: str = ..., **kwargs: Any) -> None: ...

    @property
    def is_grayscale(self) -> bool: ...

    def set_cmap(self, cmap: Optional[Union[str, Colormap]]) -> None: ...
    def set_data(self, x: ArrayLike, y: ArrayLike, A: ArrayLike) -> None: ...
    def set_norm(self, norm: Optional[Normalize]) -> None: ...

class PcolorImage(AxesImage):
    def __init__(
        self,
        ax: Axes,
        x: Optional[ArrayLike] = ...,
        y: Optional[ArrayLike] = ...,
        A: Optional[ArrayLike] = ...,
        cmap: Optional[Union[str, Colormap]] = ...,
        norm: Optional[Normalize] = ...,
        **kwargs: Any
    ) -> None: ...

    @property
    def is_grayscale(self) -> bool: ...

    def set_data(self, x: ArrayLike, y: ArrayLike, A: ArrayLike) -> None: ...

class BboxImage(_ImageBase):
    def __init__(
        self, 
        bbox: Bbox,
        cmap: Optional[Union[str, Colormap]] = ...,
        norm: Optional[Normalize] = ...,
        interpolation: Optional[str] = ...,
        origin: Optional[Literal['upper', 'lower']] = ...,
        filternorm: bool = ...,
        filterrad: float = ...,
        resample: bool = ...,
        **kwargs: Any
    ) -> None: ...

    def get_window_extent(self, renderer: Optional[RendererBase] = ...) -> Tuple[float, float, float, float]: ...

class FigureImage(_ImageBase):
    def __init__(
        self, 
        fig: Figure,
        cmap: Optional[Union[str, Colormap]] = ...,
        norm: Optional[Normalize] = ...,
        interpolation: Optional[str] = ...,
        origin: Optional[Literal['upper', 'lower']] = ...,
        filternorm: bool = ...,
        filterrad: float = ...,
        resample: bool = ...,
        **kwargs: Any
    ) -> None: ...

    def get_extent(self) -> Tuple[float, float, float, float]: ...


def composite_images(images: Collection[_ImageBase], renderer: RendererBase, magnification: float = ...) -> Tuple[ndarray, float, float]: ...

def imread(fname: _PathOrIO, format: Optional[str] = ...) -> ndarray: ...

def imsave(
    fname: _PathOrIO,
    arr: ArrayLike,
    vmin: Optional[float] = ...,
    vmax: Optional[float] = ...,
    cmap: Optional[Union[str, Colormap]] = ...,
    format: Optional[str] = ...,
    origin: Optional[Literal['upper', 'lower']] = ...,
    dpi: float = ...,
    *,
    metadata: Optional[Dict[Any, Any]] = ...,
    pil_kwargs: Optional[Dict[str, Any]] = ...
) -> None: ...

def pil_to_array(pilImage: PILImage) -> ndarray: ...

def thumbnail(infile: _PathOrIO, thumbfile: _PathOrIO, scale: float = ..., interpolation: str = ..., preview: bool = ...) -> Figure: ...
