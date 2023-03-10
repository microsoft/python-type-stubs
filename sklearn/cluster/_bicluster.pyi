from typing import Any, Literal
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from scipy.linalg import norm as norm
from ..utils.extmath import (
    make_nonnegative as make_nonnegative,
    randomized_svd as randomized_svd,
    safe_sparse_dot as safe_sparse_dot,
)
from scipy.sparse.linalg import eigsh as eigsh, svds as svds
from numpy.random import RandomState
from .._typing import MatrixLike, Int
from ..base import BaseEstimator, BiclusterMixin
from ..utils.validation import assert_all_finite as assert_all_finite
from abc import ABCMeta, abstractmethod
from . import KMeans as KMeans, MiniBatchKMeans as MiniBatchKMeans
from ..utils import (
    check_random_state as check_random_state,
    check_scalar as check_scalar,
)
from numbers import Integral as Integral
from scipy.sparse import dia_matrix as dia_matrix, issparse as issparse

import numpy as np


__all__ = ["SpectralCoclustering", "SpectralBiclustering"]


class BaseSpectral(BiclusterMixin, BaseEstimator, metaclass=ABCMeta):

    _parameter_constraints: dict = ...

    @abstractmethod
    def __init__(
        self,
        n_clusters: tuple[int, int] | int = 3,
        svd_method: str = "randomized",
        n_svd_vecs=None,
        mini_batch: bool = False,
        init: str = "k-means++",
        n_init: int = 10,
        random_state: int | None = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...


class SpectralCoclustering(BaseSpectral):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_clusters: Int = 3,
        *,
        svd_method: Literal["randomized", "arpack", "randomized"] = "randomized",
        n_svd_vecs: None | Int = None,
        mini_batch: bool = False,
        init: Literal["k-means++", "random", "k-means++"] | MatrixLike = "k-means++",
        n_init: Int = 10,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...


class SpectralBiclustering(BaseSpectral):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_clusters: tuple[int, int] | int = 3,
        *,
        method: Literal[
            "bistochastic", "scale", "log", "bistochastic"
        ] = "bistochastic",
        n_components: Int = 6,
        n_best: Int = 3,
        svd_method: Literal["randomized", "arpack", "randomized"] = "randomized",
        n_svd_vecs: None | Int = None,
        mini_batch: bool = False,
        init: Literal["k-means++", "random", "k-means++"] | MatrixLike = "k-means++",
        n_init: Int = 10,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...
