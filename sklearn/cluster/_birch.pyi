from typing import Any, Self
from ..utils._param_validation import Interval as Interval
from ..utils.extmath import row_norms as row_norms
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from .._typing import Float, Int, ArrayLike, MatrixLike
from math import sqrt as sqrt
from scipy import sparse as sparse
from ..base import (
    TransformerMixin,
    ClusterMixin,
    BaseEstimator,
    ClassNamePrefixFeaturesOutMixin,
)
from ..utils.validation import check_is_fitted as check_is_fitted
from ..metrics.pairwise import euclidean_distances as euclidean_distances
from numpy import ndarray
from . import AgglomerativeClustering as AgglomerativeClustering
from numbers import Integral as Integral, Real as Real
from scipy.sparse import spmatrix
from .._config import config_context as config_context
from ..metrics import pairwise_distances_argmin as pairwise_distances_argmin

# Authors: Manoj Kumar <manojkumarsivaraj334@gmail.com>
#          Alexandre Gramfort <alexandre.gramfort@telecom-paristech.fr>
#          Joel Nothman <joel.nothman@gmail.com>
# License: BSD 3 clause

import warnings
import numpy as np


class _CFNode:
    def __init__(
        self,
        *,
        threshold: Float,
        branching_factor: Int,
        is_leaf: bool,
        n_features: Int,
        dtype,
    ) -> None:
        ...

    def append_subcluster(self, subcluster: _CFSubcluster) -> None:
        ...

    def update_split_subclusters(
        self,
        subcluster: _CFSubcluster,
        new_subcluster1: _CFSubcluster,
        new_subcluster2: _CFSubcluster,
    ) -> None:
        ...

    def insert_cf_subcluster(self, subcluster: _CFSubcluster) -> bool:
        ...


class _CFSubcluster:
    def __init__(self, *, linear_sum: None | ArrayLike = None) -> None:
        ...

    def update(self, subcluster: _CFSubcluster) -> None:
        ...

    def merge_subcluster(
        self, nominee_cluster: _CFSubcluster, threshold: float
    ) -> bool:
        ...

    @property
    def radius(self):
        ...


class Birch(
    ClassNamePrefixFeaturesOutMixin, ClusterMixin, TransformerMixin, BaseEstimator
):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        threshold: Float = 0.5,
        branching_factor: Int = 50,
        n_clusters: int | None = 3,
        compute_labels: bool = True,
        copy: bool = True,
    ) -> None:
        ...

    def fit(self, X: MatrixLike | ArrayLike, y: Any = None) -> Birch | Self:
        ...

    def partial_fit(
        self, X: None | MatrixLike | ArrayLike = None, y: Any = None
    ) -> Self:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> spmatrix | ndarray:
        ...
