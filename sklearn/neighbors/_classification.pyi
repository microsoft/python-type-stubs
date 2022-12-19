from sklearn.neighbors._classification import (
    KNeighborsClassifier,
    RadiusNeighborsClassifier,
)
from numpy import ndarray
from typing import Dict, Union, Callable, Literal, Mapping
from numpy.typing import ArrayLike, NDArray

# Authors: Jake Vanderplas <vanderplas@astro.washington.edu>
#          Fabian Pedregosa <fabian.pedregosa@inria.fr>
#          Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Sparseness support by Lars Buitinck
#          Multi-output support by Arnaud Joly <a.joly@ulg.ac.be>
#
# License: BSD 3 clause (C) INRIA, University of Amsterdam

import numpy as np
from ..utils.fixes import _mode
from ..utils.extmath import weighted_mode
from ..utils.validation import _is_arraylike, _num_samples

import warnings
from ._base import _check_weights, _get_weights
from ._base import NeighborsBase, KNeighborsMixin, RadiusNeighborsMixin
from ..base import ClassifierMixin
from pandas.core.series import Series
from scipy.sparse._csr import csr_matrix

class KNeighborsClassifier(KNeighborsMixin, ClassifierMixin, NeighborsBase):
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
    def fit(self, X: ArrayLike, y: NDArray | ArrayLike) -> KNeighborsClassifier: ...
    def predict(self, X: ArrayLike) -> np.ndarray: ...
    def predict_proba(self, X: ArrayLike) -> NDArray | list[NDArray]: ...
    def _more_tags(self) -> Dict[str, bool]: ...

class RadiusNeighborsClassifier(RadiusNeighborsMixin, ClassifierMixin, NeighborsBase):
    def __init__(
        self,
        radius: float = 1.0,
        *,
        weights: Literal["uniform", "distance"] | Callable = "uniform",
        algorithm: Literal["auto", "ball_tree", "kd_tree", "brute"] = "auto",
        leaf_size: int = 30,
        p: int = 2,
        metric: str | Callable = "minkowski",
        outlier_label=None,
        metric_params: Mapping | None = None,
        n_jobs: int | None = None,
        **kwargs,
    ): ...
    def fit(self, X: ArrayLike, y: NDArray | ArrayLike) -> RadiusNeighborsClassifier: ...
    def predict(self, X: ArrayLike) -> np.ndarray: ...
    def predict_proba(self, X: ArrayLike) -> NDArray | list[NDArray]: ...
    def _more_tags(self): ...
