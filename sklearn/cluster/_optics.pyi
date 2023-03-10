from typing import Any, Callable, Literal
from ..utils._param_validation import (
    Interval as Interval,
    HasMethods as HasMethods,
    StrOptions as StrOptions,
)
from ..exceptions import DataConversionWarning as DataConversionWarning
from .._typing import Float, Int, MatrixLike, ArrayLike
from ..base import BaseEstimator, ClusterMixin
from ..neighbors import NearestNeighbors as NearestNeighbors
from joblib import Memory
from ..utils.validation import check_memory as check_memory
from ..metrics.pairwise import PAIRWISE_BOOLEAN_FUNCTIONS as PAIRWISE_BOOLEAN_FUNCTIONS
from numpy import ndarray
from ..utils import gen_batches as gen_batches, get_chunk_n_rows as get_chunk_n_rows
from numbers import Integral as Integral, Real as Real
from scipy.sparse import (
    issparse as issparse,
    SparseEfficiencyWarning as SparseEfficiencyWarning,
)
from ..metrics import pairwise_distances as pairwise_distances

import warnings
import numpy as np


class OPTICS(ClusterMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        min_samples: int | float = 5,
        max_eps: Float = ...,
        metric: str | Callable = "minkowski",
        p: Float = 2,
        metric_params: dict | None = None,
        cluster_method: str = "xi",
        eps: None | Float = None,
        xi: float = 0.05,
        predecessor_correction: bool = True,
        min_cluster_size: int | float | None = None,
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute", "auto"] = "auto",
        leaf_size: Int = 30,
        memory: Memory | str | None = None,
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...


def compute_optics_graph(
    X: MatrixLike,
    *,
    min_samples: int | float,
    max_eps: Float,
    metric: str | Callable,
    p: Int,
    metric_params: dict,
    algorithm: Literal["auto", "ball_tree", "kd_tree", "brute"],
    leaf_size: Int,
    n_jobs: Int,
) -> tuple[ndarray, ndarray, ndarray, ndarray]:
    ...


def cluster_optics_dbscan(
    *,
    reachability: ArrayLike,
    core_distances: ArrayLike,
    ordering: ArrayLike,
    eps: Float,
) -> ndarray:
    ...


def cluster_optics_xi(
    *,
    reachability: ArrayLike,
    predecessor: ArrayLike,
    ordering: ArrayLike,
    min_samples: int | float,
    min_cluster_size: int | float | None = None,
    xi: float = 0.05,
    predecessor_correction: bool = True,
) -> tuple[ndarray, ndarray]:
    ...
