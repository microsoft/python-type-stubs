from vispy.util.svg.color import Color
from numpy.typing import NDArray

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

import warnings
from .box import BoxVisual

class CubeVisual(BoxVisual):
    def __init__(
        self,
        size: float | tuple = 1.0,
        vertex_colors: NDArray | None = None,
        face_colors: NDArray | None = None,
        color: Color = ...,
        edge_color: tuple | Color | None = None,
        **kwargs,
    ): ...
