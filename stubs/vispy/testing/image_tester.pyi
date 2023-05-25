from numpy.typing import NDArray

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

import time
import os
import sys
import inspect
import base64
from subprocess import check_call, CalledProcessError
import numpy as np
from typing import Literal

from http.client import HTTPConnection
from urllib.parse import urlencode

from .. import scene, config
from ..io import read_png, write_png
from ..gloo.util import _screenshot
from ..util import run_subprocess
from . import IS_CI

tester: None = ...

def _get_tester(): ...
def assert_image_approved(image: NDArray | Literal["screenshot"], standard_file: str, message: str | None = None, **kwargs): ...
def assert_image_match(
    im1: NDArray,
    im2: NDArray,
    min_corr: float | None = 0.9,
    px_threshold: float = 50.0,
    px_count: int | None = None,
    max_px_diff: float | None = None,
    avg_px_diff: float | None = None,
    img_diff: float | None = None,
): ...
def _save_failed_test(data, expect, filename): ...
def make_diff_image(im1, im2): ...
def downsample(data, n, axis=0): ...

class ImageTester(scene.SceneCanvas):
    def __init__(self): ...
    def test(self, im1, im2, message): ...
    def on_key_press(self, event): ...

def get_test_data_repo(): ...
def git_cmd_base(path): ...
def git_status(path): ...
def git_commit_id(path, ref): ...
