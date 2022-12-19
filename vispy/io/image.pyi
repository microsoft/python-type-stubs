from numpy.typing import ArrayLike

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
# Author: Luke Campagnola
# -----------------------------------------------------------------------------

import struct
import zlib
import numpy as np

def _make_png(data, level=6): ...
def read_png(filename: str) -> ArrayLike: ...
def write_png(filename: str, data: ArrayLike): ...
def imread(filename: str, format: str | None = None) -> ArrayLike: ...
def imsave(filename: str, im: ArrayLike, format: str | None = None): ...
def _check_img_lib(): ...
