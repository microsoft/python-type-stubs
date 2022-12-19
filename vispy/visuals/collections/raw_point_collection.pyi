from vispy.util.svg.transform import Transform
from numpy.typing import ArrayLike, NDArray

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

import numpy as np
from ... import glsl
from .collection import Collection
from ..transforms import NullTransform

class RawPointCollection(Collection):
    def __init__(
        self,
        user_dtype: ArrayLike | None = None,
        transform: Transform | None = None,
        vertex: str | None = None,
        fragment: str | None = None,
        **kwargs,
    ): ...
    def append(self, P: NDArray, itemsize: int | None = None, **kwargs): ...
