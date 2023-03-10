from typing import Any, Iterable, Self
from .._typing import ArrayLike, Int, MatrixLike, Float
from ..utils.multiclass import (
    unique_labels as unique_labels,
    type_of_target as type_of_target,
)
from ..base import BaseEstimator, TransformerMixin
from ..utils.validation import (
    check_array as check_array,
    check_is_fitted as check_is_fitted,
)
from pandas.core.frame import DataFrame
from collections import defaultdict as defaultdict
from numpy import ndarray
from ..utils import column_or_1d as column_or_1d
from numbers import Integral as Integral
from scipy.sparse import spmatrix, csr_matrix
from ..utils.sparsefuncs import min_max_axis as min_max_axis

# Authors: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Mathieu Blondel <mathieu@mblondel.org>
#          Olivier Grisel <olivier.grisel@ensta.org>
#          Andreas Mueller <amueller@ais.uni-bonn.de>
#          Joel Nothman <joel.nothman@gmail.com>
#          Hamzeh Alsalhi <ha258@cornell.edu>
# License: BSD 3 clause

import itertools
import array
import warnings

import numpy as np
import scipy.sparse as sp


__all__ = [
    "label_binarize",
    "LabelBinarizer",
    "LabelEncoder",
    "MultiLabelBinarizer",
]


class LabelEncoder(TransformerMixin, BaseEstimator):
    def fit(self, y: ArrayLike) -> LabelEncoder | Self:
        ...

    def fit_transform(self, y: ArrayLike) -> ArrayLike:
        ...

    def transform(self, y: ArrayLike) -> ArrayLike:
        ...

    def inverse_transform(self, y: ArrayLike) -> ndarray:
        ...


class LabelBinarizer(TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self, *, neg_label: Int = 0, pos_label: Int = 1, sparse_output: bool = False
    ) -> None:
        ...

    def fit(self, y: MatrixLike | ArrayLike) -> Any:
        ...

    def fit_transform(
        self, y: MatrixLike | ArrayLike
    ) -> csr_matrix | spmatrix | ndarray:
        ...

    def transform(self, y: MatrixLike | ArrayLike) -> csr_matrix | spmatrix | ndarray:
        ...

    def inverse_transform(
        self, Y: MatrixLike, threshold: None | Float = None
    ) -> spmatrix | ndarray:
        ...


def label_binarize(
    y: DataFrame | ArrayLike,
    *,
    classes: ArrayLike,
    neg_label: Int = 0,
    pos_label: Int = 1,
    sparse_output: bool = False
) -> csr_matrix | spmatrix | ndarray:
    ...


class MultiLabelBinarizer(TransformerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self, *, classes: None | ArrayLike = None, sparse_output: bool = False
    ) -> None:
        ...

    def fit(self, y: list[range] | Iterable[Iterable]) -> Any:
        ...

    def fit_transform(self, y: Iterable[Iterable]) -> spmatrix:
        ...

    def transform(
        self, y: list[list[Any | Int]] | Iterable[Iterable]
    ) -> csr_matrix | ndarray:
        ...

    def inverse_transform(self, yt: MatrixLike) -> ndarray:
        ...
