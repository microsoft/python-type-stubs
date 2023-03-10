from typing import Any, Callable, Literal
from ..utils._param_validation import StrOptions as StrOptions
from .._typing import Int, Float, MatrixLike
from ..base import TransformerMixin, ClassNamePrefixFeaturesOutMixin
from ._ball_tree import BallTree
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import KNeighborsMixin, RadiusNeighborsMixin, NeighborsBase
from numpy import ndarray
from scipy.sparse._csr import csr_matrix
from scipy.sparse import spmatrix
from ._unsupervised import NearestNeighbors


def kneighbors_graph(
    X: NearestNeighbors | BallTree | ndarray,
    n_neighbors: Int,
    *,
    mode: Literal["connectivity", "distance", "connectivity"] = "connectivity",
    metric: str = "minkowski",
    p: Int = 2,
    metric_params: dict | None = None,
    include_self: bool | str = False,
    n_jobs: None | Int = None,
) -> spmatrix | csr_matrix:
    ...


def radius_neighbors_graph(
    X: BallTree,
    radius: Float,
    *,
    mode: Literal["connectivity", "distance", "connectivity"] = "connectivity",
    metric: str = "minkowski",
    p: Int = 2,
    metric_params: dict | None = None,
    include_self: bool | str = False,
    n_jobs: None | Int = None,
) -> spmatrix:
    ...


class KNeighborsTransformer(
    ClassNamePrefixFeaturesOutMixin, KNeighborsMixin, TransformerMixin, NeighborsBase
):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        mode: Literal["distance", "connectivity", "distance"] = "distance",
        n_neighbors: Int = 5,
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute", "auto"] = "auto",
        leaf_size: Int = 30,
        metric: str | Callable = "minkowski",
        p: Int = 2,
        metric_params: dict | None = None,
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> KNeighborsTransformer:
        ...

    def transform(self, X: MatrixLike) -> spmatrix | csr_matrix:
        ...

    def fit_transform(self, X: MatrixLike, y: Any = None) -> spmatrix | csr_matrix:
        ...


class RadiusNeighborsTransformer(
    ClassNamePrefixFeaturesOutMixin,
    RadiusNeighborsMixin,
    TransformerMixin,
    NeighborsBase,
):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        mode: Literal["distance", "connectivity", "distance"] = "distance",
        radius: Float = 1.0,
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute", "auto"] = "auto",
        leaf_size: Int = 30,
        metric: str | Callable = "minkowski",
        p: Int = 2,
        metric_params: dict | None = None,
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> RadiusNeighborsTransformer:
        ...

    def transform(self, X: MatrixLike) -> spmatrix:
        ...

    def fit_transform(self, X: MatrixLike, y: Any = None) -> spmatrix:
        ...
