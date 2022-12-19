from numpy.typing import ArrayLike

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

import numpy as np

from ..util import _straight_line_vertices, _rescale_layout

class fruchterman_reingold(object):
    def __init__(
        self,
        optimal: float | None = None,
        iterations: int = 50,
        pos: ArrayLike | None = None,
    ): ...
    def __call__(self, adjacency_mat: ArrayLike, directed: bool = False): ...
    def _fruchterman_reingold(self, adjacency_mat, directed=False): ...
    def _sparse_fruchterman_reingold(self, adjacency_mat, directed=False): ...

def _calculate_delta_pos(adjacency_arr, pos, t, optimal): ...
