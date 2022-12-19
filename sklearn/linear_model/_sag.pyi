from typing import Literal, Mapping
from numpy.typing import ArrayLike, NDArray

# Authors: Tom Dupre la Tour <tom.dupre-la-tour@m4x.org>
#
# License: BSD 3 clause

import warnings

import numpy as np
from numpy.random import RandomState

from ._base import make_dataset
from ..exceptions import ConvergenceWarning
from ..utils import check_array
from ..utils.validation import _check_sample_weight
from ..utils.extmath import row_norms

def get_auto_step_size(
    max_squared_sum: float,
    alpha_scaled: float,
    loss: Literal["log", "squared", "multinomial"],
    fit_intercept: bool,
    n_samples: int | None = None,
    is_saga: bool = False,
) -> float: ...
def sag_solver(
    X: NDArray | ArrayLike,
    y: NDArray,
    sample_weight: ArrayLike | None = None,
    loss: Literal["log", "squared", "multinomial"] = "log",
    alpha: float = 1.0,
    beta: float = 0.0,
    max_iter: int = 1000,
    tol: float = 0.001,
    verbose: int = 0,
    random_state: int | RandomState | None = None,
    check_input: bool = True,
    max_squared_sum: float | None = None,
    warm_start_mem: Mapping | None = None,
    is_saga: bool = False,
) -> tuple[NDArray, int, Mapping]: ...
