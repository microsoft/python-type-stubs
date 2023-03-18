from typing import Any, Callable, ClassVar, TypeVar
from numpy.random import RandomState
from ._base import LinearRegression as LinearRegression
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils._param_validation import (
    Interval as Interval,
    Options as Options,
    StrOptions as StrOptions,
    HasMethods as HasMethods,
    Hidden as Hidden,
)
from numpy import ndarray
from numbers import Integral as Integral, Real as Real
from ..base import (
    BaseEstimator,
    MetaEstimatorMixin,
    RegressorMixin,
    clone as clone,
    MultiOutputMixin,
)
from ..utils.random import sample_without_replacement as sample_without_replacement
from .._typing import Float, Int, MatrixLike, ArrayLike
from ..utils import (
    check_random_state as check_random_state,
    check_consistent_length as check_consistent_length,
)
from ..utils.validation import (
    check_is_fitted as check_is_fitted,
    has_fit_parameter as has_fit_parameter,
)

RANSACRegressor_Self = TypeVar("RANSACRegressor_Self", bound="RANSACRegressor")

# Author: Johannes Schönberger
#
# License: BSD 3 clause

import warnings

import numpy as np

_EPSILON = ...


class RANSACRegressor(
    MetaEstimatorMixin, RegressorMixin, MultiOutputMixin, BaseEstimator
):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_skips_invalid_model_: int = ...
    n_skips_invalid_data_: int = ...
    n_skips_no_inliers_: int = ...
    inlier_mask_: ndarray = ...
    n_trials_: int = ...
    estimator_: Any = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        estimator: Any = None,
        *,
        min_samples: float | None | int = None,
        residual_threshold: None | Float = None,
        is_data_valid: None | Callable = None,
        is_model_valid: None | Callable = None,
        max_trials: Int = 100,
        max_skips: Int = ...,
        stop_n_inliers: Int = ...,
        stop_score: Float = ...,
        stop_probability: float = 0.99,
        loss: str | Callable = "absolute_error",
        random_state: RandomState | None | Int = None,
        base_estimator: Any = "deprecated",
    ) -> None:
        ...

    def fit(
        self: RANSACRegressor_Self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> RANSACRegressor_Self:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...

    def score(self, X: MatrixLike, y: MatrixLike | ArrayLike) -> float:
        ...
