from numpy import float64, ndarray
from numpy.typing import ArrayLike, NDArray

# Authors: Olivier Grisel <olivier.grisel@ensta.org>
#          Wei LI <kuantkid@gmail.com>
#          Diego Molla <dmolla-aliod@gmail.com>
#          Arnaud Fouchet <foucheta@gmail.com>
#          Thierry Guillemot <thierry.guillemot.work@gmail.com>
#          Gregory Stupp <stuppie@gmail.com>
#          Joel Nothman <joel.nothman@gmail.com>
#          Arya McCarthy <arya@jhu.edu>
#          Uwe F Mayer <uwe_f_mayer@yahoo.com>
# License: BSD 3 clause

import warnings
from math import log

import numpy as np
from scipy import sparse as sp

from ._expected_mutual_info_fast import expected_mutual_information
from ...utils.multiclass import type_of_target
from ...utils.validation import check_array, check_consistent_length
from scipy.sparse._csr import csr_matrix
from typing import Optional, Tuple

def check_clusterings(
    labels_true: ArrayLike, labels_pred: ArrayLike
) -> Tuple[ndarray, ndarray]: ...
def _generalized_average(U: float64, V: float64, average_method: str) -> float64: ...
def contingency_matrix(
    labels_true: NDArray,
    labels_pred: ArrayLike,
    *,
    eps: float | None = None,
    sparse: bool = False,
    dtype: int | float = ...
) -> NDArray | ArrayLike: ...

# clustering measures

def pair_confusion_matrix(
    labels_true: ArrayLike, labels_pred: ArrayLike
) -> np.ndarray: ...
def rand_score(labels_true: ArrayLike, labels_pred: ArrayLike) -> float: ...
def adjusted_rand_score(labels_true: NDArray, labels_pred: ArrayLike) -> float: ...
def homogeneity_completeness_v_measure(
    labels_true: NDArray, labels_pred: ArrayLike, *, beta: float = 1.0
) -> tuple[float, float, float]: ...
def homogeneity_score(labels_true: NDArray, labels_pred: ArrayLike) -> float: ...
def completeness_score(labels_true: NDArray, labels_pred: ArrayLike) -> float: ...
def v_measure_score(
    labels_true: NDArray, labels_pred: ArrayLike, *, beta: float = 1.0
) -> float: ...
def mutual_info_score(
    labels_true: NDArray, labels_pred: ArrayLike, *, contingency: NDArray | None = None
) -> float: ...
def adjusted_mutual_info_score(
    labels_true: NDArray, labels_pred: ArrayLike, *, average_method: str = "arithmetic"
) -> float: ...
def normalized_mutual_info_score(
    labels_true: NDArray, labels_pred: ArrayLike, *, average_method: str = "arithmetic"
) -> float: ...
def fowlkes_mallows_score(
    labels_true: NDArray, labels_pred: NDArray, *, sparse: bool = False
) -> float: ...
def entropy(labels: ArrayLike) -> float64: ...
