from typing import Callable, Literal
from ..utils._param_validation import StrOptions as StrOptions
from ..utils.extmath import weighted_mode as weighted_mode
from .._typing import Int, MatrixLike, ArrayLike, Float
from ..base import ClassifierMixin
from ._base import NeighborsBase, KNeighborsMixin, RadiusNeighborsMixin
from numpy import ndarray
from numbers import Integral as Integral

import numpy as np

import warnings


class KNeighborsClassifier(KNeighborsMixin, ClassifierMixin, NeighborsBase):

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

    def fit(self, X: MatrixLike, y: MatrixLike | ArrayLike) -> KNeighborsClassifier:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike) -> list[ndarray] | ndarray:
        ...


class RadiusNeighborsClassifier(RadiusNeighborsMixin, ClassifierMixin, NeighborsBase):

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
        outlier_label: str | None = None,
        metric_params: dict | None = None,
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit(
        self, X: MatrixLike, y: MatrixLike | ArrayLike
    ) -> RadiusNeighborsClassifier:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike) -> list[ndarray] | ndarray:
        ...
