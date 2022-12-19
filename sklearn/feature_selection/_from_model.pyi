from typing import Optional, Any, Callable
from numpy.typing import ArrayLike

# Authors: Gilles Louppe, Mathieu Blondel, Maheshakya Wijewardena
# License: BSD 3 clause

from copy import deepcopy

import numpy as np
import numbers

from ._base import SelectorMixin
from ._base import _get_feature_importances
from ..base import BaseEstimator, clone, MetaEstimatorMixin
from ..utils._tags import _safe_tags
from ..utils.validation import check_is_fitted, check_scalar, _num_features

from ..exceptions import NotFittedError
from ..utils.metaestimators import available_if
from numpy import float64, ndarray
from sklearn.linear_model._ridge import RidgeCV

def _calculate_threshold(estimator: RidgeCV, importances: ndarray, threshold: float64) -> float: ...
def _estimator_has(attr: str) -> Callable: ...

class SelectFromModel(MetaEstimatorMixin, SelectorMixin, BaseEstimator):
    def __init__(
        self,
        estimator: RidgeCV,
        *,
        threshold: str | float | None = None,
        prefit: bool = False,
        norm_order: int = 1,
        max_features: int | Callable | None = None,
        importance_getter: str | Callable = "auto",
    ) -> None: ...
    def _get_support_mask(self) -> ndarray: ...
    def _check_max_features(self, X: ndarray) -> None: ...
    def fit(self, X: ArrayLike, y: ArrayLike | None = None, **fit_params) -> "SelectFromModel": ...
    @property
    def threshold_(self): ...
    @available_if(_estimator_has("partial_fit"))
    def partial_fit(self, X: ArrayLike, y: ArrayLike | None = None, **fit_params) -> Any: ...
    @property
    def n_features_in_(self): ...
    def _more_tags(self): ...
