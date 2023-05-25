# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

from .color import Color
from .number import Number
from .length import Length

_converters: dict = ...

class Style(object):
    def __init__(self): ...
    def update(self, content): ...
    @property
    def xml(self): ...
    def _xml(self, prefix=""): ...
