# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
from .arcball import ArcballCamera
from .base_camera import BaseCamera
from .fly import FlyCamera
from .panzoom import PanZoomCamera
from .perspective import PerspectiveCamera
from .turntable import TurntableCamera

def make_camera(cam_type: str, *args, **kwargs): ...
