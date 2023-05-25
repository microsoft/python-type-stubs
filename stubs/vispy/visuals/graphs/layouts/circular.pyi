from numpy.typing import ArrayLike, NDArray

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

import numpy as np

from ..util import _straight_line_vertices, issparse

def circular(adjacency_mat: ArrayLike | NDArray, directed: bool = False): ...
