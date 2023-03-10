from typing import Any, Callable
from .metrics.pairwise import (
    PAIRWISE_KERNEL_FUNCTIONS as PAIRWISE_KERNEL_FUNCTIONS,
    pairwise_kernels as pairwise_kernels,
)
from ._typing import ArrayLike, Float, Int, MatrixLike
from .base import BaseEstimator, RegressorMixin, MultiOutputMixin
from numpy import ndarray
from .utils._param_validation import Interval as Interval, StrOptions as StrOptions
from numbers import Integral as Integral, Real as Real
from .utils.validation import check_is_fitted as check_is_fitted

import numpy as np


class KernelRidge(MultiOutputMixin, RegressorMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        alpha: Float | ArrayLike = 1,
        *,
        kernel: str | Callable = "linear",
        gamma: None | Float = None,
        degree: Int = 3,
        coef0: Float = 1,
        kernel_params: dict | None = None,
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...
