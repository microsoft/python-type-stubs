from numpy import float64, ndarray
from sklearn.gaussian_process.kernels import Product, Sum, Kernel
from typing import Optional, Tuple, Union, Callable, Literal, Any, Sequence
from numpy.typing import NDArray, ArrayLike

# Authors: Jan Hendrik Metzen <jhm@informatik.uni-bremen.de>
# Modified by: Pete Green <p.l.green@liverpool.ac.uk>
# License: BSD 3 clause

import warnings
from operator import itemgetter

import numpy as np
from numpy.random import RandomState
from scipy.linalg import cholesky, cho_solve, solve_triangular
import scipy.optimize

from ..base import BaseEstimator, RegressorMixin, clone
from ..base import MultiOutputMixin
from .kernels import RBF, ConstantKernel as C
from ..preprocessing._data import _handle_zeros_in_scale
from ..utils import check_random_state
from ..utils.optimize import _check_optimize_result

GPR_CHOLESKY_LOWER: bool = ...

class GaussianProcessRegressor(MultiOutputMixin, RegressorMixin, BaseEstimator):
    def __init__(
        self,
        kernel: Kernel | None = None,
        *,
        alpha: float | NDArray = 1e-10,
        optimizer: Callable | Literal["fmin_l_bfgs_b"] = "fmin_l_bfgs_b",
        n_restarts_optimizer: int = 0,
        normalize_y: bool = False,
        copy_X_train: bool = True,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def fit(self, X: ArrayLike | Sequence[Any], y: ArrayLike) -> "GaussianProcessRegressor": ...
    def predict(
        self,
        X: ArrayLike | Sequence[Any],
        return_std: bool = False,
        return_cov: bool = False,
    ) -> tuple[NDArray, NDArray, np.ndarray]: ...
    def sample_y(
        self,
        X: ArrayLike | Sequence[Any],
        n_samples: int = 1,
        random_state: int | RandomState | None = 0,
    ) -> NDArray | tuple[int, int, int]: ...
    def log_marginal_likelihood(
        self,
        theta: ArrayLike | None = None,
        eval_gradient: bool = False,
        clone_kernel: bool = True,
    ) -> tuple[float, np.ndarray]: ...
    def _constrained_optimization(
        self, obj_func: Callable, initial_theta: ndarray, bounds: ndarray
    ) -> Tuple[ndarray, float64]: ...
    def _more_tags(self): ...
