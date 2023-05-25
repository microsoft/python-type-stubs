from numpy.typing import ArrayLike

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

import subprocess

def use(app: str | None = None, gl: str | None = None): ...
def run_subprocess(command: ArrayLike, return_code: bool = False, **kwargs) -> tuple[str, str, int]: ...
def test(*args, **kwargs): ...
