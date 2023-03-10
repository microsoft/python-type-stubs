from typing import Literal
from ..utils.extmath import row_norms as row_norms
from numpy.random import RandomState
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from .._typing import Float, Int, ArrayLike, MatrixLike
from ._sag_fast import sag32 as sag32, sag64 as sag64
from ._base import make_dataset as make_dataset
from numpy import ndarray
from ..utils import check_array as check_array

# Authors: Tom Dupre la Tour <tom.dupre-la-tour@m4x.org>
#
# License: BSD 3 clause

import warnings

import numpy as np


def get_auto_step_size(
    max_squared_sum: Float,
    alpha_scaled: Float,
    loss: Literal["log", "squared", "multinomial"],
    fit_intercept: bool,
    n_samples: None | Int = None,
    is_saga: bool = False,
) -> Float:
    ...


def sag_solver(
    X: MatrixLike | ArrayLike,
    y: ArrayLike,
    sample_weight: None | ArrayLike = None,
    loss: Literal["log", "log", "squared", "multinomial"] = "log",
    alpha: Float = 1.0,
    beta: Float = 0.0,
    max_iter: Int = 1000,
    tol: Float = 0.001,
    verbose: Int = 0,
    random_state: RandomState | None | Int = None,
    check_input: bool = True,
    max_squared_sum: None | Float = None,
    warm_start_mem: dict[str, ndarray] | dict | None = None,
    is_saga: bool = False,
) -> tuple[ndarray, int, dict[str, ndarray | int]] | tuple[ndarray, int, dict]:
    ...
