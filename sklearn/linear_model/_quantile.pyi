from typing import Any, Literal
from ..utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from .._typing import Float, ArrayLike, MatrixLike
from scipy import sparse as sparse
from ..base import BaseEstimator, RegressorMixin
from ._base import LinearModel
from numbers import Real as Real
from scipy.optimize import linprog as linprog
from ..utils.fixes import sp_version as sp_version, parse_version as parse_version

# Authors: David Dale <dale.david@mail.ru>
#          Christian Lorentzen <lorentzen.ch@gmail.com>
# License: BSD 3 clause
import warnings

import numpy as np


class QuantileRegressor(LinearModel, RegressorMixin, BaseEstimator):

    _parameter_constraints: dict = ...

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
        solver_options: dict | None = None,
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...
