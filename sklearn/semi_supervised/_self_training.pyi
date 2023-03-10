from typing import Any, Literal
from ..utils._param_validation import (
    HasMethods as HasMethods,
    Interval as Interval,
    StrOptions as StrOptions,
)
from .._typing import Estimator, Float, Int, ArrayLike, MatrixLike
from ..base import MetaEstimatorMixin, clone as clone, BaseEstimator
from ..utils.validation import check_is_fitted as check_is_fitted
from numpy import ndarray
from ..utils import safe_mask as safe_mask
from ..svm._classes import SVC
from numbers import Integral as Integral, Real as Real
from ..utils.metaestimators import available_if as available_if
from ..linear_model._stochastic_gradient import SGDClassifier
import warnings

import numpy as np

__all__ = ["SelfTrainingClassifier"]


class SelfTrainingClassifier(MetaEstimatorMixin, BaseEstimator):

    _estimator_type: str = ...

    _parameter_constraints: dict = ...

    def __init__(
        self,
        base_estimator: SVC | Estimator | SGDClassifier,
        threshold: Float = 0.75,
        criterion: Literal["threshold", "k_best", "threshold"] = "threshold",
        k_best: Int = 10,
        max_iter: int | None = 10,
        verbose: bool = False,
    ) -> None:
        ...

    def fit(self, X: MatrixLike | ArrayLike, y: ArrayLike) -> Any:
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
