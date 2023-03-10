from typing import Any, Callable, Iterable, Literal, Mapping
from .._typing import ArrayLike, MatrixLike, Int, Float
from ..preprocessing import LabelBinarizer as LabelBinarizer
from scipy.sparse import linalg as sp_linalg
from ..model_selection import BaseCrossValidator
from ..utils.sparsefuncs import mean_variance_axis as mean_variance_axis
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot, row_norms as row_norms
from scipy.sparse.linalg import LinearOperator
from ..model_selection import GridSearchCV as GridSearchCV
from abc import ABCMeta, abstractmethod
from ._base import LinearClassifierMixin, LinearModel
from ..utils import (
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    check_scalar as check_scalar,
    compute_sample_weight as compute_sample_weight,
    column_or_1d as column_or_1d,
)
from ..metrics import (
    check_scoring as check_scoring,
    get_scorer_names as get_scorer_names,
)
from ._sag import sag_solver as sag_solver
from pandas.core.series import Series
from scipy import linalg, sparse, optimize as optimize
from ..utils.validation import check_is_fitted as check_is_fitted
from scipy.sparse._csr import csr_matrix
from numpy import ndarray
from scipy.sparse._coo import coo_matrix
from collections.abc import Iterable
from numpy.random import RandomState
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..base import MultiOutputMixin, RegressorMixin, is_classifier as is_classifier
from functools import partial as partial
from pandas.core.frame import DataFrame
from numbers import Integral as Integral, Real as Real
import warnings

import numpy as np
import numbers


def ridge_regression(
    X: LinearOperator,
    y: MatrixLike | ArrayLike,
    alpha: float | ArrayLike,
    *,
    sample_weight: None | ArrayLike = None,
    solver: Literal[
        "auto", "svd", "cholesky", "lsqr", "sparse_cg", "sag", "saga", "lbfgs", "auto"
    ] = "auto",
    max_iter: None | Int = None,
    tol: Float = 1e-4,
    verbose: Int = 0,
    positive: bool = False,
    random_state: RandomState | None | Int = None,
    return_n_iter: bool = False,
    return_intercept: bool = False,
    check_input: bool = True,
) -> tuple[ndarray, int, float | ndarray]:
    ...


class _BaseRidge(LinearModel, metaclass=ABCMeta):

    _parameter_constraints: dict = ...

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
    ) -> None:
        ...

    def fit(
        self,
        X: csr_matrix | ndarray,
        y: ndarray,
        sample_weight: Series | None | ndarray = None,
    ) -> Ridge | RidgeClassifier:
        ...


class Ridge(MultiOutputMixin, RegressorMixin, _BaseRidge):
    def __init__(
        self,
        alpha: Float | ArrayLike = 1.0,
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
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | coo_matrix,
        y: MatrixLike | ArrayLike,
        sample_weight: float | None | ArrayLike = None,
    ) -> Any:
        ...


class _RidgeClassifierMixin(LinearClassifierMixin):
    def predict(self, X: MatrixLike) -> ndarray:
        ...

    @property
    def classes_(self) -> ndarray:
        ...


class RidgeClassifier(_RidgeClassifierMixin, _BaseRidge):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        alpha: Float = 1.0,
        *,
        fit_intercept: bool = True,
        copy_X: bool = True,
        max_iter: None | Int = None,
        tol: Float = 1e-4,
        class_weight: str | Mapping | None = None,
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
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike,
        y: ArrayLike,
        sample_weight: float | None | ArrayLike = None,
    ) -> Any:
        ...


class _X_CenterStackOp(LinearOperator): 
    def __init__(self, X, X_mean, sqrt_sw) -> None:
        ...


class _XT_CenterStackOp(LinearOperator):
    def __init__(self, X, X_mean, sqrt_sw) -> None:
        ...


class _IdentityRegressor:
    def decision_function(self, y_predict):
        ...

    def predict(self, y_predict):
        ...


class _IdentityClassifier(LinearClassifierMixin):
    def __init__(self, classes) -> None:
        ...

    def decision_function(self, y_predict) -> ndarray:
        ...


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
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike,
        y: MatrixLike | ArrayLike,
        sample_weight: float | None | ArrayLike = None,
    ) -> Any:
        ...


class _BaseRidgeCV(LinearModel):

    _parameter_constraints: dict = ...

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
    ) -> None:
        ...

    def fit(
        self,
        X: DataFrame | ArrayLike,
        y: MatrixLike | ArrayLike,
        sample_weight: float | None | ArrayLike = None,
    ) -> Any:
        ...


class RidgeCV(MultiOutputMixin, RegressorMixin, _BaseRidgeCV):
    def fit(
        self,
        X: DataFrame | ArrayLike,
        y: MatrixLike | ArrayLike,
        sample_weight: float | None | ArrayLike = None,
    ) -> Any:
        ...


class RidgeClassifierCV(_RidgeClassifierMixin, _BaseRidgeCV):

    _parameter_constraints: dict = ...
    for param in ("gcv_mode", "alpha_per_target"):
        pass

    def __init__(
        self,
        alphas: ArrayLike = ...,
        *,
        fit_intercept: bool = True,
        scoring: str | None | Callable = None,
        cv: Iterable | BaseCrossValidator | int | None = None,
        class_weight: str | Mapping | None = None,
        store_cv_values: bool = False,
    ) -> None:
        ...

    def fit(
        self, X: ArrayLike, y: ArrayLike, sample_weight: float | None | ArrayLike = None
    ) -> Any:
        ...
