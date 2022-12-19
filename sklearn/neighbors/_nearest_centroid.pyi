from typing import Union, Callable, Any
from numpy.typing import ArrayLike, NDArray

# Author: Robert Layton <robertlayton@gmail.com>
#         Olivier Grisel <olivier.grisel@ensta.org>
#
# License: BSD 3 clause

import warnings
import numpy as np
from scipy import sparse as sp

from ..base import BaseEstimator, ClassifierMixin
from ..metrics.pairwise import pairwise_distances
from ..preprocessing import LabelEncoder
from ..utils.validation import check_is_fitted
from ..utils.sparsefuncs import csc_median_axis_0
from ..utils.multiclass import check_classification_targets
from numpy import ndarray
from scipy.sparse._csr import csr_matrix

class NearestCentroid(ClassifierMixin, BaseEstimator):
    def __init__(self, metric: str | Callable = "euclidean", *, shrink_threshold: float | None = None) -> None: ...
    def fit(self, X: NDArray | ArrayLike, y: ArrayLike) -> "NearestCentroid": ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
