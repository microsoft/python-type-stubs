from typing import Callable, Literal
from ..utils._param_validation import StrOptions as StrOptions
from .._typing import Int, MatrixLike, ArrayLike, Float
from ..base import RegressorMixin
from ._base import NeighborsBase, KNeighborsMixin, RadiusNeighborsMixin
from numpy import ndarray

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

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_neighbors: Int = 5,
        *,
        weights: Literal["uniform", "distance", "uniform"]
        | None
        | Callable = "uniform",
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute", "auto"] = "auto",
        leaf_size: Int = 30,
        p: Int = 2,
        metric: str | Callable = "minkowski",
        metric_params: dict | None = None,
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: MatrixLike | ArrayLike) -> KNeighborsRegressor:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...


class RadiusNeighborsRegressor(RadiusNeighborsMixin, RegressorMixin, NeighborsBase):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        radius: Float = 1.0,
        *,
        weights: Literal["uniform", "distance", "uniform"]
        | None
        | Callable = "uniform",
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute", "auto"] = "auto",
        leaf_size: Int = 30,
        p: Int = 2,
        metric: str | Callable = "minkowski",
        metric_params: dict | None = None,
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: MatrixLike | ArrayLike) -> RadiusNeighborsRegressor:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...
