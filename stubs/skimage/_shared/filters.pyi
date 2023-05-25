from skimage._typing import Scalar
from numpy.typing import ArrayLike, NDArray
from typing import Literal
from collections.abc import Iterable

import numpy as np
from scipy import ndimage as ndi

from .._shared import utils
from .._shared.utils import _supported_float_type, convert_to_float, warn

@utils.deprecate_multichannel_kwarg(multichannel_position=5)
def gaussian(
    image: ArrayLike,
    sigma=1,
    output: ArrayLike | None = None,
    mode: Literal["reflect", "constant", "nearest", "mirror", "wrap"] = "nearest",
    cval: Scalar = 0,
    multichannel=None,
    preserve_range: bool = False,
    truncate: float = 4.0,
    *,
    channel_axis: int | None = None
) -> NDArray: ...
