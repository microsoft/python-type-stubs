from typing import Literal
from numpy.typing import ArrayLike

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

import numpy as np

from . import LineVisual

class MeshNormalsVisual(LineVisual):
    def __init__(
        self,
        meshdata=None,
        primitive: Literal["face", "vertex"] = "face",
        length: float | ArrayLike | None = None,
        length_method: Literal["median_edge", "max_extent"] = "median_edge",
        length_scale: float = 1.0,
        **kwargs,
    ): ...
    def set_data(
        self,
        meshdata=None,
        primitive: Literal["face", "vertex"] = "face",
        length: float | ArrayLike | None = None,
        length_method: Literal["median_edge", "max_extent"] = "median_edge",
        length_scale: float = 1.0,
        **kwargs,
    ): ...
