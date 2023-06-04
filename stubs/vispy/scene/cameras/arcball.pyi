# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from __future__ import division

import numpy as np

from ...util import transforms
from ...util.quaternion import Quaternion
from ...visuals.transforms import MatrixTransform
from .perspective import Base3DRotationCamera

class ArcballCamera(Base3DRotationCamera):

    _state_props = ...

    def __init__(self, fov: float = 45.0, distance: None | float = None, translate_speed: float = 1.0, **kwargs): ...
    def _update_rotation(self, event): ...
    def _get_rotation_tr(self): ...
    def _dist_to_trans(self, dist): ...
    def _get_dim_vectors(self): ...

def _arcball(xy, wh): ...
