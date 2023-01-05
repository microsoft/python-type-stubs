from vispy.util.svg.color import Color
from typing import Literal
from numpy.typing import ArrayLike

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

import numpy as np

from .mesh import MeshVisual

class HistogramVisual(MeshVisual):
    def __init__(
        self,
        data: ArrayLike,
        bins: ArrayLike | int = 10,
        color: Color | str = "w",
        orientation: Literal["h", "v"] = "h",
    ): ...
