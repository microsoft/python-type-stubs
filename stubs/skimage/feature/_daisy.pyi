from numpy.typing import ArrayLike
import math

import numpy as np
from numpy import arctan2, exp, pi, sqrt

from .. import draw

from .._shared.filters import gaussian
from .._shared.utils import check_nD

def daisy(
    image,
    step: int = 4,
    radius: int = 15,
    rings: int = 3,
    histograms: int = 8,
    orientations: int = 8,
    normalization="l1",
    sigmas=None,
    ring_radii=None,
    visualize: bool = False,
): ...
