from typing import Any, Callable, ClassVar, Literal, TypeVar
from ..multiclass import (
    OneVsRestClassifier as OneVsRestClassifier,
    OneVsOneClassifier as OneVsOneClassifier,
)
from numpy.random import RandomState
from scipy.special import erf, expit as expit
from operator import itemgetter as itemgetter
from ..preprocessing import LabelEncoder as LabelEncoder
from .kernels import Kernel, Product
from ..base import BaseEstimator
from numpy import ndarray
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from scipy.linalg import cholesky as cholesky, cho_solve as cho_solve, solve as solve
from numbers import Integral as Integral
from ..base import ClassifierMixin, clone as clone
from .kernels import RBF as RBF, CompoundKernel as CompoundKernel, ConstantKernel as C
from .._typing import Int, MatrixLike, ArrayLike, Float
from ..utils import check_random_state as check_random_state
from ..utils.validation import check_is_fitted as check_is_fitted

_BinaryGaussianProcessClassifierLaplace_Self = TypeVar(
    "_BinaryGaussianProcessClassifierLaplace_Self",
    bound="_BinaryGaussianProcessClassifierLaplace",
)
GaussianProcessClassifier_Self = TypeVar(
    "GaussianProcessClassifier_Self", bound="GaussianProcessClassifier"
)


import numpy as np
import scipy.optimize


# Values required for approximating the logistic sigmoid by
# error functions. coefs are obtained via:
# x = np.array([0, 0.6, 2, 3.5, 4.5, np.inf])
# b = logistic(x)
# A = (erf(np.dot(x, self.lambdas)) + 1) / 2
# coefs = lstsq(A, b)[0]
LAMBDAS = ...
COEFS = ...


class _BinaryGaussianProcessClassifierLaplace(BaseEstimator):
    log_marginal_likelihood_value_: float = ...
    W_sr_: ArrayLike = ...
    pi_: ArrayLike = ...
    L_: ArrayLike = ...
    kernel_: Kernel = ...
    classes_: ArrayLike = ...
    y_train_: ArrayLike = ...
    X_train_: ArrayLike | list[Any] = ...

    def __init__(
        self,
        kernel: Product | None | Kernel = None,
        *,
        optimizer: Literal["fmin_l_bfgs_b", "fmin_l_bfgs_b"]
        | Callable = "fmin_l_bfgs_b",
        n_restarts_optimizer: Int = 0,
        max_iter_predict: Int = 100,
        warm_start: bool = False,
        copy_X_train: bool = True,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def fit(
        self: _BinaryGaussianProcessClassifierLaplace_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
    ) -> _BinaryGaussianProcessClassifierLaplace_Self:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def log_marginal_likelihood(
        self,
        theta: None | ArrayLike = None,
        eval_gradient: bool = False,
        clone_kernel: bool = True,
    ) -> tuple[float, ndarray] | tuple[Float, ndarray] | Float:
        ...


class GaussianProcessClassifier(ClassifierMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_classes_: int = ...
    classes_: ArrayLike = ...
    log_marginal_likelihood_value_: float = ...
    base_estimator_: BaseEstimator = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        kernel: Product | None | Kernel = None,
        *,
        optimizer: Literal["fmin_l_bfgs_b", "fmin_l_bfgs_b"]
        | None
        | Callable = "fmin_l_bfgs_b",
        n_restarts_optimizer: Int = 0,
        max_iter_predict: Int = 100,
        warm_start: bool = False,
        copy_X_train: bool = True,
        random_state: RandomState | None | Int = None,
        multi_class: Literal[
            "one_vs_rest", "one_vs_one", "one_vs_rest"
        ] = "one_vs_rest",
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit(
        self: GaussianProcessClassifier_Self, X: MatrixLike | ArrayLike, y: ArrayLike
    ) -> GaussianProcessClassifier_Self:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    @property
    def kernel_(self) -> Product | Kernel:
        ...

    def log_marginal_likelihood(
        self,
        theta: None | ArrayLike = None,
        eval_gradient: bool = False,
        clone_kernel: bool = True,
    ) -> tuple[float, ndarray] | Float:
        ...
