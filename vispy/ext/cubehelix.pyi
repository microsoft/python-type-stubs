from numpy import ndarray
from .._typing import Scalar

# -*- coding: utf-8 -*-

from math import pi
import numpy as np

def cubehelix(
    start: Scalar = 0.5,
    rot: Scalar = 1,
    gamma: Scalar = 1.0,
    reverse: bool = True,
    nlev: Scalar = 256.0,
    minSat: Scalar = 1.2,
    maxSat: Scalar = 1.2,
    minLight: Scalar = 0.0,
    maxLight: Scalar = 1.0,
    **kwargs,
) -> np.ndarray: ...
