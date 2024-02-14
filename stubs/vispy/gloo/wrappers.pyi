from copy import deepcopy
from typing import Literal, Mapping

import numpy as np
from numpy import dtype
from numpy.typing import ArrayLike

from ..color import Color
from ..util import logger
from . import gl

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

__all__ = (
    "set_viewport",
    "set_depth_range",
    "set_front_face",  # noqa
    "set_cull_face",
    "set_line_width",
    "set_polygon_offset",  # noqa
    "clear",
    "set_clear_color",
    "set_clear_depth",
    "set_clear_stencil",  # noqa
    "set_blend_func",
    "set_blend_color",
    "set_blend_equation",  # noqa
    "set_scissor",
    "set_stencil_func",
    "set_stencil_mask",  # noqa
    "set_stencil_op",
    "set_depth_func",
    "set_depth_mask",  # noqa
    "set_color_mask",
    "set_sample_coverage",  # noqa
    "get_state_presets",
    "set_state",
    "finish",
    "flush",  # noqa
    "read_pixels",
    "set_hint",  # noqa
    "get_gl_configuration",
    "_check_valid",
    "GL_PRESETS",
    "GlooFunctions",
    "global_gloo_functions",
)

_setters: list = ...

# NOTE: If these are updated to have things beyond glEnable/glBlendFunc
# calls, set_state will need to be updated to deal with it.
#: Some OpenGL state presets for common use cases: 'opaque', 'translucent',
#: 'additive'.
#:
#: To be used in :func:`.set_state`.
GL_PRESETS: dict = ...

def get_current_canvas(): ...

# Helpers that are needed for efficient wrapping

def _check_valid(key, val, valid): ...
def _to_args(x): ...
def _check_conversion(key, valid_dict): ...

class BaseGlooFunctions(object):
    ##########################################################################
    # PRIMITIVE/VERTEX

    #
    # Viewport, DepthRangef, CullFace, FrontFace, LineWidth, PolygonOffset
    #

    def set_viewport(self, *args): ...
    def set_depth_range(self, near: float = 0.0, far: float = 1.0): ...
    def set_front_face(self, mode: str = "ccw"): ...
    def set_cull_face(self, mode: str = "back"): ...
    def set_line_width(self, width: float = 1.0): ...
    def set_polygon_offset(self, factor: float = 0.0, units: float = 0.0): ...

    ##########################################################################
    # FRAGMENT/SCREEN

    #
    # glClear, glClearColor, glClearDepthf, glClearStencil
    #

    def clear(self, color=True, depth: bool | float = True, stencil: bool | int = True): ...
    def set_clear_color(self, color="black", alpha: None | float = None): ...
    def set_clear_depth(self, depth: float = 1.0): ...
    def set_clear_stencil(self, index: int = 0): ...

    # glBlendFunc(Separate), glBlendColor, glBlendEquation(Separate)

    def set_blend_func(
        self,
        srgb: str = "one",
        drgb: str = "zero",
        salpha: str | None = None,
        dalpha: str | None = None,
    ): ...
    def set_blend_color(self, color): ...
    def set_blend_equation(self, mode_rgb: str, mode_alpha: str | None = None): ...

    # glScissor, glStencilFunc(Separate), glStencilMask(Separate),
    # glStencilOp(Separate),

    def set_scissor(self, x: int, y: int, w: int, h: int): ...
    def set_stencil_func(
        self,
        func: str = "always",
        ref: int = 0,
        mask: int = 8,
        face: str = "front_and_back",
    ): ...
    def set_stencil_mask(self, mask: int = 8, face: str = "front_and_back"): ...
    def set_stencil_op(
        self,
        sfail: str = "keep",
        dpfail: str = "keep",
        dppass: str = "keep",
        face: str = "front_and_back",
    ): ...

    # glDepthFunc, glDepthMask, glColorMask, glSampleCoverage

    def set_depth_func(self, func: str = "less"): ...
    def set_depth_mask(self, flag: bool): ...
    def set_color_mask(self, red: bool, green: bool, blue: bool, alpha: bool): ...
    def set_sample_coverage(self, value: float = 1.0, invert: bool = False): ...

    ##########################################################################
    # STATE

    #
    # glEnable/Disable
    #

    def get_state_presets(self) -> Mapping: ...
    def set_state(self, preset: Literal["opaque", "translucent", "additive"] | None = None, **kwargs): ...

    #
    # glFinish, glFlush, glReadPixels, glHint
    #

    def finish(self): ...
    def flush(self): ...
    def set_hint(self, target: str, mode: str): ...

class GlooFunctions(BaseGlooFunctions):
    @property
    def glir(self): ...

# Create global functions object and inject names here

# GlooFunctions without queue: use queue of canvas that is current at call-time
global_gloo_functions = ...

# Functions that do not use the glir queue

def read_pixels(
    viewport: ArrayLike | None = None,
    alpha: bool = True,
    mode: str = "color",
    out_type: str | np.dtype = "unsigned_byte",
) -> ArrayLike: ...
def get_gl_configuration() -> Mapping: ...
