from numbers import Integral as Integral, Real as Real
from typing import Any, Callable, ClassVar, Literal, TypeVar

from numpy import ndarray
from numpy.random import RandomState
from scipy import linalg as linalg
from scipy.sparse.linalg import eigsh as eigsh

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin
from ..exceptions import NotFittedError as NotFittedError
from ..metrics.pairwise import pairwise_kernels as pairwise_kernels
from ..preprocessing import KernelCenterer as KernelCenterer
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import svd_flip as svd_flip
from ..utils.validation import check_is_fitted as check_is_fitted

KernelPCA_Self = TypeVar("KernelPCA_Self", bound=KernelPCA)

# Author: Mathieu Blondel <mathieu@mblondel.org>
#         Sylvain Marie <sylvain.marie@schneider-electric.com>
# License: BSD 3 clause

import numpy as np

class KernelPCA(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    X_fit_: ndarray = ...
    X_transformed_fit_: ndarray = ...
    dual_coef_: ndarray = ...
    eigenvectors_: ndarray = ...
    eigenvalues_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        n_components: None | Int = None,
        *,
        kernel: Callable | Literal["linear", "poly", "rbf", "sigmoid", "cosine", "precomputed"] = "linear",
        gamma: None | Float = None,
        degree: Int = 3,
        coef0: Float = 1,
        kernel_params: None | dict = None,
        alpha: Float = 1.0,
        fit_inverse_transform: bool = False,
        eigen_solver: Literal["auto", "dense", "arpack", "randomized"] = "auto",
        tol: Float = 0,
        max_iter: None | Int = None,
        iterated_power: Literal["auto"] | int = "auto",
        remove_zero_eig: bool = False,
        random_state: RandomState | None | Int = None,
        copy_X: bool = True,
        n_jobs: None | Int = None,
    ) -> None: ...
    def fit(self: KernelPCA_Self, X: MatrixLike | ArrayLike, y: Any = None) -> KernelPCA_Self: ...
    def fit_transform(self, X: MatrixLike | ArrayLike, y: Any = None, **params) -> ndarray: ...
    def transform(self, X: MatrixLike | ArrayLike) -> ndarray: ...
    def inverse_transform(self, X: MatrixLike) -> ndarray: ...
