from numpy import float64, ndarray
from sklearn.gaussian_process.kernels import CompoundKernel, Product, Kernel
from typing import List, Optional, Tuple, Union, Callable, Literal, Any, Sequence
from numpy.typing import ArrayLike, NDArray

# Authors: Jan Hendrik Metzen <jhm@informatik.uni-bremen.de>
#
# License: BSD 3 clause

from operator import itemgetter

import numpy as np
from numpy.random import RandomState
from scipy.linalg import cholesky, cho_solve, solve
import scipy.optimize
from scipy.special import erf, expit

from ..base import BaseEstimator, ClassifierMixin, clone
from .kernels import RBF, CompoundKernel, ConstantKernel as C
from ..utils.validation import check_is_fitted
from ..utils import check_random_state
from ..utils.optimize import _check_optimize_result
from ..preprocessing import LabelEncoder
from ..multiclass import OneVsRestClassifier, OneVsOneClassifier

# Values required for approximating the logistic sigmoid by
# error functions. coefs are obtained via:
# x = np.array([0, 0.6, 2, 3.5, 4.5, np.inf])
# b = logistic(x)
# A = (erf(np.dot(x, self.lambdas)) + 1) / 2
# coefs = lstsq(A, b)[0]
LAMBDAS = ...
COEFS = ...

class _BinaryGaussianProcessClassifierLaplace(BaseEstimator):
    def __init__(
        self,
        kernel: Kernel | None = None,
        *,
        optimizer: Callable | Literal["fmin_l_bfgs_b"] = "fmin_l_bfgs_b",
        n_restarts_optimizer: int = 0,
        max_iter_predict: int = 100,
        warm_start: bool = False,
        copy_X_train: bool = True,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def fit(self, X: ArrayLike | Sequence[Any], y: ArrayLike) -> "_BinaryGaussianProcessClassifierLaplace": ...
    def predict(self, X: ArrayLike | Sequence[Any]) -> NDArray: ...
    def predict_proba(self, X: ArrayLike | Sequence[Any]) -> ArrayLike: ...
    def log_marginal_likelihood(
        self,
        theta: ArrayLike | None = None,
        eval_gradient: bool = False,
        clone_kernel: bool = True,
    ) -> tuple[float, np.ndarray]: ...
    def _posterior_mode(
        self, K: ndarray, return_temporaries: bool = False
    ) -> Tuple[float64, Tuple[ndarray, ndarray, ndarray, ndarray, ndarray]]: ...
    def _constrained_optimization(
        self, obj_func: Callable, initial_theta: ndarray, bounds: ndarray
    ) -> Tuple[ndarray, float64]: ...

class GaussianProcessClassifier(ClassifierMixin, BaseEstimator):
    def __init__(
        self,
        kernel: Kernel | None = None,
        *,
        optimizer: Callable | Literal["fmin_l_bfgs_b"] = "fmin_l_bfgs_b",
        n_restarts_optimizer: int = 0,
        max_iter_predict: int = 100,
        warm_start: bool = False,
        copy_X_train: bool = True,
        random_state: int | RandomState | None = None,
        multi_class: Literal["one_vs_rest", "one_vs_one"] = "one_vs_rest",
        n_jobs: int | None = None,
    ) -> None: ...
    def fit(self, X: ArrayLike | Sequence[Any], y: ArrayLike) -> "GaussianProcessClassifier": ...
    def predict(self, X: ArrayLike | Sequence[Any]) -> NDArray: ...
    def predict_proba(self, X: ArrayLike | Sequence[Any]) -> ArrayLike: ...
    @property
    def kernel_(self) -> Union[CompoundKernel, Product]: ...
    def log_marginal_likelihood(
        self,
        theta: ArrayLike | None = None,
        eval_gradient: bool = False,
        clone_kernel: bool = True,
    ) -> tuple[float, np.ndarray]: ...
