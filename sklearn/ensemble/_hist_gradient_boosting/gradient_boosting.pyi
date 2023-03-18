from typing import Callable, ClassVar, Literal, Mapping, Sequence, TypeVar
from numpy.random import RandomState
from ...utils.validation import (
    check_is_fitted as check_is_fitted,
    check_consistent_length as check_consistent_length,
)
from ...utils import (
    check_random_state as check_random_state,
    resample as resample,
    compute_sample_weight as compute_sample_weight,
)
from ...utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..._loss.loss import (
    _LOSSES,
    BaseLoss as BaseLoss,
    HalfBinomialLoss as HalfBinomialLoss,
    HalfMultinomialLoss as HalfMultinomialLoss,
    HalfPoissonLoss as HalfPoissonLoss,
    PinballLoss as PinballLoss,
)
from ...metrics import check_scoring as check_scoring
from timeit import default_timer as time
from .grower import TreeGrower as TreeGrower
from abc import ABC, abstractmethod
from numpy import ndarray
from ...utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from numbers import Real as Real, Integral as Integral
from ...model_selection import train_test_split as train_test_split
from functools import partial as partial
from ...preprocessing import LabelEncoder as LabelEncoder
from ...base import (
    BaseEstimator,
    RegressorMixin,
    ClassifierMixin,
    is_classifier as is_classifier,
)
from .common import Y_DTYPE as Y_DTYPE, X_DTYPE as X_DTYPE, G_H_DTYPE as G_H_DTYPE
from ..._typing import MatrixLike, ArrayLike, Float, Int

BaseHistGradientBoosting_Self = TypeVar(
    "BaseHistGradientBoosting_Self", bound="BaseHistGradientBoosting"
)

import itertools
import warnings

import numpy as np


_LOSSES = ...


class BaseHistGradientBoosting(BaseEstimator, ABC):

    _parameter_constraints: ClassVar[dict] = ...

    @abstractmethod
    def __init__(
        self,
        loss: str,
        *,
        learning_rate,
        max_iter,
        max_leaf_nodes,
        max_depth,
        min_samples_leaf,
        l2_regularization,
        max_bins,
        categorical_features,
        monotonic_cst,
        interaction_cst,
        warm_start,
        early_stopping,
        scoring,
        validation_fraction,
        n_iter_no_change,
        tol,
        verbose,
        random_state,
    ) -> None:
        ...

    def fit(
        self: BaseHistGradientBoosting_Self,
        X: MatrixLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> BaseHistGradientBoosting_Self:
        ...

    def n_iter_(self):
        ...


class HistGradientBoostingRegressor(RegressorMixin, BaseHistGradientBoosting):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    is_categorical_: None | ndarray = ...
    validation_score_: ndarray = ...
    train_score_: ndarray = ...
    n_trees_per_iteration_: int = ...
    n_iter_: int = ...
    do_early_stopping_: bool = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        loss: Literal[
            "squared_error", "absolute_error", "poisson", "quantile", "squared_error"
        ] = "squared_error",
        *,
        quantile: None | Float = None,
        learning_rate: Float = 0.1,
        max_iter: Int = 100,
        max_leaf_nodes: None | int = 31,
        max_depth: None | int = None,
        min_samples_leaf: Int = 20,
        l2_regularization: Float = 0.0,
        max_bins: Int = 255,
        categorical_features: None | MatrixLike | ArrayLike = None,
        monotonic_cst: None | Mapping | ArrayLike = None,
        interaction_cst: None
        | Literal["pairwise", "no_interaction"]
        | Sequence[list[int] | tuple[int, ...] | set[int]] = None,
        warm_start: bool = False,
        early_stopping: Literal["auto", "auto"] | bool = "auto",
        scoring: None | str | Callable = "loss",
        validation_fraction: float | None | int = 0.1,
        n_iter_no_change: Int = 10,
        tol: Float = 1e-7,
        verbose: Int = 0,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...

    def staged_predict(self, X: MatrixLike):
        ...


class HistGradientBoostingClassifier(ClassifierMixin, BaseHistGradientBoosting):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    is_categorical_: None | ndarray = ...
    validation_score_: ndarray = ...
    train_score_: ndarray = ...
    n_trees_per_iteration_: int = ...
    n_iter_: int = ...
    do_early_stopping_: bool = ...
    classes_: ndarray = ...

    # TODO(1.3): Remove "binary_crossentropy", "categorical_crossentropy", "auto"
    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        loss: Literal[
            "log_loss",
            "log_loss",
            "auto",
            "binary_crossentropy",
            "categorical_crossentropy",
        ] = "log_loss",
        *,
        learning_rate: Float = 0.1,
        max_iter: Int = 100,
        max_leaf_nodes: None | int = 31,
        max_depth: None | int = None,
        min_samples_leaf: Int = 20,
        l2_regularization: Float = 0.0,
        max_bins: Int = 255,
        categorical_features: None | MatrixLike | ArrayLike = None,
        monotonic_cst: None | Mapping | ArrayLike = None,
        interaction_cst: None
        | Literal["pairwise", "no_interaction"]
        | Sequence[list[int] | tuple[int, ...] | set[int]] = None,
        warm_start: bool = False,
        early_stopping: Literal["auto", "auto"] | bool = "auto",
        scoring: None | str | Callable = "loss",
        validation_fraction: float | None | int = 0.1,
        n_iter_no_change: Int = 10,
        tol: Float = 1e-7,
        verbose: Int = 0,
        random_state: RandomState | None | Int = None,
        class_weight: None | Mapping | str = None,
    ) -> None:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...

    def staged_predict(self, X: MatrixLike):
        ...

    def predict_proba(self, X: MatrixLike) -> ndarray:
        ...

    def staged_predict_proba(self, X: MatrixLike):
        ...

    def decision_function(self, X: MatrixLike) -> ndarray:
        ...

    def staged_decision_function(self, X: MatrixLike):
        ...
