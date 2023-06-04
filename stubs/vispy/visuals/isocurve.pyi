from numpy.typing import NDArray

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

import numpy as np

from vispy.color.color_array import Color

from .line import LineVisual
from ..color import ColorArray
from ..color.colormap import _normalize, get_colormap
from ..geometry.isocurve import isocurve

class IsocurveVisual(LineVisual):
    def __init__(
        self,
        data: NDArray | None = None,
        levels: NDArray | None = None,
        color_lev: Color | str | tuple | list | np.ndarray | None = None,
        clim: tuple | None = None,
        **kwargs,
    ): ...
    @property
    def levels(self): ...
    @levels.setter
    def levels(self, levels): ...
    @property
    def color(self): ...
    @color.setter
    def color(self, color): ...
    def set_data(self, data: NDArray): ...
    def _get_verts_and_connect(self, paths): ...
    def _compute_iso_line(self): ...
    def _compute_iso_color(self): ...
    def _levels_to_colors(self): ...
    def _prepare_draw(self, view): ...
