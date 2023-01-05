from numpy import ndarray
from typing import Dict, Optional, Union, Any, Callable, Mapping
from numpy.typing import ArrayLike, NDArray
from numpy.random import RandomState

# Author: Andreas Mueller <amueller@ais.uni-bonn.de>
#         Daniel Lopez-Sanchez (TensorSketch) <lope@usal.es>

# License: BSD 3 clause

import warnings

import numpy as np
import scipy.sparse as sp
from scipy.linalg import svd

from .base import BaseEstimator
from .base import TransformerMixin
from .base import _ClassNamePrefixFeaturesOutMixin
from .utils import check_random_state
from .utils.extmath import safe_sparse_dot
from .utils.validation import check_is_fitted
from .utils.validation import _check_feature_names_in
from .metrics.pairwise import pairwise_kernels, KERNEL_PARAMS
from .utils.validation import check_non_negative

class PolynomialCountSketch(_ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        *,
        gamma: float = 1.0,
        degree: int = 2,
        coef0: int = 0,
        n_components: int = 100,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def fit(self, X: NDArray | ArrayLike, y: ArrayLike | None = None) -> "PolynomialCountSketch": ...
    def transform(self, X: ArrayLike) -> ArrayLike: ...

class RBFSampler(_ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        *,
        gamma: float = 1.0,
        n_components: int = 100,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def fit(self, X: NDArray | ArrayLike, y: ArrayLike | None = None) -> "RBFSampler": ...
    def transform(self, X: NDArray | ArrayLike) -> ArrayLike: ...

class SkewedChi2Sampler(_ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        *,
        skewedness: float = 1.0,
        n_components: int = 100,
        random_state: int | RandomState | None = None,
    ): ...
    def fit(self, X: ArrayLike, y: ArrayLike | None = None) -> Any: ...
    def transform(self, X: ArrayLike) -> ArrayLike: ...

class AdditiveChi2Sampler(TransformerMixin, BaseEstimator):
    def __init__(self, *, sample_steps: int = 2, sample_interval: float | None = None): ...
    def fit(self, X: ArrayLike, y: ArrayLike | None = None) -> Any: ...
    def transform(self, X: NDArray | ArrayLike) -> NDArray: ...
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...
    def _transform_dense(self, X): ...
    def _transform_sparse(self, X): ...
    def _more_tags(self): ...

class Nystroem(_ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        kernel: str | Callable = "rbf",
        *,
        gamma: float | None = None,
        coef0: float | None = None,
        degree: float | None = None,
        kernel_params: Mapping | None = None,
        n_components: int = 100,
        random_state: int | RandomState | None = None,
        n_jobs: int | None = None,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: ArrayLike | None = None) -> "Nystroem": ...
    def transform(self, X: ArrayLike) -> NDArray: ...
    def _get_kernel_params(self) -> Dict[str, Union[float, int]]: ...
    def _more_tags(self): ...
