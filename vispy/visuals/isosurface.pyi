from vispy.util.svg.color import Color
from numpy.typing import NDArray, ArrayLike

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from __future__ import division

from .mesh import MeshVisual
from ..geometry.isosurface import isosurface
from ..color import Color

class IsosurfaceVisual(MeshVisual):
    def __init__(
        self,
        data: NDArray | None = None,
        level: None | float = None,
        vertex_colors: NDArray | None = None,
        face_colors: NDArray | None = None,
        color: NDArray | None = ...,
        **kwargs,
    ): ...
    @property
    def level(self): ...
    @level.setter
    def level(self, level): ...
    def set_data(
        self,
        data: NDArray | None = None,
        vertex_colors: ArrayLike | None = None,
        face_colors: ArrayLike | None = None,
        color: Color | None = None,
    ): ...
    def _prepare_draw(self, view): ...
