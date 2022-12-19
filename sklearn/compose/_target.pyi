from typing import Any, Callable
from numpy.typing import ArrayLike, NDArray

# Authors: Andreas Mueller <andreas.mueller@columbia.edu>
#          Guillaume Lemaitre <guillaume.lemaitre@inria.fr>
# License: BSD 3 clause

import warnings

import numpy as np

from ..base import BaseEstimator, RegressorMixin, clone
from ..utils.validation import check_is_fitted
from ..utils._tags import _safe_tags
from ..utils import check_array, _safe_indexing
from ..preprocessing import FunctionTransformer
from ..exceptions import NotFittedError

__all__ = ["TransformedTargetRegressor"]

class TransformedTargetRegressor(RegressorMixin, BaseEstimator):
    def __init__(
        self,
        regressor: Any = None,
        *,
        transformer: Any = None,
        func: Callable | None = None,
        inverse_func: Callable | None = None,
        check_inverse: bool = True,
    ): ...
    def _fit_transformer(self, y): ...
    def fit(self, X: NDArray | ArrayLike, y: ArrayLike, **fit_params) -> Any: ...
    def predict(self, X: NDArray | ArrayLike, **predict_params) -> NDArray: ...
    def _more_tags(self): ...
    @property
    def n_features_in_(self): ...
