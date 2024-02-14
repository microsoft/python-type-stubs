from abc import ABCMeta, abstractmethod
from numbers import Integral as Integral, Real as Real
from time import time as time
from typing import Callable, ClassVar, Iterator, Literal, TypeVar

from numpy import ndarray
from numpy.random import RandomState
from scipy.sparse import csc_matrix as csc_matrix, csr_matrix as csr_matrix, issparse as issparse

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, ClassifierMixin, RegressorMixin, is_classifier as is_classifier
from ..exceptions import NotFittedError as NotFittedError
from ..model_selection import train_test_split as train_test_split
from ..tree import DecisionTreeRegressor as DecisionTreeRegressor
from ..tree._tree import DOUBLE as DOUBLE, DTYPE as DTYPE
from ..utils import check_array as check_array, check_random_state as check_random_state, column_or_1d as column_or_1d, deprecated
from ..utils._param_validation import HasMethods as HasMethods, Interval as Interval, StrOptions as StrOptions
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import BaseEnsemble
from ._gb_losses import LossFunction
from ._gradient_boosting import predict_stage as predict_stage, predict_stages as predict_stages

BaseGradientBoosting_Self = TypeVar("BaseGradientBoosting_Self", bound="BaseGradientBoosting")

import warnings

import numpy as np

class VerboseReporter:
    def __init__(self, verbose: Int) -> None: ...
    def init(self, est: BaseEstimator, begin_at_stage: Int = 0): ...
    def update(self, j: Int, est: BaseEstimator): ...

class BaseGradientBoosting(BaseEnsemble, metaclass=ABCMeta):
    _parameter_constraints: ClassVar[dict] = ...

    @abstractmethod
    def __init__(
        self,
        *,
        loss,
        learning_rate,
        n_estimators,
        criterion,
        min_samples_split,
        min_samples_leaf,
        min_weight_fraction_leaf,
        max_depth,
        min_impurity_decrease,
        init,
        subsample,
        max_features,
        ccp_alpha,
        random_state,
        alpha: float = 0.9,
        verbose: int = 0,
        max_leaf_nodes=None,
        warm_start: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change=None,
        tol: float = 1e-4,
    ) -> None: ...
    def fit(
        self: BaseGradientBoosting_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
        monitor: None | Callable = None,
    ) -> BaseGradientBoosting_Self: ...
    @property
    def feature_importances_(self) -> ndarray: ...
    def apply(self, X: MatrixLike | ArrayLike) -> ndarray: ...

    # TODO(1.3): Remove
    # mypy error: Decorated property not supported
    @deprecated("Attribute `loss_` was deprecated in version 1.1 and will be removed in 1.3.")  # type: ignore
    def loss_(self): ...

class GradientBoostingClassifier(ClassifierMixin, BaseGradientBoosting):
    max_features_: int = ...
    n_classes_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    classes_: ndarray = ...
    estimators_: ndarray = ...
    init_: BaseEstimator = ...
    loss_: LossFunction = ...
    train_score_: ndarray = ...
    oob_improvement_: ndarray = ...
    feature_importances_: ndarray = ...
    n_estimators_: int = ...

    # TODO(1.3): remove "deviance"
    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        loss: Literal["log_loss", "deviance", "exponential", "log_loss"] = "log_loss",
        learning_rate: Float = 0.1,
        n_estimators: Int = 100,
        subsample: Float = 1.0,
        criterion: Literal["friedman_mse", "squared_error", "friedman_mse"] = "friedman_mse",
        min_samples_split: float | int = 2,
        min_samples_leaf: float | int = 1,
        min_weight_fraction_leaf: Float = 0.0,
        max_depth: None | int = 3,
        min_impurity_decrease: Float = 0.0,
        init: None | str | BaseEstimator = None,
        random_state: RandomState | None | Int = None,
        max_features: float | None | Literal["auto", "sqrt", "log2"] | int = None,
        verbose: Int = 0,
        max_leaf_nodes: None | Int = None,
        warm_start: bool = False,
        validation_fraction: Float = 0.1,
        n_iter_no_change: None | Int = None,
        tol: Float = 1e-4,
        ccp_alpha: float = 0.0,
    ) -> None: ...
    def decision_function(self, X: MatrixLike | ArrayLike) -> ndarray: ...
    def staged_decision_function(self, X: MatrixLike | ArrayLike): ...
    def predict(self, X: MatrixLike | ArrayLike) -> ndarray: ...
    def staged_predict(self, X: MatrixLike | ArrayLike): ...
    def predict_proba(self, X: MatrixLike | ArrayLike) -> ndarray: ...
    def predict_log_proba(self, X: MatrixLike | ArrayLike) -> ndarray: ...
    def staged_predict_proba(self, X: MatrixLike | ArrayLike) -> Iterator[ndarray]: ...

class GradientBoostingRegressor(RegressorMixin, BaseGradientBoosting):
    max_features_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_estimators_: int = ...
    estimators_: ndarray = ...
    init_: BaseEstimator = ...
    loss_: LossFunction = ...
    train_score_: ndarray = ...
    oob_improvement_: ndarray = ...
    feature_importances_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        loss: Literal["squared_error", "absolute_error", "huber", "quantile", "squared_error"] = "squared_error",
        learning_rate: Float = 0.1,
        n_estimators: Int = 100,
        subsample: Float = 1.0,
        criterion: Literal["friedman_mse", "squared_error", "friedman_mse"] = "friedman_mse",
        min_samples_split: float | int = 2,
        min_samples_leaf: float | int = 1,
        min_weight_fraction_leaf: Float = 0.0,
        max_depth: None | int = 3,
        min_impurity_decrease: Float = 0.0,
        init: None | str | BaseEstimator = None,
        random_state: RandomState | None | Int = None,
        max_features: float | None | Literal["auto", "sqrt", "log2"] | int = None,
        alpha: Float = 0.9,
        verbose: Int = 0,
        max_leaf_nodes: None | Int = None,
        warm_start: bool = False,
        validation_fraction: Float = 0.1,
        n_iter_no_change: None | Int = None,
        tol: Float = 1e-4,
        ccp_alpha: float = 0.0,
    ) -> None: ...
    def predict(self, X: MatrixLike | ArrayLike) -> ndarray: ...
    def staged_predict(self, X: MatrixLike | ArrayLike) -> Iterator[ndarray]: ...
    def apply(self, X: MatrixLike | ArrayLike) -> ndarray: ...
