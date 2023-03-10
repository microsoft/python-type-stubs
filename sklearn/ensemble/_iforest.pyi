from typing import Any, Literal
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from numpy.random import RandomState
from .._typing import Int, ArrayLike, MatrixLike
from ..base import OutlierMixin
from ..tree import ExtraTreeRegressor as ExtraTreeRegressor
from ..utils.validation import check_is_fitted as check_is_fitted
from ..tree._tree import DTYPE as tree_dtype
from numpy import ndarray
from ._bagging import BaseBagging
from ..utils import (
    check_random_state as check_random_state,
    check_array as check_array,
    gen_batches as gen_batches,
    get_chunk_n_rows as get_chunk_n_rows,
)
from numbers import Integral as Integral, Real as Real
from scipy.sparse import issparse as issparse
from warnings import warn as warn

# Authors: Nicolas Goix <nicolas.goix@telecom-paristech.fr>
#          Alexandre Gramfort <alexandre.gramfort@telecom-paristech.fr>
# License: BSD 3 clause

import numbers
import numpy as np

__all__ = ["IsolationForest"]


class IsolationForest(OutlierMixin, BaseBagging):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        n_estimators: Int = 100,
        max_samples: int | float | Literal["auto", "auto"] = "auto",
        contamination: float | str = "auto",
        max_features: int | float = 1.0,
        bootstrap: bool = False,
        n_jobs: None | Int = None,
        random_state: RandomState | None | Int = None,
        verbose: Int = 0,
        warm_start: bool = False,
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: Any = None,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def decision_function(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def score_samples(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...
