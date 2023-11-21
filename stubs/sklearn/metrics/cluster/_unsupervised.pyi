import functools
from typing import Callable

import numpy as np
from numpy.random import RandomState

from ..._typing import ArrayLike, Float, Int, MatrixLike
from ...preprocessing import LabelEncoder as LabelEncoder
from ...utils import check_random_state as check_random_state, check_X_y as check_X_y
from ..pairwise import pairwise_distances as pairwise_distances, pairwise_distances_chunked as pairwise_distances_chunked

# Authors: Robert Layton <robertlayton@gmail.com>
#          Arnaud Fouchet <foucheta@gmail.com>
#          Thierry Guillemot <thierry.guillemot.work@gmail.com>
# License: BSD 3 clause

def check_number_of_labels(n_labels: Int, n_samples: Int) -> None: ...
def silhouette_score(
    X: MatrixLike,
    labels: ArrayLike,
    *,
    metric: str | Callable = "euclidean",
    sample_size: None | Int = None,
    random_state: RandomState | None | Int = None,
    **kwds,
) -> Float: ...
def silhouette_samples(X: MatrixLike, labels: ArrayLike, *, metric: str | Callable = "euclidean", **kwds) -> ArrayLike: ...
def calinski_harabasz_score(X: MatrixLike, labels: ArrayLike) -> float: ...
def davies_bouldin_score(X: MatrixLike, labels: ArrayLike) -> float: ...
