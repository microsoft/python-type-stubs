# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# Adapted from PyQtGraph
import sys

from .. import config
from . import ptime

class Profiler:
    _profilers = ...

    _depth: int = ...
    _msgs: list = ...
    # set this flag to disable all or individual profilers at runtime
    disable: bool = ...

    _disabled_profiler = ...

    def __new__(cls, msg=None, disabled="env", delayed=True): ...
    def __call__(self, msg=None, *args): ...
    def mark(self, msg=None): ...
    def _new_msg(self, msg, *args): ...
    def __del__(self): ...
    def finish(self, msg=None): ...
    def flush(self): ...
