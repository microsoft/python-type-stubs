from numpy.typing import ArrayLike

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np

from .visual import Visual
from .. import gloo

class ScrollingLinesVisual(Visual):

    vertex_code: str = ...

    fragment_code: str = ...

    def __init__(
        self,
        n_lines: int,
        line_size: int,
        dx: float,
        color: ArrayLike | None = None,
        pos_offset: ArrayLike | None = None,
        columns: int | None = None,
        cell_size: tuple | None = None,
    ): ...
    def set_pos_offset(self, po: ArrayLike): ...
    def set_color(self, color: ArrayLike): ...
    def _prepare_transforms(self, view): ...
    def _prepare_draw(self, view): ...
    def _compute_bounds(self, axis, view): ...
    def roll_data(self, data: ArrayLike): ...
    def set_data(self, index: int, data: ArrayLike): ...
