from typing import Callable, ClassVar, Literal, TypeVar
from ._base import NeighborsBase, KNeighborsMixin, RadiusNeighborsMixin
from numpy import ndarray
from ..utils.extmath import weighted_mode as weighted_mode
from ..utils._param_validation import StrOptions as StrOptions
from numbers import Integral as Integral
from ..base import ClassifierMixin
from .._typing import Int, MatrixLike, ArrayLike, Float

RadiusNeighborsClassifier_Self = TypeVar(
    "RadiusNeighborsClassifier_Self", bound="RadiusNeighborsClassifier"
)
KNeighborsClassifier_Self = TypeVar(
    "KNeighborsClassifier_Self", bound="KNeighborsClassifier"
)


import numpy as np

import warnings


class KNeighborsClassifier(KNeighborsMixin, ClassifierMixin, NeighborsBase):
    outputs_2d_: bool = ...
    n_samples_fit_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    effective_metric_params_: dict = ...
    effective_metric_: str | Callable = ...
    classes_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_neighbors: Int = 5,
        *,
        weights: None
        | Literal["uniform", "distance", "uniform"]
        | Callable = "uniform",
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute", "auto"] = "auto",
        leaf_size: Int = 30,
        p: Int = 2,
        metric: str | Callable = "minkowski",
        metric_params: None | dict = None,
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit(
        self: KNeighborsClassifier_Self, X: MatrixLike, y: MatrixLike | ArrayLike
    ) -> KNeighborsClassifier_Self:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike) -> ndarray | list[ndarray]:
        ...


class RadiusNeighborsClassifier(RadiusNeighborsMixin, ClassifierMixin, NeighborsBase):
    outputs_2d_: bool = ...
    outlier_label_: ArrayLike | int = ...
    n_samples_fit_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    effective_metric_params_: dict = ...
    effective_metric_: str | Callable = ...
    classes_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        radius: Float = 1.0,
        *,
        weights: None
        | Literal["uniform", "distance", "uniform"]
        | Callable = "uniform",
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute", "auto"] = "auto",
        leaf_size: Int = 30,
        p: Int = 2,
        metric: str | Callable = "minkowski",
        outlier_label: None | str = None,
        metric_params: None | dict = None,
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit(
        self: RadiusNeighborsClassifier_Self, X: MatrixLike, y: MatrixLike | ArrayLike
    ) -> RadiusNeighborsClassifier_Self:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike) -> ndarray:
        ...
