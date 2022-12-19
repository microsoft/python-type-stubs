from numpy.typing import ArrayLike

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

import numpy as np

from .triangulation import Triangulation

class PolygonData(object):
    def __init__(
        self,
        vertices: ArrayLike | None = None,
        edges: ArrayLike | None = None,
        faces: ArrayLike | None = None,
    ): ...
    @property
    def faces(self): ...
    @faces.setter
    def faces(self, f): ...
    @property
    def vertices(self): ...
    @vertices.setter
    def vertices(self, v): ...
    @property
    def edges(self): ...
    @edges.setter
    def edges(self, e): ...
    @property
    def convex_hull(self): ...
    def triangulate(self): ...
    def add_vertex(self, vertex: ArrayLike): ...
