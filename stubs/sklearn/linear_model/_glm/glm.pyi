from numbers import Integral as Integral, Real as Real
from typing import ClassVar, Literal, TypeVar

from numpy import ndarray

from ..._loss.glm_distribution import TweedieDistribution as TweedieDistribution
from ..._loss.loss import (
    BaseLoss,
    HalfGammaLoss as HalfGammaLoss,
    HalfPoissonLoss as HalfPoissonLoss,
    HalfSquaredError as HalfSquaredError,
    HalfTweedieLoss as HalfTweedieLoss,
    HalfTweedieLossIdentity as HalfTweedieLossIdentity,
)
from ..._typing import ArrayLike, Float, Int, MatrixLike
from ...base import BaseEstimator, RegressorMixin
from ...utils import check_array as check_array, deprecated
from ...utils._param_validation import Hidden as Hidden, Interval as Interval, StrOptions as StrOptions
from ...utils.validation import check_is_fitted as check_is_fitted
from .._linear_loss import LinearModelLoss as LinearModelLoss
from ._newton_solver import NewtonCholeskySolver as NewtonCholeskySolver, NewtonSolver

_GeneralizedLinearRegressor_Self = TypeVar("_GeneralizedLinearRegressor_Self", bound=_GeneralizedLinearRegressor)

import numpy as np
import scipy.optimize

class _GeneralizedLinearRegressor(RegressorMixin, BaseEstimator):
    _base_loss: BaseLoss = ...
    n_iter_: int = ...
    intercept_: float = ...
    coef_: ndarray = ...

    # We allow for NewtonSolver classes for the "solver" parameter but do not
    # make them public in the docstrings. This facilitates testing and
    # benchmarking.
    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        alpha: Float = 1.0,
        fit_intercept: bool = True,
        solver: Literal["lbfgs", "newton-cholesky"] = "lbfgs",
        max_iter: Int = 100,
        tol: Float = 1e-4,
        warm_start: bool = False,
        verbose: Int = 0,
    ) -> None: ...
    def fit(
        self: _GeneralizedLinearRegressor_Self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> _GeneralizedLinearRegressor_Self: ...
    def predict(self, X: MatrixLike | ArrayLike) -> ndarray: ...
    def score(
        self,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Float: ...

    # TODO(1.3): remove
    @deprecated("Attribute `family` was deprecated in version 1.1 and will be removed in 1.3.")  # type: ignore
    def family(self): ...

class PoissonRegressor(_GeneralizedLinearRegressor):
    n_iter_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    intercept_: float = ...
    coef_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        alpha: Float = 1.0,
        fit_intercept: bool = True,
        solver: Literal["lbfgs", "newton-cholesky"] = "lbfgs",
        max_iter: Int = 100,
        tol: Float = 1e-4,
        warm_start: bool = False,
        verbose: Int = 0,
    ) -> None: ...

class GammaRegressor(_GeneralizedLinearRegressor):
    feature_names_in_: ndarray = ...
    n_iter_: int = ...
    n_features_in_: int = ...
    intercept_: float = ...
    coef_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        alpha: Float = 1.0,
        fit_intercept: bool = True,
        solver: Literal["lbfgs", "newton-cholesky"] = "lbfgs",
        max_iter: Int = 100,
        tol: Float = 1e-4,
        warm_start: bool = False,
        verbose: Int = 0,
    ) -> None: ...

class TweedieRegressor(_GeneralizedLinearRegressor):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_iter_: int = ...
    intercept_: float = ...
    coef_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        power: Float = 0.0,
        alpha: Float = 1.0,
        fit_intercept: bool = True,
        link: Literal["auto", "identity", "log"] = "auto",
        solver: Literal["lbfgs", "newton-cholesky"] = "lbfgs",
        max_iter: Int = 100,
        tol: Float = 1e-4,
        warm_start: bool = False,
        verbose: Int = 0,
    ) -> None: ...
