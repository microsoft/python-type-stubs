from typing import Any, Iterable, Literal, Sequence
from .._typing import ArrayLike, MatrixLike, Float, Int
from ..model_selection import BaseCrossValidator
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from ..model_selection import check_cv as check_cv
from joblib import effective_n_jobs as effective_n_jobs
from abc import ABC, abstractmethod
from ._base import LinearModel
from ..utils import check_array as check_array, check_scalar as check_scalar
from scipy import sparse as sparse
from ..utils.validation import (
    check_random_state as check_random_state,
    check_consistent_length as check_consistent_length,
    check_is_fitted as check_is_fitted,
    column_or_1d as column_or_1d,
)
from numpy import ndarray
from scipy.sparse._coo import coo_matrix
from collections.abc import Iterable
from numpy.random import RandomState
from ..base import RegressorMixin, MultiOutputMixin
from functools import partial as partial
from numbers import Integral as Integral, Real as Real
from ..utils.parallel import delayed as delayed, Parallel as Parallel

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Fabian Pedregosa <fabian.pedregosa@inria.fr>
#         Olivier Grisel <olivier.grisel@ensta.org>
#         Gael Varoquaux <gael.varoquaux@inria.fr>
#
# License: BSD 3 clause

import sys
import warnings
import numbers

import numpy as np


def lasso_path(
    X: MatrixLike | ArrayLike,
    y: MatrixLike | ArrayLike,
    *,
    eps: Float = 1e-3,
    n_alphas: Int = 100,
    alphas: None | ArrayLike = None,
    precompute: Literal["auto", "auto"] | bool | MatrixLike = "auto",
    Xy: None | MatrixLike | ArrayLike = None,
    copy_X: bool = True,
    coef_init: None | ArrayLike = None,
    verbose: bool | int = False,
    return_n_iter: bool = False,
    positive: bool = False,
    **params,
) -> tuple[ndarray, ndarray, ndarray, list[int]] | tuple[ndarray, ndarray, ndarray]:
    ...


def enet_path(
    X: MatrixLike | ArrayLike,
    y: MatrixLike | ArrayLike,
    *,
    l1_ratio: Float = 0.5,
    eps: Float = 1e-3,
    n_alphas: Int = 100,
    alphas: None | ArrayLike = None,
    precompute: Literal["auto", "auto"] | bool | MatrixLike = "auto",
    Xy: None | MatrixLike | ArrayLike = None,
    copy_X: bool = True,
    coef_init: None | ArrayLike = None,
    verbose: bool | int = False,
    return_n_iter: bool = False,
    positive: bool = False,
    check_input: bool = True,
    **params,
) -> tuple[ndarray, ndarray, ndarray, list[int]]:
    ...


###############################################################################
# ElasticNet model


class ElasticNet(MultiOutputMixin, RegressorMixin, LinearModel):

    _parameter_constraints: dict = ...

    path = ...

    def __init__(
        self,
        alpha: Float = 1.0,
        *,
        l1_ratio: Float = 0.5,
        fit_intercept: bool = True,
        precompute: bool | MatrixLike = False,
        max_iter: Int = 1000,
        copy_X: bool = True,
        tol: Float = 1e-4,
        warm_start: bool = False,
        positive: bool = False,
        random_state: RandomState | None | Int = None,
        selection: Literal["cyclic", "random", "cyclic"] = "cyclic",
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | coo_matrix,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
        check_input: bool = True,
    ) -> Any:
        ...

    @property
    def sparse_coef_(self):
        ...


###############################################################################
# Lasso model


class Lasso(ElasticNet):

    _parameter_constraints: dict = ...

    path = ...

    def __init__(
        self,
        alpha: Float = 1.0,
        *,
        fit_intercept: bool = True,
        precompute: bool | MatrixLike = False,
        copy_X: bool = True,
        max_iter: Int = 1000,
        tol: Float = 1e-4,
        warm_start: bool = False,
        positive: bool = False,
        random_state: RandomState | None | Int = None,
        selection: Literal["cyclic", "random", "cyclic"] = "cyclic",
    ) -> None:
        ...


class LinearModelCV(MultiOutputMixin, LinearModel, ABC):

    _parameter_constraints: dict = ...

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
        cv: int | None = None,
        verbose: bool = False,
        n_jobs=None,
        positive: bool = False,
        random_state: int | None = None,
        selection: str = "cyclic",
    ) -> None:
        ...

    @staticmethod
    @abstractmethod
    def path(X, y, **kwargs):
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...


class LassoCV(RegressorMixin, LinearModelCV):

    path = ...

    def __init__(
        self,
        *,
        eps: Float = 1e-3,
        n_alphas: Int = 100,
        alphas: None | ArrayLike = None,
        fit_intercept: bool = True,
        precompute: Literal["auto", "auto"] | bool | MatrixLike = "auto",
        max_iter: Int = 1000,
        tol: Float = 1e-4,
        copy_X: bool = True,
        cv: Iterable | BaseCrossValidator | int | None = None,
        verbose: bool | int = False,
        n_jobs: None | Int = None,
        positive: bool = False,
        random_state: RandomState | None | Int = None,
        selection: Literal["cyclic", "random", "cyclic"] = "cyclic",
    ) -> None:
        ...


class ElasticNetCV(RegressorMixin, LinearModelCV):

    _parameter_constraints: dict = ...

    path = ...

    def __init__(
        self,
        *,
        l1_ratio: Sequence[float] | float = 0.5,
        eps: Float = 1e-3,
        n_alphas: Int = 100,
        alphas: None | ArrayLike = None,
        fit_intercept: bool = True,
        precompute: Literal["auto", "auto"] | bool | MatrixLike = "auto",
        max_iter: Int = 1000,
        tol: Float = 1e-4,
        cv: Iterable | BaseCrossValidator | int | None = None,
        copy_X: bool = True,
        verbose: bool | int = 0,
        n_jobs: None | Int = None,
        positive: bool = False,
        random_state: RandomState | None | Int = None,
        selection: Literal["cyclic", "random", "cyclic"] = "cyclic",
    ) -> None:
        ...


###############################################################################
# Multi Task ElasticNet and Lasso models (with joint feature selection)


class MultiTaskElasticNet(Lasso):

    _parameter_constraints: dict = ...
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
    ) -> None:
        ...

    def fit(self, X: ArrayLike, y: MatrixLike) -> Any:
        ...


class MultiTaskLasso(MultiTaskElasticNet):

    _parameter_constraints: dict = ...

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
    ) -> None:
        ...


class MultiTaskElasticNetCV(RegressorMixin, LinearModelCV):

    _parameter_constraints: dict = ...

    path = ...

    def __init__(
        self,
        *,
        l1_ratio: Sequence[float] | float = 0.5,
        eps: Float = 1e-3,
        n_alphas: Int = 100,
        alphas: None | ArrayLike = None,
        fit_intercept: bool = True,
        max_iter: Int = 1000,
        tol: Float = 1e-4,
        cv: Iterable | BaseCrossValidator | int | None = None,
        copy_X: bool = True,
        verbose: bool | int = 0,
        n_jobs: None | Int = None,
        random_state: RandomState | None | Int = None,
        selection: Literal["cyclic", "random", "cyclic"] = "cyclic",
    ) -> None:
        ...

    # This is necessary as LinearModelCV now supports sample_weight while
    # MultiTaskElasticNet does not (yet).
    def fit(self, X: ArrayLike, y: MatrixLike) -> Any:
        ...


class MultiTaskLassoCV(RegressorMixin, LinearModelCV):

    _parameter_constraints: dict = ...

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
        cv: Iterable | BaseCrossValidator | int | None = None,
        verbose: bool | int = False,
        n_jobs: None | Int = None,
        random_state: RandomState | None | Int = None,
        selection: Literal["cyclic", "random", "cyclic"] = "cyclic",
    ) -> None:
        ...

    # This is necessary as LinearModelCV now supports sample_weight while
    # MultiTaskElasticNet does not (yet).
    def fit(self, X: ArrayLike, y: MatrixLike) -> Any:
        ...
