from numpy.typing import NDArray

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from __future__ import division

import numpy as np

from .mesh import MeshVisual
from ..geometry import MeshData

class SurfacePlotVisual(MeshVisual):
    def __init__(
        self,
        x: NDArray | None = None,
        y: NDArray | None = None,
        z: NDArray | None = None,
        colors: NDArray | None = None,
        **kwargs,
    ): ...
    def _update_x_data(self, x): ...
    def _update_y_data(self, y): ...
    def _update_z_data(self, z): ...
    def _update_mesh_vertices(self, x_is_new, y_is_new, z_is_new): ...
    def _prepare_mesh_colors(self, colors): ...
    def set_data(
        self,
        x: NDArray | None = None,
        y: NDArray | None = None,
        z: NDArray | None = None,
        colors: NDArray | None = None,
    ): ...
    def _generate_faces(self): ...
