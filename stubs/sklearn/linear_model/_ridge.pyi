from abc import ABCMeta, abstractmethod
from functools import partial as partial
from numbers import Integral as Integral, Real as Real
from typing import Callable, ClassVar, Iterable, Literal, Mapping, TypeVar

from numpy import ndarray
from numpy.random import RandomState
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from scipy import linalg, optimize as optimize, sparse
from scipy.sparse import linalg as sp_linalg
from scipy.sparse._coo import coo_matrix
from scipy.sparse._csr import csr_matrix
from scipy.sparse.linalg import LinearOperator

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import MultiOutputMixin, RegressorMixin, is_classifier as is_classifier
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..metrics import check_scoring as check_scoring, get_scorer_names as get_scorer_names
from ..model_selection import BaseCrossValidator, GridSearchCV as GridSearchCV
from ..model_selection._split import BaseShuffleSplit
from ..preprocessing import LabelBinarizer as LabelBinarizer
from ..utils import (
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    check_scalar as check_scalar,
    column_or_1d as column_or_1d,
    compute_sample_weight as compute_sample_weight,
)
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import row_norms as row_norms, safe_sparse_dot as safe_sparse_dot
from ..utils.sparsefuncs import mean_variance_axis as mean_variance_axis
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import LinearClassifierMixin, LinearModel
from ._sag import sag_solver as sag_solver

_BaseRidgeCV_Self = TypeVar("_BaseRidgeCV_Self", bound="_BaseRidgeCV")
_RidgeGCV_Self = TypeVar("_RidgeGCV_Self", bound="_RidgeGCV")
RidgeClassifier_Self = TypeVar("RidgeClassifier_Self", bound="RidgeClassifier")
RidgeClassifierCV_Self = TypeVar("RidgeClassifierCV_Self", bound="RidgeClassifierCV")
RidgeCV_Self = TypeVar("RidgeCV_Self", bound="RidgeCV")
Ridge_Self = TypeVar("Ridge_Self", bound="Ridge")

import numbers
import warnings

import numpy as np

def ridge_regression(
    X: MatrixLike | LinearOperator,
    y: MatrixLike | ArrayLike,
    alpha: float | ArrayLike,
    *,
    sample_weight: None | ArrayLike = None,
    solver: Literal["auto", "svd", "cholesky", "lsqr", "sparse_cg", "sag", "saga", "lbfgs", "auto"] = "auto",
    max_iter: None | Int = None,
    tol: Float = 1e-4,
    verbose: Int = 0,
    positive: bool = False,
    random_state: RandomState | None | Int = None,
    return_n_iter: bool = False,
    return_intercept: bool = False,
    check_input: bool = True,
) -> tuple[ndarray, int, float | ndarray]: ...

class _BaseRidge(LinearModel, metaclass=ABCMeta):
    _parameter_constraints: ClassVar[dict] = ...

    @abstractmethod
    def __init__(
        self,
        alpha: Float = 1.0,
        *,
        fit_intercept: bool = True,
        copy_X: bool = True,
        max_iter=None,
        tol: float = 1e-4,
        solver: str = "auto",
        positive: bool = False,
        random_state=None,
    ) -> None: ...
    def fit(
        self,
        X: csr_matrix | ndarray,
        y: ndarray,
        sample_weight: Series | None | ndarray = None,
    ): ...

class Ridge(MultiOutputMixin, RegressorMixin, _BaseRidge):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_iter_: None | ndarray = ...
    intercept_: float | ndarray = ...
    coef_: ndarray = ...

    def __init__(
        self,
        alpha: ArrayLike | Float = 1.0,
        *,
        fit_intercept: bool = True,
        copy_X: bool = True,
        max_iter: None | Int = None,
        tol: Float = 1e-4,
        solver: Literal[
            "auto",
            "svd",
            "cholesky",
            "lsqr",
            "sparse_cg",
            "sag",
            "saga",
            "lbfgs",
            "auto",
        ] = "auto",
        positive: bool = False,
        random_state: RandomState | None | Int = None,
    ) -> None: ...
    def fit(
        self: Ridge_Self,
        X: coo_matrix | MatrixLike,
        y: MatrixLike | ArrayLike,
        sample_weight: float | None | ArrayLike = None,
    ) -> Ridge_Self: ...

class _RidgeClassifierMixin(LinearClassifierMixin):
    def predict(self, X: MatrixLike) -> ndarray: ...
    def classes_(self) -> ndarray: ...

class RidgeClassifier(_RidgeClassifierMixin, _BaseRidge):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    classes_: ndarray = ...
    n_iter_: None | ndarray = ...
    intercept_: float | ndarray = ...
    coef_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        alpha: Float = 1.0,
        *,
        fit_intercept: bool = True,
        copy_X: bool = True,
        max_iter: None | Int = None,
        tol: Float = 1e-4,
        class_weight: None | Mapping | str = None,
        solver: Literal[
            "auto",
            "svd",
            "cholesky",
            "lsqr",
            "sparse_cg",
            "sag",
            "saga",
            "lbfgs",
            "auto",
        ] = "auto",
        positive: bool = False,
        random_state: RandomState | None | Int = None,
    ) -> None: ...
    def fit(
        self: RidgeClassifier_Self,
        X: MatrixLike,
        y: ArrayLike,
        sample_weight: float | None | ArrayLike = None,
    ) -> RidgeClassifier_Self: ...

class _X_CenterStackOp(LinearOperator):
    def __init__(self, X, X_mean, sqrt_sw) -> None: ...

class _XT_CenterStackOp(LinearOperator):
    def __init__(self, X, X_mean, sqrt_sw) -> None: ...

class _IdentityRegressor:
    def decision_function(self, y_predict): ...
    def predict(self, y_predict): ...

class _IdentityClassifier(LinearClassifierMixin):
    def __init__(self, classes) -> None: ...
    def decision_function(self, y_predict) -> ndarray: ...

class _RidgeGCV(LinearModel):
    def __init__(
        self,
        alphas: ndarray = ...,
        *,
        fit_intercept: bool = True,
        scoring=None,
        copy_X: bool = True,
        gcv_mode=None,
        store_cv_values: bool = False,
        is_clf: bool = False,
        alpha_per_target: bool = False,
    ) -> None: ...
    def fit(
        self: _RidgeGCV_Self,
        X: MatrixLike,
        y: MatrixLike | ArrayLike,
        sample_weight: float | None | ArrayLike = None,
    ) -> _RidgeGCV_Self: ...

class _BaseRidgeCV(LinearModel):
    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        alphas: tuple[float, float, float] | ndarray = ...,
        *,
        fit_intercept: bool = True,
        scoring=None,
        cv=None,
        gcv_mode=None,
        store_cv_values: bool = False,
        alpha_per_target: bool = False,
    ) -> None: ...
    def fit(
        self: _BaseRidgeCV_Self,
        X: ArrayLike | DataFrame,
        y: MatrixLike | ArrayLike,
        sample_weight: float | None | ArrayLike = None,
    ) -> _BaseRidgeCV_Self | RidgeCV: ...

class RidgeCV(MultiOutputMixin, RegressorMixin, _BaseRidgeCV):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    best_score_: float | ndarray = ...
    alpha_: float | ndarray = ...
    intercept_: float | ndarray = ...
    coef_: ndarray = ...
    cv_values_: ndarray = ...

    def fit(
        self: RidgeCV_Self,
        X: ArrayLike | DataFrame,
        y: MatrixLike | ArrayLike,
        sample_weight: float | None | ArrayLike = None,
    ) -> RidgeCV_Self: ...

class RidgeClassifierCV(_RidgeClassifierMixin, _BaseRidgeCV):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    classes_: ndarray = ...
    best_score_: float = ...
    alpha_: float = ...
    intercept_: float | ndarray = ...
    coef_: ndarray = ...
    cv_values_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...
    for param in ("gcv_mode", "alpha_per_target"):
        pass

    def __init__(
        self,
        alphas: ArrayLike = ...,
        *,
        fit_intercept: bool = True,
        scoring: None | str | Callable = None,
        cv: int | BaseCrossValidator | Iterable | None | BaseShuffleSplit = None,
        class_weight: None | Mapping | str = None,
        store_cv_values: bool = False,
    ) -> None: ...
    def fit(
        self: RidgeClassifierCV_Self,
        X: ArrayLike,
        y: ArrayLike,
        sample_weight: float | None | ArrayLike = None,
    ) -> RidgeClassifierCV_Self: ...
