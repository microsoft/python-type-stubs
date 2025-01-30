from typing import Callable, ClassVar, Literal, TypeVar

from numpy import ndarray

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import RegressorMixin
from ..utils._param_validation import StrOptions as StrOptions
from ._base import KNeighborsMixin, NeighborsBase, RadiusNeighborsMixin

KNeighborsRegressor_Self = TypeVar("KNeighborsRegressor_Self", bound=KNeighborsRegressor)
RadiusNeighborsRegressor_Self = TypeVar("RadiusNeighborsRegressor_Self", bound=RadiusNeighborsRegressor)

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

class KNeighborsRegressor(KNeighborsMixin, RegressorMixin, NeighborsBase):
    n_samples_fit_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    effective_metric_params_: dict = ...
    effective_metric_: str | Callable = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_neighbors: Int = 5,
        *,
        weights: None | Literal["uniform", "distance"] | Callable = "uniform",
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute"] = "auto",
        leaf_size: Int = 30,
        p: Int = 2,
        metric: str | Callable = "minkowski",
        metric_params: None | dict = None,
        n_jobs: None | Int = None,
    ) -> None: ...
    def fit(self: KNeighborsRegressor_Self, X: MatrixLike, y: MatrixLike | ArrayLike) -> KNeighborsRegressor_Self: ...
    def predict(self, X: MatrixLike) -> ndarray: ...

class RadiusNeighborsRegressor(RadiusNeighborsMixin, RegressorMixin, NeighborsBase):
    n_samples_fit_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    effective_metric_params_: dict = ...
    effective_metric_: str | Callable = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        radius: Float = 1.0,
        *,
        weights: None | Literal["uniform", "distance"] | Callable = "uniform",
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute"] = "auto",
        leaf_size: Int = 30,
        p: Int = 2,
        metric: str | Callable = "minkowski",
        metric_params: None | dict = None,
        n_jobs: None | Int = None,
    ) -> None: ...
    def fit(self: RadiusNeighborsRegressor_Self, X: MatrixLike, y: MatrixLike | ArrayLike) -> RadiusNeighborsRegressor_Self: ...
    def predict(self, X: MatrixLike) -> ndarray: ...
