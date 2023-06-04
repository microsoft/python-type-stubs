# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from __future__ import division

import numpy as np

from ...util import transforms
from .perspective import Base3DRotationCamera

class TurntableCamera(Base3DRotationCamera):

    _state_props = ...

    def __init__(
        self,
        fov: float = 45.0,
        elevation: float = 30.0,
        azimuth: float = 30.0,
        roll: float = 0.0,
        distance: None | float = None,
        translate_speed: float = 1.0,
        **kwargs,
    ): ...
    @property
    def elevation(self): ...
    @elevation.setter
    def elevation(self, elev): ...
    @property
    def azimuth(self): ...
    @azimuth.setter
    def azimuth(self, azim): ...
    @property
    def roll(self): ...
    @roll.setter
    def roll(self, roll): ...
    def orbit(self, azim: float, elev: float): ...
    def _update_rotation(self, event): ...
    def _get_rotation_tr(self): ...
    def _dist_to_trans(self, dist): ...
