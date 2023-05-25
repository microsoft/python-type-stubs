# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from .base_filter import Filter as Filter  # noqa
from .clipper import Clipper as Clipper  # noqa
from .color import (
    Alpha as Alpha,
    ColorFilter as ColorFilter,
    IsolineFilter as IsolineFilter,
    ZColormapFilter as ZColormapFilter,
)  # noqa
from .picking import PickingFilter as PickingFilter  # noqa
from .mesh import (
    TextureFilter as TextureFilter,
    ShadingFilter as ShadingFilter,
    WireframeFilter as WireframeFilter,
)  # noqa
