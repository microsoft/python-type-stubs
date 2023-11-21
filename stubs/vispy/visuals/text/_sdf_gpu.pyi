import numpy as np
from numpy.typing import ArrayLike
from vispy.gloo.texture import Texture2D

from ...gloo import FrameBuffer, Program, Texture2D, VertexBuffer, set_state, set_viewport

# -*- coding: utf-8 -*-

vert_seed: str = ...

vert: str = ...

frag_seed: str = ...

frag_flood: str = ...

frag_insert: str = ...

class SDFRendererGPU(object):
    def __init__(self): ...
    def render_to_texture(
        self,
        data: ArrayLike,
        texture: Texture2D,
        offset: tuple[int, ...],
        size: tuple[int, ...],
    ): ...
    def _render_edf(self, orig_tex): ...
