from vispy.util.event import Event

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

from .widget import Widget
from ...visuals import TextVisual

class Label(Widget):
    def __init__(self, text: str, rotation: float = 0.0, **kwargs): ...
    def on_resize(self, event: Event): ...
    def _set_pos(self): ...
    @property
    def text(self): ...
    @text.setter
    def text(self, t): ...
