from typing import Any, Callable
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from .._typing import Float, ArrayLike, MatrixLike
from ..utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from scipy import sparse as sp
from ..base import BaseEstimator, ClassifierMixin
from ..preprocessing import LabelEncoder as LabelEncoder
from ..utils.validation import check_is_fitted as check_is_fitted
from ..metrics.pairwise import pairwise_distances_argmin as pairwise_distances_argmin
from numpy import ndarray
from numbers import Real as Real
from ..utils.sparsefuncs import csc_median_axis_0 as csc_median_axis_0

# Author: Robert Layton <robertlayton@gmail.com>
#         Olivier Grisel <olivier.grisel@ensta.org>
#
# License: BSD 3 clause

import warnings
import numpy as np


class NearestCentroid(ClassifierMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        metric: str | Callable = "euclidean",
        *,
        shrink_threshold: None | Float = None
    ) -> None:
        ...

    def fit(self, X: MatrixLike | ArrayLike, y: ArrayLike) -> Any:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...
