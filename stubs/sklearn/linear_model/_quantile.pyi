from numbers import Real as Real
from typing import ClassVar, Literal, TypeVar

from numpy import ndarray
from scipy import sparse as sparse
from scipy.optimize import linprog as linprog

from .._typing import ArrayLike, Float, MatrixLike
from ..base import BaseEstimator, RegressorMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils._param_validation import Hidden as Hidden, Interval as Interval, StrOptions as StrOptions
from ._base import LinearModel

QuantileRegressor_Self = TypeVar("QuantileRegressor_Self", bound=QuantileRegressor)

# Authors: David Dale <dale.david@mail.ru>
#          Christian Lorentzen <lorentzen.ch@gmail.com>
# License: BSD 3 clause
import warnings

import numpy as np

class QuantileRegressor(LinearModel, RegressorMixin, BaseEstimator):
    n_iter_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    intercept_: float = ...
    coef_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        quantile: Float = 0.5,
        alpha: Float = 1.0,
        fit_intercept: bool = True,
        solver: Literal[
            "highs-ds",
            "highs-ipm",
            "highs",
            "interior-point",
            "revised simplex",
            "warn",
        ] = "warn",
        solver_options: None | dict = None,
    ) -> None: ...
    def fit(
        self: QuantileRegressor_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> QuantileRegressor_Self: ...
