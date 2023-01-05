from numpy import ndarray
from typing import Dict, Callable, Literal, Mapping
from numpy.typing import ArrayLike, NDArray
from sklearn.neighbors._regression import KNeighborsRegressor, RadiusNeighborsRegressor

# Authors: Jake Vanderplas <vanderplas@astro.washington.edu>
#          Fabian Pedregosa <fabian.pedregosa@inria.fr>
#          Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Sparseness support by Lars Buitinck
#          Multi-output support by Arnaud Joly <a.joly@ulg.ac.be>
#          Empty radius support by Andreas Bjerre-Nielsen
#
# License: BSD 3 clause (C) INRIA, University of Amsterdam,
#                           University of Copenhagen

import warnings

import numpy as np

from ._base import _get_weights, _check_weights
from ._base import NeighborsBase, KNeighborsMixin, RadiusNeighborsMixin
from ..base import RegressorMixin

class KNeighborsRegressor(KNeighborsMixin, RegressorMixin, NeighborsBase):
    def __init__(
        self,
        n_neighbors: int = 5,
        *,
        weights: Literal["uniform", "distance"] | Callable = "uniform",
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute"] = "auto",
        leaf_size: int = 30,
        p: int = 2,
        metric: str | Callable = "minkowski",
        metric_params: Mapping | None = None,
        n_jobs: int | None = None,
    ) -> None: ...
    def _more_tags(self) -> Dict[str, bool]: ...
    def fit(self, X: ArrayLike, y: NDArray | ArrayLike) -> KNeighborsRegressor: ...
    def predict(self, X: ArrayLike) -> np.ndarray: ...

class RadiusNeighborsRegressor(RadiusNeighborsMixin, RegressorMixin, NeighborsBase):
    def __init__(
        self,
        radius: float = 1.0,
        *,
        weights: Literal["uniform", "distance"] | Callable = "uniform",
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute"] = "auto",
        leaf_size: int = 30,
        p: int = 2,
        metric: str | Callable = "minkowski",
        metric_params: Mapping | None = None,
        n_jobs: int | None = None,
    ): ...
    def fit(self, X: ArrayLike, y: NDArray | ArrayLike) -> RadiusNeighborsRegressor: ...
    def predict(self, X: ArrayLike) -> NDArray: ...
