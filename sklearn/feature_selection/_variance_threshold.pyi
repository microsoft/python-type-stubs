from typing import Any
from ..utils._param_validation import Interval as Interval
from .._typing import Float, MatrixLike
from ..base import BaseEstimator
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import SelectorMixin
from numbers import Real as Real
from ..utils.sparsefuncs import (
    mean_variance_axis as mean_variance_axis,
    min_max_axis as min_max_axis,
)

# Author: Lars Buitinck
# License: 3-clause BSD

import numpy as np


class VarianceThreshold(SelectorMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(self, threshold: Float = 0.0) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...
