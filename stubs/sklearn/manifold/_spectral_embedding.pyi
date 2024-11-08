from numbers import Integral as Integral, Real as Real
from typing import Any, Callable, ClassVar, Literal, TypeVar

from numpy import ndarray
from numpy.random import RandomState
from scipy import sparse as sparse
from scipy.linalg import eigh as eigh
from scipy.sparse._coo import coo_matrix
from scipy.sparse.csgraph import connected_components as connected_components, laplacian as csgraph_laplacian
from scipy.sparse.linalg import eigsh as eigsh

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator
from ..metrics.pairwise import rbf_kernel as rbf_kernel
from ..neighbors import NearestNeighbors as NearestNeighbors, kneighbors_graph as kneighbors_graph
from ..utils import check_array as check_array, check_random_state as check_random_state, check_symmetric as check_symmetric
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions

SpectralEmbedding_Self = TypeVar("SpectralEmbedding_Self", bound="SpectralEmbedding")

import warnings

import numpy as np

def spectral_embedding(
    adjacency: coo_matrix | MatrixLike,
    *,
    n_components: Int = 8,
    eigen_solver: None | Literal["arpack", "lobpcg", "amg"] = None,
    random_state: RandomState | None | Int = None,
    eigen_tol: str | Float = "auto",
    norm_laplacian: bool = True,
    drop_first: bool = True,
) -> ndarray: ...

class SpectralEmbedding(BaseEstimator):
    n_neighbors_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    affinity_matrix_: ndarray = ...
    embedding_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_components: Int = 2,
        *,
        affinity: (
            Literal[
                "nearest_neighbors",
                "rbf",
                "precomputed",
                "precomputed_nearest_neighbors",
                "nearest_neighbors",
            ]
            | Callable
        ) = "nearest_neighbors",
        gamma: None | Float = None,
        random_state: RandomState | None | Int = None,
        eigen_solver: None | Literal["arpack", "lobpcg", "amg"] = None,
        eigen_tol: str | Float = "auto",
        n_neighbors: None | Int = None,
        n_jobs: None | Int = None,
    ) -> None: ...
    def fit(self: SpectralEmbedding_Self, X: MatrixLike | ArrayLike, y: Any = None) -> SpectralEmbedding_Self: ...
    def fit_transform(self, X: MatrixLike | ArrayLike, y: Any = None) -> ndarray: ...
