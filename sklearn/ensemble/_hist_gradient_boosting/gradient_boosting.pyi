from numpy import ndarray
from typing import List, Tuple, Union, Any, Literal, Callable
from numpy.typing import ArrayLike, NDArray

# Author: Nicolas Hug

from abc import ABC, abstractmethod
from functools import partial
import warnings

import numpy as np
from numpy.random import RandomState
from timeit import default_timer as time
from ..._loss.loss import (
    _LOSSES,
    BaseLoss,
    AbsoluteError,
    HalfBinomialLoss,
    HalfMultinomialLoss,
    HalfPoissonLoss,
    HalfSquaredError,
    PinballLoss,
)
from ...base import BaseEstimator, RegressorMixin, ClassifierMixin, is_classifier
from ...utils import check_random_state, resample
from ...utils.validation import (
    check_is_fitted,
    check_consistent_length,
    _check_sample_weight,
)

from ...utils.multiclass import check_classification_targets
from ...metrics import check_scoring
from ...model_selection import train_test_split
from ...preprocessing import LabelEncoder

from .binning import _BinMapper
from .grower import TreeGrower
from pandas.core.frame import DataFrame
from sklearn._loss.loss import (
    HalfBinomialLoss,
    HalfPoissonLoss,
    HalfSquaredError,
    PinballLoss,
)
from sklearn.ensemble._hist_gradient_boosting.grower import TreeGrower
from sklearn.ensemble._hist_gradient_boosting.predictor import TreePredictor

_LOSSES = ...

def _update_leaves_values(
    loss: PinballLoss,
    grower: TreeGrower,
    y_true: ndarray,
    raw_prediction: ndarray,
    sample_weight: None,
) -> None: ...

class BaseHistGradientBoosting(BaseEstimator, ABC):
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
        warm_start,
        early_stopping,
        scoring,
        validation_fraction,
        n_iter_no_change,
        tol,
        verbose,
        random_state,
    ) -> None: ...
    def _validate_parameters(self) -> None: ...
    def _check_categories(self, X: ndarray) -> Tuple[None, None]: ...
    def fit(
        self, X: ArrayLike, y: ArrayLike, sample_weight: ArrayLike | None = None
    ) -> Union[HistGradientBoostingRegressor, HistGradientBoostingClassifier]: ...
    def _is_fitted(self) -> bool: ...
    def _clear_state(self) -> None: ...
    def _get_small_trainset(self, X_binned_train, y_train, sample_weight_train, seed): ...
    def _check_early_stopping_scorer(
        self,
        X_binned_small_train,
        y_small_train,
        sample_weight_small_train,
        X_binned_val,
        y_val,
        sample_weight_val,
    ): ...
    def _check_early_stopping_loss(
        self,
        raw_predictions,
        y_train,
        sample_weight_train,
        raw_predictions_val,
        y_val,
        sample_weight_val,
        n_threads=1,
    ): ...
    def _should_stop(self, scores): ...
    def _bin_data(self, X: ndarray, is_training_data: bool) -> ndarray: ...
    def _print_iteration_stats(self, iteration_start_time): ...
    def _raw_predict(self, X: ndarray, n_threads: None = None) -> ndarray: ...
    def _predict_iterations(
        self,
        X: ndarray,
        predictors: List[List[TreePredictor]],
        raw_predictions: ndarray,
        is_binned: bool,
        n_threads: int,
    ) -> None: ...
    def _staged_raw_predict(self, X): ...
    def _compute_partial_dependence_recursion(self, grid: ndarray, target_features: ndarray) -> ndarray: ...
    def _more_tags(self): ...
    @abstractmethod
    def _get_loss(self, sample_weight): ...
    @abstractmethod
    def _encode_y(self, y=None): ...
    @property
    def n_iter_(self): ...

class HistGradientBoostingRegressor(RegressorMixin, BaseHistGradientBoosting):

    # TODO(1.2): remove "least_absolute_deviation"
    _VALID_LOSSES = ...

    def __init__(
        self,
        loss: Literal["squared_error", "absolute_error", "poisson", "quantile"] = "squared_error",
        *,
        quantile: float | None = None,
        learning_rate: float = 0.1,
        max_iter: int = 100,
        max_leaf_nodes: int | None = 31,
        max_depth: int | None = None,
        min_samples_leaf: int = 20,
        l2_regularization: float = 0.0,
        max_bins: int = 255,
        categorical_features: ArrayLike | None = None,
        monotonic_cst: ArrayLike | None = None,
        warm_start: bool = False,
        early_stopping: bool | Literal["auto"] = "auto",
        scoring: str | Callable | None = "loss",
        validation_fraction: int | float | None = 0.1,
        n_iter_no_change: int = 10,
        tol: float = 1e-7,
        verbose: int = 0,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def predict(self, X: ArrayLike) -> NDArray: ...
    def staged_predict(self, X: ArrayLike): ...
    def _encode_y(self, y: ndarray) -> ndarray: ...
    def _get_loss(self, sample_weight: None) -> Union[HalfPoissonLoss, PinballLoss, HalfSquaredError]: ...

class HistGradientBoostingClassifier(ClassifierMixin, BaseHistGradientBoosting):

    # TODO(1.3): Remove "binary_crossentropy", "categorical_crossentropy", "auto"
    _VALID_LOSSES = ...

    def __init__(
        self,
        loss: Literal["log_loss", "auto", "binary_crossentropy", "categorical_crossentropy"] = "log_loss",
        *,
        learning_rate: float = 0.1,
        max_iter: int = 100,
        max_leaf_nodes: int | None = 31,
        max_depth: int | None = None,
        min_samples_leaf: int = 20,
        l2_regularization: float = 0.0,
        max_bins: int = 255,
        categorical_features: ArrayLike | None = None,
        monotonic_cst: ArrayLike | None = None,
        warm_start: bool = False,
        early_stopping: bool | Literal["auto"] = "auto",
        scoring: str | Callable | None = "loss",
        validation_fraction: int | float | None = 0.1,
        n_iter_no_change: int = 10,
        tol: float = 1e-7,
        verbose: int = 0,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def predict(self, X: ArrayLike) -> NDArray: ...
    def staged_predict(self, X: ArrayLike): ...
    def predict_proba(self, X: ArrayLike) -> NDArray: ...
    def staged_predict_proba(self, X: ArrayLike): ...
    def decision_function(self, X: ArrayLike) -> NDArray: ...
    def staged_decision_function(self, X: ArrayLike): ...
    def _encode_y(self, y: ndarray) -> ndarray: ...
    def _get_loss(self, sample_weight: None) -> HalfBinomialLoss: ...
