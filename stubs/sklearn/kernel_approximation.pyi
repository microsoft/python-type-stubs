from typing import Callable, ClassVar, TypeVar
from numpy.random import RandomState
from .base import BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin
from .utils.validation import (
    check_is_fitted as check_is_fitted,
    check_non_negative as check_non_negative,
)
from numpy import ndarray
from scipy.linalg import svd as svd
from numbers import Integral as Integral, Real as Real
from .utils.extmath import safe_sparse_dot as safe_sparse_dot
from .utils import check_random_state as check_random_state
from .utils._param_validation import Interval as Interval, StrOptions as StrOptions
from scipy.sparse import spmatrix
from scipy.fftpack import fft as fft, ifft as ifft
from .metrics.pairwise import (
    pairwise_kernels as pairwise_kernels,
    KERNEL_PARAMS as KERNEL_PARAMS,
    PAIRWISE_KERNEL_FUNCTIONS as PAIRWISE_KERNEL_FUNCTIONS,
)
from ._typing import Float, Int, MatrixLike, ArrayLike

SkewedChi2Sampler_Self = TypeVar("SkewedChi2Sampler_Self", bound="SkewedChi2Sampler")
PolynomialCountSketch_Self = TypeVar(
    "PolynomialCountSketch_Self", bound="PolynomialCountSketch"
)
AdditiveChi2Sampler_Self = TypeVar(
    "AdditiveChi2Sampler_Self", bound="AdditiveChi2Sampler"
)
RBFSampler_Self = TypeVar("RBFSampler_Self", bound="RBFSampler")
Nystroem_Self = TypeVar("Nystroem_Self", bound="Nystroem")

import warnings

import numpy as np
import scipy.sparse as sp


class PolynomialCountSketch(
    ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator
):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    bitHash_: ndarray = ...
    indexHash_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

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
        self: PolynomialCountSketch_Self,
        X: MatrixLike | ArrayLike,
        y: None | MatrixLike | ArrayLike = None,
    ) -> PolynomialCountSketch_Self:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...


class RBFSampler(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    random_weights_: ndarray = ...
    random_offset_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        gamma: float | str = 1.0,
        n_components: Int = 100,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def fit(
        self: RBFSampler_Self, X: MatrixLike, y: None | MatrixLike | ArrayLike = None
    ) -> RBFSampler_Self:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...


class SkewedChi2Sampler(
    ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator
):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    random_offset_: ndarray = ...
    random_weights_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        skewedness: Float = 1.0,
        n_components: Int = 100,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def fit(
        self: SkewedChi2Sampler_Self,
        X: MatrixLike,
        y: None | MatrixLike | ArrayLike = None,
    ) -> SkewedChi2Sampler_Self:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...


class AdditiveChi2Sampler(TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    sample_interval_: float = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self, *, sample_steps: Int = 2, sample_interval: None | Float = None
    ) -> None:
        ...

    def fit(
        self: AdditiveChi2Sampler_Self,
        X: MatrixLike,
        y: None | MatrixLike | ArrayLike = None,
    ) -> AdditiveChi2Sampler_Self:
        ...

    def transform(self, X: MatrixLike) -> ndarray | spmatrix:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...


class Nystroem(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    normalization_: ndarray = ...
    component_indices_: ndarray = ...
    components_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        kernel: str | Callable = "rbf",
        *,
        gamma: None | Float = None,
        coef0: None | Float = None,
        degree: None | Float = None,
        kernel_params: None | dict = None,
        n_components: Int = 100,
        random_state: RandomState | None | Int = None,
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit(
        self: Nystroem_Self, X: MatrixLike, y: None | MatrixLike | ArrayLike = None
    ) -> Nystroem_Self:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...
