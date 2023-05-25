from vispy.color import Color

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
# Author: Siddharth Bhat
# -----------------------------------------------------------------------------

import numpy as np

from . import Visual
from ..color import Color

_VERTEX_SHADER: str = ...

_FRAGMENT_SHADER: str = ...  # noqa

class _BorderVisual(Visual):

    _shaders: dict = ...

    def __init__(
        self,
        pos: tuple[float, float],
        halfdim: tuple[float, float],
        border_width: float = 1.0,
        border_color: str | Color | None = None,
        **kwargs,
    ): ...
    @staticmethod
    def _prepare_transforms(view): ...
    @property
    def visual_border_width(self): ...
    def _update(self): ...
    def _prepare_draw(self, view=None): ...
    @property
    def border_width(self): ...
    @border_width.setter
    def border_width(self, border_width): ...
    @property
    def border_color(self): ...
    @border_color.setter
    def border_color(self, border_color): ...
    @property
    def pos(self): ...
    @pos.setter
    def pos(self, pos): ...
    @property
    def halfdim(self): ...
    @halfdim.setter
    def halfdim(self, halfdim): ...
