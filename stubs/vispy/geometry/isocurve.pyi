import numpy as np
from numpy.typing import NDArray

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

def isocurve(data: NDArray, level: float, connected: bool = False, extend_to_edge: bool = False): ...
