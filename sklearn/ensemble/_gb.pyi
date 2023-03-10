from typing import Any, Callable, Iterator, Literal
from .._typing import Int, Estimator, ArrayLike, MatrixLike, Float
from time import time as time
from scipy.sparse import (
    csc_matrix as csc_matrix,
    csr_matrix as csr_matrix,
    issparse as issparse,
)
from ..utils._param_validation import (
    HasMethods as HasMethods,
    Interval as Interval,
    StrOptions as StrOptions,
)
from ..model_selection import train_test_split as train_test_split
from abc import ABCMeta, abstractmethod
from ._base import BaseEnsemble
from ..utils import (
    deprecated,
    check_array as check_array,
    check_random_state as check_random_state,
    column_or_1d as column_or_1d,
)
from ._gradient_boosting import (
    predict_stages as predict_stages,
    predict_stage as predict_stage,
)
from ..utils.validation import check_is_fitted as check_is_fitted
from ..tree._tree import DTYPE as DTYPE, DOUBLE as DOUBLE
from numpy import ndarray
from numpy.random import RandomState
from ..exceptions import NotFittedError as NotFittedError
from ..utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from ..base import ClassifierMixin, RegressorMixin, is_classifier as is_classifier
from ..tree import DecisionTreeRegressor as DecisionTreeRegressor
from numbers import Integral as Integral, Real as Real
import warnings

import numpy as np


class VerboseReporter:
    def __init__(self, verbose: Int) -> None:
        ...

    def init(self, est: Estimator, begin_at_stage: Int = 0):
        ...

    def update(self, j: Int, est: Estimator):
        ...


class BaseGradientBoosting(BaseEnsemble, metaclass=ABCMeta):

    _parameter_constraints: dict = ...

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
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
        monitor: None | Callable = None,
    ) -> Any:
        ...

    @property
    def feature_importances_(self) -> ndarray:
        ...

    def apply(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    # TODO(1.3): Remove
    # mypy error: Decorated property not supported
    @deprecated(  # type: ignore
        "Attribute `loss_` was deprecated in version 1.1 and will be removed in 1.3."
    )
    @property
    def loss_(self):
        ...


class GradientBoostingClassifier(ClassifierMixin, BaseGradientBoosting):

    # TODO(1.3): remove "deviance"
    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        loss: Literal["log_loss", "deviance", "exponential", "log_loss"] = "log_loss",
        learning_rate: Float = 0.1,
        n_estimators: Int = 100,
        subsample: Float = 1.0,
        criterion: Literal[
            "friedman_mse", "squared_error", "friedman_mse"
        ] = "friedman_mse",
        min_samples_split: int | float = 2,
        min_samples_leaf: int | float = 1,
        min_weight_fraction_leaf: Float = 0.0,
        max_depth: int | None = 3,
        min_impurity_decrease: Float = 0.0,
        init: Estimator | str | None = None,
        random_state: RandomState | None | Int = None,
        max_features: Literal["auto", "sqrt", "log2"] | int | float | None = None,
        verbose: Int = 0,
        max_leaf_nodes: None | Int = None,
        warm_start: bool = False,
        validation_fraction: Float = 0.1,
        n_iter_no_change: None | Int = None,
        tol: Float = 1e-4,
        ccp_alpha: float = 0.0,
    ) -> None:
        ...

    def decision_function(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def staged_decision_function(self, X: MatrixLike | ArrayLike):
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def staged_predict(self, X: MatrixLike | ArrayLike):
        ...

    def predict_proba(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def predict_log_proba(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def staged_predict_proba(self, X: MatrixLike | ArrayLike) -> Iterator[ndarray]:
        ...


class GradientBoostingRegressor(RegressorMixin, BaseGradientBoosting):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        loss: Literal[
            "squared_error", "absolute_error", "huber", "quantile", "squared_error"
        ] = "squared_error",
        learning_rate: Float = 0.1,
        n_estimators: Int = 100,
        subsample: Float = 1.0,
        criterion: Literal[
            "friedman_mse", "squared_error", "friedman_mse"
        ] = "friedman_mse",
        min_samples_split: int | float = 2,
        min_samples_leaf: int | float = 1,
        min_weight_fraction_leaf: Float = 0.0,
        max_depth: int | None = 3,
        min_impurity_decrease: Float = 0.0,
        init: Estimator | str | None = None,
        random_state: RandomState | None | Int = None,
        max_features: Literal["auto", "sqrt", "log2"] | int | float | None = None,
        alpha: Float = 0.9,
        verbose: Int = 0,
        max_leaf_nodes: None | Int = None,
        warm_start: bool = False,
        validation_fraction: Float = 0.1,
        n_iter_no_change: None | Int = None,
        tol: Float = 1e-4,
        ccp_alpha: float = 0.0,
    ) -> None:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def staged_predict(self, X: MatrixLike | ArrayLike) -> Iterator[ndarray]:
        ...

    def apply(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...
