from numpy import bool_, float64, ndarray
from typing import Iterator, Union, Literal
from numpy.typing import ArrayLike, NDArray

# Author: Nikolay Mayorov <n59_ru@hotmail.com>
# License: 3-clause BSD

import numpy as np
from numpy.random import RandomState
from scipy.sparse import issparse
from scipy.special import digamma

from ..metrics.cluster import mutual_info_score
from ..preprocessing import scale
from ..utils import check_random_state
from ..utils.validation import check_array, check_X_y
from ..utils.multiclass import check_classification_targets

def _compute_mi_cc(x: ndarray, y: ndarray, n_neighbors: int) -> Union[int, float64]: ...
def _compute_mi_cd(c, d, n_neighbors): ...
def _compute_mi(x: ndarray, y: ndarray, x_discrete: bool_, y_discrete: bool, n_neighbors: int = 3) -> Union[int, float64]: ...
def _iterate_columns(X: ndarray, columns: None = None) -> Iterator[ndarray]: ...
def _estimate_mi(
    X: ndarray,
    y: ndarray,
    discrete_features: str = "auto",
    discrete_target: bool = False,
    n_neighbors: int = 3,
    copy: bool = True,
    random_state: None = None,
) -> ndarray: ...
def mutual_info_regression(
    X: ArrayLike | NDArray,
    y: ArrayLike,
    *,
    discrete_features: Literal["auto"] | bool | ArrayLike = "auto",
    n_neighbors: int = 3,
    copy: bool = True,
    random_state: int | RandomState | None = None,
) -> NDArray: ...
def mutual_info_classif(
    X: ArrayLike | NDArray,
    y: ArrayLike,
    *,
    discrete_features: Literal["auto"] | bool | ArrayLike = "auto",
    n_neighbors: int = 3,
    copy: bool = True,
    random_state: int | RandomState | None = None,
) -> NDArray: ...
