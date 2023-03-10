from typing import Any, Callable, Literal
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from .._typing import Int, ArrayLike, MatrixLike
from ..base import OutlierMixin
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import NeighborsBase, KNeighborsMixin
from numpy import ndarray
from ..utils import check_array as check_array
from numbers import Real as Real
from ..utils.metaestimators import available_if as available_if

# Authors: Nicolas Goix <nicolas.goix@telecom-paristech.fr>
#          Alexandre Gramfort <alexandre.gramfort@telecom-paristech.fr>
# License: BSD 3 clause

import numpy as np
import warnings

__all__ = ["LocalOutlierFactor"]


class LocalOutlierFactor(KNeighborsMixin, OutlierMixin, NeighborsBase):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_neighbors: Int = 20,
        *,
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute", "auto"] = "auto",
        leaf_size: Int = 30,
        metric: str | Callable = "minkowski",
        p: Int = 2,
        metric_params: dict | None = None,
        contamination: float | str = "auto",
        novelty: bool = False,
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit_predict(self, X: MatrixLike | ArrayLike, y: Any = None) -> ndarray:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> LocalOutlierFactor:
        ...

    def predict(self, X: None | MatrixLike | ArrayLike = None) -> ndarray:
        ...

    def decision_function(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def score_samples(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...
