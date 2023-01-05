from numpy import float64, ndarray
from typing import List, Optional, Tuple, Union, Any, Literal
from numpy.typing import NDArray, ArrayLike
from numpy.random import RandomState

# Authors: Issam H. Laradji <issam.laradji@gmail.com>
#          Andreas Mueller
#          Jiyuan Qian
# License: BSD 3 clause

import numpy as np

from abc import ABCMeta, abstractmethod
import warnings
from itertools import chain

import scipy.optimize

from ..base import (
    BaseEstimator,
    ClassifierMixin,
    RegressorMixin,
)
from ..base import is_classifier
from ._base import ACTIVATIONS, DERIVATIVES, LOSS_FUNCTIONS
from ._stochastic_optimizers import SGDOptimizer, AdamOptimizer
from ..model_selection import train_test_split
from ..preprocessing import LabelBinarizer
from ..utils import gen_batches, check_random_state
from ..utils import shuffle
from ..utils import _safe_indexing
from ..utils import column_or_1d
from ..exceptions import ConvergenceWarning
from ..utils.extmath import safe_sparse_dot
from ..utils.validation import check_is_fitted
from ..utils.multiclass import _check_partial_fit_first_call, unique_labels
from ..utils.multiclass import type_of_target
from ..utils.optimize import _check_optimize_result
from ..utils.metaestimators import available_if

_STOCHASTIC_SOLVERS: list = ...

def _pack(coefs_: List[ndarray], intercepts_: List[ndarray]) -> ndarray: ...

class BaseMultilayerPerceptron(BaseEstimator, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        hidden_layer_sizes: Union[List[int], Tuple[int], Tuple[int, int]],
        activation: str,
        solver: str,
        alpha: Union[int, float, float64],
        batch_size: str,
        learning_rate: str,
        learning_rate_init: float,
        power_t: float,
        max_iter: int,
        loss: str,
        shuffle: bool,
        random_state: Optional[int],
        tol: float,
        verbose: bool,
        warm_start: bool,
        momentum: Union[int, float],
        nesterovs_momentum: bool,
        early_stopping: bool,
        validation_fraction: float,
        beta_1: float,
        beta_2: float,
        epsilon: float,
        n_iter_no_change: int,
        max_fun: int,
    ) -> None: ...
    def _unpack(self, packed_parameters: ndarray) -> None: ...
    def _forward_pass(self, activations: List[Optional[ndarray]]) -> List[ndarray]: ...
    def _forward_pass_fast(self, X: ndarray) -> ndarray: ...
    def _compute_loss_grad(
        self,
        layer: int,
        n_samples: int,
        activations: List[ndarray],
        deltas: List[Optional[ndarray]],
        coef_grads: List[ndarray],
        intercept_grads: List[ndarray],
    ) -> None: ...
    def _loss_grad_lbfgs(
        self,
        packed_coef_inter: ndarray,
        X: ndarray,
        y: ndarray,
        activations: List[Optional[ndarray]],
        deltas: List[Optional[ndarray]],
        coef_grads: List[ndarray],
        intercept_grads: List[ndarray],
    ) -> Tuple[float64, ndarray]: ...
    def _backprop(
        self,
        X: ndarray,
        y: ndarray,
        activations: List[Optional[ndarray]],
        deltas: List[Optional[ndarray]],
        coef_grads: List[ndarray],
        intercept_grads: List[ndarray],
    ) -> Tuple[float64, List[ndarray], List[ndarray]]: ...
    def _initialize(self, y, layer_units, dtype): ...
    def _init_coef(self, fan_in, fan_out, dtype): ...
    def _fit(self, X: ndarray, y: ndarray, incremental: bool = False) -> Union[MLPRegressor, MLPClassifier]: ...
    def _validate_hyperparameters(self) -> None: ...
    def _fit_lbfgs(
        self,
        X: ndarray,
        y: ndarray,
        activations: List[Optional[ndarray]],
        deltas: List[None],
        coef_grads: List[ndarray],
        intercept_grads: List[ndarray],
        layer_units: List[int],
    ) -> None: ...
    def _fit_stochastic(
        self,
        X: ndarray,
        y: ndarray,
        activations: List[Optional[ndarray]],
        deltas: List[None],
        coef_grads: List[ndarray],
        intercept_grads: List[ndarray],
        layer_units: List[int],
        incremental: bool,
    ) -> None: ...
    def _update_no_improvement_count(self, early_stopping: bool, X_val: None, y_val: None) -> None: ...
    def fit(self, X: NDArray, y: NDArray) -> Union[MLPRegressor, MLPClassifier]: ...
    def _check_solver(self): ...
    @available_if(_check_solver)
    def partial_fit(self, X: NDArray | ArrayLike, y: NDArray) -> Any: ...

class MLPClassifier(ClassifierMixin, BaseMultilayerPerceptron):
    def __init__(
        self,
        hidden_layer_sizes: tuple = ...,
        activation: Literal["identity", "logistic", "tanh", "relu"] = "relu",
        *,
        solver: Literal["lbfgs", "sgd", "adam"] = "adam",
        alpha: float = 0.0001,
        batch_size: int | str = "auto",
        learning_rate: Literal["constant", "invscaling", "adaptive"] = "constant",
        learning_rate_init: float = 0.001,
        power_t: float = 0.5,
        max_iter: int = 200,
        shuffle: bool = True,
        random_state: int | RandomState | None = None,
        tol: float = 1e-4,
        verbose: bool = False,
        warm_start: bool = False,
        momentum: float = 0.9,
        nesterovs_momentum: bool = True,
        early_stopping: bool = False,
        validation_fraction: float = 0.1,
        beta_1: float = 0.9,
        beta_2: float = 0.999,
        epsilon: float = 1e-8,
        n_iter_no_change: int = 10,
        max_fun: int = 15000,
    ) -> None: ...
    def _validate_input(self, X: ndarray, y: ndarray, incremental: bool, reset: bool) -> Tuple[ndarray, ndarray]: ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    @available_if(lambda est: est._check_solver())
    def partial_fit(self, X: NDArray | ArrayLike, y: ArrayLike, classes: ArrayLike | None = None) -> Any: ...
    def predict_log_proba(self, X: NDArray) -> np.ndarray: ...
    def predict_proba(self, X: NDArray | ArrayLike) -> np.ndarray: ...
    def _more_tags(self): ...

class MLPRegressor(RegressorMixin, BaseMultilayerPerceptron):
    def __init__(
        self,
        hidden_layer_sizes: tuple = ...,
        activation: Literal["identity", "logistic", "tanh", "relu"] = "relu",
        *,
        solver: Literal["lbfgs", "sgd", "adam"] = "adam",
        alpha: float = 0.0001,
        batch_size: int | str = "auto",
        learning_rate: Literal["constant", "invscaling", "adaptive"] = "constant",
        learning_rate_init: float = 0.001,
        power_t: float = 0.5,
        max_iter: int = 200,
        shuffle: bool = True,
        random_state: int | RandomState | None = None,
        tol: float = 1e-4,
        verbose: bool = False,
        warm_start: bool = False,
        momentum: float = 0.9,
        nesterovs_momentum: bool = True,
        early_stopping: bool = False,
        validation_fraction: float = 0.1,
        beta_1: float = 0.9,
        beta_2: float = 0.999,
        epsilon: float = 1e-8,
        n_iter_no_change: int = 10,
        max_fun: int = 15000,
    ) -> None: ...
    def predict(self, X: NDArray | ArrayLike) -> np.ndarray: ...
    def _validate_input(self, X: ndarray, y: ndarray, incremental: bool, reset: bool) -> Tuple[ndarray, ndarray]: ...
