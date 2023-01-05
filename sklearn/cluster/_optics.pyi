from numpy import float64, int64, ndarray
from typing import Dict, List, Tuple, Union, Callable, Mapping, Literal, Any
from numpy.typing import ArrayLike, NDArray

import warnings
import numpy as np

from ..exceptions import DataConversionWarning
from ..metrics.pairwise import PAIRWISE_BOOLEAN_FUNCTIONS
from ..utils import gen_batches, get_chunk_n_rows
from ..utils.validation import check_memory
from ..neighbors import NearestNeighbors
from ..base import BaseEstimator, ClusterMixin
from ..metrics import pairwise_distances
from sklearn.neighbors._unsupervised import NearestNeighbors

class OPTICS(ClusterMixin, BaseEstimator):
    def __init__(
        self,
        *,
        min_samples: int | float = 5,
        max_eps: float = ...,
        metric: str | Callable = "minkowski",
        p: int = 2,
        metric_params: Mapping | None = None,
        cluster_method: str = "xi",
        eps: float | None = None,
        xi: float = 0.05,
        predecessor_correction: bool = True,
        min_cluster_size: int | float | None = None,
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute"] = "auto",
        leaf_size: int = 30,
        memory: str | Memory | None = None,
        n_jobs: int | None = None,
    ) -> None: ...
    def fit(self, X: NDArray, y: None = None) -> "OPTICS": ...

def _validate_size(size: Union[int, float], n_samples: int, param_name: str) -> None: ...

# OPTICS helper functions
def _compute_core_distances_(X: ndarray, neighbors: NearestNeighbors, min_samples: int, working_memory: None) -> ndarray: ...
def compute_optics_graph(
    X: NDArray,
    *,
    min_samples: int | float,
    max_eps: float,
    metric: str | Callable,
    p: int,
    metric_params: Mapping,
    algorithm: Literal["auto", "ball_tree", "kd_tree", "brute"],
    leaf_size: int,
    n_jobs: int,
) -> tuple[ArrayLike, ArrayLike, ArrayLike, ArrayLike]: ...
def _set_reach_dist(
    core_distances_: ndarray,
    reachability_: ndarray,
    predecessor_: ndarray,
    point_index: int64,
    processed: ndarray,
    X: ndarray,
    nbrs: NearestNeighbors,
    metric: str,
    metric_params: None,
    p: int,
    max_eps: float,
) -> None: ...
def cluster_optics_dbscan(
    *,
    reachability: ArrayLike,
    core_distances: ArrayLike,
    ordering: ArrayLike,
    eps: float,
) -> ArrayLike: ...
def cluster_optics_xi(
    *,
    reachability: NDArray,
    predecessor: NDArray,
    ordering: NDArray,
    min_samples: int | float,
    min_cluster_size: int | float | None = None,
    xi: float = 0.05,
    predecessor_correction: bool = True,
) -> tuple[NDArray, np.ndarray]: ...
def _extend_region(steep_point: ndarray, xward_point: ndarray, start: int64, min_samples: int) -> int64: ...
def _update_filter_sdas(
    sdas: List[Union[Dict[str, Union[int64, float64]], Dict[str, Union[int64, float]], Any]],
    mib: float64,
    xi_complement: float,
    reachability_plot: ndarray,
) -> List[Union[Dict[str, Union[int64, float64]], Any]]: ...
def _correct_predecessor(
    reachability_plot: ndarray,
    predecessor_plot: ndarray,
    ordering: ndarray,
    s: int64,
    e: int64,
) -> Tuple[int64, int64]: ...
def _xi_cluster(
    reachability_plot: ndarray,
    predecessor_plot: ndarray,
    ordering: ndarray,
    xi: float,
    min_samples: int,
    min_cluster_size: int,
    predecessor_correction: bool,
) -> ndarray: ...
def _extract_xi_labels(ordering: ndarray, clusters: ndarray) -> ndarray: ...
