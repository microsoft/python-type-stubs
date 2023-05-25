from numpy.typing import ArrayLike

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
from ... import glsl
from .collection import Collection
from ..transforms import NullTransform

class AggSegmentCollection(Collection):
    def __init__(
        self,
        user_dtype: ArrayLike | None = None,
        transform: str | None = None,
        vertex: str | None = None,
        fragment: str | None = None,
        **kwargs,
    ): ...
    def append(self, P0, P1, itemsize: int | None = None, **kwargs): ...
