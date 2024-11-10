# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
from numpy.typing import NDArray

from .collection import Collection

class RawPolygonCollection(Collection):
    def __init__(
        self,
        user_dtype=None,
        transform=None,
        vertex: str | tuple[str, ...] | None = None,
        fragment: str | tuple[str, ...] | None = None,
        **kwargs: str,
    ): ...
    def append(self, points: NDArray, **kwargs): ...
