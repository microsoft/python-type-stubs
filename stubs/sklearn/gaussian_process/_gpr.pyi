from numbers import Integral as Integral, Real as Real
from operator import itemgetter as itemgetter
from typing import Any, Callable, ClassVar, Literal, TypeVar

from numpy import ndarray
from numpy.random import RandomState
from scipy.linalg import cho_solve as cho_solve, cholesky as cholesky, solve_triangular as solve_triangular

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, MultiOutputMixin, RegressorMixin, clone as clone
from ..utils import check_random_state as check_random_state
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from .kernels import RBF as RBF, ConstantKernel as C, Kernel

GaussianProcessRegressor_Self = TypeVar("GaussianProcessRegressor_Self", bound="GaussianProcessRegressor")

# Authors: Jan Hendrik Metzen <jhm@informatik.uni-bremen.de>
# Modified by: Pete Green <p.l.green@liverpool.ac.uk>
# License: BSD 3 clause

import warnings

import numpy as np
import scipy.optimize

GPR_CHOLESKY_LOWER: bool = ...

class GaussianProcessRegressor(MultiOutputMixin, RegressorMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    log_marginal_likelihood_value_: float = ...
    alpha_: ArrayLike = ...
    L_: ArrayLike = ...
    kernel_: Kernel = ...
    y_train_: ArrayLike = ...
    X_train_: ArrayLike | list[Any] = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        kernel: None | Kernel = None,
        *,
        alpha: float | ArrayLike = 1e-10,
        optimizer: Literal["fmin_l_bfgs_b", "fmin_l_bfgs_b"] | None | Callable = "fmin_l_bfgs_b",
        n_restarts_optimizer: Int = 0,
        normalize_y: bool = False,
        copy_X_train: bool = True,
        n_targets: Int | None = None,
        random_state: RandomState | None | Int = None,
    ) -> None: ...
    def fit(
        self: GaussianProcessRegressor_Self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike | ArrayLike,
    ) -> GaussianProcessRegressor_Self: ...
    def predict(
        self,
        X: MatrixLike | ArrayLike,
        return_std: bool = False,
        return_cov: bool = False,
    ) -> ndarray | tuple[ndarray, ndarray, ndarray] | tuple[ndarray, ndarray]: ...
    def sample_y(
        self,
        X: MatrixLike | ArrayLike,
        n_samples: Int = 1,
        random_state: RandomState | None | Int = 0,
    ) -> ndarray: ...
    def log_marginal_likelihood(
        self,
        theta: None | ArrayLike = None,
        eval_gradient: bool = False,
        clone_kernel: bool = True,
    ) -> tuple[float, ndarray] | tuple[Float, ndarray] | Float: ...
