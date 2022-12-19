from typing import Literal, Any
from numpy.typing import ArrayLike, NDArray

# Author: Christian Lorentzen <lorentzen.ch@gmail.com>
# some parts and tricks stolen from other sklearn files.
# License: BSD 3 clause

import numbers

import numpy as np
import scipy.optimize

from ..._loss.glm_distribution import TweedieDistribution
from ..._loss.loss import (
    HalfGammaLoss,
    HalfPoissonLoss,
    HalfSquaredError,
    HalfTweedieLoss,
    HalfTweedieLossIdentity,
)
from ...base import BaseEstimator, RegressorMixin
from ...utils.optimize import _check_optimize_result
from ...utils import check_scalar, check_array, deprecated
from ...utils.validation import check_is_fitted, _check_sample_weight
from ...utils._openmp_helpers import _openmp_effective_n_threads
from .._linear_loss import LinearModelLoss
from numpy import float64, ndarray
from sklearn._loss.loss import HalfPoissonLoss

class _GeneralizedLinearRegressor(RegressorMixin, BaseEstimator):
    def __init__(
        self,
        *,
        alpha: float = 1.0,
        fit_intercept: bool = True,
        solver: Literal["lbfgs"] = "lbfgs",
        max_iter: int = 100,
        tol: float = 1e-4,
        warm_start: bool = False,
        verbose: int = 0,
    ) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> "PoissonRegressor": ...
    def _linear_predictor(self, X: ndarray) -> ndarray: ...
    def predict(self, X: NDArray | ArrayLike) -> ArrayLike: ...
    def score(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> float: ...
    def _more_tags(self): ...
    def _get_loss(self): ...

    # TODO(1.3): remove
    @deprecated("Attribute `family` was deprecated in version 1.1 and will be removed in 1.3.")  # type: ignore
    @property
    def family(self): ...

class PoissonRegressor(_GeneralizedLinearRegressor):
    def __init__(
        self,
        *,
        alpha: float = 1.0,
        fit_intercept: bool = True,
        max_iter: int = 100,
        tol: float = 1e-4,
        warm_start: bool = False,
        verbose: int = 0,
    ) -> None: ...
    def _get_loss(self) -> HalfPoissonLoss: ...

class GammaRegressor(_GeneralizedLinearRegressor):
    def __init__(
        self,
        *,
        alpha: float = 1.0,
        fit_intercept: bool = True,
        max_iter: int = 100,
        tol: float = 1e-4,
        warm_start: bool = False,
        verbose: int = 0,
    ): ...
    def _get_loss(self): ...

class TweedieRegressor(_GeneralizedLinearRegressor):
    def __init__(
        self,
        *,
        power: float = 0.0,
        alpha: float = 1.0,
        fit_intercept: bool = True,
        link: Literal["auto", "identity", "log"] = "auto",
        max_iter: int = 100,
        tol: float = 1e-4,
        warm_start: bool = False,
        verbose: int = 0,
    ): ...
    def _get_loss(self): ...
