from numpy.typing import ArrayLike
import numpy as np
from scipy.signal import fftconvolve

from .._shared.utils import check_nD, _supported_float_type

def _window_sum_2d(image, window_shape): ...
def _window_sum_3d(image, window_shape): ...
def match_template(
    image, template, pad_input: bool = False, mode="constant", constant_values=0
) -> ArrayLike: ...
