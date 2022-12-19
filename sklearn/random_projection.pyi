from numpy import float64, int64, ndarray
from typing import Optional, Union, Any, Literal
from numpy.typing import ArrayLike, NDArray

# Authors: Olivier Grisel <olivier.grisel@ensta.org>,
#          Arnaud Joly <a.joly@ulg.ac.be>
# License: BSD 3 clause

import warnings
from abc import ABCMeta, abstractmethod

import numpy as np
from scipy import linalg
import scipy.sparse as sp

from .base import BaseEstimator, TransformerMixin
from .base import _ClassNamePrefixFeaturesOutMixin

from .utils import check_random_state
from .utils.extmath import safe_sparse_dot

from .utils.validation import check_array, check_is_fitted
from .exceptions import DataDimensionalityWarning
from numpy.random import RandomState
from scipy.sparse._csr import csr_matrix

__all__ = [
    "SparseRandomProjection",
    "GaussianRandomProjection",
    "johnson_lindenstrauss_min_dim",
]

def johnson_lindenstrauss_min_dim(n_samples: int | ArrayLike, *, eps: float | NDArray = 0.1) -> int | np.ndarray: ...
def _check_density(density: Union[str, float64], n_features: int) -> float64: ...
def _check_input_size(n_components: int64, n_features: int) -> None: ...
def _gaussian_random_matrix(n_components, n_features, random_state=None): ...
def _sparse_random_matrix(
    n_components: int64,
    n_features: int,
    density: float64 | str = "auto",
    random_state: Optional[RandomState] = None,
) -> csr_matrix: ...

class BaseRandomProjection(TransformerMixin, BaseEstimator, _ClassNamePrefixFeaturesOutMixin, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        n_components: Union[int64, int, str] = "auto",
        *,
        eps=0.1,
        compute_inverse_components=False,
        random_state=None,
    ) -> None: ...
    @abstractmethod
    def _make_random_matrix(self, n_components, n_features): ...
    def _compute_inverse_components(self): ...
    def fit(self, X: NDArray, y: None = None) -> "SparseRandomProjection": ...
    @property
    def _n_features_out(self): ...
    def inverse_transform(self, X: NDArray | ArrayLike) -> NDArray: ...
    def _more_tags(self): ...

class GaussianRandomProjection(BaseRandomProjection):
    def __init__(
        self,
        n_components: int | Literal["auto"] = "auto",
        *,
        eps: float = 0.1,
        compute_inverse_components: bool = False,
        random_state: int | RandomState | None = None,
    ): ...
    def _make_random_matrix(self, n_components, n_features): ...
    def transform(self, X: NDArray) -> NDArray: ...

class SparseRandomProjection(BaseRandomProjection):
    def __init__(
        self,
        n_components: int | Literal["auto"] = "auto",
        *,
        density: float | Literal["auto"] = "auto",
        eps: float = 0.1,
        dense_output: bool = False,
        compute_inverse_components: bool = False,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def _make_random_matrix(self, n_components: int64, n_features: int) -> csr_matrix: ...
    def transform(self, X: NDArray) -> NDArray: ...
