from typing import Literal, Sequence
from numpy import ndarray
from .._typing import Float, Int

# Authors: Jiyuan Qian <jq401@nyu.edu>
# License: BSD 3 clause

import numpy as np


class BaseOptimizer:
    def __init__(self, learning_rate_init: Float = 0.1) -> None:
        ...

    def update_params(
        self, params: Sequence | list[ndarray], grads: Sequence | list[ndarray]
    ) -> None:
        ...

    def iteration_ends(self, time_step: int) -> None:
        ...

    def trigger_stopping(self, msg: str, verbose: bool) -> bool:
        ...


class SGDOptimizer(BaseOptimizer):
    def __init__(
        self,
        params: Sequence | list[ndarray],
        learning_rate_init: Float = 0.1,
        lr_schedule: Literal[
            "constant", "constant", "adaptive", "invscaling"
        ] = "constant",
        momentum: Float = 0.9,
        nesterov: bool = True,
        power_t: Float = 0.5,
    ) -> None:
        ...

    def iteration_ends(self, time_step: Int) -> None:
        ...

    def trigger_stopping(self, msg: str, verbose: bool) -> bool:
        ...


class AdamOptimizer(BaseOptimizer):
    def __init__(
        self,
        params: Sequence | list[ndarray],
        learning_rate_init: Float = 0.001,
        beta_1: Float = 0.9,
        beta_2: Float = 0.999,
        epsilon: Float = 1e-8,
    ) -> None:
        ...
