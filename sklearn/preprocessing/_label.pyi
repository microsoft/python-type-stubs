from numpy import int64, ndarray
from typing import Dict, List, Union, Any, Iterable
from numpy.typing import ArrayLike, NDArray

# Authors: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Mathieu Blondel <mathieu@mblondel.org>
#          Olivier Grisel <olivier.grisel@ensta.org>
#          Andreas Mueller <amueller@ais.uni-bonn.de>
#          Joel Nothman <joel.nothman@gmail.com>
#          Hamzeh Alsalhi <ha258@cornell.edu>
# License: BSD 3 clause

from collections import defaultdict
import itertools
import array
import warnings

import numpy as np
import scipy.sparse as sp

from ..base import BaseEstimator, TransformerMixin

from ..utils.sparsefuncs import min_max_axis
from ..utils import column_or_1d
from ..utils.validation import _num_samples, check_array, check_is_fitted
from ..utils.multiclass import unique_labels
from ..utils.multiclass import type_of_target
from ..utils._encode import _encode, _unique
from scipy.sparse._csr import csr_matrix

__all__ = [
    "label_binarize",
    "LabelBinarizer",
    "LabelEncoder",
    "MultiLabelBinarizer",
]

class LabelEncoder(TransformerMixin, BaseEstimator):
    def fit(self, y: ArrayLike) -> "LabelEncoder": ...
    def fit_transform(self, y: ArrayLike) -> ArrayLike: ...
    def transform(self, y: ArrayLike) -> ArrayLike: ...
    def inverse_transform(self, y: NDArray) -> NDArray: ...
    def _more_tags(self): ...

class LabelBinarizer(TransformerMixin, BaseEstimator):
    def __init__(
        self, *, neg_label: int = 0, pos_label: int = 1, sparse_output: bool = False
    ) -> None: ...
    def fit(self, y: NDArray) -> "LabelBinarizer": ...
    def fit_transform(self, y: NDArray) -> NDArray: ...
    def transform(self, y: NDArray) -> NDArray: ...
    def inverse_transform(
        self, Y: NDArray, threshold: float | None = None
    ) -> NDArray: ...
    def _more_tags(self): ...

def label_binarize(
    y: ArrayLike,
    *,
    classes: ArrayLike,
    neg_label: int = 0,
    pos_label: int = 1,
    sparse_output: bool = False
) -> NDArray: ...
def _inverse_binarize_multiclass(y: ndarray, classes: ndarray) -> ndarray: ...
def _inverse_binarize_thresholding(
    y: ndarray, output_type: str, classes: ndarray, threshold: float
) -> ndarray: ...

class MultiLabelBinarizer(TransformerMixin, BaseEstimator):
    def __init__(
        self, *, classes: ArrayLike | None = None, sparse_output: bool = False
    ) -> None: ...
    def fit(self, y: Iterable[Iterable]) -> "MultiLabelBinarizer": ...
    def fit_transform(self, y: Iterable[Iterable]) -> NDArray: ...
    def transform(self, y: Iterable[Iterable]) -> NDArray: ...
    def _build_cache(self) -> Dict[int64, int]: ...
    def _transform(
        self, y: List[List[Union[Any, int64]]], class_mapping: Dict[int64, int]
    ) -> csr_matrix: ...
    def inverse_transform(self, yt: NDArray) -> ArrayLike: ...
    def _more_tags(self): ...
