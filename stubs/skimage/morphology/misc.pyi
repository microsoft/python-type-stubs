from numpy.typing import NDArray
import numpy as np
import functools
from scipy import ndimage as ndi
from .._shared.utils import warn, remove_arg
from .footprints import _default_footprint

# Our function names don't exactly correspond to ndimages.
# This dictionary translates from our names to scipy's.
funcs = ...
skimage2ndimage: dict = ...

# These function names are the same in ndimage.
funcs = ...

def default_footprint(func): ...
def _check_dtype_supported(ar): ...
@remove_arg(
    "in_place", changed_version="1.0", help_msg="Please use out argument instead."
)
def remove_small_objects(
    ar, min_size=64, connectivity=1, in_place=False, *, out: NDArray | None = None
): ...
@remove_arg(
    "in_place", changed_version="1.0", help_msg="Please use out argument instead."
)
def remove_small_holes(
    ar, area_threshold=64, connectivity=1, in_place=False, *, out: NDArray | None = None
): ...
