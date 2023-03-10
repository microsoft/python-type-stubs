from typing import Any, Callable, Literal
from .._typing import Int, Float, MatrixLike
from ._base import NeighborsBase, KNeighborsMixin, RadiusNeighborsMixin


class NearestNeighbors(KNeighborsMixin, RadiusNeighborsMixin, NeighborsBase):
    def __init__(
        self,
        *,
        n_neighbors: Int = 5,
        radius: Float = 1.0,
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute", "auto"] = "auto",
        leaf_size: Int = 30,
        metric: str | Callable = "minkowski",
        p: Float = 2,
        metric_params: dict | None = None,
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit(self, X: NearestNeighbors | MatrixLike, y: Any = None) -> NearestNeighbors:
        ...
