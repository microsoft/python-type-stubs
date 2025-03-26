import weakref
from collections.abc import Mapping
from copy import deepcopy
from typing import Any

from ..util.event import Event
from .glir import BaseGlirParser, GlirParser, GlirQueue, glir_logger
from .wrappers import BaseGlooFunctions

# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

_default_dict = ...

canvasses: list = ...

def get_default_config() -> Mapping: ...
def get_current_canvas(): ...
def set_current_canvas(canvas): ...
def forget_canvas(canvas): ...

class GLContext(BaseGlooFunctions):
    def __init__(self, config: Mapping | None = None, shared: None | GLContext = None): ...
    def __repr__(self): ...
    def _set_config(self, config): ...
    def create_shared(self, name: str, ref: Any): ...
    @property
    def config(self): ...
    @property
    def glir(self): ...
    @property
    def shared(self): ...
    @property
    def capabilities(self): ...
    def flush_commands(self, event: Event | None = None): ...
    def set_viewport(self, *args): ...
    def get_viewport(self): ...

class GLShared:
    # We keep a (weak) ref of each backend that gets associated with
    # this object. In theory, this means that multiple canvases can
    # be created and also deleted; as long as there is at least one
    # left, things should Just Work.

    def __init__(self): ...
    def __repr__(self): ...
    @property
    def parser(self): ...
    @parser.setter
    def parser(self, parser): ...
    def add_ref(self, name, ref): ...
    @property
    def name(self): ...
    @property
    def ref(self): ...

class FakeCanvas:
    def __init__(self): ...
    def flush(self): ...
