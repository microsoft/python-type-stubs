from typing import List, Union, Literal
from numpy.typing import ArrayLike

# Authors: Jiyuan Qian <jq401@nyu.edu>
# License: BSD 3 clause

import numpy as np
from numpy import ndarray

class BaseOptimizer:
    def __init__(self, learning_rate_init: float = 0.1) -> None: ...
    def update_params(self, params: list, grads: list) -> None: ...
    def iteration_ends(self, time_step: int) -> None: ...
    def trigger_stopping(self, msg: str, verbose: bool) -> bool: ...

class SGDOptimizer(BaseOptimizer):
    def __init__(
        self,
        params: list,
        learning_rate_init: float = 0.1,
        lr_schedule: Literal["constant", "adaptive", "invscaling"] = "constant",
        momentum: float = 0.9,
        nesterov: bool = True,
        power_t: float = 0.5,
    ) -> None: ...
    def iteration_ends(self, time_step: int) -> None: ...
    def trigger_stopping(self, msg: str, verbose: bool) -> bool: ...
    def _get_updates(self, grads: List[ndarray]) -> List[ndarray]: ...

class AdamOptimizer(BaseOptimizer):
    def __init__(
        self,
        params: list,
        learning_rate_init: float = 0.001,
        beta_1: float = 0.9,
        beta_2: float = 0.999,
        epsilon: float = 1e-8,
    ) -> None: ...
    def _get_updates(self, grads: List[ndarray]) -> List[ndarray]: ...
