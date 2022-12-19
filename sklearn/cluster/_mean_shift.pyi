from numpy import float64, ndarray
from typing import Tuple, Any
from numpy.typing import ArrayLike, NDArray

# Authors: Conrad Lee <conradlee@gmail.com>
#          Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Gael Varoquaux <gael.varoquaux@normalesup.org>
#          Martino Sorbaro <martino.sorbaro@ed.ac.uk>

import numpy as np
from numpy.random import RandomState
import warnings

from collections import defaultdict
from ..utils.validation import check_is_fitted
from ..utils.fixes import delayed
from ..utils import check_random_state, gen_batches, check_array
from ..base import BaseEstimator, ClusterMixin
from ..neighbors import NearestNeighbors
from ..metrics.pairwise import pairwise_distances_argmin
from .._config import config_context
from sklearn.neighbors._unsupervised import NearestNeighbors

def estimate_bandwidth(
    X: ArrayLike,
    *,
    quantile: float = 0.3,
    n_samples: int | None = None,
    random_state: int | RandomState = 0,
    n_jobs: int | None = None,
) -> float: ...

# separate function for each seed's iterative loop
def _mean_shift_single_seed(
    my_mean: ndarray, X: ndarray, nbrs: NearestNeighbors, max_iter: int
) -> Tuple[Tuple[float64, float64], int, int]: ...
def mean_shift(
    X: ArrayLike,
    *,
    bandwidth: float | None = None,
    seeds: ArrayLike | None = None,
    bin_seeding: bool = False,
    min_bin_freq: int = 1,
    cluster_all: bool = True,
    max_iter: int = 300,
    n_jobs: int | None = None,
) -> tuple[np.ndarray, NDArray]: ...
def get_bin_seeds(X: ArrayLike, bin_size: float, min_bin_freq: int = 1) -> ArrayLike: ...

class MeanShift(ClusterMixin, BaseEstimator):
    def __init__(
        self,
        *,
        bandwidth: float | None = None,
        seeds: ArrayLike | None = None,
        bin_seeding: bool = False,
        min_bin_freq: int = 1,
        cluster_all: bool = True,
        n_jobs: int | None = None,
        max_iter: int = 300,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: None = None) -> "MeanShift": ...
    def predict(self, X: ArrayLike) -> NDArray: ...
