from typing import Any, ClassVar, TypeVar
from scipy import sparse as sparse
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from numpy import ndarray
from ..utils.extmath import row_norms as row_norms
from ..utils._param_validation import Interval as Interval
from numbers import Integral as Integral, Real as Real
from .._config import config_context as config_context
from math import sqrt as sqrt
from ..base import (
    TransformerMixin,
    ClusterMixin,
    BaseEstimator,
    ClassNamePrefixFeaturesOutMixin,
)
from scipy.sparse import spmatrix
from ..metrics.pairwise import euclidean_distances as euclidean_distances
from .._typing import Float, Int, ArrayLike, MatrixLike
from ..metrics import pairwise_distances_argmin as pairwise_distances_argmin
from ..utils.validation import check_is_fitted as check_is_fitted
from . import AgglomerativeClustering as AgglomerativeClustering

Birch_Self = TypeVar("Birch_Self", bound="Birch")

# Authors: Manoj Kumar <manojkumarsivaraj334@gmail.com>
#          Alexandre Gramfort <alexandre.gramfort@telecom-paristech.fr>
#          Joel Nothman <joel.nothman@gmail.com>
# License: BSD 3 clause

import warnings
import numpy as np


class _CFNode:
    squared_norm_: ndarray = ...
    centroids_: ndarray = ...
    init_sq_norm_: ndarray = ...
    init_centroids_: ndarray = ...
    next_leaf_: _CFNode = ...
    prev_leaf_: _CFNode = ...
    subclusters_: list = ...

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
    sq_norm_: ndarray = ...
    child_: _CFNode = ...
    centroid_: ndarray = ...
    squared_sum_: float = ...
    linear_sum_: ndarray = ...
    n_samples_: int = ...

    def __init__(self, *, linear_sum: None | ArrayLike = None) -> None:
        ...

    def update(self, subcluster: _CFSubcluster) -> None:
        ...

    def merge_subcluster(
        self, nominee_cluster: _CFSubcluster, threshold: float
    ) -> bool:
        ...

    def radius(self):
        ...


class Birch(
    ClassNamePrefixFeaturesOutMixin, ClusterMixin, TransformerMixin, BaseEstimator
):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    labels_: ndarray = ...
    subcluster_labels_: ndarray = ...
    subcluster_centers_: ndarray = ...
    dummy_leaf_: _CFNode = ...
    root_: _CFNode = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        threshold: Float = 0.5,
        branching_factor: Int = 50,
        n_clusters: None | int = 3,
        compute_labels: bool = True,
        copy: bool = True,
    ) -> None:
        ...

    def fit(self: Birch_Self, X: MatrixLike | ArrayLike, y: Any = None) -> Birch_Self:
        ...

    def partial_fit(
        self: Birch_Self, X: None | MatrixLike | ArrayLike = None, y: Any = None
    ) -> Birch_Self:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> ndarray | spmatrix:
        ...
