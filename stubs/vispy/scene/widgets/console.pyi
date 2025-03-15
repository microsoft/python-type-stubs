import numpy as np

from ...color import Color
from ...gloo import VertexBuffer
from ...util.event import Event
from ...visuals import Visual
from .widget import Widget

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

# Code translated from glumpy

# Translated from
# http://www.piclist.com/tecHREF/datafile/charset/
#     extractor/charset_extractor.htm
__font_6x8__ = ...

VERTEX_SHADER: str = ...

FRAGMENT_SHADER: str = ...

class Console(Widget):
    def __init__(self, text_color: Color | str = "black", font_size: float = 12.0, **kwargs): ...
    def on_resize(self, event: Event): ...
    def clear(self): ...
    def write(self, text: str = "", wrap: str | bool = True): ...
    @property
    def text_color(self): ...
    @text_color.setter
    def text_color(self, color): ...
    @property
    def font_size(self): ...
    @font_size.setter
    def font_size(self, font_size): ...

class ConsoleVisual(Visual):
    def __init__(self, text_color, font_size, **kwargs): ...
    @property
    def size(self): ...
    @size.setter
    def size(self, s): ...
    @property
    def text_color(self): ...
    @text_color.setter
    def text_color(self, color): ...
    @property
    def font_size(self): ...
    @font_size.setter
    def font_size(self, font_size): ...
    def _resize_buffers(self, font_scale): ...
    def _prepare_draw(self, view): ...
    def _prepare_transforms(self, view): ...
    def clear(self): ...
    def write(self, text: str = "", wrap: str | bool = True): ...
    def _do_pending_writes(self): ...
    def _insert_text_buf(self, line, idx): ...
