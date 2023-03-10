from typing import Any, Callable, Iterable
from .._typing import Estimator, Int, ArrayLike, MatrixLike
from ..model_selection import BaseCrossValidator
from ..utils._param_validation import HasMethods as HasMethods, Interval as Interval
from ..model_selection import check_cv as check_cv
from joblib import effective_n_jobs as effective_n_jobs
from ._base import SelectorMixin
from ..svm._classes import SVC
from ..metrics import check_scoring as check_scoring
from ..utils.validation import check_is_fitted as check_is_fitted
from numpy import ndarray
from ..linear_model._logistic import LogisticRegression
from collections.abc import Iterable
from ..base import (
    BaseEstimator,
    MetaEstimatorMixin,
    clone as clone,
    is_classifier as is_classifier,
)
from numbers import Integral as Integral, Real as Real
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from ..utils.metaestimators import available_if as available_if

# Authors: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Vincent Michel <vincent.michel@inria.fr>
#          Gilles Louppe <g.louppe@gmail.com>
#
# License: BSD 3 clause


import numpy as np


class RFE(SelectorMixin, MetaEstimatorMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        estimator: SVC | Estimator | LogisticRegression,
        *,
        n_features_to_select: int | float | None = None,
        step: int | float = 1,
        verbose: Int = 0,
        importance_getter: str | Callable = "auto",
    ) -> None:
        ...

    @property
    def classes_(self) -> ndarray:
        ...

    def fit(self, X: MatrixLike | ArrayLike, y: ArrayLike, **fit_params) -> Any:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...

    def score(self, X: MatrixLike, y: ArrayLike, **fit_params) -> float:
        ...

    def decision_function(self, X: MatrixLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike) -> ndarray:
        ...

    def predict_log_proba(self, X: MatrixLike) -> ndarray:
        ...


class RFECV(RFE):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        estimator: Estimator | LogisticRegression,
        *,
        step: int | float = 1,
        min_features_to_select: Int = 1,
        cv: Iterable | BaseCrossValidator | int | None = None,
        scoring: str | None | Callable = None,
        verbose: Int = 0,
        n_jobs: int | None = None,
        importance_getter: str | Callable = "auto",
    ) -> None:
        ...

    def fit(
        self, X: MatrixLike | ArrayLike, y: ArrayLike, groups: None | ArrayLike = None
    ) -> Any:
        ...
