from typing import Any, Literal
from .._typing import Float, MatrixLike, ArrayLike, Int
from ..preprocessing import LabelBinarizer as LabelBinarizer
from ..utils._param_validation import (
    StrOptions as StrOptions,
    Options as Options,
    Interval as Interval,
)
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from ..model_selection import train_test_split as train_test_split
from abc import ABCMeta, abstractmethod
from ._base import (
    ACTIVATIONS as ACTIVATIONS,
    DERIVATIVES as DERIVATIVES,
    LOSS_FUNCTIONS as LOSS_FUNCTIONS,
)
from ._stochastic_optimizers import (
    SGDOptimizer as SGDOptimizer,
    AdamOptimizer as AdamOptimizer,
)
from itertools import chain as chain
from ..utils import (
    gen_batches as gen_batches,
    check_random_state as check_random_state,
    shuffle,
    column_or_1d as column_or_1d,
)
from ..metrics import accuracy_score as accuracy_score, r2_score as r2_score
from ..utils.validation import check_is_fitted as check_is_fitted
from numpy import ndarray
from numpy.random import RandomState
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils.multiclass import (
    unique_labels as unique_labels,
    type_of_target as type_of_target,
)
from ..base import (
    BaseEstimator,
    ClassifierMixin,
    RegressorMixin,
    is_classifier as is_classifier,
)
from numbers import Integral as Integral, Real as Real
from ..utils.metaestimators import available_if as available_if
import numpy as np
import warnings

import scipy.optimize


_STOCHASTIC_SOLVERS: list = ...


class BaseMultilayerPerceptron(BaseEstimator, metaclass=ABCMeta):

    _parameter_constraints: dict = ...

    @abstractmethod
    def __init__(
        self,
        hidden_layer_sizes: tuple[int, int] | list[int] | tuple[int],
        activation: str,
        solver: str,
        alpha: Float,
        batch_size: str,
        learning_rate: str,
        learning_rate_init: float,
        power_t: float,
        max_iter: int,
        loss: str,
        shuffle: bool,
        random_state: int | None,
        tol: float,
        verbose: int | bool,
        warm_start: bool,
        momentum: int | float,
        nesterovs_momentum: bool,
        early_stopping: bool,
        validation_fraction: float,
        beta_1: float,
        beta_2: float,
        epsilon: float,
        n_iter_no_change: int,
        max_fun: int,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: MatrixLike | ArrayLike) -> Any:
        ...


class MLPClassifier(ClassifierMixin, BaseMultilayerPerceptron):
    def __init__(
        self,
        hidden_layer_sizes: ArrayLike | tuple[int] = ...,
        activation: Literal["relu", "identity", "logistic", "tanh", "relu"] = "relu",
        *,
        solver: Literal["lbfgs", "sgd", "adam", "adam"] = "adam",
        alpha: Float = 0.0001,
        batch_size: str | Int = "auto",
        learning_rate: Literal[
            "constant", "invscaling", "adaptive", "constant"
        ] = "constant",
        learning_rate_init: Float = 0.001,
        power_t: Float = 0.5,
        max_iter: Int = 200,
        shuffle: bool = True,
        random_state: RandomState | None | Int = None,
        tol: Float = 1e-4,
        verbose: bool = False,
        warm_start: bool = False,
        momentum: Float = 0.9,
        nesterovs_momentum: bool = True,
        early_stopping: bool = False,
        validation_fraction: Float = 0.1,
        beta_1: Float = 0.9,
        beta_2: Float = 0.999,
        epsilon: Float = 1e-8,
        n_iter_no_change: Int = 10,
        max_fun: Int = 15000,
    ) -> None:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def partial_fit(
        self, X: MatrixLike | ArrayLike, y: ArrayLike, classes: None | ArrayLike = None
    ) -> Any:
        ...

    def predict_log_proba(self, X: ArrayLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...


class MLPRegressor(RegressorMixin, BaseMultilayerPerceptron):
    def __init__(
        self,
        hidden_layer_sizes: tuple[int, int] | ArrayLike = ...,
        activation: Literal["relu", "identity", "logistic", "tanh", "relu"] = "relu",
        *,
        solver: Literal["lbfgs", "sgd", "adam", "adam"] = "adam",
        alpha: Float = 0.0001,
        batch_size: str | Int = "auto",
        learning_rate: Literal[
            "constant", "invscaling", "adaptive", "constant"
        ] = "constant",
        learning_rate_init: Float = 0.001,
        power_t: Float = 0.5,
        max_iter: Int = 200,
        shuffle: bool = True,
        random_state: RandomState | None | Int = None,
        tol: Float = 1e-4,
        verbose: bool = False,
        warm_start: bool = False,
        momentum: Float = 0.9,
        nesterovs_momentum: bool = True,
        early_stopping: bool = False,
        validation_fraction: Float = 0.1,
        beta_1: Float = 0.9,
        beta_2: Float = 0.999,
        epsilon: Float = 1e-8,
        n_iter_no_change: Int = 10,
        max_fun: Int = 15000,
    ) -> None:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def partial_fit(self, X: MatrixLike | ArrayLike, y: ArrayLike) -> Any:
        ...
