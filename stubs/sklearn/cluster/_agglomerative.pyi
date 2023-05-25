from typing import Any, Callable, ClassVar, Literal, Set, TypeVar
from scipy import sparse as sparse
from joblib import Memory
from ..metrics import DistanceMetric as DistanceMetric
from scipy.cluster import hierarchy as hierarchy
from ..metrics._dist_metrics import METRIC_MAPPING as METRIC_MAPPING
from scipy.sparse.csgraph import connected_components as connected_components
from ._feature_agglomeration import AgglomerationTransform
from heapq import (
    heapify as heapify,
    heappop as heappop,
    heappush as heappush,
    heappushpop as heappushpop,
)
from ..metrics.pairwise import paired_distances as paired_distances
from ..utils.validation import check_memory as check_memory
from numpy import ndarray
from ..utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
    HasMethods as HasMethods,
)
from numbers import Integral as Integral, Real as Real
from ..utils._fast_dict import IntFloatDict as IntFloatDict
from ..base import BaseEstimator, ClusterMixin, ClassNamePrefixFeaturesOutMixin
from ..utils import check_array as check_array
from .._typing import MatrixLike, Int, ArrayLike, Float

FeatureAgglomeration_Self = TypeVar(
    "FeatureAgglomeration_Self", bound="FeatureAgglomeration"
)
AgglomerativeClustering_Self = TypeVar(
    "AgglomerativeClustering_Self", bound="AgglomerativeClustering"
)

import warnings

import numpy as np


###############################################################################
# Hierarchical tree building functions


def ward_tree(
    X: MatrixLike,
    *,
    connectivity: None | MatrixLike = None,
    n_clusters: None | Int = None,
    return_distance: bool = False,
) -> tuple[ndarray, int, int, ndarray | None, ndarray]:
    ...


# single average and complete linkage
def linkage_tree(
    X: MatrixLike,
    connectivity: None | MatrixLike = None,
    n_clusters: None | Int = None,
    linkage: Literal["complete", "average", "complete", "single"] = "complete",
    affinity: str | Callable = "euclidean",
    return_distance: bool = False,
) -> tuple[ndarray, int, int, ndarray | None, ndarray]:
    ...


_TREE_BUILDERS = ...


###############################################################################


class AgglomerativeClustering(ClusterMixin, BaseEstimator):
    distances_: ArrayLike = ...
    children_: ArrayLike = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_connected_components_: int = ...
    n_leaves_: int = ...
    labels_: ndarray = ...
    n_clusters_: int = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_clusters: None | int = 2,
        *,
        affinity: str | Callable = "deprecated",  # TODO(1.4): Remove
        metric: None | str | Callable = None,  # TODO(1.4): Set to "euclidean"
        memory: None | Memory | str = None,
        connectivity: None | ArrayLike | Callable = None,
        compute_full_tree: Literal["auto", "auto"] | bool = "auto",
        linkage: Literal["ward", "complete", "average", "single", "ward"] = "ward",
        distance_threshold: None | Float = None,
        compute_distances: bool = False,
    ) -> None:
        ...

    def fit(
        self: AgglomerativeClustering_Self, X: MatrixLike, y: Any = None
    ) -> AgglomerativeClustering_Self:
        ...

    def fit_predict(self, X: MatrixLike, y: Any = None) -> ndarray:
        ...


class FeatureAgglomeration(
    ClassNamePrefixFeaturesOutMixin, AgglomerativeClustering, AgglomerationTransform
):
    distances_: ArrayLike = ...
    children_: ArrayLike = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_connected_components_: int = ...
    n_leaves_: int = ...
    labels_: ArrayLike = ...
    n_clusters_: int = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_clusters: None | int = 2,
        *,
        affinity: str | Callable = "deprecated",  # TODO(1.4): Remove
        metric: None | str | Callable = None,  # TODO(1.4): Set to "euclidean"
        memory: None | Memory | str = None,
        connectivity: None | ArrayLike | Callable = None,
        compute_full_tree: Literal["auto", "auto"] | bool = "auto",
        linkage: Literal["ward", "complete", "average", "single", "ward"] = "ward",
        pooling_func: Callable = ...,
        distance_threshold: None | Float = None,
        compute_distances: bool = False,
    ) -> None:
        ...

    def fit(
        self: FeatureAgglomeration_Self, X: MatrixLike, y: Any = None
    ) -> FeatureAgglomeration_Self:
        ...

    def fit_predict(self):
        ...
