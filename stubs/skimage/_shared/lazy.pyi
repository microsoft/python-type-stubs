from typing import Mapping
import importlib
import importlib.util
import os
import sys

def attach(
    package_name: str,
    submodules: set | None = None,
    submod_attrs: Mapping | None = None,
): ...
def load(fullname: str): ...
