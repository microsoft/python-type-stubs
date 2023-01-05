from numpy import ndarray
from typing import Literal, Any
from numpy.typing import ArrayLike, NDArray
from numpy.random import RandomState

# Author: Mathieu Blondel <mathieu@mblondel.org>
#         Arnaud Joly <a.joly@ulg.ac.be>
#         Maheshakya Wijewardena <maheshakya.10@cse.mrt.ac.lk>
# License: BSD 3 clause

import warnings
import numpy as np
import scipy.sparse as sp

from .base import BaseEstimator, ClassifierMixin, RegressorMixin
from .base import MultiOutputMixin
from .utils import check_random_state
from .utils import deprecated
from .utils.validation import _num_samples
from .utils.validation import check_array
from .utils.validation import check_consistent_length
from .utils.validation import check_is_fitted, _check_sample_weight
from .utils.random import _random_choice_csc
from .utils.stats import _weighted_percentile
from .utils.multiclass import class_distribution

class DummyClassifier(MultiOutputMixin, ClassifierMixin, BaseEstimator):
    def __init__(
        self,
        *,
        strategy: Literal["most_frequent", "prior", "stratified", "uniform", "constant"] = "prior",
        random_state: int | RandomState | None = None,
        constant: int | str | ArrayLike | None = None,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: ArrayLike, sample_weight: ArrayLike | None = None) -> "DummyClassifier": ...
    def predict(self, X: ArrayLike) -> ArrayLike: ...
    def predict_proba(self, X: ArrayLike) -> NDArray | list[ArrayLike]: ...
    def predict_log_proba(self, X: ArrayLike) -> NDArray | list[ArrayLike]: ...
    def _more_tags(self): ...
    def score(self, X: ArrayLike | None, y: ArrayLike, sample_weight: ArrayLike | None = None) -> float: ...

    # TODO: Remove in 1.2
    # mypy error: Decorated property not supported
    @deprecated("`n_features_in_` is deprecated in 1.0 and will be removed in 1.2.")  # type: ignore
    @property
    def n_features_in_(self): ...

class DummyRegressor(MultiOutputMixin, RegressorMixin, BaseEstimator):
    def __init__(
        self,
        *,
        strategy: Literal["mean", "median", "quantile", "constant"] = "mean",
        constant: int | float | ArrayLike | None = None,
        quantile: float | None = None,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: ArrayLike, sample_weight: ArrayLike | None = None) -> "DummyRegressor": ...
    def predict(self, X: ArrayLike, return_std: bool = False) -> tuple[ArrayLike, ArrayLike]: ...
    def _more_tags(self): ...
    def score(self, X: ArrayLike | None, y: ArrayLike, sample_weight: ArrayLike | None = None) -> float: ...

    # TODO: Remove in 1.2
    # mypy error: Decorated property not supported
    @deprecated("`n_features_in_` is deprecated in 1.0 and will be removed in 1.2.")  # type: ignore
    @property
    def n_features_in_(self): ...
