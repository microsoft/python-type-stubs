from numbers import Real as Real
from typing import Any, Callable, ClassVar, Literal, TypeVar

from numpy import ndarray

from .._typing import ArrayLike, Int, MatrixLike
from ..base import OutlierMixin
from ..utils import check_array as check_array
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.metaestimators import available_if as available_if
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import KNeighborsMixin, NeighborsBase

LocalOutlierFactor_Self = TypeVar("LocalOutlierFactor_Self", bound="LocalOutlierFactor")

# Authors: Nicolas Goix <nicolas.goix@telecom-paristech.fr>
#          Alexandre Gramfort <alexandre.gramfort@telecom-paristech.fr>
# License: BSD 3 clause

import warnings

import numpy as np

__all__ = ["LocalOutlierFactor"]

class LocalOutlierFactor(KNeighborsMixin, OutlierMixin, NeighborsBase):
    n_samples_fit_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    effective_metric_params_: dict = ...
    effective_metric_: str = ...
    offset_: float = ...
    n_neighbors_: int = ...
    negative_outlier_factor_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_neighbors: Int = 20,
        *,
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute", "auto"] = "auto",
        leaf_size: Int = 30,
        metric: str | Callable = "minkowski",
        p: Int = 2,
        metric_params: None | dict = None,
        contamination: float | str = "auto",
        novelty: bool = False,
        n_jobs: None | Int = None,
    ) -> None: ...
    def fit_predict(self, X: MatrixLike | ArrayLike, y: Any = None) -> ndarray: ...
    def fit(self: LocalOutlierFactor_Self, X: MatrixLike, y: Any = None) -> LocalOutlierFactor_Self: ...
    def predict(self, X: None | MatrixLike | ArrayLike = None) -> ndarray: ...
    def decision_function(self, X: MatrixLike | ArrayLike) -> ndarray: ...
    def score_samples(self, X: MatrixLike | ArrayLike) -> ndarray: ...
