from typing import Any
from numpy.typing import ArrayLike, NDArray

# Author: Lars Buitinck
# License: 3-clause BSD

import numpy as np
from ..base import BaseEstimator
from ._base import SelectorMixin
from ..utils.sparsefuncs import mean_variance_axis, min_max_axis
from ..utils.validation import check_is_fitted

class VarianceThreshold(SelectorMixin, BaseEstimator):
    def __init__(self, threshold: float = 0.0): ...
    def fit(self, X: NDArray | ArrayLike, y: Any = None) -> Any: ...
    def _get_support_mask(self): ...
    def _more_tags(self): ...
