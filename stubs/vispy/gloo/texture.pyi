import numpy as np
from numpy import ndarray
from numpy.typing import NDArray

from .globject import GLObject

F64_PRECISION_WARNING: str = ...

def should_cast_to_f32(data_dtype): ...

class BaseTexture(GLObject):
    _ndim: int = ...

    _formats: dict = ...

    _inv_formats: dict = ...

    # NOTE: non-normalized formats ending with 'i' and 'ui' are currently
    #   disabled as they don't work with the current VisPy implementation.
    #   Attempting to use them along with the additional enums defined in
    #   vispy/gloo/glir.py produces an invalid operation from OpenGL.
    _inv_internalformats = ...

    def __init__(
        self,
        data: ndarray | tuple | None = None,
        format=None,
        resizable: bool = True,
        interpolation: str | None = None,
        wrapping: str | None = None,
        shape: tuple | None = None,
        internalformat: str | None = None,
        resizeable=None,
    ): ...
    def _normalize_shape(self, data_or_shape): ...
    @property
    def shape(self): ...
    @property
    def format(self): ...
    @property
    def internalformat(self): ...
    @property
    def wrapping(self): ...
    @wrapping.setter
    def wrapping(self, value): ...
    @property
    def interpolation(self): ...
    @interpolation.setter
    def interpolation(self, value): ...
    def resize(self, shape: tuple[int, ...], format=None, internalformat=None): ...
    def _check_format_change(self, format, num_channels): ...
    def _check_internalformat_change(self, internalformat, num_channels): ...
    def _resize(self, shape, format=None, internalformat=None): ...
    def set_data(
        self,
        data: NDArray,
        offset: tuple[int, ...] | int | None = None,
        copy: bool = False,
    ): ...
    def _set_data(self, data, offset=None, copy=False): ...
    def __setitem__(self, key, data): ...
    def __repr__(self): ...

# --------------------------------------------------------- Texture1D class ---
class Texture1D(BaseTexture):
    _ndim: int = ...
    _GLIR_TYPE: str = ...

    def __init__(
        self,
        data: ndarray | tuple | None = None,
        format=None,
        resizable: bool = True,
        interpolation: str | None = None,
        wrapping: str | None = None,
        shape: tuple | None = None,
        internalformat: str | None = None,
        resizeable=None,
    ): ...
    @property
    def width(self): ...
    @property
    def glsl_type(self): ...
    @property
    def glsl_sampler_type(self): ...
    @property
    def glsl_sample(self): ...

# --------------------------------------------------------- Texture2D class ---
class Texture2D(BaseTexture):
    _ndim: int = ...
    _GLIR_TYPE: str = ...

    def __init__(
        self,
        data: NDArray | None = None,
        format=None,
        resizable: bool = True,
        interpolation: str | None = None,
        wrapping: str | None = None,
        shape: tuple | None = None,
        internalformat: str | None = None,
        resizeable=None,
    ): ...
    @property
    def height(self): ...
    @property
    def width(self): ...
    @property
    def glsl_type(self): ...
    @property
    def glsl_sampler_type(self): ...
    @property
    def glsl_sample(self): ...

# --------------------------------------------------------- Texture3D class ---
class Texture3D(BaseTexture):
    _ndim: int = ...
    _GLIR_TYPE: str = ...

    def __init__(
        self,
        data: ndarray | tuple | None = None,
        format=None,
        resizable: bool = True,
        interpolation: str | None = None,
        wrapping: str | None = None,
        shape: tuple | None = None,
        internalformat: str | None = None,
        resizeable=None,
    ): ...
    @property
    def width(self): ...
    @property
    def height(self): ...
    @property
    def depth(self): ...
    @property
    def glsl_type(self): ...
    @property
    def glsl_sampler_type(self): ...
    @property
    def glsl_sample(self): ...

# --------------------------------------------------------- TextureCube class ---
class TextureCube(BaseTexture):
    _ndim: int = ...
    _GLIR_TYPE: str = ...

    def __init__(
        self,
        data: ndarray | tuple | None = None,
        format=None,
        resizable: bool = True,
        interpolation: str | None = None,
        wrapping: str | None = None,
        shape: tuple | None = None,
        internalformat: str | None = None,
        resizeable=None,
    ): ...
    @property
    def height(self): ...
    @property
    def width(self): ...
    @property
    def depth(self): ...
    @property
    def glsl_type(self): ...
    @property
    def glsl_sampler_type(self): ...
    @property
    def glsl_sample(self): ...

# ------------------------------------------------- TextureEmulated3D class ---
class TextureEmulated3D(Texture2D):
    _glsl_sample_nearest: str = ...

    _glsl_sample_linear: str = ...

    _gl_max_texture_size: int = ...

    def __init__(
        self,
        data: ndarray | tuple | None = None,
        format=None,
        resizable: bool = True,
        interpolation: str | None = None,
        wrapping: str | None = None,
        shape: tuple | None = None,
        internalformat: str | None = None,
        resizeable=None,
    ): ...
    def _set_emulated_shape(self, data_or_shape): ...
    def _normalize_emulated_shape(self, data_or_shape): ...
    def _update_variables(self): ...
    def set_data(
        self,
        data: NDArray,
        offset: tuple[int, ...] | int | None = None,
        copy: bool = False,
    ): ...
    def resize(self, shape: tuple[int, ...], format=None, internalformat=None): ...
    @property
    def shape(self): ...
    @property
    def width(self): ...
    @property
    def height(self): ...
    @property
    def depth(self): ...
    @property
    def glsl_sample(self): ...

# ------------------------------------------------------ TextureAtlas class ---
class TextureAtlas(Texture2D):
    def __init__(self, shape: tuple[int, ...] = ..., dtype: np.dtype = ...): ...
    def get_free_region(self, width: int, height: int) -> tuple | None: ...
    def _fit(self, index, width, height): ...
