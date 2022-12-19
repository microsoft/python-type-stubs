from collections.abc import Generator, Iterable
from typing import Dict, Optional, Tuple, Union, Literal, Any, Callable
from numpy.typing import ArrayLike
import numbers

import numpy as np

import warnings

from ._base import SelectorMixin
from ..base import BaseEstimator, MetaEstimatorMixin, clone
from ..utils._tags import _safe_tags
from ..utils.validation import check_is_fitted
from ..model_selection import cross_val_score
from numpy import float64, int64, ndarray
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from sklearn.linear_model._ridge import RidgeCV
from sklearn.neighbors._classification import KNeighborsClassifier

class SequentialFeatureSelector(SelectorMixin, MetaEstimatorMixin, BaseEstimator):
    def __init__(
        self,
        estimator: BaseEstimator,
        *,
        n_features_to_select: int | float | Literal["auto", "warn"] = "warn",
        tol: float | None = None,
        direction: Literal["forward", "backward"] = "forward",
        scoring: str | Callable | list | tuple | dict | None = None,
        cv: int | Generator | Iterable = 5,
        n_jobs: int | None = None,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: ArrayLike | None = None) -> "SequentialFeatureSelector": ...
    def _get_best_new_feature_score(
        self,
        estimator: Union[RidgeCV, KNeighborsClassifier],
        X: ndarray,
        y: Union[ndarray, Series],
        current_mask: ndarray,
    ) -> Tuple[int64, float64]: ...
    def _get_support_mask(self) -> ndarray: ...
    def _more_tags(self) -> Dict[str, bool]: ...
