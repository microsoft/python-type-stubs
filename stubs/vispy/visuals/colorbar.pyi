# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
# Author: Siddharth Bhat
# -----------------------------------------------------------------------------

from functools import lru_cache

import numpy as np

from ..color import get_colormap
from . import CompoundVisual, TextVisual, Visual, _BorderVisual

# from .border import _BorderVisual
from .shaders import Function

_VERTEX_SHADER: str = ...

_FRAGMENT_SHADER: str = ...

class _CoreColorBarVisual(Visual):
    _shaders: dict = ...

    def __init__(self, pos, halfdim, cmap, orientation, **kwargs): ...
    def _update(self): ...
    @staticmethod
    @lru_cache(maxsize=4)
    def _get_texcoord_func(orientation): ...
    @staticmethod
    def _check_orientation(orientation): ...
    @property
    def pos(self): ...
    @pos.setter
    def pos(self, pos): ...
    @property
    def halfdim(self): ...
    @halfdim.setter
    def halfdim(self, halfdim): ...
    @property
    def cmap(self): ...
    @cmap.setter
    def cmap(self, cmap): ...
    @staticmethod
    def _prepare_transforms(view): ...
    def _prepare_draw(self, view): ...

class ColorBarVisual(CompoundVisual):
    # The padding multiplier that's used to place the text
    # next to the Colorbar. Makes sure the text isn't
    # visually "sticking" to the Colorbar
    text_padding_factor: float = ...

    def __init__(
        self,
        cmap,
        orientation,
        size,
        pos=[0, 0],
        label="",
        label_color="black",
        clim=...,
        border_width=1.0,
        border_color="black",
    ): ...
    def _update(self): ...
    def _update_positions(self): ...
    @staticmethod
    def _get_label_anchors(center, halfdim, orientation, transforms): ...
    @staticmethod
    def _get_ticks_anchors(center, halfdim, orientation, transforms): ...
    @staticmethod
    def _calc_positions(center, halfdim, border_width, orientation, transforms): ...
    @property
    def pos(self): ...
    @pos.setter
    def pos(self, pos): ...
    @property
    def cmap(self): ...
    @cmap.setter
    def cmap(self, cmap): ...
    @property
    def clim(self): ...
    @clim.setter
    def clim(self, clim): ...
    @property
    def label(self): ...
    @label.setter
    def label(self, label): ...
    @property
    def ticks(self): ...
    @ticks.setter
    def ticks(self, ticks): ...
    @property
    def border_width(self): ...
    @border_width.setter
    def border_width(self, border_width): ...
    @property
    def border_color(self): ...
    @border_color.setter
    def border_color(self, border_color): ...
    @property
    def orientation(self): ...
    @property
    def size(self): ...
    @size.setter
    def size(self, size): ...
