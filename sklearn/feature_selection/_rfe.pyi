from collections.abc import Generator, Iterable
from typing import Dict, Union, Callable, Any
from numpy.typing import NDArray, ArrayLike

# Authors: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Vincent Michel <vincent.michel@inria.fr>
#          Gilles Louppe <g.louppe@gmail.com>
#
# License: BSD 3 clause

import numpy as np
import numbers

from ..utils.metaestimators import available_if
from ..utils.metaestimators import _safe_split
from ..utils._tags import _safe_tags
from ..utils.validation import check_is_fitted
from ..utils.fixes import delayed
from ..utils.deprecation import deprecated
from ..base import BaseEstimator
from ..base import MetaEstimatorMixin
from ..base import clone
from ..base import is_classifier
from ..model_selection import check_cv
from ..model_selection._validation import _score
from ..metrics import check_scoring
from ._base import SelectorMixin
from ._base import _get_feature_importances
from numpy import ndarray
from sklearn.linear_model._logistic import LogisticRegression
from sklearn.svm._classes import SVC

def _rfe_single_fit(rfe, estimator, X, y, train, test, scorer): ...
def _estimator_has(attr: str) -> Callable: ...

class RFE(SelectorMixin, MetaEstimatorMixin, BaseEstimator):
    def __init__(
        self,
        estimator: BaseEstimator,
        *,
        n_features_to_select: int | float | None = None,
        step: int | float = 1,
        verbose: int = 0,
        importance_getter: str | Callable = "auto",
    ) -> None: ...
    @property
    def _estimator_type(self): ...
    @property
    def classes_(self) -> NDArray: ...
    def fit(self, X: NDArray | ArrayLike, y: ArrayLike, **fit_params) -> "RFE": ...
    def _fit(self, X: ndarray, y: ndarray, step_score: None = None, **fit_params) -> "RFE": ...
    @available_if(_estimator_has("predict"))
    def predict(self, X: ArrayLike) -> ArrayLike: ...
    @available_if(_estimator_has("score"))
    def score(self, X: ArrayLike, y: ArrayLike, **fit_params) -> float: ...
    def _get_support_mask(self) -> ndarray: ...
    @available_if(_estimator_has("decision_function"))
    def decision_function(self, X: ArrayLike) -> NDArray | tuple: ...
    @available_if(_estimator_has("predict_proba"))
    def predict_proba(self, X: ArrayLike) -> ArrayLike: ...
    @available_if(_estimator_has("predict_log_proba"))
    def predict_log_proba(self, X: ArrayLike) -> ArrayLike: ...
    def _more_tags(self) -> Dict[str, bool]: ...

class RFECV(RFE):
    def __init__(
        self,
        estimator: BaseEstimator,
        *,
        step: int | float = 1,
        min_features_to_select: int = 1,
        cv: int | Generator | Iterable | None = None,
        scoring: str | Callable | None = None,
        verbose: int = 0,
        n_jobs: int | None = None,
        importance_getter: str | Callable = "auto",
    ) -> None: ...
    def fit(self, X: NDArray | ArrayLike, y: ArrayLike, groups: ArrayLike | None = None) -> "RFECV": ...

    # TODO: Remove in v1.2 when grid_scores_ is removed
    # mypy error: Decorated property not supported
    @deprecated(  # type: ignore
        "The `grid_scores_` attribute is deprecated in version 1.0 in favor "
        "of `cv_results_` and will be removed in version 1.2."
    )
    @property
    def grid_scores_(self): ...
