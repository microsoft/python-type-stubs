from typing import ClassVar, Sequence, TypeVar
from .model_selection import cross_val_predict as cross_val_predict
from .ensemble._forest import RandomForestRegressor
from abc import ABCMeta, abstractmethod
from .base import (
    clone as clone,
    MetaEstimatorMixin,
    RegressorMixin,
    ClassifierMixin,
    is_classifier as is_classifier,
)
from .utils.validation import (
    check_is_fitted as check_is_fitted,
    has_fit_parameter as has_fit_parameter,
)
from .base import BaseEstimator
from .utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from numpy import ndarray
from numbers import Integral as Integral
from .utils.metaestimators import available_if as available_if
from .utils import check_random_state as check_random_state
from .utils._param_validation import HasMethods as HasMethods, StrOptions as StrOptions
from ._typing import MatrixLike, ArrayLike
from scipy.sparse import spmatrix
from .utils.parallel import delayed as delayed, Parallel as Parallel
from .linear_model._logistic import LogisticRegression

MultiOutputClassifier_Self = TypeVar(
    "MultiOutputClassifier_Self", bound="MultiOutputClassifier"
)
RegressorChain_Self = TypeVar("RegressorChain_Self", bound="RegressorChain")
_BaseChain_Self = TypeVar("_BaseChain_Self", bound="_BaseChain")
_MultiOutputEstimator_Self = TypeVar(
    "_MultiOutputEstimator_Self", bound="_MultiOutputEstimator"
)
MultiOutputRegressor_Self = TypeVar(
    "MultiOutputRegressor_Self", bound="MultiOutputRegressor"
)
ClassifierChain_Self = TypeVar("ClassifierChain_Self", bound="ClassifierChain")


import numpy as np
import scipy.sparse as sp

__all__ = [
    "MultiOutputRegressor",
    "MultiOutputClassifier",
    "ClassifierChain",
    "RegressorChain",
]


class _MultiOutputEstimator(MetaEstimatorMixin, BaseEstimator, metaclass=ABCMeta):

    _parameter_constraints: ClassVar[dict] = ...

    @abstractmethod
    def __init__(self, estimator: RandomForestRegressor, *, n_jobs=None) -> None:
        ...

    def partial_fit(
        self: _MultiOutputEstimator_Self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike,
        classes: Sequence[ArrayLike] | None = None,
        sample_weight: None | ArrayLike = None,
    ) -> _MultiOutputEstimator_Self:
        ...

    def fit(
        self: _MultiOutputEstimator_Self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike,
        sample_weight: None | ArrayLike = None,
        **fit_params
    ) -> _MultiOutputEstimator_Self | MultiOutputRegressor:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray | spmatrix:
        ...


class MultiOutputRegressor(RegressorMixin, _MultiOutputEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    estimators_: list[BaseEstimator] = ...

    def __init__(
        self,
        estimator: BaseEstimator | RandomForestRegressor,
        *,
        n_jobs: None | int = None
    ) -> None:
        ...

    def partial_fit(
        self: MultiOutputRegressor_Self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike,
        sample_weight: None | ArrayLike = None,
    ) -> MultiOutputRegressor_Self:
        ...


class MultiOutputClassifier(ClassifierMixin, _MultiOutputEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    estimators_: list[BaseEstimator] = ...
    classes_: ndarray = ...

    def __init__(self, estimator: BaseEstimator, *, n_jobs: None | int = None) -> None:
        ...

    def fit(
        self: MultiOutputClassifier_Self,
        X: MatrixLike | ArrayLike,
        Y: MatrixLike,
        sample_weight: None | ArrayLike = None,
        **fit_params
    ) -> MultiOutputClassifier_Self:
        ...

    def predict_proba(self, X: MatrixLike) -> ndarray | list[ndarray]:
        ...

    def score(self, X: MatrixLike, y: MatrixLike) -> float:
        ...


class _BaseChain(BaseEstimator, metaclass=ABCMeta):

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        base_estimator: LogisticRegression,
        *,
        order=None,
        cv=None,
        random_state=None,
        verbose: bool = False
    ) -> None:
        ...

    @abstractmethod
    def fit(
        self: _BaseChain_Self, X: MatrixLike | ArrayLike, Y: MatrixLike, **fit_params
    ) -> _BaseChain_Self | ClassifierChain:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...


class ClassifierChain(MetaEstimatorMixin, ClassifierMixin, _BaseChain):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    order_: list = ...
    estimators_: list = ...
    classes_: list = ...

    def fit(
        self: ClassifierChain_Self, X: MatrixLike | ArrayLike, Y: MatrixLike
    ) -> ClassifierChain_Self:
        ...

    def predict_proba(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def decision_function(self, X: MatrixLike) -> ndarray:
        ...


class RegressorChain(MetaEstimatorMixin, RegressorMixin, _BaseChain):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    order_: list = ...
    estimators_: list = ...

    def fit(
        self: RegressorChain_Self,
        X: MatrixLike | ArrayLike,
        Y: MatrixLike,
        **fit_params
    ) -> RegressorChain_Self:
        ...
