from typing import Any, Callable
from scipy.linalg import svd as svd
from .utils import check_random_state as check_random_state
from .metrics.pairwise import (
    pairwise_kernels as pairwise_kernels,
    KERNEL_PARAMS as KERNEL_PARAMS,
    PAIRWISE_KERNEL_FUNCTIONS as PAIRWISE_KERNEL_FUNCTIONS,
)
from ._typing import Float, Int, ArrayLike, MatrixLike
from scipy.fftpack import fft as fft, ifft as ifft
from .base import BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin
from numpy.random import RandomState
from numpy import ndarray
from .utils.extmath import safe_sparse_dot as safe_sparse_dot
from .utils._param_validation import Interval as Interval, StrOptions as StrOptions
from numbers import Integral as Integral, Real as Real
from .utils.validation import (
    check_is_fitted as check_is_fitted,
    check_non_negative as check_non_negative,
)
from scipy.sparse import spmatrix
import warnings

import numpy as np
import scipy.sparse as sp


class PolynomialCountSketch(
    ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator
):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        gamma: Float = 1.0,
        degree: Int = 2,
        coef0: Int = 0,
        n_components: Int = 100,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def fit(
        self, X: MatrixLike | ArrayLike, y: None | MatrixLike | ArrayLike = None
    ) -> Any:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...


class RBFSampler(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        gamma: float | str = 1.0,
        n_components: Int = 100,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: None | MatrixLike | ArrayLike = None) -> Any:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...


class SkewedChi2Sampler(
    ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator
):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        skewedness: Float = 1.0,
        n_components: Int = 100,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: None | MatrixLike | ArrayLike = None) -> Any:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...


class AdditiveChi2Sampler(TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self, *, sample_steps: Int = 2, sample_interval: None | Float = None
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: None | MatrixLike | ArrayLike = None) -> Any:
        ...

    def transform(self, X: MatrixLike) -> spmatrix:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...


class Nystroem(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        kernel: str | Callable = "rbf",
        *,
        gamma: None | Float = None,
        coef0: None | Float = None,
        degree: None | Float = None,
        kernel_params: dict | None = None,
        n_components: Int = 100,
        random_state: RandomState | None | Int = None,
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: None | MatrixLike | ArrayLike = None) -> Any:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...
