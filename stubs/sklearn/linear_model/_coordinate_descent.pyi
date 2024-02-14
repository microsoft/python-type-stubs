from abc import ABC, abstractmethod
from functools import partial as partial
from numbers import Integral as Integral, Real as Real
from typing import ClassVar, Iterable, Literal, Sequence, TypeVar

from joblib import effective_n_jobs as effective_n_jobs
from numpy import ndarray
from numpy.random import RandomState
from scipy import sparse as sparse
from scipy.sparse import spmatrix
from scipy.sparse._coo import coo_matrix

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import MultiOutputMixin, RegressorMixin
from ..model_selection import BaseCrossValidator, check_cv as check_cv
from ..model_selection._split import BaseShuffleSplit
from ..utils import check_array as check_array, check_scalar as check_scalar
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from ..utils.parallel import Parallel as Parallel, delayed as delayed
from ..utils.validation import (
    check_consistent_length as check_consistent_length,
    check_is_fitted as check_is_fitted,
    check_random_state as check_random_state,
    column_or_1d as column_or_1d,
)
from ._base import LinearModel

LinearModelCV_Self = TypeVar("LinearModelCV_Self", bound="LinearModelCV")
MultiTaskElasticNetCV_Self = TypeVar("MultiTaskElasticNetCV_Self", bound="MultiTaskElasticNetCV")
MultiTaskLassoCV_Self = TypeVar("MultiTaskLassoCV_Self", bound="MultiTaskLassoCV")
ElasticNet_Self = TypeVar("ElasticNet_Self", bound="ElasticNet")
MultiTaskElasticNet_Self = TypeVar("MultiTaskElasticNet_Self", bound="MultiTaskElasticNet")

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Fabian Pedregosa <fabian.pedregosa@inria.fr>
#         Olivier Grisel <olivier.grisel@ensta.org>
#         Gael Varoquaux <gael.varoquaux@inria.fr>
#
# License: BSD 3 clause

import numbers
import sys
import warnings

import numpy as np

def lasso_path(
    X: MatrixLike | ArrayLike,
    y: MatrixLike | ArrayLike,
    *,
    eps: Float = 1e-3,
    n_alphas: Int = 100,
    alphas: None | ArrayLike = None,
    precompute: Literal["auto", "auto"] | MatrixLike | bool = "auto",
    Xy: None | MatrixLike | ArrayLike = None,
    copy_X: bool = True,
    coef_init: None | ArrayLike = None,
    verbose: int | bool = False,
    return_n_iter: bool = False,
    positive: bool = False,
    **params,
) -> tuple[ndarray, ndarray, ndarray] | tuple[ndarray, ndarray, ndarray, list[int]]: ...
def enet_path(
    X: MatrixLike | ArrayLike,
    y: MatrixLike | ArrayLike,
    *,
    l1_ratio: Float = 0.5,
    eps: Float = 1e-3,
    n_alphas: Int = 100,
    alphas: None | ArrayLike = None,
    precompute: Literal["auto", "auto"] | MatrixLike | bool = "auto",
    Xy: None | MatrixLike | ArrayLike = None,
    copy_X: bool = True,
    coef_init: None | ArrayLike = None,
    verbose: int | bool = False,
    return_n_iter: bool = False,
    positive: bool = False,
    check_input: bool = True,
    **params,
) -> tuple[ndarray, ndarray, ndarray, list[int]]: ...

###############################################################################
# ElasticNet model

class ElasticNet(MultiOutputMixin, RegressorMixin, LinearModel):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    dual_gap_: float | ndarray = ...
    n_iter_: list[int] = ...
    intercept_: float | ndarray = ...
    coef_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    path = ...

    def __init__(
        self,
        alpha: Float = 1.0,
        *,
        l1_ratio: Float = 0.5,
        fit_intercept: bool = True,
        precompute: MatrixLike | bool = False,
        max_iter: Int = 1000,
        copy_X: bool = True,
        tol: Float = 1e-4,
        warm_start: bool = False,
        positive: bool = False,
        random_state: RandomState | None | Int = None,
        selection: Literal["cyclic", "random", "cyclic"] = "cyclic",
    ) -> None: ...
    def fit(
        self: ElasticNet_Self,
        X: coo_matrix | MatrixLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
        check_input: bool = True,
    ) -> ElasticNet_Self: ...
    @property
    def sparse_coef_(self) -> spmatrix: ...

###############################################################################
# Lasso model

class Lasso(ElasticNet):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_iter_: int | list[int] = ...
    intercept_: float | ndarray = ...
    sparse_coef_: spmatrix = ...
    dual_gap_: float | ndarray = ...
    coef_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    path = ...

    def __init__(
        self,
        alpha: Float = 1.0,
        *,
        fit_intercept: bool = True,
        precompute: MatrixLike | bool = False,
        copy_X: bool = True,
        max_iter: Int = 1000,
        tol: Float = 1e-4,
        warm_start: bool = False,
        positive: bool = False,
        random_state: RandomState | None | Int = None,
        selection: Literal["cyclic", "random", "cyclic"] = "cyclic",
    ) -> None: ...

class LinearModelCV(MultiOutputMixin, LinearModel, ABC):
    _parameter_constraints: ClassVar[dict] = ...

    @abstractmethod
    def __init__(
        self,
        eps: float = 1e-3,
        n_alphas: int = 100,
        alphas: None | ndarray = None,
        fit_intercept: bool = True,
        precompute: str = "auto",
        max_iter: int = 1000,
        tol: float = 1e-4,
        copy_X: bool = True,
        cv: None | int = None,
        verbose: bool = False,
        n_jobs=None,
        positive: bool = False,
        random_state: None | int = None,
        selection: str = "cyclic",
    ) -> None: ...
    @staticmethod
    @abstractmethod
    def path(X, y, **kwargs): ...
    def fit(
        self: LinearModelCV_Self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> LinearModelCV_Self | LassoCV: ...

class LassoCV(RegressorMixin, LinearModelCV):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_iter_: int = ...
    dual_gap_: float | ndarray = ...
    alphas_: ndarray = ...
    mse_path_: ndarray = ...
    intercept_: float | ndarray = ...
    coef_: ndarray = ...
    alpha_: float = ...

    path = ...

    def __init__(
        self,
        *,
        eps: Float = 1e-3,
        n_alphas: Int = 100,
        alphas: None | ArrayLike = None,
        fit_intercept: bool = True,
        precompute: Literal["auto", "auto"] | MatrixLike | bool = "auto",
        max_iter: Int = 1000,
        tol: Float = 1e-4,
        copy_X: bool = True,
        cv: int | BaseCrossValidator | Iterable | None | BaseShuffleSplit = None,
        verbose: int | bool = False,
        n_jobs: None | Int = None,
        positive: bool = False,
        random_state: RandomState | None | Int = None,
        selection: Literal["cyclic", "random", "cyclic"] = "cyclic",
    ) -> None: ...

class ElasticNetCV(RegressorMixin, LinearModelCV):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_iter_: int = ...
    dual_gap_: float = ...
    alphas_: ndarray = ...
    mse_path_: ndarray = ...
    intercept_: float | ndarray = ...
    coef_: ndarray = ...
    l1_ratio_: float = ...
    alpha_: float = ...

    _parameter_constraints: ClassVar[dict] = ...

    path = ...

    def __init__(
        self,
        *,
        l1_ratio: float | Sequence[float] = 0.5,
        eps: Float = 1e-3,
        n_alphas: Int = 100,
        alphas: None | ArrayLike = None,
        fit_intercept: bool = True,
        precompute: Literal["auto", "auto"] | MatrixLike | bool = "auto",
        max_iter: Int = 1000,
        tol: Float = 1e-4,
        cv: int | BaseCrossValidator | Iterable | None | BaseShuffleSplit = None,
        copy_X: bool = True,
        verbose: int | bool = 0,
        n_jobs: None | Int = None,
        positive: bool = False,
        random_state: RandomState | None | Int = None,
        selection: Literal["cyclic", "random", "cyclic"] = "cyclic",
    ) -> None: ...

###############################################################################
# Multi Task ElasticNet and Lasso models (with joint feature selection)

class MultiTaskElasticNet(Lasso):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    sparse_coef_: spmatrix = ...
    eps_: float = ...
    dual_gap_: float = ...
    n_iter_: int = ...
    coef_: ndarray = ...
    intercept_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...
    for param in ("precompute", "positive"):
        pass

    def __init__(
        self,
        alpha: Float = 1.0,
        *,
        l1_ratio: Float = 0.5,
        fit_intercept: bool = True,
        copy_X: bool = True,
        max_iter: Int = 1000,
        tol: Float = 1e-4,
        warm_start: bool = False,
        random_state: RandomState | None | Int = None,
        selection: Literal["cyclic", "random", "cyclic"] = "cyclic",
    ) -> None: ...
    def fit(self: MultiTaskElasticNet_Self, X: ArrayLike, y: MatrixLike) -> MultiTaskElasticNet_Self | MultiTaskLasso: ...

class MultiTaskLasso(MultiTaskElasticNet):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    sparse_coef_: spmatrix = ...
    eps_: float = ...
    dual_gap_: ndarray = ...
    n_iter_: int = ...
    intercept_: ndarray = ...
    coef_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        alpha: Float = 1.0,
        *,
        fit_intercept: bool = True,
        copy_X: bool = True,
        max_iter: Int = 1000,
        tol: Float = 1e-4,
        warm_start: bool = False,
        random_state: RandomState | None | Int = None,
        selection: Literal["cyclic", "random", "cyclic"] = "cyclic",
    ) -> None: ...

class MultiTaskElasticNetCV(RegressorMixin, LinearModelCV):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    dual_gap_: float = ...
    n_iter_: int = ...
    l1_ratio_: float = ...
    alphas_: ndarray = ...
    mse_path_: ndarray = ...
    alpha_: float = ...
    coef_: ndarray = ...
    intercept_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    path = ...

    def __init__(
        self,
        *,
        l1_ratio: float | Sequence[float] = 0.5,
        eps: Float = 1e-3,
        n_alphas: Int = 100,
        alphas: None | ArrayLike = None,
        fit_intercept: bool = True,
        max_iter: Int = 1000,
        tol: Float = 1e-4,
        cv: int | BaseCrossValidator | Iterable | None | BaseShuffleSplit = None,
        copy_X: bool = True,
        verbose: int | bool = 0,
        n_jobs: None | Int = None,
        random_state: RandomState | None | Int = None,
        selection: Literal["cyclic", "random", "cyclic"] = "cyclic",
    ) -> None: ...

    # This is necessary as LinearModelCV now supports sample_weight while
    # MultiTaskElasticNet does not (yet).
    def fit(self: MultiTaskElasticNetCV_Self, X: ArrayLike, y: MatrixLike) -> MultiTaskElasticNetCV_Self: ...

class MultiTaskLassoCV(RegressorMixin, LinearModelCV):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    dual_gap_: float = ...
    n_iter_: int = ...
    alphas_: ndarray = ...
    mse_path_: ndarray = ...
    alpha_: float = ...
    coef_: ndarray = ...
    intercept_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    path = ...

    def __init__(
        self,
        *,
        eps: Float = 1e-3,
        n_alphas: Int = 100,
        alphas: None | ArrayLike = None,
        fit_intercept: bool = True,
        max_iter: Int = 1000,
        tol: Float = 1e-4,
        copy_X: bool = True,
        cv: int | BaseCrossValidator | Iterable | None | BaseShuffleSplit = None,
        verbose: int | bool = False,
        n_jobs: None | Int = None,
        random_state: RandomState | None | Int = None,
        selection: Literal["cyclic", "random", "cyclic"] = "cyclic",
    ) -> None: ...

    # This is necessary as LinearModelCV now supports sample_weight while
    # MultiTaskElasticNet does not (yet).
    def fit(self: MultiTaskLassoCV_Self, X: ArrayLike, y: MatrixLike) -> MultiTaskLassoCV_Self: ...
