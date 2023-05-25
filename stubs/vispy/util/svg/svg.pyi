# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier. All rights reserved.
# Distributed under the terms of the new BSD License.
# -----------------------------------------------------------------------------

from .group import Group
from .viewport import Viewport

class SVG(Group):
    def __init__(self, content=None, parent=None): ...
    @property
    def viewport(self): ...
    def __repr__(self): ...
    @property
    def xml(self): ...
    def _xml(self, prefix=""): ...
