from typing import Any, Callable, Literal, TypeVar
from numpy import ndarray
from ._base import NeighborsBase, KNeighborsMixin, RadiusNeighborsMixin
from .._typing import Int, Float, MatrixLike

NearestNeighbors_Self = TypeVar("NearestNeighbors_Self", bound="NearestNeighbors")


class NearestNeighbors(KNeighborsMixin, RadiusNeighborsMixin, NeighborsBase):
    n_samples_fit_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    effective_metric_params_: dict = ...
    effective_metric_: str = ...

    def __init__(
        self,
        *,
        n_neighbors: Int = 5,
        radius: Float = 1.0,
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute", "auto"] = "auto",
        leaf_size: Int = 30,
        metric: str | Callable = "minkowski",
        p: Float = 2,
        metric_params: None | dict = None,
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit(
        self: NearestNeighbors_Self, X: MatrixLike, y: Any = None
    ) -> NearestNeighbors_Self:
        ...
