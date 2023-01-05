from sklearn.neighbors._unsupervised import NearestNeighbors
from typing import Union, Literal, Callable, Mapping
from numpy.typing import ArrayLike
from ._base import NeighborsBase
from ._base import KNeighborsMixin
from ._base import RadiusNeighborsMixin
from numpy import ndarray
from scipy.sparse._csr import csr_matrix

class NearestNeighbors(KNeighborsMixin, RadiusNeighborsMixin, NeighborsBase):
    def __init__(
        self,
        *,
        n_neighbors: int = 5,
        radius: float = 1.0,
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute"] = "auto",
        leaf_size: int = 30,
        metric: str | Callable = "minkowski",
        p: int = 2,
        metric_params: Mapping | None = None,
        n_jobs: int | None = None,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: None = None) -> NearestNeighbors: ...
