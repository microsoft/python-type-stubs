from numbers import Integral as Integral, Real as Real
from typing import Any, ClassVar, Literal, TypeVar

from joblib import effective_n_jobs as effective_n_jobs
from numpy import ndarray
from numpy.random import RandomState

from .._typing import Float, Int, MatrixLike
from ..base import BaseEstimator
from ..isotonic import IsotonicRegression as IsotonicRegression
from ..metrics import euclidean_distances as euclidean_distances
from ..utils import check_array as check_array, check_random_state as check_random_state, check_symmetric as check_symmetric
from ..utils._param_validation import Hidden as Hidden, Interval as Interval, StrOptions as StrOptions
from ..utils.parallel import Parallel as Parallel, delayed as delayed

MDS_Self = TypeVar("MDS_Self", bound=MDS)

import warnings

import numpy as np

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
) -> tuple[ndarray, float, int] | tuple[ndarray, Float, int]: ...

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
        dissimilarity: Literal["euclidean", "precomputed"] = "euclidean",
        normalized_stress: Literal["auto", "warn"] | bool = "warn",
    ) -> None: ...
    def fit(self: MDS_Self, X: MatrixLike, y: Any = None, init: None | MatrixLike = None) -> MDS_Self: ...
    def fit_transform(self, X: MatrixLike, y: Any = None, init: None | MatrixLike = None) -> ndarray: ...
