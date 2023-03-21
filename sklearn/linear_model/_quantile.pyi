from typing import ClassVar, Literal, TypeVar
from scipy import sparse as sparse
from ._base import LinearModel
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from numpy import ndarray
from scipy.optimize import linprog as linprog
from numbers import Real as Real
from ..base import BaseEstimator, RegressorMixin
from .._typing import Float, MatrixLike, ArrayLike
from ..utils.fixes import sp_version as sp_version, parse_version as parse_version

QuantileRegressor_Self = TypeVar("QuantileRegressor_Self", bound="QuantileRegressor")

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
    ) -> None:
        ...

    def fit(
        self: QuantileRegressor_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> QuantileRegressor_Self:
        ...
