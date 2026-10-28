# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from .datasets import (
    load_crate,
    load_data_file,
    load_iris,
    load_spatial_filters,
)
from .image import (
    imread,
    imsave,
    read_png,
    write_png,
)
from .mesh import read_mesh, write_mesh

_data_dir = ...

__all__ = [
    "imread",
    "imsave",
    "load_iris",
    "load_crate",
    "load_spatial_filters",
    "load_data_file",
    "read_mesh",
    "read_png",
    "write_mesh",
    "write_png",
]
