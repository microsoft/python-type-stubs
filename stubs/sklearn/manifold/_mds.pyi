from typing import Any, ClassVar, Literal, TypeVar
from numpy.random import RandomState
from ..isotonic import IsotonicRegression as IsotonicRegression
from numpy import ndarray
from ..utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    Hidden as Hidden,
)
from joblib import effective_n_jobs as effective_n_jobs
from numbers import Integral as Integral, Real as Real
from ..metrics import euclidean_distances as euclidean_distances
from ..base import BaseEstimator
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from .._typing import MatrixLike, Int, Float
from ..utils import (
    check_random_state as check_random_state,
    check_array as check_array,
    check_symmetric as check_symmetric,
)

MDS_Self = TypeVar("MDS_Self", bound="MDS")


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
    normalized_stress: Literal["auto", "warn"] | bool = "warn",
) -> tuple[ndarray, float, int] | tuple[ndarray, Float, int]:
    ...


class MDS(BaseEstimator):
    n_iter_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    dissimilarity_matrix_: ndarray = ...
    stress_: float = ...
    embedding_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

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
        normalized_stress: Literal["auto", "warn"] | bool = "warn",
    ) -> None:
        ...

    def fit(
        self: MDS_Self, X: MatrixLike, y: Any = None, init: None | MatrixLike = None
    ) -> MDS_Self:
        ...

    def fit_transform(
        self, X: MatrixLike, y: Any = None, init: None | MatrixLike = None
    ) -> ndarray:
        ...
