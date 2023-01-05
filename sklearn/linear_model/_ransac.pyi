from numpy import int64, ndarray
from typing import Any, Callable
from numpy.typing import ArrayLike, NDArray
from numpy.random import RandomState

# Author: Johannes Schönberger
#
# License: BSD 3 clause

import numpy as np
import warnings

from ..base import BaseEstimator, MetaEstimatorMixin, RegressorMixin, clone
from ..base import MultiOutputMixin
from ..utils import check_random_state, check_consistent_length

from ..utils.validation import check_is_fitted, _check_sample_weight
from ._base import LinearRegression
from ..utils.validation import has_fit_parameter
from ..exceptions import ConvergenceWarning

_EPSILON = ...

def _dynamic_max_trials(n_inliers: int64, n_samples: int, min_samples: int, probability: float) -> float: ...

class RANSACRegressor(MetaEstimatorMixin, RegressorMixin, MultiOutputMixin, BaseEstimator):
    def __init__(
        self,
        estimator: None = None,
        *,
        min_samples: int | float | None = None,
        residual_threshold: float | None = None,
        is_data_valid: Callable | None = None,
        is_model_valid: Callable | None = None,
        max_trials: int = 100,
        max_skips: int = ...,
        stop_n_inliers: int = ...,
        stop_score: float = ...,
        stop_probability: float = 0.99,
        loss: str | Callable = "absolute_error",
        random_state: int | RandomState | None = None,
        base_estimator: Any = "deprecated",
    ) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> "RANSACRegressor": ...
    def predict(self, X: ArrayLike) -> NDArray | tuple[int, int]: ...
    def score(self, X: ArrayLike, y: ArrayLike) -> float: ...
    def _more_tags(self): ...
