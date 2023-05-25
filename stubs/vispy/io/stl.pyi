from typing import IO
from vispy._typing import FileLike

# -*- coding: utf-8 -*-
# Copyright (c) 2015 Michael Dawson-Haggerty
# Distributed under the MIT License.
# Copied from the trimesh project.
# See https://github.com/mikedh/trimesh for more information.
# See https://github.com/mikedh/trimesh/blob/master/LICENSE.md for
# the license.

import numpy as np

class HeaderError(Exception):
    pass

# define a numpy datatype for the data section of a binary STL file
_stl_dtype = ...
# define a numpy datatype for the header of a binary STL file
_stl_dtype_header = ...

def load_stl(file_obj: FileLike, file_type=None): ...
def load_stl_binary(file_obj: FileLike): ...
def load_stl_ascii(file_obj: FileLike): ...

_stl_loaders: dict = ...
