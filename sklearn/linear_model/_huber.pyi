from typing import Optional, Tuple, Union, Any
from numpy.typing import ArrayLike

# Authors: Manoj Kumar mks542@nyu.edu
# License: BSD 3 clause

import numpy as np

from scipy import optimize

from ..base import BaseEstimator, RegressorMixin
from ._base import LinearModel
from ..utils import axis0_safe_slice
from ..utils.validation import _check_sample_weight
from ..utils.extmath import safe_sparse_dot
from ..utils.optimize import _check_optimize_result
from numpy import float64, ndarray

def _huber_loss_and_gradient(
    w: ndarray,
    X: ndarray,
    y: ndarray,
    epsilon: Union[int, float],
    alpha: float,
    sample_weight: Optional[ndarray] = None,
) -> Tuple[float64, ndarray]: ...

class HuberRegressor(LinearModel, RegressorMixin, BaseEstimator):
    def __init__(
        self,
        *,
        epsilon: float = 1.35,
        max_iter: int = 100,
        alpha: float = 0.0001,
        warm_start: bool = False,
        fit_intercept: bool = True,
        tol: float = 1e-05,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: ArrayLike, sample_weight: ArrayLike | None = None) -> "HuberRegressor": ...
