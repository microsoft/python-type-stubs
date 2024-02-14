# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from __future__ import annotations

from functools import lru_cache
from typing import Optional

import numpy as np

from ..shaders import Function, Varying
from .base_filter import Filter

class PlanesClipper(Filter):
    VERT_CODE: str = ...

    FRAG_CODE: str = ...

    def __init__(self, clipping_planes: Optional[np.ndarray] = None, coord_system: str = "scene"): ...
    @property
    def coord_system(self) -> str: ...
    def _attach(self, visual): ...
    @staticmethod
    @lru_cache(maxsize=10)
    def _build_clipping_planes_glsl(n_planes: int) -> str: ...
    @property
    def clipping_planes(self) -> np.ndarray: ...
    @clipping_planes.setter
    def clipping_planes(self, value: Optional[np.ndarray]): ...
