from typing import Dict, List, Union, Literal, Any
from numpy.typing import ArrayLike, NDArray

# Authors: Nicolas Goix <nicolas.goix@telecom-paristech.fr>
#          Alexandre Gramfort <alexandre.gramfort@telecom-paristech.fr>
# License: BSD 3 clause

import numbers
import numpy as np
from numpy.random import RandomState
from scipy.sparse import issparse
from warnings import warn

from ..tree import ExtraTreeRegressor
from ..utils import (
    check_random_state,
    check_array,
    gen_batches,
    get_chunk_n_rows,
)
from ..utils.validation import check_is_fitted, _num_samples
from ..base import OutlierMixin

from ._bagging import BaseBagging
from numpy import ndarray

__all__ = ["IsolationForest"]

class IsolationForest(OutlierMixin, BaseBagging):
    def __init__(
        self,
        *,
        n_estimators: int = 100,
        max_samples: int | float | Literal["auto"] = "auto",
        contamination: float | Literal["auto"] = "auto",
        max_features: int | float = 1.0,
        bootstrap: bool = False,
        n_jobs: int | None = None,
        random_state: int | RandomState | None = None,
        verbose: int = 0,
        warm_start: bool = False,
    ) -> None: ...
    def _set_oob_score(self, X, y): ...
    def _parallel_args(self) -> Dict[str, str]: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: None = None,
        sample_weight: ArrayLike | None = None,
    ) -> "IsolationForest": ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    def decision_function(self, X: NDArray | ArrayLike) -> NDArray: ...
    def score_samples(self, X: NDArray | ArrayLike) -> NDArray: ...
    def _compute_chunked_score_samples(self, X: ndarray) -> ndarray: ...
    def _compute_score_samples(self, X: ndarray, subsample_features: bool) -> ndarray: ...
    def _more_tags(self): ...

def _average_path_length(n_samples_leaf: Union[List[int], ndarray]) -> ndarray: ...
