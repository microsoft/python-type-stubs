from typing import Tuple, Union, Any
from numpy.typing import NDArray, ArrayLike

# Authors: V. Michel, F. Pedregosa, A. Gramfort
# License: BSD 3 clause

from math import log
import numpy as np
from scipy import linalg

from ._base import LinearModel, _preprocess_data, _rescale_data
from ..base import RegressorMixin
from ._base import _deprecate_normalize
from ..utils.extmath import fast_logdet
from scipy.linalg import pinvh
from ..utils.validation import _check_sample_weight
from numpy import float64, ndarray

###############################################################################
# BayesianRidge regression

class BayesianRidge(RegressorMixin, LinearModel):
    def __init__(
        self,
        *,
        n_iter: int = 300,
        tol: float = 1.0e-3,
        alpha_1: float = 1.0e-6,
        alpha_2: float = 1.0e-6,
        lambda_1: float = 1.0e-6,
        lambda_2: float = 1.0e-6,
        alpha_init: float | None = None,
        lambda_init: float | None = None,
        compute_score: bool = False,
        fit_intercept: bool = True,
        normalize: bool | str = "deprecated",
        copy_X: bool = True,
        verbose: bool = False,
    ) -> None: ...
    def fit(self, X: NDArray, y: NDArray, sample_weight: NDArray | None = None) -> "BayesianRidge": ...
    def predict(self, X: NDArray | ArrayLike, return_std: bool = False) -> tuple[ArrayLike, ArrayLike]: ...
    def _update_coef_(
        self,
        X: ndarray,
        y: ndarray,
        n_samples: int,
        n_features: int,
        XT_y: ndarray,
        U: ndarray,
        Vh: ndarray,
        eigen_vals_: ndarray,
        alpha_: Union[float, float64],
        lambda_: Union[float, float64],
    ) -> Tuple[ndarray, float64]: ...
    def _log_marginal_likelihood(
        self,
        n_samples: int,
        n_features: int,
        eigen_vals: ndarray,
        alpha_: Union[float, float64],
        lambda_: Union[float, float64],
        coef: ndarray,
        rmse: float64,
    ) -> float64: ...

###############################################################################
# ARD (Automatic Relevance Determination) regression

class ARDRegression(RegressorMixin, LinearModel):
    def __init__(
        self,
        *,
        n_iter: int = 300,
        tol: float = 1.0e-3,
        alpha_1: float = 1.0e-6,
        alpha_2: float = 1.0e-6,
        lambda_1: float = 1.0e-6,
        lambda_2: float = 1.0e-6,
        compute_score: bool = False,
        threshold_lambda: float = 1.0e4,
        fit_intercept: bool = True,
        normalize: bool | str = "deprecated",
        copy_X: bool = True,
        verbose: bool = False,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: ArrayLike) -> "ARDRegression": ...
    def _update_sigma_woodbury(self, X, alpha_, lambda_, keep_lambda): ...
    def _update_sigma(self, X: ndarray, alpha_: float64, lambda_: ndarray, keep_lambda: ndarray) -> ndarray: ...
    def predict(self, X: NDArray | ArrayLike, return_std: bool = False) -> tuple[ArrayLike, ArrayLike]: ...
