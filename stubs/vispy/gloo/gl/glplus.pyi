# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from OpenGL import GL as _GL
from . import _pyopengl2
from . import _constants

def _inject(): ...

# List of deprecated functions, obtained by parsing gl.spec
_deprecated_functions: str = ...
