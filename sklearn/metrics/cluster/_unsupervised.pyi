from typing import Callable
from numpy.random import RandomState
from ..pairwise import (
    pairwise_distances_chunked as pairwise_distances_chunked,
    pairwise_distances as pairwise_distances,
)
from ...preprocessing import LabelEncoder as LabelEncoder
from ...utils import check_random_state as check_random_state, check_X_y as check_X_y
from ..._typing import Int, MatrixLike, ArrayLike, Float

# Authors: Robert Layton <robertlayton@gmail.com>
#          Arnaud Fouchet <foucheta@gmail.com>
#          Thierry Guillemot <thierry.guillemot.work@gmail.com>
# License: BSD 3 clause


import functools

import numpy as np


def check_number_of_labels(n_labels: Int, n_samples: Int) -> None:
    ...


def silhouette_score(
    X: MatrixLike,
    labels: ArrayLike,
    *,
    metric: str | Callable = "euclidean",
    sample_size: None | Int = None,
    random_state: RandomState | None | Int = None,
    **kwds
) -> Float:
    ...


def silhouette_samples(
    X: MatrixLike, labels: ArrayLike, *, metric: str | Callable = "euclidean", **kwds
) -> ArrayLike:
    ...


def calinski_harabasz_score(X: MatrixLike, labels: ArrayLike) -> float:
    ...


def davies_bouldin_score(X: MatrixLike, labels: ArrayLike) -> float:
    ...
