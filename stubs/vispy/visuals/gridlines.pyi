from vispy.util.svg.color import Color

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from .image import ImageVisual
from ..color import Color
from .shaders import Function

_GRID_COLOR: str = ...

class GridLinesVisual(ImageVisual):
    def __init__(self, scale: tuple = ..., color: Color | str = "w"): ...
    @property
    def size(self): ...
    def _prepare_transforms(self, view): ...
    def _prepare_draw(self, view): ...
