# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from ._color_dict import (
    get_color_names as get_color_names,
    get_color_dict as get_color_dict,
)  # noqa
from .color_array import Color as Color, ColorArray as ColorArray
from .colormap import (
    Colormap as Colormap,
    BaseColormap as BaseColormap,  # noqa
    get_colormap as get_colormap,
    get_colormaps as get_colormaps,
)  # noqa

__all__ = [
    "Color",
    "ColorArray",
    "Colormap",
    "BaseColormap",
    "get_colormap",
    "get_colormaps",
    "get_color_names",
    "get_color_dict",
]
