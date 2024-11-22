# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from ._constants import *  # noqa

def _patch(): ...

# Inject

def _make_unavailable_func(funcname): ...
def _get_function_from_pyopengl(funcname): ...
def _inject(): ...

from . import _pyopengl2  # noqa
