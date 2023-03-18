from typing import ClassVar, Literal, TypeVar
from ..base import BaseEstimator
from numpy import ndarray
from ..utils._param_validation import (
    HasMethods as HasMethods,
    Interval as Interval,
    StrOptions as StrOptions,
)
from numbers import Integral as Integral, Real as Real
from ..utils.metaestimators import available_if as available_if
from ..base import MetaEstimatorMixin, clone as clone
from .._typing import Float, Int, MatrixLike, ArrayLike
from ..utils import safe_mask as safe_mask
from ..utils.validation import check_is_fitted as check_is_fitted

SelfTrainingClassifier_Self = TypeVar(
    "SelfTrainingClassifier_Self", bound="SelfTrainingClassifier"
)

import warnings

import numpy as np

__all__ = ["SelfTrainingClassifier"]


class SelfTrainingClassifier(MetaEstimatorMixin, BaseEstimator):
    termination_condition_: Literal["max_iter", "no_change", "all_labeled"] = ...
    n_iter_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    labeled_iter_: ndarray = ...
    transduction_: ndarray = ...
    classes_: ndarray | list[ndarray] = ...
    base_estimator_: BaseEstimator = ...

    _estimator_type: ClassVar[str] = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        base_estimator: BaseEstimator,
        threshold: Float = 0.75,
        criterion: Literal["threshold", "k_best", "threshold"] = "threshold",
        k_best: Int = 10,
        max_iter: None | int = 10,
        verbose: bool = False,
    ) -> None:
        ...

    def fit(
        self: SelfTrainingClassifier_Self, X: MatrixLike | ArrayLike, y: ArrayLike
    ) -> SelfTrainingClassifier_Self:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def decision_function(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def predict_log_proba(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def score(self, X: MatrixLike | ArrayLike, y: ArrayLike) -> float:
        ...
