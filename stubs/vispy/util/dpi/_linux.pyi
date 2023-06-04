# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

import os
import re
from subprocess import CalledProcessError

from ..logs import logger
from ..wrappers import run_subprocess

def _get_dpi_from(cmd, pattern, func): ...
def _xrandr_calc(x_px, y_px, x_mm, y_mm): ...
def get_dpi(raise_error: bool = True) -> float: ...
