from typing import Literal
from numpy.random import RandomState
from scipy.special import digamma as digamma
from .._typing import MatrixLike, ArrayLike, Int
from ..utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from ..neighbors import NearestNeighbors as NearestNeighbors, KDTree as KDTree
from ..preprocessing import scale as scale
from ..utils.validation import check_array as check_array, check_X_y as check_X_y
from numpy import ndarray
from ..utils import check_random_state as check_random_state
from scipy.sparse import issparse as issparse
from ..metrics.cluster import mutual_info_score as mutual_info_score

# Author: Nikolay Mayorov <n59_ru@hotmail.com>
# License: 3-clause BSD

import numpy as np


def mutual_info_regression(
    X: MatrixLike,
    y: ArrayLike,
    *,
    discrete_features: bool | Literal["auto", "auto"] | ArrayLike = "auto",
    n_neighbors: Int = 3,
    copy: bool = True,
    random_state: RandomState | None | Int = None
) -> ndarray:
    ...


def mutual_info_classif(
    X: MatrixLike,
    y: ArrayLike,
    *,
    discrete_features: bool | Literal["auto", "auto"] | ArrayLike = "auto",
    n_neighbors: Int = 3,
    copy: bool = True,
    random_state: RandomState | None | Int = None
) -> ndarray:
    ...
