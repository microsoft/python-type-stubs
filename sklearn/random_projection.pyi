from typing import Any, Literal, Sequence
from .exceptions import DataDimensionalityWarning as DataDimensionalityWarning
from .utils import check_random_state as check_random_state
from numpy.random import RandomState
from ._typing import Float, ArrayLike, Int, MatrixLike
from scipy import linalg as linalg
from .base import BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin
from abc import ABCMeta, abstractmethod
from scipy.sparse._csr import csr_matrix
from numpy import ndarray
from .utils.extmath import safe_sparse_dot as safe_sparse_dot
from .utils._param_validation import Interval as Interval, StrOptions as StrOptions
from numbers import Integral as Integral, Real as Real
from .utils.random import sample_without_replacement as sample_without_replacement
from .utils.validation import (
    check_array as check_array,
    check_is_fitted as check_is_fitted,
)
from scipy.sparse import spmatrix

# Authors: Olivier Grisel <olivier.grisel@ensta.org>,
#          Arnaud Joly <a.joly@ulg.ac.be>
# License: BSD 3 clause

import warnings

import numpy as np
import scipy.sparse as sp

__all__ = [
    "SparseRandomProjection",
    "GaussianRandomProjection",
    "johnson_lindenstrauss_min_dim",
]


def johnson_lindenstrauss_min_dim(
    n_samples: Sequence[int] | Float | ndarray, *, eps: float | ArrayLike = 0.1
) -> int | ndarray:
    ...


class BaseRandomProjection(
    TransformerMixin, BaseEstimator, ClassNamePrefixFeaturesOutMixin, metaclass=ABCMeta
):

    _parameter_constraints: dict = ...

    @abstractmethod
    def __init__(
        self,
        n_components: str | Int = "auto",
        *,
        eps: float = 0.1,
        compute_inverse_components: bool = False,
        random_state=None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...

    def inverse_transform(self, X: MatrixLike) -> ndarray:
        ...


class GaussianRandomProjection(BaseRandomProjection):
    def __init__(
        self,
        n_components: Literal["auto", "auto"] | Int = "auto",
        *,
        eps: Float = 0.1,
        compute_inverse_components: bool = False,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def transform(self, X: MatrixLike) -> ndarray:
        ...


class SparseRandomProjection(BaseRandomProjection):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_components: Literal["auto", "auto"] | Int = "auto",
        *,
        density: float | Literal["auto", "auto"] = "auto",
        eps: Float = 0.1,
        dense_output: bool = False,
        compute_inverse_components: bool = False,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def transform(self, X: MatrixLike) -> csr_matrix | spmatrix | ndarray:
        ...
