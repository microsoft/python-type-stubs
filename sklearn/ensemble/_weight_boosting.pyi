from numpy import float64, ndarray
from typing import Iterator, Optional, Tuple, Union, Any, Literal
from numpy.typing import ArrayLike, NDArray

# Authors: Noel Dawe <noel@dawe.me>
#          Gilles Louppe <g.louppe@gmail.com>
#          Hamzeh Alsalhi <ha258@cornell.edu>
#          Arnaud Joly <arnaud.v.joly@gmail.com>
#
# License: BSD 3 clause

from abc import ABCMeta, abstractmethod

import numbers
import numpy as np

import warnings

from scipy.special import xlogy

from ._base import BaseEnsemble
from ..base import ClassifierMixin, RegressorMixin, is_classifier, is_regressor

from ..tree import DecisionTreeClassifier, DecisionTreeRegressor
from ..utils import check_random_state, _safe_indexing
from ..utils import check_scalar
from ..utils.extmath import softmax
from ..utils.extmath import stable_cumsum
from ..metrics import accuracy_score, r2_score
from ..utils.validation import check_is_fitted
from ..utils.validation import _check_sample_weight
from ..utils.validation import has_fit_parameter
from ..utils.validation import _num_samples
from numpy.random import RandomState
from sklearn.tree._classes import DecisionTreeClassifier, DecisionTreeRegressor

__all__ = [
    "AdaBoostClassifier",
    "AdaBoostRegressor",
]

class BaseWeightBoosting(BaseEnsemble, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        base_estimator: Optional[Union[DecisionTreeRegressor, DecisionTreeClassifier]] = None,
        *,
        n_estimators=50,
        estimator_params=...,
        learning_rate=1.0,
        random_state=None,
    ) -> None: ...
    def _check_X(self, X: ndarray) -> ndarray: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> Union[AdaBoostClassifier, AdaBoostRegressor]: ...
    @abstractmethod
    def _boost(self, iboost, X, y, sample_weight, random_state): ...
    def staged_score(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ): ...
    @property
    def feature_importances_(self) -> NDArray: ...

def _samme_proba(estimator: DecisionTreeClassifier, n_classes: int, X: ndarray) -> ndarray: ...

class AdaBoostClassifier(ClassifierMixin, BaseWeightBoosting):
    def __init__(
        self,
        base_estimator: Optional[DecisionTreeClassifier] = None,
        *,
        n_estimators: int = 50,
        learning_rate: float = 1.0,
        algorithm: Literal["SAMME", "SAMME.R"] = "SAMME.R",
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> "AdaBoostClassifier": ...
    def _validate_estimator(self) -> None: ...
    def _boost(
        self,
        iboost: int,
        X: ndarray,
        y: ndarray,
        sample_weight: ndarray,
        random_state: RandomState,
    ) -> Union[Tuple[ndarray, float64, float64], Tuple[ndarray, float, float64]]: ...
    def _boost_real(
        self,
        iboost: int,
        X: ndarray,
        y: ndarray,
        sample_weight: ndarray,
        random_state: RandomState,
    ) -> Tuple[ndarray, float, float64]: ...
    def _boost_discrete(
        self,
        iboost: int,
        X: ndarray,
        y: ndarray,
        sample_weight: ndarray,
        random_state: RandomState,
    ) -> Tuple[ndarray, float64, float64]: ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    def staged_predict(self, X: ArrayLike) -> Iterator[ndarray]: ...
    def decision_function(self, X: NDArray | ArrayLike) -> NDArray: ...
    def staged_decision_function(self, X: NDArray | ArrayLike) -> Iterator[ndarray]: ...
    @staticmethod
    def _compute_proba_from_decision(decision, n_classes): ...
    def predict_proba(self, X: NDArray | ArrayLike) -> np.ndarray: ...
    def staged_predict_proba(self, X: NDArray | ArrayLike): ...
    def predict_log_proba(self, X: NDArray | ArrayLike) -> np.ndarray: ...

class AdaBoostRegressor(RegressorMixin, BaseWeightBoosting):
    def __init__(
        self,
        base_estimator: Optional[DecisionTreeRegressor] = None,
        *,
        n_estimators: int = 50,
        learning_rate: float = 1.0,
        loss: Literal["linear", "square", "exponential"] = "linear",
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> "AdaBoostRegressor": ...
    def _validate_estimator(self) -> None: ...
    def _boost(
        self,
        iboost: int,
        X: ndarray,
        y: ndarray,
        sample_weight: ndarray,
        random_state: RandomState,
    ) -> Tuple[ndarray, float64, float64]: ...
    def _get_median_predict(self, X: ndarray, limit: int) -> ndarray: ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    def staged_predict(self, X: NDArray | ArrayLike): ...
