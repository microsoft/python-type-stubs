from numpy import ndarray
from vispy.util.svg.color import Color
from numpy.typing import NDArray
from vispy._typing import ArrayLike

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

import numpy as np

from .line import LineVisual
from ..color import ColorArray
from ..color.colormap import _normalize, get_colormap

def iso_mesh_line(
    vertices: NDArray, tris: NDArray, vertex_data: NDArray, levels: NDArray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]: ...

class IsolineVisual(LineVisual):
    def __init__(
        self,
        vertices: NDArray | None = None,
        tris: NDArray | None = None,
        data: NDArray | None = None,
        levels: NDArray | None = None,
        color_lev: Color | tuple | ArrayLike | str | None = None,
        **kwargs,
    ): ...
    @property
    def levels(self): ...
    @levels.setter
    def levels(self, levels): ...
    @property
    def data(self): ...
    def set_data(
        self,
        vertices: NDArray | None = None,
        tris: NDArray | None = None,
        data: NDArray | None = None,
    ): ...
    @property
    def color(self): ...
    def set_color(self, color: Color): ...
    def _levels_to_colors(self): ...
    def _compute_iso_color(self): ...
    def _prepare_draw(self, view): ...
