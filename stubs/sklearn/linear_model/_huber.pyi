from numbers import Integral as Integral, Real as Real
from typing import ClassVar, TypeVar

from numpy import ndarray
from scipy import optimize as optimize

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, RegressorMixin
from ..utils import axis0_safe_slice as axis0_safe_slice
from ..utils._param_validation import Interval as Interval
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from ._base import LinearModel

HuberRegressor_Self = TypeVar("HuberRegressor_Self", bound=HuberRegressor)

# Authors: Manoj Kumar mks542@nyu.edu
# License: BSD 3 clause

import numpy as np

class HuberRegressor(LinearModel, RegressorMixin, BaseEstimator):
    outliers_: ndarray = ...
    n_iter_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    scale_: float = ...
    intercept_: float = ...
    coef_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        epsilon: Float = 1.35,
        max_iter: Int = 100,
        alpha: Float = 0.0001,
        warm_start: bool = False,
        fit_intercept: bool = True,
        tol: Float = 1e-05,
    ) -> None: ...
    def fit(
        self: HuberRegressor_Self,
        X: MatrixLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> HuberRegressor_Self: ...
