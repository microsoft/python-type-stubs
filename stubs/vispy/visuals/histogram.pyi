from typing import Literal

import numpy as np
from numpy.typing import ArrayLike
from vispy.util.svg.color import Color

from .mesh import MeshVisual

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

class HistogramVisual(MeshVisual):
    def __init__(
        self,
        data: ArrayLike,
        bins: ArrayLike | int = 10,
        color: Color | str = "w",
        orientation: Literal["h", "v"] = "h",
    ): ...
