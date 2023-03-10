from typing import Any, Callable, Literal
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from scipy.linalg import (
    cholesky as cholesky,
    cho_solve as cho_solve,
    solve_triangular as solve_triangular,
)
from numpy.random import RandomState
from .._typing import ArrayLike, Int, MatrixLike, Float
from ..base import BaseEstimator, RegressorMixin, clone as clone, MultiOutputMixin
from operator import itemgetter as itemgetter
from numpy import ndarray
from ..utils import check_random_state as check_random_state
from numbers import Integral as Integral, Real as Real
from .kernels import RBF as RBF, ConstantKernel as C
from .kernels import Kernel, Product, Sum

# Authors: Jan Hendrik Metzen <jhm@informatik.uni-bremen.de>
# Modified by: Pete Green <p.l.green@liverpool.ac.uk>
# License: BSD 3 clause

import warnings

import numpy as np
import scipy.optimize

GPR_CHOLESKY_LOWER: bool = ...


class GaussianProcessRegressor(MultiOutputMixin, RegressorMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        kernel: Product | None | Kernel | Sum = None,
        *,
        alpha: float | ArrayLike = 1e-10,
        optimizer: Literal["fmin_l_bfgs_b", "fmin_l_bfgs_b"]
        | None
        | Callable = "fmin_l_bfgs_b",
        n_restarts_optimizer: Int = 0,
        normalize_y: bool = False,
        copy_X_train: bool = True,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike | ArrayLike, y: MatrixLike | ArrayLike) -> Any:
        ...

    def predict(
        self,
        X: MatrixLike | ArrayLike,
        return_std: bool = False,
        return_cov: bool = False,
    ) -> tuple[ndarray, ndarray] | tuple[ndarray, ndarray, ndarray] | ndarray:
        ...

    def sample_y(
        self,
        X: MatrixLike | ArrayLike,
        n_samples: Int = 1,
        random_state: RandomState | None | Int = 0,
    ) -> ndarray:
        ...

    def log_marginal_likelihood(
        self,
        theta: None | ArrayLike = None,
        eval_gradient: bool = False,
        clone_kernel: bool = True,
    ) -> tuple[Float, ndarray] | Float | tuple[float, ndarray]:
        ...
