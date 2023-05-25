from numpy.typing import ArrayLike
from typing import Sequence

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

import numpy as np

from .visual import CompoundVisual
from .mesh import MeshVisual
from .line import LineVisual
from ..color import Color
from ..geometry import PolygonData

class PolygonVisual(CompoundVisual):
    def __init__(
        self,
        pos: ArrayLike | None = None,
        color: str | tuple | Sequence = "black",
        border_color: str | tuple | Sequence | None = None,
        border_width: int = 1,
        border_method: str = "gl",
        triangulate: bool = True,
        **kwargs,
    ): ...
    def _update(self): ...
    @property
    def pos(self): ...
    @pos.setter
    def pos(self, pos): ...
    @property
    def color(self): ...
    @color.setter
    def color(self, color): ...
    @property
    def border_color(self): ...
    @border_color.setter
    def border_color(self, border_color): ...
    @property
    def mesh(self): ...
    @mesh.setter
    def mesh(self, mesh): ...
    @property
    def border(self): ...
    @border.setter
    def border(self, border): ...
