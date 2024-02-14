import sys

from numpy.typing import ArrayLike

from ._vispy_fonts import _vispy_fonts

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

_fonts: dict = ...

def list_fonts() -> ArrayLike: ...
