from typing import Optional, Literal, Callable, Mapping
from numpy.typing import ArrayLike, NDArray
from sklearn.neighbors._lof import LocalOutlierFactor

# Authors: Nicolas Goix <nicolas.goix@telecom-paristech.fr>
#          Alexandre Gramfort <alexandre.gramfort@telecom-paristech.fr>
# License: BSD 3 clause

import numpy as np
import warnings

from ._base import NeighborsBase
from ._base import KNeighborsMixin
from ..base import OutlierMixin

from ..utils.metaestimators import available_if
from ..utils.validation import check_is_fitted
from ..utils import check_array
from numpy import ndarray

__all__ = ["LocalOutlierFactor"]

class LocalOutlierFactor(KNeighborsMixin, OutlierMixin, NeighborsBase):
    def __init__(
        self,
        n_neighbors: int = 20,
        *,
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute"] = "auto",
        leaf_size: int = 30,
        metric: str | Callable = "minkowski",
        p: int = 2,
        metric_params: Mapping | None = None,
        contamination: float | Literal["auto"] = "auto",
        novelty: bool = False,
        n_jobs: int | None = None,
    ) -> None: ...
    def _check_novelty_fit_predict(self) -> bool: ...
    @available_if(_check_novelty_fit_predict)
    def fit_predict(self, X: ArrayLike, y: None = None) -> NDArray: ...
    def fit(self, X: ArrayLike, y: None = None) -> LocalOutlierFactor: ...
    def _check_novelty_predict(self) -> bool: ...
    @available_if(_check_novelty_predict)
    def predict(self, X: ArrayLike | None = None) -> NDArray: ...
    def _predict(self, X: Optional[ndarray] = None) -> ndarray: ...
    def _check_novelty_decision_function(self) -> bool: ...
    @available_if(_check_novelty_decision_function)
    def decision_function(self, X: ArrayLike) -> NDArray: ...
    def _check_novelty_score_samples(self) -> bool: ...
    @available_if(_check_novelty_score_samples)
    def score_samples(self, X: ArrayLike) -> NDArray: ...
    def _local_reachability_density(self, distances_X: ndarray, neighbors_indices: ndarray) -> ndarray: ...
