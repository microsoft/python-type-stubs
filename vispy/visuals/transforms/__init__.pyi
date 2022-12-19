# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from .base_transform import BaseTransform as BaseTransform  # noqa
from .linear import (
    NullTransform as NullTransform,
    STTransform as STTransform,  # noqa
    MatrixTransform as MatrixTransform,
)  # noqa
from .nonlinear import (
    LogTransform as LogTransform,
    PolarTransform as PolarTransform,
)  # noqa
from .interactive import PanZoomTransform as PanZoomTransform
from .chain import ChainTransform as ChainTransform  # noqa
from ._util import (
    arg_to_array as arg_to_array,
    arg_to_vec4 as arg_to_vec4,
    as_vec4 as as_vec4,
    TransformCache as TransformCache,
)  # noqa
from .transform_system import TransformSystem as TransformSystem

__all__ = [
    "NullTransform",
    "STTransform",
    "MatrixTransform",
    "LogTransform",
    "PolarTransform",
    "ChainTransform",
    "TransformSystem",
    "PanZoomTransform",
]

transform_types: dict = ...

def create_transform(type, *args, **kwargs): ...
