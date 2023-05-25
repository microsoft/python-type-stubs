from vispy.util.svg.color import Color
from typing import Mapping, Any
from numpy.typing import ArrayLike

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

##############################################################################
# Load font into texture

import numpy as np
from copy import deepcopy
import sys

from ._sdf_gpu import SDFRendererGPU
from ...gloo import TextureAtlas, IndexBuffer, VertexBuffer
from ...gloo import context
from ...gloo.wrappers import _check_valid
from ..transforms import STTransform
from ...color import ColorArray
from ..visual import Visual
from ...io import load_spatial_filters

class TextureFont(object):
    def __init__(self, font: Mapping, renderer: SDFRendererGPU): ...
    @property
    def ratio(self): ...
    @property
    def slop(self): ...
    def __getitem__(self, char): ...
    def _load_char(self, char): ...

class FontManager(object):

    # XXX: should store a font-manager on each context,
    # or let TextureFont use a TextureAtlas for each context
    def __init__(self, method="cpu"): ...
    def get_font(self, face, bold=False, italic=False): ...

##############################################################################
# The visual

_VERTEX_SHADER: str = ...

_FRAGMENT_SHADER: str = ...

def _text_to_vbo(text, font, anchor_x, anchor_y, lowres_size): ...

class TextVisual(Visual):

    _shaders: dict = ...

    def __init__(
        self,
        text: str | ArrayLike | None = None,
        color: Color | str = "black",
        bold: bool = False,
        italic: bool = False,
        face: str = "OpenSans",
        font_size: float = 12,
        pos=[0, 0, 0],
        rotation: float = 0.0,
        anchor_x: str = "center",
        anchor_y: str = "center",
        method: str = "cpu",
        font_manager: Any | None = None,
        depth_test: bool = False,
    ): ...
    @property
    def text(self): ...
    @text.setter
    def text(self, text): ...
    @property
    def anchors(self): ...
    @anchors.setter
    def anchors(self, a): ...
    @property
    def font_size(self): ...
    @font_size.setter
    def font_size(self, size): ...
    @property
    def color(self): ...
    @color.setter
    def color(self, color): ...
    @property
    def rotation(self): ...
    @rotation.setter
    def rotation(self, rotation): ...
    @property
    def pos(self): ...
    @pos.setter
    def pos(self, pos): ...
    def _prepare_draw(self, view): ...
    def _prepare_transforms(self, view): ...
    def _compute_bounds(self, axis, view): ...
    @property
    def face(self): ...
    @face.setter
    def face(self, value): ...
    @property
    def bold(self): ...
    @bold.setter
    def bold(self, value): ...
    @property
    def italic(self): ...
    @italic.setter
    def italic(self, value): ...
    def _update_font(self): ...

class SDFRendererCPU(object):

    # This should probably live in _sdf_cpu.pyx, but doing so makes
    # debugging substantially more annoying
    def render_to_texture(self, data, texture, offset, size): ...
