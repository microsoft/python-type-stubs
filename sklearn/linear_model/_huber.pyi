from typing import Any
from ..utils._param_validation import Interval as Interval
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from .._typing import Float, Int, MatrixLike, ArrayLike
from scipy import optimize as optimize
from ..base import BaseEstimator, RegressorMixin
from ._base import LinearModel
from ..utils import axis0_safe_slice as axis0_safe_slice
from numbers import Integral as Integral, Real as Real

# Authors: Manoj Kumar mks542@nyu.edu
# License: BSD 3 clause

import numpy as np


class HuberRegressor(LinearModel, RegressorMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        epsilon: Float = 1.35,
        max_iter: Int = 100,
        alpha: Float = 0.0001,
        warm_start: bool = False,
        fit_intercept: bool = True,
        tol: Float = 1e-05,
    ) -> None:
        ...

    def fit(
        self, X: MatrixLike, y: ArrayLike, sample_weight: None | ArrayLike = None
    ) -> Any:
        ...
