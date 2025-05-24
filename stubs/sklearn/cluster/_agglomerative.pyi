from typing import Any, Callable, ClassVar, Literal
from typing_extensions import Self

from joblib import Memory
from numpy import ndarray

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, ClusterMixin
from ._feature_agglomeration import AgglomerationTransform

###############################################################################
# Hierarchical tree building functions

def ward_tree(
    X: MatrixLike,
    *,
    connectivity: None | MatrixLike = None,
    n_clusters: None | Int = None,
    return_distance: bool = False,
) -> tuple[ndarray, int, int, ndarray | None, ndarray]: ...

# single average and complete linkage
def linkage_tree(
    X: MatrixLike,
    connectivity: None | MatrixLike = None,
    n_clusters: None | Int = None,
    linkage: Literal["complete", "average", "single"] = "complete",
    affinity: str | Callable = "euclidean",
    return_distance: bool = False,
) -> tuple[ndarray, int, int, ndarray | None, ndarray]: ...

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
        compute_full_tree: Literal["auto"] | bool = "auto",
        linkage: Literal["ward", "complete", "average", "single"] = "ward",
        distance_threshold: None | Float = None,
        compute_distances: bool = False,
    ) -> None: ...
    def fit(self, X: MatrixLike, y: Any = None) -> Self: ...
    def fit_predict(self, X: MatrixLike, y: Any = None) -> ndarray: ...

class FeatureAgglomeration(ClassNamePrefixFeaturesOutMixin, AgglomerativeClustering, AgglomerationTransform):
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
        compute_full_tree: Literal["auto"] | bool = "auto",
        linkage: Literal["ward", "complete", "average", "single"] = "ward",
        pooling_func: Callable = ...,
        distance_threshold: None | Float = None,
        compute_distances: bool = False,
    ) -> None: ...
    def fit(self, X: MatrixLike, y: Any = None) -> Self: ...
    def fit_predict(self): ...
