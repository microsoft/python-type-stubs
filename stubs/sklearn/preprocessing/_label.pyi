from collections import defaultdict as defaultdict
from numbers import Integral as Integral
from typing import Any, ClassVar, Iterable, TypeVar

from numpy import ndarray
from pandas.core.frame import DataFrame
from scipy.sparse import csr_matrix, spmatrix

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, TransformerMixin
from ..utils import column_or_1d as column_or_1d
from ..utils.multiclass import type_of_target as type_of_target, unique_labels as unique_labels
from ..utils.sparsefuncs import min_max_axis as min_max_axis
from ..utils.validation import check_array as check_array, check_is_fitted as check_is_fitted

MultiLabelBinarizer_Self = TypeVar("MultiLabelBinarizer_Self", bound=MultiLabelBinarizer)
LabelEncoder_Self = TypeVar("LabelEncoder_Self", bound=LabelEncoder)
LabelBinarizer_Self = TypeVar("LabelBinarizer_Self", bound=LabelBinarizer)

# Authors: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Mathieu Blondel <mathieu@mblondel.org>
#          Olivier Grisel <olivier.grisel@ensta.org>
#          Andreas Mueller <amueller@ais.uni-bonn.de>
#          Joel Nothman <joel.nothman@gmail.com>
#          Hamzeh Alsalhi <ha258@cornell.edu>
# License: BSD 3 clause

import array
import itertools
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
    classes_: ndarray = ...

    def fit(self: LabelEncoder_Self, y: ArrayLike) -> LabelEncoder_Self: ...
    def fit_transform(self, y: ArrayLike) -> ArrayLike: ...
    def transform(self, y: ArrayLike) -> ArrayLike: ...
    def inverse_transform(self, y: ArrayLike) -> ndarray: ...

class LabelBinarizer(TransformerMixin, BaseEstimator):
    sparse_input_: bool = ...
    y_type_: str = ...
    classes_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(self, *, neg_label: Int = 0, pos_label: Int = 1, sparse_output: bool = False) -> None: ...
    def fit(self: LabelBinarizer_Self, y: MatrixLike | ArrayLike) -> LabelBinarizer_Self: ...
    def fit_transform(self, y: MatrixLike | ArrayLike) -> ndarray | spmatrix: ...
    def transform(self, y: MatrixLike | ArrayLike) -> ndarray | spmatrix: ...
    def inverse_transform(self, Y: MatrixLike, threshold: None | Float = None) -> ndarray | spmatrix: ...

def label_binarize(
    y: ArrayLike | DataFrame, *, classes: ArrayLike, neg_label: Int = 0, pos_label: Int = 1, sparse_output: bool = False
) -> ndarray | spmatrix: ...

class MultiLabelBinarizer(TransformerMixin, BaseEstimator):
    classes_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(self, *, classes: None | ArrayLike = None, sparse_output: bool = False) -> None: ...
    def fit(self: MultiLabelBinarizer_Self, y: Iterable[Iterable] | list[range]) -> MultiLabelBinarizer_Self: ...
    def fit_transform(self, y: Iterable[Iterable]) -> ndarray | spmatrix: ...
    def transform(self, y: list[list[Any | Int]] | Iterable[Iterable]) -> csr_matrix | ndarray: ...
    def inverse_transform(self, yt: MatrixLike) -> ndarray: ...
