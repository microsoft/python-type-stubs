from typing import Any, ClassVar, TypeVar
from ..utils.sparsefuncs import (
    mean_variance_axis as mean_variance_axis,
    min_max_axis as min_max_axis,
)
from ._base import SelectorMixin
from numpy import ndarray
from ..utils._param_validation import Interval as Interval
from numbers import Real as Real
from ..base import BaseEstimator
from .._typing import Float, MatrixLike
from ..utils.validation import check_is_fitted as check_is_fitted

VarianceThreshold_Self = TypeVar("VarianceThreshold_Self", bound="VarianceThreshold")

# Author: Lars Buitinck
# License: 3-clause BSD

import numpy as np


class VarianceThreshold(SelectorMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    variances_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(self, threshold: Float = 0.0) -> None:
        ...

    def fit(
        self: VarianceThreshold_Self, X: MatrixLike, y: Any = None
    ) -> VarianceThreshold_Self:
        ...
