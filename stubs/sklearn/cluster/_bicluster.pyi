from abc import ABCMeta, abstractmethod
from numbers import Integral as Integral
from typing import Any, ClassVar, Literal, TypeVar

from numpy import ndarray
from numpy.random import RandomState
from scipy.linalg import norm as norm
from scipy.sparse import dia_matrix as dia_matrix, issparse as issparse
from scipy.sparse.linalg import eigsh as eigsh, svds as svds

from .._typing import ArrayLike, Int, MatrixLike
from ..base import BaseEstimator, BiclusterMixin
from ..utils import check_random_state as check_random_state, check_scalar as check_scalar
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import (
    make_nonnegative as make_nonnegative,
    randomized_svd as randomized_svd,
    safe_sparse_dot as safe_sparse_dot,
)
from ..utils.validation import assert_all_finite as assert_all_finite
from . import KMeans as KMeans, MiniBatchKMeans as MiniBatchKMeans

BaseSpectral_Self = TypeVar("BaseSpectral_Self", bound=BaseSpectral)

import numpy as np

__all__ = ["SpectralCoclustering", "SpectralBiclustering"]

class BaseSpectral(BiclusterMixin, BaseEstimator, metaclass=ABCMeta):
    _parameter_constraints: ClassVar[dict] = ...

    @abstractmethod
    def __init__(
        self,
        n_clusters: int | tuple[int, int] = 3,
        svd_method: str = "randomized",
        n_svd_vecs=None,
        mini_batch: bool = False,
        init: str = "k-means++",
        n_init: int = 10,
        random_state: None | int = None,
    ) -> None: ...
    def fit(self: BaseSpectral_Self, X: MatrixLike, y: Any = None) -> BaseSpectral_Self: ...

class SpectralCoclustering(BaseSpectral):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    biclusters_: tuple[ndarray, ndarray] = ...
    column_labels_: ArrayLike = ...
    row_labels_: ArrayLike = ...
    columns_: ArrayLike = ...
    rows_: ArrayLike = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_clusters: Int = 3,
        *,
        svd_method: Literal["randomized", "arpack"] = "randomized",
        n_svd_vecs: None | Int = None,
        mini_batch: bool = False,
        init: MatrixLike | Literal["k-means++", "random"] = "k-means++",
        n_init: Int = 10,
        random_state: RandomState | None | Int = None,
    ) -> None: ...

class SpectralBiclustering(BaseSpectral):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    biclusters_: tuple[ndarray, ndarray] = ...
    column_labels_: ArrayLike = ...
    row_labels_: ArrayLike = ...
    columns_: ArrayLike = ...
    rows_: ArrayLike = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_clusters: tuple[int, int] | int = 3,
        *,
        method: Literal["bistochastic", "scale", "log"] = "bistochastic",
        n_components: Int = 6,
        n_best: Int = 3,
        svd_method: Literal["randomized", "arpack"] = "randomized",
        n_svd_vecs: None | Int = None,
        mini_batch: bool = False,
        init: MatrixLike | Literal["k-means++", "random"] = "k-means++",
        n_init: Int = 10,
        random_state: RandomState | None | Int = None,
    ) -> None: ...
