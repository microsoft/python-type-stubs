from math import log as log, sqrt as sqrt
from numbers import Integral as Integral, Real as Real
from typing import Any, ClassVar, Literal, TypeVar

from numpy import ndarray
from numpy.random import RandomState
from scipy import linalg as linalg
from scipy.sparse import issparse as issparse
from scipy.sparse.linalg import svds as svds
from scipy.special import gammaln as gammaln

from .._typing import Float, Int, MatrixLike
from ..utils import check_random_state as check_random_state
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.deprecation import deprecated
from ..utils.extmath import (
    fast_logdet as fast_logdet,
    randomized_svd as randomized_svd,
    stable_cumsum as stable_cumsum,
    svd_flip as svd_flip,
)
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import _BasePCA

PCA_Self = TypeVar("PCA_Self", bound="PCA")

import numpy as np

class PCA(_BasePCA):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    noise_variance_: float = ...
    n_samples_: int = ...
    n_components_: int = ...
    mean_: ndarray = ...
    singular_values_: ndarray = ...
    explained_variance_ratio_: ndarray = ...
    explained_variance_: ndarray = ...
    components_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_components: float | None | str | Int = None,
        *,
        copy: bool = True,
        whiten: bool = False,
        svd_solver: Literal["auto", "full", "arpack", "randomized", "auto"] = "auto",
        tol: Float = 0.0,
        iterated_power: Literal["auto", "auto"] | Int = "auto",
        n_oversamples: Int = 10,
        power_iteration_normalizer: Literal["auto", "QR", "LU", "none", "auto"] = "auto",
        random_state: RandomState | None | Int = None,
    ) -> None: ...

    # TODO(1.4): remove in 1.4
    # mypy error: Decorated property not supported
    @deprecated(  # type: ignore
        "Attribute `n_features_` was deprecated in version 1.2 and will be " "removed in 1.4. Use `n_features_in_` instead."
    )
    @property
    def n_features_(self) -> int: ...
    def fit(self: PCA_Self, X: MatrixLike, y: Any = None) -> PCA_Self: ...
    def fit_transform(self, X: MatrixLike, y: Any = None) -> ndarray: ...
    def score_samples(self, X: MatrixLike) -> ndarray: ...
    def score(self, X: MatrixLike, y: Any = None) -> float: ...
