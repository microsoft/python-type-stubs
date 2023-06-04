from typing import Callable, ClassVar, TypeVar
from .base import BaseEstimator, RegressorMixin, MultiOutputMixin
from .utils.validation import check_is_fitted as check_is_fitted
from numpy import ndarray
from numbers import Integral as Integral, Real as Real
from .utils._param_validation import Interval as Interval, StrOptions as StrOptions
from scipy.sparse import spmatrix
from .metrics.pairwise import (
    PAIRWISE_KERNEL_FUNCTIONS as PAIRWISE_KERNEL_FUNCTIONS,
    pairwise_kernels as pairwise_kernels,
)
from ._typing import Float, ArrayLike, Int, MatrixLike

KernelRidge_Self = TypeVar("KernelRidge_Self", bound="KernelRidge")


import numpy as np


class KernelRidge(MultiOutputMixin, RegressorMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    X_fit_: ndarray | spmatrix = ...
    dual_coef_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        alpha: ArrayLike | Float = 1,
        *,
        kernel: str | Callable = "linear",
        gamma: None | Float = None,
        degree: Int = 3,
        coef0: Float = 1,
        kernel_params: None | dict = None,
    ) -> None:
        ...

    def fit(
        self: KernelRidge_Self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> KernelRidge_Self:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...
