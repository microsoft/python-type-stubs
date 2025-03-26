import numpy as np

from ...util.event import Event
from ...visuals.filters import Clipper
from ..cameras import BaseCamera, make_camera
from ..node import Node
from ..subscene import SubScene
from .widget import Widget

# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

class ViewBox(Widget):
    def __init__(self, camera: None | str | BaseCamera = None, **kwargs): ...
    @property
    def camera(self): ...
    @camera.setter
    def camera(self, cam): ...
    def is_in_scene(self, node: Node): ...
    def get_scene_bounds(self, dim: None | int = None) -> list | tuple: ...
    @property
    def scene(self): ...
    def add(self, node: Node): ...
    def on_resize(self, event: Event): ...
    def _update_scene_clipper(self, event=None): ...
