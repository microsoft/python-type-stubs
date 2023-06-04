from .._typing import Scalar
from numpy.typing import NDArray, ArrayLike
from typing import Sequence

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

import warnings

import numpy as np

from .color_array import ColorArray
from ..ext.cubehelix import cubehelix
from ..util.check_environment import has_matplotlib
import vispy.gloo

###############################################################################
# Color maps

# Length of the texture map used for luminance to RGBA conversion
LUT_len: int = ...

# Utility functions for interpolation in NumPy.
def _vector_or_scalar(x, type="row"): ...
def _vector(x, type="row"): ...
def _find_controls(x, controls=None, clip=None): ...

# Normalization
def _normalize(x, cmin=None, cmax=None, clip=True): ...

# Interpolation functions in NumPy.
def _mix_simple(a, b, x): ...
def _interpolate_multi(colors, x, controls): ...
def mix(colors, x, controls=None): ...
def smoothstep(edge0, edge1, x): ...
def step(colors, x, controls=None): ...

# GLSL interpolation functions.
def _glsl_mix(controls=None, colors=None, texture_map_data=None): ...
def _glsl_step(controls=None, colors=None, texture_map_data=None): ...

# Mini GLSL template system for colors.
def _process_glsl_template(template, colors): ...

class BaseColormap(object):

    # Control colors used by the colormap.
    colors: None = ...

    # GLSL string with a function implementing the color map.
    glsl_map: None = ...

    # Texture map data used by the 'colormap' GLSL function
    # for luminance to RGBA conversion.
    texture_map_data: None = ...

    def __init__(self, colors: Sequence[ArrayLike | tuple | NDArray] | None = None): ...
    def map(self, item: NDArray) -> NDArray: ...
    def texture_lut(self): ...
    def __getitem__(self, item): ...
    def __setitem__(self, item, value): ...
    def _repr_html_(self): ...

def _default_controls(ncolors): ...

# List the parameters of every supported interpolation mode.
_interpolation_info: dict = ...

class Colormap(BaseColormap):
    def __init__(
        self,
        colors: ArrayLike,
        controls: ArrayLike | None = None,
        interpolation: str = "linear",
    ): ...
    @property
    def interpolation(self): ...
    @interpolation.setter
    def interpolation(self, val): ...
    def map(self, x: ArrayLike) -> ArrayLike: ...
    def texture_lut(self): ...

class MatplotlibColormap(Colormap):
    def __init__(self, name: str): ...

class CubeHelixColormap(Colormap):
    def __init__(
        self,
        start: Scalar = 0.5,
        rot: Scalar = 1,
        gamma: Scalar = 1.0,
        reverse: bool = True,
        nlev: Scalar = 32,
        minSat: Scalar = 1.2,
        maxSat: Scalar = 1.2,
        minLight: Scalar = 0.0,
        maxLight: Scalar = 1.0,
        **kwargs,
    ): ...

class _Fire(BaseColormap):
    colors: list = ...

    glsl_map: str = ...

    def map(self, t) -> NDArray: ...

class _Grays(BaseColormap):
    glsl_map: str = ...

    def map(self, t) -> NDArray: ...

class _Ice(BaseColormap):
    glsl_map: str = ...

    def map(self, t) -> NDArray: ...

class _Hot(BaseColormap):
    colors: list = ...

    glsl_map: str = ...

    def map(self, t) -> NDArray: ...

class _Winter(BaseColormap):
    colors: list = ...

    glsl_map: str = ...

    def map(self, t) -> NDArray: ...

class SingleHue(Colormap):
    def __init__(
        self,
        hue: Scalar = 200,
        saturation_range: ArrayLike = [0.1, 0.8],
        value: Scalar = 1.0,
    ): ...

class HSL(Colormap):
    def __init__(
        self,
        ncolors=6,
        hue_start: int = 0,
        saturation: float = 1.0,
        value: float = 1.0,
        controls: ArrayLike | None = None,
        interpolation: str = "linear",
    ): ...

class HSLuv(Colormap):
    def __init__(
        self,
        ncolors=6,
        hue_start: int = 0,
        saturation: float = 1.0,
        value: float = 0.7,
        controls: ArrayLike | None = None,
        interpolation: str = "linear",
    ): ...

class _HUSL(HSLuv):
    def __init__(self, *args, **kwargs): ...

class Diverging(Colormap):
    def __init__(self, h_pos=20, h_neg=250, saturation=1.0, value=0.7, center="light"): ...

class RedYellowBlueCyan(Colormap):
    def __init__(self, limits: ArrayLike = ...): ...

# https://github.com/matplotlib/matplotlib/pull/4707/files#diff-893cf0348279e9f4570488a7a297ab1eR774  # noqa
# Taken from original Viridis colormap data in matplotlib implementation
#
# Issue #1331 https://github.com/vispy/vispy/issues/1331 explains that the
# 128 viridis sample size fails on some GPUs
# but lowering to 64 samples allows more GPUs to use viridis.
#
# VisPy has beem updated to use a texture map lookup.
# Thus, sampling of the Viridis colormap data is no longer necessary.
_viridis_data: list = ...

_colormaps = ...

def get_colormap(name: str | Colormap, *args, **kwargs): ...
def get_colormaps(): ...
