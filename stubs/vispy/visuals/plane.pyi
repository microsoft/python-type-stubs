from vispy.util.svg.color import Color
from numpy.typing import NDArray

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

from ..geometry import create_plane
from .visual import CompoundVisual
from .mesh import MeshVisual

class PlaneVisual(CompoundVisual):
    def __init__(
        self,
        width: float = 1,
        height: float = 1,
        width_segments: int = 1,
        height_segments: float = 1,
        direction: str = "+z",
        vertex_colors: NDArray | None = None,
        face_colors: NDArray | None = None,
        color: Color = ...,
        edge_color: tuple | Color | None = None,
    ): ...
