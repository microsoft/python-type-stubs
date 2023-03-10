from typing import Any, Callable, Literal
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from .._typing import MatrixLike, Float, Int, ArrayLike
from ._dbscan_inner import dbscan_inner as dbscan_inner
from scipy import sparse as sparse
from ..base import BaseEstimator, ClusterMixin
from ..neighbors import NearestNeighbors as NearestNeighbors
from numpy import ndarray
from numbers import Integral as Integral, Real as Real

# Author: Robert Layton <robertlayton@gmail.com>
#         Joel Nothman <joel.nothman@gmail.com>
#         Lars Buitinck
#
# License: BSD 3 clause

import warnings

import numpy as np


def dbscan(
    X: MatrixLike,
    eps: Float = 0.5,
    *,
    min_samples: Int = 5,
    metric: str | Callable = "minkowski",
    metric_params: dict | None = None,
    algorithm: Literal["auto", "ball_tree", "kd_tree", "brute", "auto"] = "auto",
    leaf_size: Int = 30,
    p: Float = 2,
    sample_weight: None | ArrayLike = None,
    n_jobs: None | Int = None,
) -> tuple[ndarray, ndarray]:
    ...


class DBSCAN(ClusterMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        eps: Float = 0.5,
        *,
        min_samples: Int = 5,
        metric: str | Callable = "euclidean",
        metric_params: dict | None = None,
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute", "auto"] = "auto",
        leaf_size: Int = 30,
        p: None | Float = None,
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit(
        self, X: MatrixLike, y: Any = None, sample_weight: None | ArrayLike = None
    ) -> Any:
        ...

    def fit_predict(
        self, X: MatrixLike, y: Any = None, sample_weight: None | ArrayLike = None
    ) -> ndarray:
        ...
