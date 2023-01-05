# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
import os
from distutils.version import LooseVersion

from vispy.util import use_log_level

def has_matplotlib(version="1.2"): ...
def has_skimage(version="0.11"): ...
def has_backend(backend, has=..., capable=..., out=...): ...
