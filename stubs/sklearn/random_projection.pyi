from typing import Any, ClassVar, Literal, Sequence, TypeVar
from numpy.random import RandomState
from abc import ABCMeta, abstractmethod
from scipy import linalg as linalg
from .base import BaseEstimator, TransformerMixin, ClassNamePrefixFeaturesOutMixin
from .utils.validation import (
    check_array as check_array,
    check_is_fitted as check_is_fitted,
)
from numpy import ndarray
from numbers import Integral as Integral, Real as Real
from .utils.extmath import safe_sparse_dot as safe_sparse_dot
from .exceptions import DataDimensionalityWarning as DataDimensionalityWarning
from .utils import check_random_state as check_random_state
from .utils._param_validation import Interval as Interval, StrOptions as StrOptions
from .utils.random import sample_without_replacement as sample_without_replacement
from scipy.sparse import spmatrix
from ._typing import Float, ArrayLike, Int, MatrixLike

BaseRandomProjection_Self = TypeVar(
    "BaseRandomProjection_Self", bound="BaseRandomProjection"
)

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
    n_samples: Sequence[int] | ndarray | Float, *, eps: float | ArrayLike = 0.1
) -> ndarray | int:
    ...


class BaseRandomProjection(
    TransformerMixin, BaseEstimator, ClassNamePrefixFeaturesOutMixin, metaclass=ABCMeta
):

    _parameter_constraints: ClassVar[dict] = ...

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

    def fit(
        self: BaseRandomProjection_Self, X: MatrixLike, y: Any = None
    ) -> BaseRandomProjection_Self | SparseRandomProjection:
        ...

    def inverse_transform(self, X: MatrixLike) -> ndarray:
        ...


class GaussianRandomProjection(BaseRandomProjection):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    inverse_components_: ndarray = ...
    components_: ndarray = ...
    n_components_: int = ...

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
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    density_: float = ...
    inverse_components_: ndarray = ...
    components_: spmatrix = ...
    n_components_: int = ...

    _parameter_constraints: ClassVar[dict] = ...

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

    def transform(self, X: MatrixLike) -> ndarray | spmatrix:
        ...
