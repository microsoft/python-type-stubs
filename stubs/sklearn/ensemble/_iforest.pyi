from numbers import Integral as Integral, Real as Real
from typing import Any, ClassVar, Literal, TypeVar
from warnings import warn as warn

from numpy import ndarray
from numpy.random import RandomState
from scipy.sparse import issparse as issparse

from .._typing import ArrayLike, Int, MatrixLike
from ..base import OutlierMixin
from ..tree import ExtraTreeRegressor
from ..tree._tree import DTYPE as tree_dtype
from ..utils import (
    check_array as check_array,
    check_random_state as check_random_state,
    gen_batches as gen_batches,
    get_chunk_n_rows as get_chunk_n_rows,
)
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.validation import check_is_fitted as check_is_fitted
from ._bagging import BaseBagging

IsolationForest_Self = TypeVar("IsolationForest_Self", bound="IsolationForest")

# Authors: Nicolas Goix <nicolas.goix@telecom-paristech.fr>
#          Alexandre Gramfort <alexandre.gramfort@telecom-paristech.fr>
# License: BSD 3 clause

import numbers

import numpy as np

__all__ = ["IsolationForest"]

class IsolationForest(OutlierMixin, BaseBagging):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    offset_: float = ...
    max_samples_: int = ...
    estimators_samples_: list[ndarray] = ...
    estimators_features_: list[ndarray] = ...
    estimators_: list[ExtraTreeRegressor] = ...
    base_estimator_: ExtraTreeRegressor = ...
    estimator_: ExtraTreeRegressor = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        n_estimators: Int = 100,
        max_samples: float | Literal["auto", "auto"] | int = "auto",
        contamination: float | str = "auto",
        max_features: float | int = 1.0,
        bootstrap: bool = False,
        n_jobs: None | Int = None,
        random_state: RandomState | None | Int = None,
        verbose: Int = 0,
        warm_start: bool = False,
    ) -> None: ...
    def fit(
        self: IsolationForest_Self,
        X: MatrixLike | ArrayLike,
        y: Any = None,
        sample_weight: None | ArrayLike = None,
    ) -> IsolationForest_Self: ...
    def predict(self, X: MatrixLike | ArrayLike) -> ndarray: ...
    def decision_function(self, X: MatrixLike | ArrayLike) -> ndarray: ...
    def score_samples(self, X: MatrixLike | ArrayLike) -> ndarray: ...
