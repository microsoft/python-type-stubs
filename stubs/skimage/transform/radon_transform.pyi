from numpy.typing import NDArray, ArrayLike
import numpy as np

from scipy.interpolate import interp1d
from scipy.constants import golden_ratio
from scipy.fft import fft, ifft, fftfreq, fftshift
from ._warps import warp
from .._shared.utils import convert_to_float
from warnings import warn
from functools import partial

__all__ = ["radon", "order_angles_golden_ratio", "iradon", "iradon_sart"]

def radon(
    image, theta=None, circle: bool = True, *, preserve_range: bool = False
) -> NDArray: ...
def _sinogram_circle_to_square(sinogram): ...
def _get_fourier_filter(size, filter_name): ...
def iradon(
    radon_image: ArrayLike,
    theta=None,
    output_size: int | None = None,
    filter_name: str = "ramp",
    interpolation: str = "linear",
    circle: bool = True,
    preserve_range: bool = True,
): ...
def order_angles_golden_ratio(theta): ...
def iradon_sart(
    radon_image,
    theta=None,
    image=None,
    projection_shifts=None,
    clip=None,
    relaxation: float = 0.15,
    dtype=None,
) -> NDArray: ...
