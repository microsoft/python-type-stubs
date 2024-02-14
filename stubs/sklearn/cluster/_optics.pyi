from numbers import Integral as Integral, Real as Real
from typing import Any, Callable, ClassVar, Literal, TypeVar

from joblib import Memory
from numpy import ndarray
from scipy.sparse import SparseEfficiencyWarning as SparseEfficiencyWarning, issparse as issparse

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, ClusterMixin
from ..exceptions import DataConversionWarning as DataConversionWarning
from ..metrics import pairwise_distances as pairwise_distances
from ..metrics.pairwise import PAIRWISE_BOOLEAN_FUNCTIONS as PAIRWISE_BOOLEAN_FUNCTIONS
from ..neighbors import NearestNeighbors as NearestNeighbors
from ..utils import gen_batches as gen_batches, get_chunk_n_rows as get_chunk_n_rows
from ..utils._param_validation import HasMethods as HasMethods, Interval as Interval, StrOptions as StrOptions
from ..utils.validation import check_memory as check_memory

OPTICS_Self = TypeVar("OPTICS_Self", bound="OPTICS")

import warnings

import numpy as np

class OPTICS(ClusterMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    cluster_hierarchy_: ndarray = ...
    predecessor_: ndarray = ...
    core_distances_: ndarray = ...
    ordering_: ndarray = ...
    reachability_: ndarray = ...
    labels_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        min_samples: float | int = 5,
        max_eps: Float = ...,
        metric: str | Callable = "minkowski",
        p: Float = 2,
        metric_params: None | dict = None,
        cluster_method: str = "xi",
        eps: None | Float = None,
        xi: float = 0.05,
        predecessor_correction: bool = True,
        min_cluster_size: float | None | int = None,
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute", "auto"] = "auto",
        leaf_size: Int = 30,
        memory: None | Memory | str = None,
        n_jobs: None | Int = None,
    ) -> None: ...
    def fit(self: OPTICS_Self, X: MatrixLike, y: Any = None) -> OPTICS_Self: ...

def compute_optics_graph(
    X: MatrixLike,
    *,
    min_samples: float | int,
    max_eps: Float,
    metric: str | Callable,
    p: Int,
    metric_params: dict,
    algorithm: Literal["auto", "ball_tree", "kd_tree", "brute"],
    leaf_size: Int,
    n_jobs: Int,
) -> tuple[ndarray, ndarray, ndarray, ndarray]: ...
def cluster_optics_dbscan(
    *,
    reachability: ArrayLike,
    core_distances: ArrayLike,
    ordering: ArrayLike,
    eps: Float,
) -> ndarray: ...
def cluster_optics_xi(
    *,
    reachability: ArrayLike,
    predecessor: ArrayLike,
    ordering: ArrayLike,
    min_samples: float | int,
    min_cluster_size: float | None | int = None,
    xi: float = 0.05,
    predecessor_correction: bool = True,
) -> tuple[ndarray, ndarray]: ...
