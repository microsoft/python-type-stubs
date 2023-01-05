from numpy import float64, int64, ndarray
from typing import Dict, List, Optional, Tuple, Union, Any, Literal
from numpy.typing import ArrayLike, NDArray
from numpy.random import RandomState

# Authors: Peter Prettenhofer <peter.prettenhofer@gmail.com> (main author)
#          Mathieu Blondel (partial_fit support)
#
# License: BSD 3 clause

import numpy as np
import warnings

from abc import ABCMeta, abstractmethod

from ..base import clone, is_classifier
from ._base import LinearClassifierMixin, SparseCoefMixin
from ._base import make_dataset
from ..base import BaseEstimator, RegressorMixin, OutlierMixin
from ..utils import check_random_state
from ..utils.metaestimators import available_if
from ..utils.extmath import safe_sparse_dot
from ..utils.multiclass import _check_partial_fit_first_call
from ..utils.validation import check_is_fitted, _check_sample_weight
from ..utils.fixes import delayed
from ..exceptions import ConvergenceWarning
from ..model_selection import StratifiedShuffleSplit, ShuffleSplit

from ..utils import compute_class_weight

from scipy.sparse._csr import csr_matrix
from sklearn.linear_model._passive_aggressive import PassiveAggressiveClassifier
from sklearn.linear_model._perceptron import Perceptron

class LossFunction:
    def loss(self, p: float, y: float) -> float: ...
    def dloss(self, p: float, y: float) -> float: ...

class Regression(LossFunction): ...
class Classification(LossFunction): ...
class Log(Classification): ...
class SquaredLoss(Regression): ...
class ModifiedHuber(Classification): ...
class Hinge(Classification): ...
class SquaredHinge(Classification): ...
class Huber(Regression): ...
class EpsilonInsensitive(Regression): ...
class SquaredEpsilonInsensitive(Regression): ...

LEARNING_RATE_TYPES: dict = ...

PENALTY_TYPES: dict = ...

DEFAULT_EPSILON: float = ...
# Default value of ``epsilon`` parameter.

MAX_INT = ...

class _ValidationScoreCallback:
    def __init__(
        self,
        estimator: "SGDClassifier",
        X_val: csr_matrix,
        y_val: ndarray,
        sample_weight_val: ndarray,
        classes: Optional[ndarray] = None,
    ) -> None: ...
    def __call__(self, coef: ndarray, intercept: float) -> float64: ...

class BaseSGD(SparseCoefMixin, BaseEstimator, metaclass=ABCMeta):
    def __init__(
        self,
        loss: str,
        *,
        penalty="l2",
        alpha=0.0001,
        C=1.0,
        l1_ratio=0.15,
        fit_intercept=True,
        max_iter=1000,
        tol=1e-3,
        shuffle=True,
        verbose=0,
        epsilon=0.1,
        random_state=None,
        learning_rate="optimal",
        eta0=0.0,
        power_t=0.5,
        early_stopping=False,
        validation_fraction=0.1,
        n_iter_no_change=5,
        warm_start=False,
        average=False,
    ) -> None: ...
    @abstractmethod
    def fit(self, X, y): ...
    def _validate_params(self, for_partial_fit: bool = False) -> None: ...
    def _get_loss_function(self, loss: str) -> Union[ModifiedHuber, Hinge, Log, SquaredLoss]: ...
    def _get_learning_rate_type(self, learning_rate: str) -> int: ...
    def _get_penalty_type(self, penalty: Optional[str]) -> int: ...
    def _allocate_parameter_mem(
        self,
        n_classes: int,
        n_features: int,
        coef_init: None = None,
        intercept_init: None = None,
        one_class: int = 0,
    ) -> None: ...
    def _make_validation_split(self, y: ndarray) -> ndarray: ...
    def _make_validation_score_cb(
        self,
        validation_mask: ndarray,
        X: Union[ndarray, csr_matrix],
        y: ndarray,
        sample_weight: ndarray,
        classes: Optional[ndarray] = None,
    ) -> Optional[_ValidationScoreCallback]: ...

def _prepare_fit_binary(
    est: Union[PassiveAggressiveClassifier, Perceptron, SGDClassifier],
    y: ndarray,
    i: int,
) -> Union[Tuple[ndarray, ndarray, float64, None, int], Tuple[ndarray, ndarray, float64, ndarray, float64],]: ...
def fit_binary(
    est: BaseEstimator,
    i: int,
    X: NDArray,
    y: NDArray,
    alpha: float,
    C: float,
    learning_rate: str,
    max_iter: int,
    pos_weight: float,
    neg_weight: float,
    sample_weight: NDArray,
    validation_mask: NDArray | None = None,
    random_state: int | RandomState | None = None,
) -> Tuple[ndarray, float, int]: ...

class BaseSGDClassifier(LinearClassifierMixin, BaseSGD, metaclass=ABCMeta):

    # TODO(1.2): Remove "squared_loss"
    # TODO(1.3): Remove "log""
    loss_functions: dict = ...

    @abstractmethod
    def __init__(
        self,
        loss: str = "hinge",
        *,
        penalty="l2",
        alpha=0.0001,
        l1_ratio=0.15,
        fit_intercept=True,
        max_iter=1000,
        tol=1e-3,
        shuffle=True,
        verbose=0,
        epsilon=...,
        n_jobs=None,
        random_state=None,
        learning_rate="optimal",
        eta0=0.0,
        power_t=0.5,
        early_stopping=False,
        validation_fraction=0.1,
        n_iter_no_change=5,
        class_weight=None,
        warm_start=False,
        average=False,
    ) -> None: ...
    def _partial_fit(
        self,
        X: Union[ndarray, csr_matrix],
        y: ndarray,
        alpha: Union[float, float64],
        C: float,
        loss: str,
        learning_rate: str,
        max_iter: int,
        classes: ndarray,
        sample_weight: Optional[ndarray],
        coef_init: None,
        intercept_init: None,
    ) -> Union[PassiveAggressiveClassifier, Perceptron, SGDClassifier]: ...
    def _fit(
        self,
        X: Union[ndarray, csr_matrix],
        y: Union[List[int], List[int64], ndarray],
        alpha: Union[float, float64],
        C: float,
        loss: str,
        learning_rate: str,
        coef_init: None = None,
        intercept_init: None = None,
        sample_weight: Optional[ndarray] = None,
    ) -> Union[PassiveAggressiveClassifier, Perceptron, SGDClassifier]: ...
    def _fit_binary(
        self,
        X: Union[ndarray, csr_matrix],
        y: ndarray,
        alpha: float,
        C: float,
        sample_weight: ndarray,
        learning_rate: str,
        max_iter: int,
    ) -> None: ...
    def _fit_multiclass(
        self,
        X: Union[ndarray, csr_matrix],
        y: ndarray,
        alpha: Union[float, float64],
        C: float,
        learning_rate: str,
        sample_weight: ndarray,
        max_iter: int,
    ) -> None: ...
    def partial_fit(
        self,
        X: NDArray | ArrayLike,
        y: NDArray,
        classes: NDArray | None = None,
        sample_weight: ArrayLike | None = None,
    ) -> Union[Perceptron, SGDClassifier]: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: NDArray,
        coef_init: NDArray | None = None,
        intercept_init: NDArray | None = None,
        sample_weight: ArrayLike | None = None,
    ) -> Union[Perceptron, SGDClassifier]: ...

class SGDClassifier(BaseSGDClassifier):
    def __init__(
        self,
        loss: Literal[
            "hinge",
            "log_loss",
            "log",
            "modified_huber",
            "squared_hinge",
            "perceptron",
            "squared_error",
            "huber",
            "epsilon_insensitive",
            "squared_epsilon_insensitive",
        ] = "hinge",
        *,
        penalty: Literal["l2", "l1", "elasticnet"] = "l2",
        alpha: float = 0.0001,
        l1_ratio: float = 0.15,
        fit_intercept: bool = True,
        max_iter: int = 1000,
        tol: float = 1e-3,
        shuffle: bool = True,
        verbose: int = 0,
        epsilon: float = ...,
        n_jobs: int | None = None,
        random_state: int | RandomState | None = None,
        learning_rate: str = "optimal",
        eta0: float = 0.0,
        power_t: float = 0.5,
        early_stopping: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change: int = 5,
        class_weight: dict | Literal["balanced"] | None = None,
        warm_start: bool = False,
        average: bool | int = False,
    ) -> None: ...
    def _check_proba(self) -> bool: ...
    @available_if(_check_proba)
    def predict_proba(self, X: NDArray | ArrayLike) -> np.ndarray: ...
    @available_if(_check_proba)
    def predict_log_proba(self, X: NDArray | ArrayLike) -> ArrayLike: ...
    def _more_tags(self) -> Dict[str, Dict[str, str]]: ...

class BaseSGDRegressor(RegressorMixin, BaseSGD):

    # TODO: Remove squared_loss in v1.2
    loss_functions: dict = ...

    @abstractmethod
    def __init__(
        self,
        loss: str = "squared_error",
        *,
        penalty="l2",
        alpha=0.0001,
        l1_ratio=0.15,
        fit_intercept=True,
        max_iter=1000,
        tol=1e-3,
        shuffle=True,
        verbose=0,
        epsilon=...,
        random_state=None,
        learning_rate="invscaling",
        eta0=0.01,
        power_t=0.25,
        early_stopping=False,
        validation_fraction=0.1,
        n_iter_no_change=5,
        warm_start=False,
        average=False,
    ) -> None: ...
    def _partial_fit(
        self,
        X: ndarray,
        y: ndarray,
        alpha: float,
        C: float,
        loss: str,
        learning_rate: str,
        max_iter: int,
        sample_weight: None,
        coef_init: None,
        intercept_init: None,
    ) -> "SGDRegressor": ...
    def partial_fit(self, X: NDArray | ArrayLike, y: NDArray, sample_weight: ArrayLike | None = None) -> Any: ...
    def _fit(
        self,
        X: ndarray,
        y: ndarray,
        alpha: float,
        C: float,
        loss: str,
        learning_rate: str,
        coef_init: None = None,
        intercept_init: None = None,
        sample_weight: None = None,
    ) -> "SGDRegressor": ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: NDArray,
        coef_init: NDArray | None = None,
        intercept_init: NDArray | None = None,
        sample_weight: ArrayLike | None = None,
    ) -> "SGDRegressor": ...
    def _decision_function(self, X: ndarray) -> ndarray: ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    def _fit_regressor(
        self,
        X: ndarray,
        y: ndarray,
        alpha: float,
        C: float,
        loss: str,
        learning_rate: str,
        sample_weight: ndarray,
        max_iter: int,
    ) -> None: ...

class SGDRegressor(BaseSGDRegressor):
    def __init__(
        self,
        loss: str = "squared_error",
        *,
        penalty: Literal["l2", "l1", "elasticnet"] = "l2",
        alpha: float = 0.0001,
        l1_ratio: float = 0.15,
        fit_intercept: bool = True,
        max_iter: int = 1000,
        tol: float = 1e-3,
        shuffle: bool = True,
        verbose: int = 0,
        epsilon: float = ...,
        random_state: int | RandomState | None = None,
        learning_rate: str = "invscaling",
        eta0: float = 0.01,
        power_t: float = 0.25,
        early_stopping: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change: int = 5,
        warm_start: bool = False,
        average: bool | int = False,
    ) -> None: ...
    def _more_tags(self): ...

class SGDOneClassSVM(BaseSGD, OutlierMixin):

    loss_functions: dict = ...

    def __init__(
        self,
        nu: float = 0.5,
        fit_intercept: bool = True,
        max_iter: int = 1000,
        tol: float | None = 1e-3,
        shuffle: bool = True,
        verbose: int = 0,
        random_state: int | RandomState | None = None,
        learning_rate: Literal["constant", "optimal", "invscaling", "adaptive"] = "optimal",
        eta0: float = 0.0,
        power_t: float = 0.5,
        warm_start: bool = False,
        average: bool | int = False,
    ) -> None: ...
    def _validate_params(self, for_partial_fit: bool = False) -> None: ...
    def _fit_one_class(
        self,
        X: ndarray,
        alpha: float,
        C: float,
        sample_weight: ndarray,
        learning_rate: str,
        max_iter: int,
    ) -> None: ...
    def _partial_fit(
        self,
        X: ndarray,
        alpha: float,
        C: float,
        loss: str,
        learning_rate: str,
        max_iter: int,
        sample_weight: None,
        coef_init: None,
        offset_init: None,
    ) -> "SGDOneClassSVM": ...
    def partial_fit(self, X: NDArray | ArrayLike, y=None, sample_weight: ArrayLike | None = None) -> Any: ...
    def _fit(
        self,
        X: ndarray,
        alpha: float,
        C: float,
        loss: str,
        learning_rate: str,
        coef_init: None = None,
        offset_init: None = None,
        sample_weight: None = None,
    ) -> "SGDOneClassSVM": ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: None = None,
        coef_init: NDArray | None = None,
        offset_init: NDArray | None = None,
        sample_weight: ArrayLike | None = None,
    ) -> "SGDOneClassSVM": ...
    def decision_function(self, X: NDArray | ArrayLike) -> ArrayLike: ...
    def score_samples(self, X: NDArray | ArrayLike) -> ArrayLike: ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    def _more_tags(self) -> Dict[str, Dict[str, str]]: ...
