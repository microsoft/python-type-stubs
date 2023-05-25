from typing import Callable, Literal

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

from ..shaders import Function

class BaseFilter(object):
    def _attach(self, visual): ...
    def _detach(self, visual): ...

class Filter(BaseFilter):
    def __init__(
        self,
        vcode: None | str | Callable = None,
        vhook: Literal["pre", "post"] = "post",
        vpos: int = 5,
        fcode: None | str | Callable = None,
        fhook: Literal["pre", "post"] = "post",
        fpos: int = 5,
    ): ...
    @property
    def attached(self): ...
    def _attach(self, visual): ...
    def _detach(self, visual): ...
