from vispy.util.svg.color import Color
from vispy.color.color_array import ColorArray
from numpy.typing import ArrayLike

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

import numpy as np

from vispy.color import ColorArray
from vispy.gloo import VertexBuffer
from vispy.visuals.shaders import Variable
from vispy.visuals.visual import Visual

_VERTEX_SHADER: str = ...

_FRAGMENT_SHADER: str = ...

class WindbarbVisual(Visual):

    _shaders: dict = ...

    def __init__(self, **kwargs): ...
    def set_data(
        self,
        pos: ArrayLike | None = None,
        wind: ArrayLike | None = None,
        trig: bool = True,
        size: float | ArrayLike = 50.0,
        antialias: float = 1.0,
        edge_width: None | float = 1.0,
        edge_color: ColorArray | Color | str = "black",
        face_color: ColorArray | Color | str = "white",
    ): ...
    def _prepare_transforms(self, view): ...
    def _prepare_draw(self, view): ...
    def _compute_bounds(self, axis, view): ...
