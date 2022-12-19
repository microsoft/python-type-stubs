from numpy import ndarray
from numpy.typing import NDArray, ArrayLike

# Authors: Manoj Kumar <manojkumarsivaraj334@gmail.com>
#          Alexandre Gramfort <alexandre.gramfort@telecom-paristech.fr>
#          Joel Nothman <joel.nothman@gmail.com>
# License: BSD 3 clause

import warnings
import numbers
import numpy as np
from scipy import sparse
from math import sqrt

from ..metrics import pairwise_distances_argmin
from ..metrics.pairwise import euclidean_distances
from ..base import (
    TransformerMixin,
    ClusterMixin,
    BaseEstimator,
    _ClassNamePrefixFeaturesOutMixin,
)
from ..utils.extmath import row_norms
from ..utils import check_scalar, deprecated
from ..utils.validation import check_is_fitted
from ..exceptions import ConvergenceWarning
from . import AgglomerativeClustering
from .._config import config_context
from typing import List, Optional, Tuple

def _iterate_sparse_X(X): ...
def _split_node(node: "_CFNode", threshold: float, branching_factor: int) -> Tuple[_CFSubcluster, _CFSubcluster]: ...

class _CFNode:
    def __init__(self, *, threshold: float, branching_factor: int, is_leaf: bool, n_features: int) -> None: ...
    def append_subcluster(self, subcluster: "_CFSubcluster") -> None: ...
    def update_split_subclusters(
        self,
        subcluster: "_CFSubcluster",
        new_subcluster1: "_CFSubcluster",
        new_subcluster2: "_CFSubcluster",
    ) -> None: ...
    def insert_cf_subcluster(self, subcluster: "_CFSubcluster") -> bool: ...

class _CFSubcluster:
    def __init__(self, *, linear_sum: NDArray | None = None) -> None: ...
    def update(self, subcluster: "_CFSubcluster") -> None: ...
    def merge_subcluster(self, nominee_cluster: "_CFSubcluster", threshold: float) -> bool: ...
    @property
    def radius(self): ...

class Birch(_ClassNamePrefixFeaturesOutMixin, ClusterMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        *,
        threshold: float = 0.5,
        branching_factor: int = 50,
        n_clusters: int | Model = 3,
        compute_labels: bool = True,
        copy: bool = True,
    ) -> None: ...

    # TODO: Remove in 1.2
    # mypy error: Decorated property not supported
    @deprecated("`fit_` is deprecated in 1.0 and will be removed in 1.2.")  # type: ignore
    @property
    def fit_(self): ...

    # TODO: Remove in 1.2
    # mypy error: Decorated property not supported
    @deprecated("`partial_fit_` is deprecated in 1.0 and will be removed in 1.2.")  # type: ignore
    @property
    def partial_fit_(self): ...
    def fit(self, X: NDArray | ArrayLike, y: None = None) -> "Birch": ...
    def _fit(self, X: ndarray, partial: bool) -> "Birch": ...
    def _get_leaves(self) -> List[_CFNode]: ...
    def partial_fit(self, X: NDArray | ArrayLike | None = None, y=None): ...
    def _check_fit(self, X): ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    def _predict(self, X: ndarray) -> ndarray: ...
    def transform(self, X: NDArray | ArrayLike) -> NDArray | ArrayLike: ...
    def _global_clustering(self, X: Optional[ndarray] = None) -> None: ...
