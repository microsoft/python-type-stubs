from typing import Literal, Mapping, Any
from numpy.typing import ArrayLike, NDArray

# Authors: David Dale <dale.david@mail.ru>
#          Christian Lorentzen <lorentzen.ch@gmail.com>
# License: BSD 3 clause
import warnings

import numpy as np
from scipy import sparse
from scipy.optimize import linprog

from ..base import BaseEstimator, RegressorMixin
from ._base import LinearModel
from ..exceptions import ConvergenceWarning
from ..utils import _safe_indexing
from ..utils.validation import _check_sample_weight
from ..utils.fixes import sp_version, parse_version
from numpy import ndarray

class QuantileRegressor(LinearModel, RegressorMixin, BaseEstimator):
    def __init__(
        self,
        *,
        quantile: float = 0.5,
        alpha: float = 1.0,
        fit_intercept: bool = True,
        solver: Literal["highs-ds", "highs-ipm", "highs", "interior-point", "revised simplex"] = "interior-point",
        solver_options: Mapping | None = None,
    ) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> "QuantileRegressor": ...
