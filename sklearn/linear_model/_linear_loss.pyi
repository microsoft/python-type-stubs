from numpy import float64, ndarray
from typing import Optional, Tuple, Union, Callable
from numpy.typing import ArrayLike, NDArray
from sklearn._loss.loss import (
    HalfBinomialLoss,
    HalfMultinomialLoss,
    HalfPoissonLoss,
    BaseLoss,
)
import numpy as np
from scipy import sparse
from ..utils.extmath import squared_norm
from scipy.sparse._csr import csr_matrix

class LinearModelLoss:
    def __init__(self, base_loss: BaseLoss, fit_intercept: bool) -> None: ...
    def _w_intercept_raw(
        self, coef: ndarray, X: Union[ndarray, csr_matrix]
    ) -> Union[Tuple[ndarray, float64, ndarray], Tuple[ndarray, ndarray, ndarray]]: ...
    def loss(
        self,
        coef: ndarray,
        X: NDArray | ArrayLike,
        y: NDArray,
        sample_weight: None | NDArray = None,
        l2_reg_strength: float = 0.0,
        n_threads: int = 1,
    ) -> float: ...
    def loss_gradient(
        self,
        coef: ndarray,
        X: NDArray | ArrayLike,
        y: NDArray,
        sample_weight: None | NDArray = None,
        l2_reg_strength: float = 0.0,
        n_threads: int = 1,
    ) -> tuple[float, NDArray]: ...
    def gradient(
        self,
        coef: ndarray,
        X: NDArray | ArrayLike,
        y: NDArray,
        sample_weight: None | NDArray = None,
        l2_reg_strength: float = 0.0,
        n_threads: int = 1,
    ) -> NDArray: ...
    def gradient_hessian_product(
        self,
        coef: ndarray,
        X: NDArray | ArrayLike,
        y: NDArray,
        sample_weight: None | NDArray = None,
        l2_reg_strength: float = 0.0,
        n_threads: int = 1,
    ) -> tuple[NDArray, Callable]: ...
