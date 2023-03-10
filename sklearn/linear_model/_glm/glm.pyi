from typing import Any, Literal
from ...base import BaseEstimator, RegressorMixin
from ..._typing import Float, Int, ArrayLike, MatrixLike
from ...utils.validation import check_is_fitted as check_is_fitted
from ._newton_solver import NewtonCholeskySolver as NewtonCholeskySolver, NewtonSolver
from .._linear_loss import LinearModelLoss as LinearModelLoss
from ..._loss.glm_distribution import TweedieDistribution as TweedieDistribution
from ...utils import check_array as check_array, deprecated
from ...utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from numpy import ndarray
from numbers import Integral as Integral, Real as Real
from ..._loss.loss import (
    HalfGammaLoss as HalfGammaLoss,
    HalfPoissonLoss as HalfPoissonLoss,
    HalfSquaredError as HalfSquaredError,
    HalfTweedieLoss as HalfTweedieLoss,
    HalfTweedieLossIdentity as HalfTweedieLossIdentity,
)

import numpy as np
import scipy.optimize


class _GeneralizedLinearRegressor(RegressorMixin, BaseEstimator):

    # We allow for NewtonSolver classes for the "solver" parameter but do not
    # make them public in the docstrings. This facilitates testing and
    # benchmarking.
    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        alpha: Float = 1.0,
        fit_intercept: bool = True,
        solver: Literal["lbfgs", "newton-cholesky", "lbfgs"] = "lbfgs",
        max_iter: Int = 100,
        tol: Float = 1e-4,
        warm_start: bool = False,
        verbose: Int = 0,
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def score(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Float:
        ...

    # TODO(1.3): remove
    @deprecated(  # type: ignore
        "Attribute `family` was deprecated in version 1.1 and will be removed in 1.3."
    )
    @property
    def family(self):
        ...


class PoissonRegressor(_GeneralizedLinearRegressor):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        alpha: Float = 1.0,
        fit_intercept: bool = True,
        solver: Literal["lbfgs", "newton-cholesky", "lbfgs"] = "lbfgs",
        max_iter: Int = 100,
        tol: Float = 1e-4,
        warm_start: bool = False,
        verbose: Int = 0,
    ) -> None:
        ...


class GammaRegressor(_GeneralizedLinearRegressor):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        alpha: Float = 1.0,
        fit_intercept: bool = True,
        solver: Literal["lbfgs", "newton-cholesky", "lbfgs"] = "lbfgs",
        max_iter: Int = 100,
        tol: Float = 1e-4,
        warm_start: bool = False,
        verbose: Int = 0,
    ) -> None:
        ...


class TweedieRegressor(_GeneralizedLinearRegressor):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        power: Float = 0.0,
        alpha: Float = 1.0,
        fit_intercept: bool = True,
        link: Literal["auto", "identity", "log", "auto"] = "auto",
        solver: Literal["lbfgs", "newton-cholesky", "lbfgs"] = "lbfgs",
        max_iter: Int = 100,
        tol: Float = 1e-4,
        warm_start: bool = False,
        verbose: Int = 0,
    ) -> None:
        ...
