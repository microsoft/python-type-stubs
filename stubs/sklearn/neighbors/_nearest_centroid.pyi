import warnings
from numbers import Real as Real
from typing import Callable, ClassVar
from typing_extensions import Self

import numpy as np
from numpy import ndarray
from scipy import sparse as sp

from .._typing import ArrayLike, Float, MatrixLike
from ..base import BaseEstimator, ClassifierMixin
from ..metrics.pairwise import pairwise_distances_argmin as pairwise_distances_argmin
from ..preprocessing import LabelEncoder as LabelEncoder
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.sparsefuncs import csc_median_axis_0 as csc_median_axis_0
from ..utils.validation import check_is_fitted as check_is_fitted

# Author: Robert Layton <robertlayton@gmail.com>
#         Olivier Grisel <olivier.grisel@ensta.org>
#
# License: BSD 3 clause

class NearestCentroid(ClassifierMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    classes_: ndarray = ...
    centroids_: ArrayLike = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(self, metric: str | Callable = "euclidean", *, shrink_threshold: None | Float = None) -> None: ...
    def fit(self, X: MatrixLike | ArrayLike, y: ArrayLike) -> Self: ...
    def predict(self, X: MatrixLike | ArrayLike) -> ndarray: ...
