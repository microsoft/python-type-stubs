from numpy.typing import ArrayLike, NDArray

# -*- coding: utf-8 -*-
# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

import numpy as np

def stft(
    x: ArrayLike,
    n_fft: int = 1024,
    step: None | int = 512,
    fs: float = ...,
    window: str | None = "hann",
) -> NDArray: ...
def fft_freqs(n_fft: int, fs: float): ...
