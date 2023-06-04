from vispy.util.svg.color import Color
from numpy.typing import ArrayLike, NDArray

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

from ..geometry import create_box
from .mesh import MeshVisual
from .visual import CompoundVisual

class BoxVisual(CompoundVisual):
    def __init__(
        self,
        width: float = 1,
        height: float = 1,
        depth: float = 1,
        width_segments: int = 1,
        height_segments: float = 1,
        depth_segments: float = 1,
        planes: ArrayLike | None = None,
        vertex_colors: NDArray | None = None,
        face_colors: NDArray | None = None,
        color: Color = ...,
        edge_color: tuple | Color | None = None,
        **kwargs,
    ): ...
    @property
    def mesh(self): ...
    @mesh.setter
    def mesh(self, mesh): ...
    @property
    def border(self): ...
    @border.setter
    def border(self, border): ...
