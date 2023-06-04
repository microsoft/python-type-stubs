# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
from .base_camera import BaseCamera
from .perspective import PerspectiveCamera
from .panzoom import PanZoomCamera
from .arcball import ArcballCamera
from .turntable import TurntableCamera
from .fly import FlyCamera

def make_camera(cam_type: str, *args, **kwargs): ...
