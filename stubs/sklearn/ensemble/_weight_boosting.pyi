from typing import Any, ClassVar, Iterator, Literal, TypeVar
from numpy.random import RandomState
from scipy.special import xlogy as xlogy
from abc import ABCMeta, abstractmethod
from ..tree import (
    DecisionTreeClassifier as DecisionTreeClassifier,
    DecisionTreeRegressor as DecisionTreeRegressor,
)
from ..base import ClassifierMixin, RegressorMixin, BaseEstimator
from ._base import BaseEnsemble
from numpy import ndarray
from ..utils.extmath import softmax as softmax, stable_cumsum as stable_cumsum
from ..utils._param_validation import (
    HasMethods as HasMethods,
    Interval as Interval,
    StrOptions as StrOptions,
)
from numbers import Integral as Integral, Real as Real
from ..metrics import accuracy_score as accuracy_score, r2_score as r2_score
from ..base import is_classifier as is_classifier, is_regressor as is_regressor
from .._typing import MatrixLike, ArrayLike, Int, Float
from ..utils import check_random_state as check_random_state
from ..utils.validation import (
    check_is_fitted as check_is_fitted,
    has_fit_parameter as has_fit_parameter,
)

BaseWeightBoosting_Self = TypeVar("BaseWeightBoosting_Self", bound="BaseWeightBoosting")

import numpy as np

import warnings

__all__ = [
    "AdaBoostClassifier",
    "AdaBoostRegressor",
]


class BaseWeightBoosting(BaseEnsemble, metaclass=ABCMeta):

    _parameter_constraints: ClassVar[dict] = ...

    @abstractmethod
    def __init__(
        self,
        estimator=None,
        *,
        n_estimators: int = 50,
        estimator_params=...,
        learning_rate: float = 1.0,
        random_state=None,
        base_estimator: str = "deprecated",
    ) -> None:
        ...

    def fit(
        self: BaseWeightBoosting_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> BaseWeightBoosting_Self:
        ...

    def staged_score(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ):
        ...

    @property
    def feature_importances_(self) -> ndarray:
        ...


class AdaBoostClassifier(ClassifierMixin, BaseWeightBoosting):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    feature_importances_: ndarray = ...
    estimator_errors_: ndarray = ...
    estimator_weights_: ndarray = ...
    n_classes_: int = ...
    classes_: ndarray = ...
    estimators_: list[ClassifierMixin] = ...
    base_estimator_: BaseEstimator = ...
    estimator_: BaseEstimator = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        estimator: Any = None,
        *,
        n_estimators: Int = 50,
        learning_rate: Float = 1.0,
        algorithm: Literal["SAMME", "SAMME.R", "SAMME.R"] = "SAMME.R",
        random_state: RandomState | None | Int = None,
        base_estimator: Any = "deprecated",
    ) -> None:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def staged_predict(self, X: MatrixLike) -> Iterator[ndarray]:
        ...

    def decision_function(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def staged_decision_function(self, X: MatrixLike | ArrayLike) -> Iterator[ndarray]:
        ...

    def predict_proba(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def staged_predict_proba(self, X: MatrixLike | ArrayLike):
        ...

    def predict_log_proba(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...


class AdaBoostRegressor(RegressorMixin, BaseWeightBoosting):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    feature_importances_: ndarray = ...
    estimator_errors_: ndarray = ...
    estimator_weights_: ndarray = ...
    estimators_: list[RegressorMixin] = ...
    base_estimator_: BaseEstimator = ...
    estimator_: BaseEstimator = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        estimator: Any = None,
        *,
        n_estimators: Int = 50,
        learning_rate: Float = 1.0,
        loss: Literal["linear", "square", "exponential", "linear"] = "linear",
        random_state: RandomState | None | Int = None,
        base_estimator: Any = "deprecated",
    ) -> None:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def staged_predict(self, X: MatrixLike | ArrayLike):
        ...
