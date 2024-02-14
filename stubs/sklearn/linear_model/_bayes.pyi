from math import log as log
from numbers import Integral as Integral, Real as Real
from typing import ClassVar, TypeVar

from numpy import ndarray
from scipy import linalg as linalg
from scipy.linalg import pinvh as pinvh

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import RegressorMixin
from ..utils._param_validation import Interval as Interval
from ..utils.extmath import fast_logdet as fast_logdet
from ._base import LinearModel

BayesianRidge_Self = TypeVar("BayesianRidge_Self", bound="BayesianRidge")
ARDRegression_Self = TypeVar("ARDRegression_Self", bound="ARDRegression")

import numpy as np

###############################################################################
# BayesianRidge regression

class BayesianRidge(RegressorMixin, LinearModel):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    X_scale_: ndarray = ...
    X_offset_: ndarray = ...
    n_iter_: int = ...
    scores_: ArrayLike = ...
    sigma_: ArrayLike = ...
    lambda_: float = ...
    alpha_: float = ...
    intercept_: float = ...
    coef_: ArrayLike = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        n_iter: Int = 300,
        tol: Float = 1.0e-3,
        alpha_1: Float = 1.0e-6,
        alpha_2: Float = 1.0e-6,
        lambda_1: Float = 1.0e-6,
        lambda_2: Float = 1.0e-6,
        alpha_init: None | Float = None,
        lambda_init: None | Float = None,
        compute_score: bool = False,
        fit_intercept: bool = True,
        copy_X: bool = True,
        verbose: bool = False,
    ) -> None: ...
    def fit(
        self: BayesianRidge_Self,
        X: ArrayLike,
        y: ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> BayesianRidge_Self: ...
    def predict(
        self, X: MatrixLike | ArrayLike, return_std: bool = False
    ) -> ArrayLike | tuple[ndarray, ndarray] | tuple[ArrayLike, ArrayLike]: ...

###############################################################################
# ARD (Automatic Relevance Determination) regression

class ARDRegression(RegressorMixin, LinearModel):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    X_scale_: float = ...
    X_offset_: float = ...
    intercept_: float = ...
    scores_: float = ...
    sigma_: ArrayLike = ...
    lambda_: ArrayLike = ...
    alpha_: float = ...
    coef_: ArrayLike = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        n_iter: Int = 300,
        tol: Float = 1.0e-3,
        alpha_1: Float = 1.0e-6,
        alpha_2: Float = 1.0e-6,
        lambda_1: Float = 1.0e-6,
        lambda_2: Float = 1.0e-6,
        compute_score: bool = False,
        threshold_lambda: Float = 1.0e4,
        fit_intercept: bool = True,
        copy_X: bool = True,
        verbose: bool = False,
    ) -> None: ...
    def fit(self: ARDRegression_Self, X: MatrixLike, y: ArrayLike) -> ARDRegression_Self: ...
    def predict(
        self, X: MatrixLike | ArrayLike, return_std: bool = False
    ) -> tuple[ndarray, ndarray] | tuple[ArrayLike, ArrayLike]: ...
