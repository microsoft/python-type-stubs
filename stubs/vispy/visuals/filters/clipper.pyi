# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from .base_filter import Filter
from ..transforms import NullTransform
from ...geometry import Rect

class Clipper(Filter):

    FRAG_SHADER: str = ...

    def __init__(self, bounds=..., transform=None): ...
    @property
    def bounds(self): ...
    @bounds.setter
    def bounds(self, b): ...
    @property
    def transform(self): ...
    @transform.setter
    def transform(self, tr): ...
