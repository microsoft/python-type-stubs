from typing import Any, Callable, Literal
from .._typing import MatrixLike, Int, Float, ArrayLike
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from scipy.linalg import eigh as eigh
from scipy.sparse.linalg import eigsh as eigsh
from ..neighbors import (
    kneighbors_graph as kneighbors_graph,
    NearestNeighbors as NearestNeighbors,
)
from ..metrics.pairwise import rbf_kernel as rbf_kernel
from ..utils import (
    check_array as check_array,
    check_random_state as check_random_state,
    check_symmetric as check_symmetric,
)
from pyamg import smoothed_aggregation_solver as smoothed_aggregation_solver
from scipy import sparse as sparse
from numpy import ndarray
from scipy.sparse._coo import coo_matrix
from scipy.sparse.csgraph import (
    connected_components as connected_components,
    laplacian as csgraph_laplacian,
)
from numpy.random import RandomState
from ..base import BaseEstimator
from numbers import Integral as Integral, Real as Real
from ..utils.fixes import lobpcg
import warnings

import numpy as np


def spectral_embedding(
    adjacency: MatrixLike | coo_matrix,
    *,
    n_components: Int = 8,
    eigen_solver: Literal["arpack", "lobpcg", "amg"] | None = None,
    random_state: RandomState | None | Int = None,
    eigen_tol: str | Float = "auto",
    norm_laplacian: bool = True,
    drop_first: bool = True,
) -> ndarray:
    ...


class SpectralEmbedding(BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_components: Int = 2,
        *,
        affinity: Literal[
            "nearest_neighbors",
            "rbf",
            "precomputed",
            "precomputed_nearest_neighbors",
            "nearest_neighbors",
        ]
        | Callable = "nearest_neighbors",
        gamma: None | Float = None,
        random_state: RandomState | None | Int = None,
        eigen_solver: Literal["arpack", "lobpcg", "amg"] | None = None,
        eigen_tol: str | Float = "auto",
        n_neighbors: None | Int = None,
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike | ArrayLike, y: Any = None) -> Any:
        ...

    def fit_transform(self, X: MatrixLike | ArrayLike, y: Any = None) -> ndarray:
        ...
