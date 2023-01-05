from vispy.gloo.texture import Texture2D
from numpy.typing import ArrayLike

# -*- coding: utf-8 -*-

import numpy as np

from ...gloo import (
    Program,
    FrameBuffer,
    VertexBuffer,
    Texture2D,
    set_viewport,
    set_state,
)

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
