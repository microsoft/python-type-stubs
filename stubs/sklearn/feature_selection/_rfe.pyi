from numbers import Integral as Integral, Real as Real
from typing import Callable, ClassVar, Iterable, TypeVar

from joblib import effective_n_jobs as effective_n_jobs
from numpy import ndarray

from .._typing import ArrayLike, Int, MatrixLike
from ..base import BaseEstimator, MetaEstimatorMixin, clone as clone, is_classifier as is_classifier
from ..linear_model._logistic import LogisticRegression
from ..metrics import check_scoring as check_scoring
from ..model_selection import BaseCrossValidator, check_cv as check_cv
from ..model_selection._split import BaseShuffleSplit
from ..utils._param_validation import HasMethods as HasMethods, Interval as Interval
from ..utils.metaestimators import available_if as available_if
from ..utils.parallel import Parallel as Parallel, delayed as delayed
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import SelectorMixin

RFECV_Self = TypeVar("RFECV_Self", bound="RFECV")
RFE_Self = TypeVar("RFE_Self", bound="RFE")

# Authors: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Vincent Michel <vincent.michel@inria.fr>
#          Gilles Louppe <g.louppe@gmail.com>
#
# License: BSD 3 clause

import numpy as np

class RFE(SelectorMixin, MetaEstimatorMixin, BaseEstimator):
    support_: ndarray = ...
    ranking_: ndarray = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_features_: int = ...
    estimator_: BaseEstimator = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        estimator: BaseEstimator,
        *,
        n_features_to_select: float | None | int = None,
        step: float | int = 1,
        verbose: Int = 0,
        importance_getter: str | Callable = "auto",
    ) -> None: ...
    @property
    def classes_(self) -> ndarray: ...
    def fit(self: RFE_Self, X: MatrixLike | ArrayLike, y: ArrayLike, **fit_params) -> RFE_Self: ...
    def predict(self, X: MatrixLike) -> ndarray: ...
    def score(self, X: MatrixLike, y: ArrayLike, **fit_params) -> float: ...
    def decision_function(self, X: MatrixLike) -> ndarray: ...
    def predict_proba(self, X: MatrixLike) -> ndarray: ...
    def predict_log_proba(self, X: MatrixLike) -> ndarray: ...

class RFECV(RFE):
    support_: ndarray = ...
    ranking_: ndarray = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_features_: int = ...
    cv_results_: dict[str, ndarray] = ...
    estimator_: BaseEstimator = ...
    classes_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        estimator: BaseEstimator | LogisticRegression,
        *,
        step: float | int = 1,
        min_features_to_select: Int = 1,
        cv: int | BaseCrossValidator | Iterable | None | BaseShuffleSplit = None,
        scoring: None | str | Callable = None,
        verbose: Int = 0,
        n_jobs: None | int = None,
        importance_getter: str | Callable = "auto",
    ) -> None: ...
    def fit(
        self: RFECV_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        groups: None | ArrayLike = None,
    ) -> RFECV_Self: ...
