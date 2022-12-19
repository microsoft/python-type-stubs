from typing import Tuple, Union, Callable
from numpy.typing import ArrayLike

# Authors: Robert Layton <robertlayton@gmail.com>
#          Arnaud Fouchet <foucheta@gmail.com>
#          Thierry Guillemot <thierry.guillemot.work@gmail.com>
# License: BSD 3 clause

import functools

import numpy as np
from numpy.random import RandomState

from ...utils import check_random_state
from ...utils import check_X_y
from ...utils import _safe_indexing
from ..pairwise import pairwise_distances_chunked
from ..pairwise import pairwise_distances
from ...preprocessing import LabelEncoder
from numpy import float64, ndarray
from scipy.sparse._csr import csr_matrix

def check_number_of_labels(n_labels: int, n_samples: int) -> None: ...
def silhouette_score(
    X: ArrayLike,
    labels: ArrayLike,
    *,
    metric: str | Callable = "euclidean",
    sample_size: int | None = None,
    random_state: int | RandomState | None = None,
    **kwds,
) -> float: ...
def _silhouette_reduce(D_chunk: ndarray, start: int, labels: ndarray, label_freqs: ndarray) -> Tuple[ndarray, ndarray]: ...
def silhouette_samples(X: ArrayLike, labels: ArrayLike, *, metric: str | Callable = "euclidean", **kwds) -> ArrayLike: ...
def calinski_harabasz_score(X: ArrayLike, labels: ArrayLike) -> float: ...
def davies_bouldin_score(X: ArrayLike, labels: ArrayLike) -> float: ...
