from numpy.typing import NDArray
from typing import Callable
import numpy as np
import scipy.ndimage as ndi

__all__ = ["blur_effect"]

def blur_effect(
    image: NDArray,
    h_size: int = 11,
    channel_axis: int | None = None,
    reduce_func: Callable = ...,
): ...
