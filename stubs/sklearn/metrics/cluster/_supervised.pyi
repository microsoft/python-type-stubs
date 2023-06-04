from scipy import sparse as sp
from numpy import ndarray
from ...utils.multiclass import type_of_target as type_of_target
from ...utils.validation import (
    check_array as check_array,
    check_consistent_length as check_consistent_length,
)
from math import log as log
from scipy.sparse import spmatrix
from ..._typing import ArrayLike, Float, MatrixLike
from ._expected_mutual_info_fast import (
    expected_mutual_information as expected_mutual_information,
)

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

import numpy as np


def check_clusterings(
    labels_true: ArrayLike, labels_pred: ArrayLike
) -> tuple[ndarray, ndarray]:
    ...


def contingency_matrix(
    labels_true: ArrayLike,
    labels_pred: ArrayLike,
    *,
    eps: None | Float = None,
    sparse: bool = False,
    dtype: float | int = ...
) -> ndarray | spmatrix:
    ...


# clustering measures


def pair_confusion_matrix(labels_true: ArrayLike, labels_pred: ArrayLike) -> ndarray:
    ...


def rand_score(labels_true: ArrayLike, labels_pred: ArrayLike) -> Float:
    ...


def adjusted_rand_score(labels_true: ArrayLike, labels_pred: ArrayLike) -> float:
    ...


def homogeneity_completeness_v_measure(
    labels_true: ArrayLike, labels_pred: ArrayLike, *, beta: Float = 1.0
) -> tuple[float, float, float] | tuple[Float, Float, Float]:
    ...


def homogeneity_score(labels_true: ArrayLike, labels_pred: ArrayLike) -> Float:
    ...


def completeness_score(labels_true: ArrayLike, labels_pred: ArrayLike) -> Float:
    ...


def v_measure_score(
    labels_true: ArrayLike, labels_pred: ArrayLike, *, beta: Float = 1.0
) -> Float:
    ...


def mutual_info_score(
    labels_true: None | ArrayLike,
    labels_pred: None | ArrayLike,
    *,
    contingency: None | MatrixLike = None
) -> Float:
    ...


def adjusted_mutual_info_score(
    labels_true: ArrayLike,
    labels_pred: ArrayLike,
    *,
    average_method: str = "arithmetic"
) -> Float:
    ...


def normalized_mutual_info_score(
    labels_true: ArrayLike,
    labels_pred: ArrayLike,
    *,
    average_method: str = "arithmetic"
) -> Float:
    ...


def fowlkes_mallows_score(
    labels_true: ArrayLike, labels_pred: ArrayLike, *, sparse: bool = False
) -> float:
    ...


def entropy(labels: ArrayLike) -> Float:
    ...
