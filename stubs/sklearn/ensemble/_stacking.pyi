from abc import ABCMeta, abstractmethod
from copy import deepcopy as deepcopy
from numbers import Integral as Integral
from typing import ClassVar, Iterable, Literal, Sequence, TypeVar

from numpy import ndarray

from .._typing import ArrayLike, Int, MatrixLike
from ..base import (
    BaseEstimator,
    ClassifierMixin,
    RegressorMixin,
    TransformerMixin,
    clone as clone,
    is_classifier as is_classifier,
    is_regressor as is_regressor,
)
from ..exceptions import NotFittedError as NotFittedError
from ..linear_model._logistic import LogisticRegression
from ..linear_model._ridge import RidgeCV
from ..model_selection import BaseCrossValidator, check_cv as check_cv, cross_val_predict as cross_val_predict
from ..model_selection._split import BaseShuffleSplit
from ..pipeline import Pipeline
from ..preprocessing import LabelEncoder as LabelEncoder
from ..utils import Bunch
from ..utils._param_validation import HasMethods as HasMethods, StrOptions as StrOptions
from ..utils.metaestimators import available_if as available_if
from ..utils.multiclass import check_classification_targets as check_classification_targets, type_of_target as type_of_target
from ..utils.parallel import Parallel as Parallel, delayed as delayed
from ..utils.validation import check_is_fitted as check_is_fitted, column_or_1d as column_or_1d
from ._base import _BaseHeterogeneousEnsemble

_BaseStacking_Self = TypeVar("_BaseStacking_Self", bound="_BaseStacking")
StackingRegressor_Self = TypeVar("StackingRegressor_Self", bound="StackingRegressor")
StackingClassifier_Self = TypeVar("StackingClassifier_Self", bound="StackingClassifier")

import numpy as np
import scipy.sparse as sparse

class _BaseStacking(TransformerMixin, _BaseHeterogeneousEnsemble, metaclass=ABCMeta):
    _parameter_constraints: ClassVar[dict] = ...

    @abstractmethod
    def __init__(
        self,
        estimators,
        final_estimator=None,
        *,
        cv=None,
        stack_method: str = "auto",
        n_jobs=None,
        verbose: int = 0,
        passthrough: bool = False,
    ) -> None: ...
    def fit(
        self: _BaseStacking_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> _BaseStacking_Self | StackingClassifier: ...
    def n_features_in_(self): ...
    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray: ...
    def predict(self, X: MatrixLike | ArrayLike, **predict_params) -> ndarray: ...

class StackingClassifier(ClassifierMixin, _BaseStacking):
    stack_method_: list[str] = ...
    final_estimator_: BaseEstimator = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    named_estimators_: Bunch = ...
    estimators_: list[BaseEstimator] = ...
    classes_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        estimators: Sequence[tuple[str, BaseEstimator]],
        final_estimator: None | BaseEstimator | LogisticRegression = None,
        *,
        cv: int | BaseCrossValidator | Iterable | None | str | BaseShuffleSplit = None,
        stack_method: Literal["auto", "predict_proba", "decision_function", "predict", "auto"] = "auto",
        n_jobs: None | Int = None,
        passthrough: bool = False,
        verbose: Int = 0,
    ) -> None: ...
    def fit(
        self: StackingClassifier_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> StackingClassifier_Self: ...
    def predict(self, X: MatrixLike | ArrayLike, **predict_params) -> ndarray: ...
    def predict_proba(self, X: MatrixLike | ArrayLike) -> ndarray | list[ndarray]: ...
    def decision_function(self, X: MatrixLike | ArrayLike) -> ndarray: ...
    def transform(self, X: MatrixLike | ArrayLike) -> ndarray: ...

class StackingRegressor(RegressorMixin, _BaseStacking):
    stack_method_: list[str] = ...
    final_estimator_: BaseEstimator = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    named_estimators_: Bunch = ...
    estimators_: list[BaseEstimator] = ...

    def __init__(
        self,
        estimators: Sequence[tuple[str, BaseEstimator]] | list[tuple[str, Pipeline]],
        final_estimator: None | BaseEstimator | RidgeCV = None,
        *,
        cv: int | BaseCrossValidator | Iterable | None | str | BaseShuffleSplit = None,
        n_jobs: None | Int = None,
        passthrough: bool = False,
        verbose: Int = 0,
    ) -> None: ...
    def fit(
        self: StackingRegressor_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> StackingRegressor_Self: ...
    def transform(self, X: MatrixLike | ArrayLike) -> ndarray: ...
