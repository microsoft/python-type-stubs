from typing import Any
from ..utils._param_validation import Interval as Interval
from ..utils.extmath import fast_logdet as fast_logdet
from scipy.linalg import pinvh as pinvh
from .._typing import Int, Float, ArrayLike, MatrixLike
from math import log as log
from scipy import linalg as linalg
from ..base import RegressorMixin
from ._base import LinearModel
from numpy import ndarray
from numbers import Integral as Integral, Real as Real
import numpy as np

###############################################################################
# BayesianRidge regression


class BayesianRidge(RegressorMixin, LinearModel):

    _parameter_constraints: dict = ...

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
    ) -> None:
        ...

    def fit(
        self, X: ArrayLike, y: ArrayLike, sample_weight: None | ArrayLike = None
    ) -> Any:
        ...

    def predict(
        self, X: MatrixLike | ArrayLike, return_std: bool = False
    ) -> tuple[ndarray, ndarray] | tuple[ArrayLike, ArrayLike] | ArrayLike:
        ...


###############################################################################
# ARD (Automatic Relevance Determination) regression


class ARDRegression(RegressorMixin, LinearModel):

    _parameter_constraints: dict = ...

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
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: ArrayLike) -> Any:
        ...

    def predict(
        self, X: MatrixLike | ArrayLike, return_std: bool = False
    ) -> tuple[ArrayLike, ArrayLike] | tuple[ndarray, ndarray]:
        ...
