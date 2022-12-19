from ..scene.node import Node
from ..gloo.framebuffer import FrameBuffer
from ..util.event import Event
from numpy.typing import ArrayLike
from ..visuals.visual import Visual
from typing import Mapping
from ..gloo.context import GLContext
from ..scene.widgets.widget import Widget
from ..util.svg.color import Color
from ..app.application import Application
from ..app.canvas import Canvas, DrawEvent

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

import weakref
import numpy as np

from .. import gloo
from .. import app
from .visuals import VisualNode
from ..visuals.transforms import TransformSystem
from ..color import Color
from ..util import logger, Frozen
from ..util.profiler import Profiler
from .subscene import SubScene
from .events import SceneMouseEvent
from .widgets import Widget

class SceneCanvas(app.Canvas, Frozen):
    def __init__(
        self,
        title: str = "VisPy canvas",
        size: tuple[float, float] = ...,
        position: tuple[float, float] | None = None,
        show: bool = False,
        autoswap: bool = True,
        app: str | Application | None = None,
        create_native: bool = True,
        vsync: bool = False,
        resizable: bool = True,
        decorate: bool = True,
        fullscreen: bool | int = False,
        config: Mapping | None = None,
        shared: None | Canvas | GLContext = None,
        keys: str | Mapping | None = None,
        parent: Widget | None = None,
        dpi: None | float = None,
        always_on_top: bool = False,
        px_scale: int = 1,
        bgcolor: Color | str = "black",
    ): ...
    @property
    def scene(self): ...
    @scene.setter
    def scene(self, node): ...
    @property
    def central_widget(self): ...
    @property
    def bgcolor(self): ...
    @bgcolor.setter
    def bgcolor(self, color): ...
    def update(self, node: Node | None = None): ...
    def on_draw(self, event: Event): ...
    def render(
        self,
        region: tuple | None | None = None,
        size: tuple | None | None = None,
        bgcolor: None | Color = None,
        crop: ArrayLike | None = None,
        alpha: bool = True,
    ) -> ArrayLike: ...
    def _draw_scene(self, bgcolor=None): ...
    def draw_visual(self, visual: Visual, event: DrawEvent | None = None): ...
    def _generate_draw_order(self, node=None): ...
    def _update_scenegraph(self, event): ...
    def _process_mouse_event(self, event): ...
    def visual_at(self, pos: tuple) -> None | Visual: ...
    def _visual_bounds_at(self, pos, node=None): ...
    def visuals_at(self, pos: tuple, radius: int = 10): ...
    def _render_picking(self, crop): ...
    def on_resize(self, event: Event): ...
    def on_close(self, event: Event): ...

    # -------------------------------------------------- transform handling ---
    def push_viewport(self, viewport: tuple): ...
    def pop_viewport(self): ...
    def push_fbo(self, fbo: FrameBuffer, offset: tuple, csize: tuple): ...
    def pop_fbo(self): ...
    def _current_framebuffer(self): ...
    def _update_transforms(self): ...
