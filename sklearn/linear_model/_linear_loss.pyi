from typing import Callable, Type
from scipy import sparse as sparse
from numpy import ndarray, bool_
from ..utils.extmath import squared_norm as squared_norm
from .._loss.loss import BaseLoss
from .._typing import Float, MatrixLike, ArrayLike, Int
import numpy as np


class LinearModelLoss:
    def __init__(self, base_loss: BaseLoss, fit_intercept: bool) -> None:
        ...

    def init_zero_coef(self, X: ndarray, dtype: None | Type[Float] = None) -> ndarray:
        ...

    def weight_intercept(
        self, coef: MatrixLike | ArrayLike
    ) -> tuple[ndarray, Float] | tuple[ndarray, ndarray] | tuple[
        ndarray, float | ndarray
    ]:
        ...

    def weight_intercept_raw(
        self, coef: MatrixLike | ArrayLike, X: MatrixLike | ArrayLike
    ) -> tuple[ndarray, float | ndarray, ndarray]:
        ...

    def l2_penalty(self, weights: ndarray, l2_reg_strength: Float) -> Float:
        ...

    def loss(
        self,
        coef: MatrixLike | ArrayLike,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | MatrixLike = None,
        l2_reg_strength: Float = 0.0,
        n_threads: Int = 1,
        raw_prediction: None | MatrixLike | ArrayLike = None,
    ) -> Float:
        ...

    def loss_gradient(
        self,
        coef: MatrixLike | ArrayLike,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | MatrixLike = None,
        l2_reg_strength: Float = 0.0,
        n_threads: Int = 1,
        raw_prediction: None | MatrixLike | ArrayLike = None,
    ) -> tuple[float, ndarray] | tuple[Float, ndarray]:
        ...

    def gradient(
        self,
        coef: MatrixLike | ArrayLike,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | MatrixLike = None,
        l2_reg_strength: Float = 0.0,
        n_threads: Int = 1,
        raw_prediction: None | MatrixLike | ArrayLike = None,
    ) -> ndarray:
        ...

    def gradient_hessian(
        self,
        coef: MatrixLike | ArrayLike,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | MatrixLike = None,
        l2_reg_strength: Float = 0.0,
        n_threads: Int = 1,
        gradient_out: None | ArrayLike = None,
        hessian_out: None | ArrayLike = None,
        raw_prediction: None | MatrixLike | ArrayLike = None,
    ) -> tuple[ndarray, ndarray, bool_] | tuple[ndarray, ndarray, bool]:
        ...

    def gradient_hessian_product(
        self,
        coef: MatrixLike | ArrayLike,
        X: MatrixLike | ArrayLike,
        y: ArrayLike,
        sample_weight: None | MatrixLike = None,
        l2_reg_strength: Float = 0.0,
        n_threads: Int = 1,
    ) -> tuple[ndarray, Callable]:
        ...
