from typing import Optional, Literal, Mapping, Any
from numpy.typing import ArrayLike, NDArray

# Author: Mathieu Blondel <mathieu@mblondel.org>
#         Sylvain Marie <sylvain.marie@schneider-electric.com>
# License: BSD 3 clause

import numpy as np
from numpy.random import RandomState
import numbers
from scipy import linalg
from scipy.sparse.linalg import eigsh

from ..utils._arpack import _init_arpack_v0
from ..utils.extmath import svd_flip, _randomized_eigsh
from ..utils.validation import (
    check_is_fitted,
    _check_psd_eigenvalues,
    check_scalar,
)
from ..utils.deprecation import deprecated
from ..exceptions import NotFittedError
from ..base import BaseEstimator, TransformerMixin, _ClassNamePrefixFeaturesOutMixin
from ..preprocessing import KernelCenterer
from ..metrics.pairwise import pairwise_kernels
from numpy import ndarray

class KernelPCA(_ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        n_components: int | None = None,
        *,
        kernel: Literal["linear", "poly", "rbf", "sigmoid", "cosine", "precomputed"] = "linear",
        gamma: float | None = None,
        degree: int = 3,
        coef0: float = 1,
        kernel_params: Mapping | None = None,
        alpha: float = 1.0,
        fit_inverse_transform: bool = False,
        eigen_solver: Literal["auto", "dense", "arpack", "randomized"] = "auto",
        tol: float = 0,
        max_iter: int | None = None,
        iterated_power: int | Literal["auto"] = "auto",
        remove_zero_eig: bool = False,
        random_state: int | RandomState | None = None,
        copy_X: bool = True,
        n_jobs: int | None = None,
    ) -> None: ...

    # TODO: Remove in 1.2
    # mypy error: Decorated property not supported
    @deprecated(  # type: ignore
        "Attribute `lambdas_` was deprecated in version 1.0 and will be " "removed in 1.2. Use `eigenvalues_` instead."
    )
    @property
    def lambdas_(self): ...

    # mypy error: Decorated property not supported
    @deprecated(  # type: ignore
        "Attribute `alphas_` was deprecated in version 1.0 and will be " "removed in 1.2. Use `eigenvectors_` instead."
    )
    @property
    def alphas_(self): ...
    def _get_kernel(self, X: ndarray, Y: Optional[ndarray] = None) -> ndarray: ...
    def _fit_transform(self, K: ndarray) -> ndarray: ...
    def _fit_inverse_transform(self, X_transformed: ndarray, X: ndarray) -> None: ...
    def fit(self, X: NDArray | ArrayLike, y: None = None) -> "KernelPCA": ...
    def fit_transform(self, X: NDArray | ArrayLike, y: None = None, **params) -> NDArray: ...
    def transform(self, X: NDArray | ArrayLike) -> NDArray: ...
    def inverse_transform(self, X: NDArray | ArrayLike) -> NDArray: ...
    def _more_tags(self): ...
    @property
    def _n_features_out(self): ...
