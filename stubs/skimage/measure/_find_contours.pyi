import numpy as np
from skimage._shared.utils import deprecate_kwarg

from collections import deque

_param_options = ...

@deprecate_kwarg({"array": "image"}, deprecated_version="0.18", removed_version="0.20")
def find_contours(
    image,
    level: float | None = None,
    fully_connected="low",
    positive_orientation="low",
    *,
    mask=None
): ...
def _assemble_contours(segments): ...
