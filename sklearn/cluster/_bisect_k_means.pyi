from typing import Any, Callable, Iterator, Literal, Self
from ..utils._param_validation import StrOptions as StrOptions
from ..utils.extmath import row_norms as row_norms
from numpy.random import RandomState
from .._typing import Float, Int, ArrayLike, MatrixLike
from ..utils.validation import (
    check_is_fitted as check_is_fitted,
    check_random_state as check_random_state,
)
from numpy import ndarray
from ._kmeans import _BaseKMeans

# Author: Michal Krawczyk <mkrwczyk.1@gmail.com>

import warnings

import numpy as np
import scipy.sparse as sp


class _BisectingTree:
    def __init__(self, center: ndarray, indices: ndarray, score: Float) -> None:
        ...

    def split(self, labels: ndarray, centers: ndarray, scores: ndarray) -> None:
        ...

    def get_cluster_to_bisect(self) -> _BisectingTree:
        ...

    def iter_leaves(self) -> Iterator[_BisectingTree]:
        ...


class BisectingKMeans(_BaseKMeans):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_clusters: Int = 8,
        *,
        init: Literal["k-means++", "random", "random"] | Callable = "random",
        n_init: Int = 1,
        random_state: RandomState | None | Int = None,
        max_iter: Int = 300,
        verbose: Int = 0,
        tol: Float = 1e-4,
        copy_x: bool = True,
        algorithm: Literal["lloyd", "elkan", "lloyd"] = "lloyd",
        bisecting_strategy: Literal[
            "biggest_inertia", "largest_cluster", "biggest_inertia"
        ] = "biggest_inertia",
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: Any = None,
        sample_weight: None | ArrayLike = None,
    ) -> BisectingKMeans | Self:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...
