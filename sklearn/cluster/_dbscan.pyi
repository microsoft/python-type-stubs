from numpy import ndarray
from typing import Callable, Mapping, Literal, Any
from numpy.typing import ArrayLike, NDArray

# Author: Robert Layton <robertlayton@gmail.com>
#         Joel Nothman <joel.nothman@gmail.com>
#         Lars Buitinck
#
# License: BSD 3 clause

import numpy as np
import numbers
import warnings
from scipy import sparse

from ..utils import check_scalar
from ..base import BaseEstimator, ClusterMixin
from ..utils.validation import _check_sample_weight
from ..neighbors import NearestNeighbors

def dbscan(
    X: ArrayLike,
    eps: float = 0.5,
    *,
    min_samples: int = 5,
    metric: str | Callable = "minkowski",
    metric_params: Mapping | None = None,
    algorithm: Literal["auto", "ball_tree", "kd_tree", "brute"] = "auto",
    leaf_size: int = 30,
    p: float = 2,
    sample_weight: ArrayLike | None = None,
    n_jobs: int | None = None,
) -> tuple[np.ndarray, NDArray]: ...

class DBSCAN(ClusterMixin, BaseEstimator):
    def __init__(
        self,
        eps: float = 0.5,
        *,
        min_samples: int = 5,
        metric: str | Callable = "euclidean",
        metric_params: Mapping | None = None,
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute"] = "auto",
        leaf_size: int = 30,
        p: float | None = None,
        n_jobs: int | None = None,
    ) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike | tuple[int, int],
        y: None = None,
        sample_weight: ArrayLike | None = None,
    ) -> "DBSCAN": ...
    def fit_predict(
        self,
        X: NDArray | ArrayLike | tuple[int, int],
        y=None,
        sample_weight: ArrayLike | None = None,
    ) -> NDArray: ...
    def _more_tags(self): ...
