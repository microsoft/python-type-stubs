# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

import os
import sys
import ctypes.util

from . import _copy_gl_functions
from ._constants import *  # noqa
from ...util import logger

# Ctypes stuff

# Load the OpenGL library. We more or less follow the same approach
# as PyOpenGL does internally

_have_get_proc_address: bool = ...
_lib = ...

def _have_context(): ...
def _get_gl_version(_lib): ...
def _get_gl_func(name, restype, argtypes): ...

# Inject

from . import _gl2  # noqa
