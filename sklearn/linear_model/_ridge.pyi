from numpy import float64, int64, ndarray
from collections.abc import Generator, Iterable
from typing import List, Optional, Tuple, Union, Literal, Any, Mapping, Callable
from numpy.typing import NDArray, ArrayLike
from numpy.random import RandomState

# Author: Mathieu Blondel <mathieu@mblondel.org>
#         Reuben Fletcher-Costin <reuben.fletchercostin@gmail.com>
#         Fabian Pedregosa <fabian@fseoane.net>
#         Michael Eickenberg <michael.eickenberg@nsup.org>
# License: BSD 3 clause

from abc import ABCMeta, abstractmethod
from functools import partial
import warnings

import numpy as np
import numbers
from scipy import linalg
from scipy import sparse
from scipy import optimize
from scipy.sparse import linalg as sp_linalg
from scipy.sparse.linalg import LinearOperator

from ._base import LinearClassifierMixin, LinearModel
from ._base import _deprecate_normalize, _preprocess_data, _rescale_data
from ._sag import sag_solver
from ..base import MultiOutputMixin, RegressorMixin, is_classifier
from ..utils.extmath import safe_sparse_dot
from ..utils.extmath import row_norms
from ..utils import check_array
from ..utils import check_consistent_length
from ..utils import check_scalar
from ..utils import compute_sample_weight
from ..utils import column_or_1d
from ..utils.validation import check_is_fitted
from ..utils.validation import _check_sample_weight
from ..preprocessing import LabelBinarizer
from ..model_selection import GridSearchCV
from ..metrics import check_scoring
from ..exceptions import ConvergenceWarning
from ..utils.sparsefuncs import mean_variance_axis
from scipy.sparse._coo import coo_matrix
from scipy.sparse._csr import csr_matrix
from scipy.sparse.linalg._interface import _CustomLinearOperator

def _get_rescaled_operator(X: csr_matrix, X_offset: ndarray, sample_weight_sqrt: ndarray) -> _CustomLinearOperator: ...
def _solve_sparse_cg(
    X: csr_matrix,
    y: ndarray,
    alpha: ndarray,
    max_iter: None = None,
    tol: float = 1e-3,
    verbose: int = 0,
    X_offset: Optional[ndarray] = None,
    X_scale: Optional[ndarray] = None,
    sample_weight_sqrt: Optional[ndarray] = None,
) -> ndarray: ...
def _solve_lsqr(
    X,
    y,
    *,
    alpha,
    fit_intercept=True,
    max_iter=None,
    tol=1e-3,
    X_offset=None,
    X_scale=None,
    sample_weight_sqrt=None,
): ...
def _solve_cholesky(X: ndarray, y: ndarray, alpha: ndarray) -> ndarray: ...
def _solve_cholesky_kernel(
    K: ndarray,
    y: ndarray,
    alpha: ndarray,
    sample_weight: None = None,
    copy: bool = False,
) -> ndarray: ...
def _solve_svd(X, y, alpha): ...
def _solve_lbfgs(
    X,
    y,
    alpha,
    positive=True,
    max_iter=None,
    tol=1e-3,
    X_offset=None,
    X_scale=None,
    sample_weight_sqrt=None,
): ...
def _get_valid_accept_sparse(is_X_sparse: bool, solver: str) -> Union[List[str], str]: ...
def ridge_regression(
    X: NDArray,
    y: NDArray,
    alpha: float | ArrayLike,
    *,
    sample_weight: float | ArrayLike | None = None,
    solver: Literal["auto", "svd", "cholesky", "lsqr", "sparse_cg", "sag", "saga", "lbfgs"] = "auto",
    max_iter: int | None = None,
    tol: float = 1e-3,
    verbose: int = 0,
    positive: bool = False,
    random_state: int | RandomState | None = None,
    return_n_iter: bool = False,
    return_intercept: bool = False,
    check_input: bool = True,
) -> tuple[np.ndarray, int, float | np.ndarray]: ...
def _ridge_regression(
    X: Union[ndarray, csr_matrix],
    y: ndarray,
    alpha: Union[float, float64],
    sample_weight: Optional[ndarray] = None,
    solver: str = "auto",
    max_iter: None = None,
    tol: float = 1e-3,
    verbose: int = 0,
    positive: bool = False,
    random_state: Optional[int] = None,
    return_n_iter: bool = False,
    return_intercept: bool = False,
    X_scale: Optional[ndarray] = None,
    X_offset: Optional[ndarray] = None,
    check_input: bool = True,
    fit_intercept: bool = False,
) -> Tuple[ndarray, None]: ...

class _BaseRidge(LinearModel, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        alpha: Union[float, float64] = 1.0,
        *,
        fit_intercept=True,
        normalize="deprecated",
        copy_X=True,
        max_iter=None,
        tol=1e-3,
        solver="auto",
        positive=False,
        random_state=None,
    ) -> None: ...
    def fit(
        self,
        X: Union[ndarray, csr_matrix],
        y: ndarray,
        sample_weight: Optional[ndarray] = None,
    ) -> Union[RidgeClassifier, Ridge]: ...

class Ridge(MultiOutputMixin, RegressorMixin, _BaseRidge):
    def __init__(
        self,
        alpha: NDArray | float = 1.0,
        *,
        fit_intercept: bool = True,
        normalize: bool = ...,
        copy_X: bool = True,
        max_iter: int | None = None,
        tol: float = 1e-3,
        solver: Literal["auto", "svd", "cholesky", "lsqr", "sparse_cg", "sag", "saga", "lbfgs"] = "auto",
        positive: bool = False,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def fit(self, X: NDArray, y: NDArray, sample_weight: float | NDArray | None = None) -> "Ridge": ...

class _RidgeClassifierMixin(LinearClassifierMixin):
    def _prepare_data(
        self, X: csr_matrix, y: ndarray, sample_weight: None, solver: str
    ) -> Tuple[csr_matrix, ndarray, ndarray, ndarray]: ...
    def predict(self, X: ArrayLike) -> NDArray: ...
    @property
    def classes_(self) -> ndarray: ...
    def _more_tags(self): ...

class RidgeClassifier(_RidgeClassifierMixin, _BaseRidge):
    def __init__(
        self,
        alpha: float = 1.0,
        *,
        fit_intercept: bool = True,
        normalize: bool = ...,
        copy_X: bool = True,
        max_iter: int | None = None,
        tol: float = 1e-3,
        class_weight: Mapping | Literal["balanced"] | None = None,
        solver: Literal["auto", "svd", "cholesky", "lsqr", "sparse_cg", "sag", "saga", "lbfgs"] = "auto",
        positive: bool = False,
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def fit(self, X: NDArray, y: NDArray, sample_weight: float | NDArray | None = None) -> "RidgeClassifier": ...

def _check_gcv_mode(X: ndarray, gcv_mode: None) -> str: ...
def _find_smallest_angle(query: ndarray, vectors: ndarray) -> int64: ...

class _X_CenterStackOp(LinearOperator):
    def __init__(self, X, X_mean, sqrt_sw): ...
    def _matvec(self, v): ...
    def _matmat(self, v): ...
    def _transpose(self): ...

class _XT_CenterStackOp(LinearOperator):
    def __init__(self, X, X_mean, sqrt_sw): ...
    def _matvec(self, v): ...
    def _matmat(self, v): ...

class _IdentityRegressor:
    def decision_function(self, y_predict): ...
    def predict(self, y_predict): ...

class _IdentityClassifier(LinearClassifierMixin):
    def __init__(self, classes): ...
    def decision_function(self, y_predict) -> NDArray: ...

class _RidgeGCV(LinearModel):
    def __init__(
        self,
        alphas: ndarray = ...,
        *,
        fit_intercept=True,
        normalize="deprecated",
        scoring=None,
        copy_X=True,
        gcv_mode=None,
        store_cv_values=False,
        is_clf=False,
        alpha_per_target=False,
    ) -> None: ...
    @staticmethod
    def _decomp_diag(v_prime: ndarray, Q: ndarray) -> ndarray: ...
    @staticmethod
    def _diag_dot(D: ndarray, B: ndarray) -> ndarray: ...
    def _compute_gram(self, X: ndarray, sqrt_sw: ndarray) -> Tuple[ndarray, ndarray]: ...
    def _compute_covariance(self, X, sqrt_sw): ...
    def _sparse_multidot_diag(self, X, A, X_mean, sqrt_sw): ...
    def _eigen_decompose_gram(self, X: ndarray, y: ndarray, sqrt_sw: ndarray) -> Tuple[ndarray, ndarray, ndarray, ndarray]: ...
    def _solve_eigen_gram(
        self,
        alpha: float,
        y: ndarray,
        sqrt_sw: ndarray,
        X_mean: ndarray,
        eigvals: ndarray,
        Q: ndarray,
        QT_y: ndarray,
    ) -> Tuple[ndarray, ndarray]: ...
    def _eigen_decompose_covariance(self, X, y, sqrt_sw): ...
    def _solve_eigen_covariance_no_intercept(self, alpha, y, sqrt_sw, X_mean, eigvals, V, X): ...
    def _solve_eigen_covariance_intercept(self, alpha, y, sqrt_sw, X_mean, eigvals, V, X): ...
    def _solve_eigen_covariance(self, alpha, y, sqrt_sw, X_mean, eigvals, V, X): ...
    def _svd_decompose_design_matrix(
        self, X: ndarray, y: ndarray, sqrt_sw: ndarray
    ) -> Tuple[ndarray, ndarray, ndarray, ndarray]: ...
    def _solve_svd_design_matrix(
        self,
        alpha: float,
        y: ndarray,
        sqrt_sw: ndarray,
        X_mean: ndarray,
        singvals_sq: ndarray,
        U: ndarray,
        UT_y: ndarray,
    ) -> Tuple[ndarray, ndarray]: ...
    def fit(self, X: NDArray, y: NDArray, sample_weight: float | NDArray | None = None) -> "_RidgeGCV": ...

class _BaseRidgeCV(LinearModel):
    def __init__(
        self,
        alphas: Union[ndarray, Tuple[float, float, float]] = ...,
        *,
        fit_intercept=True,
        normalize="deprecated",
        scoring=None,
        cv=None,
        gcv_mode=None,
        store_cv_values=False,
        alpha_per_target=False,
    ) -> None: ...
    def fit(self, X: NDArray, y: NDArray, sample_weight: float | NDArray | None = None) -> "RidgeCV": ...

class RidgeCV(MultiOutputMixin, RegressorMixin, _BaseRidgeCV):
    pass

class RidgeClassifierCV(_RidgeClassifierMixin, _BaseRidgeCV):
    def __init__(
        self,
        alphas: NDArray = ...,
        *,
        fit_intercept: bool = True,
        normalize: bool = ...,
        scoring: str | Callable | None = None,
        cv: int | Generator | Iterable | None = None,
        class_weight: Mapping | Literal["balanced"] | None = None,
        store_cv_values: bool = False,
    ): ...
    def fit(self, X: NDArray, y: NDArray, sample_weight: float | NDArray | None = None) -> Any: ...
    def _more_tags(self): ...
