from typing import Any, Callable, ClassVar, Literal
from typing_extensions import Self

from numpy import ndarray

from ..._typing import Float, Int, MatrixLike
from ...base import BaseEstimator, ClusterMixin

class HDBSCAN(ClusterMixin, BaseEstimator):
    labels_: ndarray = ...
    probabilities_: ndarray = ...
    n_features_in_: int = ...
    feature_names_in_: ndarray = ...
    centroids_: ndarray = ...
    medoids_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        min_cluster_size: Int = 5,
        min_samples: None | Int = None,
        cluster_selection_epsilon: Float = 0.0,
        max_cluster_size: None | Int = None,
        metric: str | Callable = "euclidean",
        metric_params: None | dict = None,
        alpha: Float = 1.0,
        algorithm: Literal["auto", "brute", "kd_tree", "ball_tree"] = "auto",
        leaf_size: Int = 40,
        n_jobs: None | Int = None,
        cluster_selection_method: Literal["eom", "leaf"] = "eom",
        allow_single_cluster: bool = False,
        store_centers: None | Literal["centroid", "medoid", "both"] = None,
        copy: bool = False,
    ) -> None: ...
    def fit(self, X: MatrixLike, y: Any = None) -> Self: ...
    def fit_predict(self, X: MatrixLike, y: Any = None) -> ndarray: ...
    def dbscan_clustering(self, cut_distance: Float, min_cluster_size: Int = 5) -> ndarray: ...
