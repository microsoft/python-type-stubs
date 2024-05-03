from typing import Literal

import numpy as np
from numpy import ndarray
from numpy.random import RandomState
from scipy.sparse import issparse as issparse
from scipy.special import digamma as digamma

from .._typing import ArrayLike, Int, MatrixLike
from ..metrics.cluster import mutual_info_score as mutual_info_score
from ..neighbors import KDTree as KDTree, NearestNeighbors as NearestNeighbors
from ..preprocessing import scale as scale
from ..utils import check_random_state as check_random_state
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.validation import check_array as check_array, check_X_y as check_X_y

# Author: Nikolay Mayorov <n59_ru@hotmail.com>
# License: 3-clause BSD

def mutual_info_regression(
    X: MatrixLike,
    y: ArrayLike,
    *,
    discrete_features: Literal["auto", "auto"] | ArrayLike | bool = "auto",
    n_neighbors: Int = 3,
    copy: bool = True,
    random_state: RandomState | None | Int = None,
) -> ndarray: ...
def mutual_info_classif(
    X: MatrixLike,
    y: ArrayLike,
    *,
    discrete_features: Literal["auto", "auto"] | ArrayLike | bool = "auto",
    n_neighbors: Int = 3,
    copy: bool = True,
    random_state: RandomState | None | Int = None,
) -> ndarray: ...
