# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
__all__ = [
    "ArcballCamera",
    "BaseCamera",
    "FlyCamera",
    "MagnifyCamera",
    "Magnify1DCamera",
    "PanZoomCamera",
    "TurntableCamera",
]

from ._base import make_camera as make_camera  # noqa
from .base_camera import BaseCamera as BaseCamera  # noqa
from .panzoom import PanZoomCamera as PanZoomCamera  # noqa
from .arcball import ArcballCamera as ArcballCamera  # noqa
from .turntable import TurntableCamera as TurntableCamera  # noqa
from .fly import FlyCamera as FlyCamera  # noqa
from .magnify import (
    MagnifyCamera as MagnifyCamera,
    Magnify1DCamera as Magnify1DCamera,
)  # noqa
