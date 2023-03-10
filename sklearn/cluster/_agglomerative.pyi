from typing import Any, Callable, Literal, Set
from .._typing import MatrixLike, Int, ArrayLike, Float
from ..utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
    HasMethods as HasMethods,
)
from joblib import Memory
from ..metrics.pairwise import paired_distances as paired_distances
from ..utils import check_array as check_array
from scipy.cluster import hierarchy as hierarchy
from ..metrics._dist_metrics import METRIC_MAPPING as METRIC_MAPPING
from ..metrics import DistanceMetric as DistanceMetric
from scipy import sparse as sparse
from ..utils._fast_dict import IntFloatDict as IntFloatDict
from ._feature_agglomeration import AgglomerationTransform
from ..utils.validation import check_memory as check_memory
from numpy import ndarray
from scipy.sparse.csgraph import connected_components as connected_components
from ..base import BaseEstimator, ClusterMixin, ClassNamePrefixFeaturesOutMixin
from numbers import Integral as Integral, Real as Real
from heapq import (
    heapify as heapify,
    heappop as heappop,
    heappush as heappush,
    heappushpop as heappushpop,
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
) -> tuple[ndarray, int, int, ndarray] | tuple[ndarray, int, int, None] | tuple[
    ndarray, int, int, ndarray | None, ndarray
]:
    ...


_TREE_BUILDERS = ...


###############################################################################


class AgglomerativeClustering(ClusterMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_clusters: int | None = 2,
        *,
        affinity: str | Callable = "deprecated",  # TODO(1.4): Remove
        metric: str | None | Callable = None,  # TODO(1.4): Set to "euclidean"
        memory: Memory | str | None = None,
        connectivity: None | Callable | ArrayLike = None,
        compute_full_tree: bool | Literal["auto", "auto"] = "auto",
        linkage: Literal["ward", "complete", "average", "single", "ward"] = "ward",
        distance_threshold: None | Float = None,
        compute_distances: bool = False,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...

    def fit_predict(self, X: MatrixLike, y: Any = None) -> ndarray:
        ...


class FeatureAgglomeration(
    ClassNamePrefixFeaturesOutMixin, AgglomerativeClustering, AgglomerationTransform
):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_clusters: int | None = 2,
        *,
        affinity: str | Callable = "deprecated",  # TODO(1.4): Remove
        metric: str | None | Callable = None,  # TODO(1.4): Set to "euclidean"
        memory: Memory | str | None = None,
        connectivity: None | Callable | ArrayLike = None,
        compute_full_tree: bool | Literal["auto", "auto"] = "auto",
        linkage: Literal["ward", "complete", "average", "single", "ward"] = "ward",
        pooling_func: Callable = ...,
        distance_threshold: None | Float = None,
        compute_distances: bool = False,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...

    @property
    def fit_predict(self):
        ...
