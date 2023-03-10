from typing import Any, Literal
from ..utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    Hidden as Hidden,
)
from numpy.random import RandomState
from .._typing import MatrixLike, Int, Float
from ..base import BaseEstimator
from joblib import effective_n_jobs as effective_n_jobs
from numpy import ndarray
from ..utils import (
    check_random_state as check_random_state,
    check_array as check_array,
    check_symmetric as check_symmetric,
)
from numbers import Integral as Integral, Real as Real
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from ..isotonic import IsotonicRegression as IsotonicRegression
from ..metrics import euclidean_distances as euclidean_distances

import numpy as np

import warnings


def smacof(
    dissimilarities: MatrixLike,
    *,
    metric: bool = True,
    n_components: Int = 2,
    init: None | MatrixLike = None,
    n_init: Int = 8,
    n_jobs: None | Int = None,
    max_iter: Int = 300,
    verbose: Int = 0,
    eps: Float = 1e-3,
    random_state: RandomState | None | Int = None,
    return_n_iter: bool = False,
    normalized_stress: bool | Literal["auto", "warn"] = "warn",
) -> tuple[ndarray, Float, int] | tuple[ndarray, float, int]:
    ...


class MDS(BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_components: Int = 2,
        *,
        metric: bool = True,
        n_init: Int = 4,
        max_iter: Int = 300,
        verbose: Int = 0,
        eps: Float = 1e-3,
        n_jobs: None | Int = None,
        random_state: RandomState | None | Int = None,
        dissimilarity: Literal["euclidean", "precomputed", "euclidean"] = "euclidean",
        normalized_stress: bool | Literal["auto", "warn"] = "warn",
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None, init: None | MatrixLike = None) -> Any:
        ...

    def fit_transform(
        self, X: MatrixLike, y: Any = None, init: None | MatrixLike = None
    ) -> ndarray:
        ...
