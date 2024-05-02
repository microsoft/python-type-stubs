import importlib
import importlib.util
import inspect
import os
import sys
import types
from typing import Mapping

__all__ = ["attach"]

def attach(module_name: str, submodules: set | None = None, submod_attrs: Mapping | None = None): ...

class DelayedImportErrorModule(types.ModuleType):
    def __init__(self, frame_data, *args, **kwargs): ...
    def __getattr__(self, x): ...
