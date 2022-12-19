from numpy import ndarray
from typing import Dict, Optional, Union, Literal, Mapping, Callable
from numpy.typing import ArrayLike, NDArray
from sklearn.neighbors._graph import KNeighborsTransformer, RadiusNeighborsTransformer

# Author: Jake Vanderplas <vanderplas@astro.washington.edu>
#         Tom Dupre la Tour
#
# License: BSD 3 clause (C) INRIA, University of Amsterdam
from ._base import KNeighborsMixin, RadiusNeighborsMixin
from ._base import NeighborsBase
from ._unsupervised import NearestNeighbors
from ..base import TransformerMixin, _ClassNamePrefixFeaturesOutMixin
from ..utils.validation import check_is_fitted
from scipy.sparse._csr import csr_matrix
from sklearn.neighbors._unsupervised import NearestNeighbors
from ._ball_tree import BallTree

def _check_params(X: NearestNeighbors, metric: str, p: int, metric_params: None) -> None: ...
def _query_include_self(X: Union[ndarray, csr_matrix], include_self: bool, mode: str) -> Optional[ndarray]: ...
def kneighbors_graph(
    X: ArrayLike | BallTree,
    n_neighbors: int,
    *,
    mode: Literal["connectivity", "distance"] = "connectivity",
    metric: str = "minkowski",
    p: int = 2,
    metric_params: Mapping | None = None,
    include_self: bool | Literal["auto"] = False,
    n_jobs: int | None = None,
) -> NDArray: ...
def radius_neighbors_graph(
    X: ArrayLike | BallTree,
    radius: float,
    *,
    mode: Literal["connectivity", "distance"] = "connectivity",
    metric: str = "minkowski",
    p: int = 2,
    metric_params: Mapping | None = None,
    include_self: bool | Literal["auto"] = False,
    n_jobs: int | None = None,
) -> NDArray: ...

class KNeighborsTransformer(_ClassNamePrefixFeaturesOutMixin, KNeighborsMixin, TransformerMixin, NeighborsBase):
    def __init__(
        self,
        *,
        mode: Literal["distance", "connectivity"] = "distance",
        n_neighbors: int = 5,
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute"] = "auto",
        leaf_size: int = 30,
        metric: str | Callable = "minkowski",
        p: int = 2,
        metric_params: Mapping | None = None,
        n_jobs: int = 1,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: None = None) -> KNeighborsTransformer: ...
    def transform(self, X: ArrayLike) -> NDArray: ...
    def fit_transform(self, X: ArrayLike, y: Optional[ndarray] = None) -> NDArray: ...
    def _more_tags(self) -> Dict[str, Dict[str, str]]: ...

class RadiusNeighborsTransformer(
    _ClassNamePrefixFeaturesOutMixin,
    RadiusNeighborsMixin,
    TransformerMixin,
    NeighborsBase,
):
    def __init__(
        self,
        *,
        mode: Literal["distance", "connectivity"] = "distance",
        radius: float = 1.0,
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute"] = "auto",
        leaf_size: int = 30,
        metric: str | Callable = "minkowski",
        p: int = 2,
        metric_params: Mapping | None = None,
        n_jobs: int = 1,
    ): ...
    def fit(self, X: ArrayLike, y=None) -> RadiusNeighborsTransformer: ...
    def transform(self, X: ArrayLike) -> NDArray: ...
    def fit_transform(self, X: ArrayLike, y=None) -> NDArray: ...
    def _more_tags(self): ...
