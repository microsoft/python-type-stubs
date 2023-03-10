from typing import Any, Sequence
from .ensemble._forest import RandomForestRegressor
from .utils import check_random_state as check_random_state
from ._typing import ArrayLike, MatrixLike, Estimator
from .base import (
    BaseEstimator,
    clone as clone,
    MetaEstimatorMixin,
    RegressorMixin,
    ClassifierMixin,
    is_classifier as is_classifier,
)
from .utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from abc import ABCMeta, abstractmethod
from numpy import ndarray
from .utils._param_validation import HasMethods as HasMethods, StrOptions as StrOptions
from numbers import Integral as Integral
from .utils.validation import (
    check_is_fitted as check_is_fitted,
    has_fit_parameter as has_fit_parameter,
)
from .utils.metaestimators import available_if as available_if
from .utils.parallel import delayed as delayed, Parallel as Parallel
from .model_selection import cross_val_predict as cross_val_predict
from scipy.sparse import spmatrix
from .linear_model._logistic import LogisticRegression

import numpy as np
import scipy.sparse as sp

__all__ = [
    "MultiOutputRegressor",
    "MultiOutputClassifier",
    "ClassifierChain",
    "RegressorChain",
]


class _MultiOutputEstimator(MetaEstimatorMixin, BaseEstimator, metaclass=ABCMeta):

    _parameter_constraints: dict = ...

    @abstractmethod
    def __init__(self, estimator: RandomForestRegressor, *, n_jobs=None) -> None:
        ...

    def partial_fit(
        self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike,
        classes: Sequence[ArrayLike] | None = None,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike,
        sample_weight: None | ArrayLike = None,
        **fit_params
    ) -> Any:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> spmatrix | ndarray:
        ...


class MultiOutputRegressor(RegressorMixin, _MultiOutputEstimator):
    def __init__(
        self, estimator: Estimator | RandomForestRegressor, *, n_jobs: int | None = None
    ) -> None:
        ...

    def partial_fit(
        self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...


class MultiOutputClassifier(ClassifierMixin, _MultiOutputEstimator):
    def __init__(self, estimator: Estimator, *, n_jobs: int | None = None) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        Y: MatrixLike,
        sample_weight: None | ArrayLike = None,
        **fit_params
    ) -> Any:
        ...

    def predict_proba(self, X: MatrixLike) -> list[ndarray] | ndarray:
        ...

    def score(self, X: MatrixLike, y: MatrixLike) -> float:
        ...


class _BaseChain(BaseEstimator, metaclass=ABCMeta):

    _parameter_constraints: dict = ...

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
    def fit(self, X: MatrixLike | ArrayLike, Y: MatrixLike, **fit_params) -> Any:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...


class ClassifierChain(MetaEstimatorMixin, ClassifierMixin, _BaseChain):
    def fit(self, X: MatrixLike | ArrayLike, Y: MatrixLike) -> Any:
        ...

    def predict_proba(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def decision_function(self, X: MatrixLike) -> ndarray:
        ...


class RegressorChain(MetaEstimatorMixin, RegressorMixin, _BaseChain):
    def fit(self, X: MatrixLike | ArrayLike, Y: MatrixLike, **fit_params) -> Any:
        ...
