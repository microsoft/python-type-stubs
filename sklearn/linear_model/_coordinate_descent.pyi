from numpy import float64, ndarray
from collections.abc import Generator, Iterable
from typing import Callable, Dict, List, Optional, Tuple, Type, Union, Literal, Any
from numpy.typing import ArrayLike, NDArray

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Fabian Pedregosa <fabian.pedregosa@inria.fr>
#         Olivier Grisel <olivier.grisel@ensta.org>
#         Gael Varoquaux <gael.varoquaux@inria.fr>
#
# License: BSD 3 clause

import sys
import warnings
import numbers
from abc import ABC, abstractmethod
from functools import partial

import numpy as np
from numpy.random import RandomState
from scipy import sparse

from ._base import LinearModel, _pre_fit
from ..base import RegressorMixin, MultiOutputMixin
from ._base import _preprocess_data, _deprecate_normalize
from ..utils import check_array
from ..utils import check_scalar
from ..utils.validation import check_random_state
from ..model_selection import check_cv
from ..utils.extmath import safe_sparse_dot
from ..utils.validation import (
    _check_sample_weight,
    check_consistent_length,
    check_is_fitted,
    column_or_1d,
)
from ..utils.fixes import delayed

# mypy error: Module 'sklearn.linear_model' has no attribute '_cd_fast'
from . import _cd_fast as cd_fast  # type: ignore
from pandas.core.series import Series
from scipy.sparse._coo import coo_matrix
from scipy.sparse._csc import csc_matrix

def _set_order(
    X: Union[ndarray, csc_matrix], y: ndarray, order: str = "C"
) -> Union[Tuple[ndarray, ndarray], Tuple[csc_matrix, ndarray]]: ...

###############################################################################
# Paths functions

def _alpha_grid(
    X: ndarray,
    y: ndarray,
    Xy: Optional[ndarray] = None,
    l1_ratio: Union[int, float] = 1.0,
    fit_intercept: bool = True,
    eps: float = 1e-3,
    n_alphas: int = 100,
    normalize: bool = False,
    copy_X: bool = True,
) -> ndarray: ...
def lasso_path(
    X: NDArray | ArrayLike,
    y: NDArray | ArrayLike,
    *,
    eps: float = 1e-3,
    n_alphas: int = 100,
    alphas: NDArray | None = None,
    precompute: bool | ArrayLike | Literal["auto"] = "auto",
    Xy: ArrayLike | None = None,
    copy_X: bool = True,
    coef_init: NDArray | None = None,
    verbose: bool | int = False,
    return_n_iter: bool = False,
    positive: bool = False,
    **params,
) -> tuple[NDArray, np.ndarray, NDArray, list[int]]: ...
def enet_path(
    X: NDArray | ArrayLike,
    y: NDArray | ArrayLike,
    *,
    l1_ratio: float = 0.5,
    eps: float = 1e-3,
    n_alphas: int = 100,
    alphas: NDArray | None = None,
    precompute: bool | ArrayLike | Literal["auto"] = "auto",
    Xy: ArrayLike | None = None,
    copy_X: bool = True,
    coef_init: NDArray | None = None,
    verbose: bool | int = False,
    return_n_iter: bool = False,
    positive: bool = False,
    check_input: bool = True,
    **params,
) -> tuple[NDArray, np.ndarray, NDArray, list[int]]: ...

###############################################################################
# ElasticNet model

class ElasticNet(MultiOutputMixin, RegressorMixin, LinearModel):

    path = ...

    def __init__(
        self,
        alpha: float = 1.0,
        *,
        l1_ratio: float = 0.5,
        fit_intercept: bool = True,
        normalize: bool = ...,
        precompute: bool | ArrayLike = False,
        max_iter: int = 1000,
        copy_X: bool = True,
        tol: float = 1e-4,
        warm_start: bool = False,
        positive: bool = False,
        random_state: int | RandomState | None = None,
        selection: Literal["cyclic", "random"] = "cyclic",
    ) -> None: ...
    def fit(
        self,
        X: NDArray,
        y: NDArray,
        sample_weight: float | ArrayLike | None = None,
        check_input: bool = True,
    ) -> Union[Lasso, ElasticNet]: ...
    @property
    def sparse_coef_(self): ...
    def _decision_function(self, X: ndarray) -> ndarray: ...

###############################################################################
# Lasso model

class Lasso(ElasticNet):

    path = ...

    def __init__(
        self,
        alpha: float = 1.0,
        *,
        fit_intercept: bool = True,
        normalize: bool = ...,
        precompute: bool | ArrayLike = False,
        copy_X: bool = True,
        max_iter: int = 1000,
        tol: float = 1e-4,
        warm_start: bool = False,
        positive: bool = False,
        random_state: int | RandomState | None = None,
        selection: Literal["cyclic", "random"] = "cyclic",
    ) -> None: ...

###############################################################################
# Functions for CV with paths functions

def _path_residuals(
    X: ndarray,
    y: ndarray,
    sample_weight: None,
    train: ndarray,
    test: ndarray,
    normalize: bool,
    fit_intercept: bool,
    path: Callable,
    path_params: Dict[str, Any],
    alphas: Optional[ndarray] = None,
    l1_ratio: int = 1,
    X_order: Optional[str] = None,
    dtype: Optional[Type[float64]] = None,
) -> ndarray: ...

class LinearModelCV(MultiOutputMixin, LinearModel, ABC):
    @abstractmethod
    def __init__(
        self,
        eps: float = 1e-3,
        n_alphas: int = 100,
        alphas: Optional[ndarray] = None,
        fit_intercept: bool = True,
        normalize: str = "deprecated",
        precompute: str = "auto",
        max_iter: int = 1000,
        tol: float = 1e-4,
        copy_X: bool = True,
        cv: Optional[int] = None,
        verbose: bool = False,
        n_jobs: None = None,
        positive: bool = False,
        random_state: Optional[int] = None,
        selection: str = "cyclic",
    ) -> None: ...
    @abstractmethod
    def _get_estimator(self): ...
    @abstractmethod
    def _is_multitask(self): ...
    @staticmethod
    @abstractmethod
    def path(X, y, **kwargs): ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: float | ArrayLike | None = None,
    ) -> "LassoCV": ...
    def _more_tags(self): ...

class LassoCV(RegressorMixin, LinearModelCV):

    path = ...

    def __init__(
        self,
        *,
        eps: float = 1e-3,
        n_alphas: int = 100,
        alphas: NDArray | None = None,
        fit_intercept: bool = True,
        normalize: bool = ...,
        precompute: bool | ArrayLike | Literal["auto"] = "auto",
        max_iter: int = 1000,
        tol: float = 1e-4,
        copy_X: bool = True,
        cv: int | Generator | Iterable | None = None,
        verbose: bool | int = False,
        n_jobs: int | None = None,
        positive: bool = False,
        random_state: int | RandomState | None = None,
        selection: Literal["cyclic", "random"] = "cyclic",
    ) -> None: ...
    def _get_estimator(self) -> Lasso: ...
    def _is_multitask(self) -> bool: ...
    def _more_tags(self): ...

class ElasticNetCV(RegressorMixin, LinearModelCV):

    path = ...

    def __init__(
        self,
        *,
        l1_ratio: float | ArrayLike = 0.5,
        eps: float = 1e-3,
        n_alphas: int = 100,
        alphas: NDArray | None = None,
        fit_intercept: bool = True,
        normalize: bool = ...,
        precompute: bool | ArrayLike | Literal["auto"] = "auto",
        max_iter: int = 1000,
        tol: float = 1e-4,
        cv: int | Generator | Iterable | None = None,
        copy_X: bool = True,
        verbose: bool | int = 0,
        n_jobs: int | None = None,
        positive: bool = False,
        random_state: int | RandomState | None = None,
        selection: Literal["cyclic", "random"] = "cyclic",
    ): ...
    def _get_estimator(self): ...
    def _is_multitask(self): ...
    def _more_tags(self): ...

###############################################################################
# Multi Task ElasticNet and Lasso models (with joint feature selection)

class MultiTaskElasticNet(Lasso):
    def __init__(
        self,
        alpha: float = 1.0,
        *,
        l1_ratio: float = 0.5,
        fit_intercept: bool = True,
        normalize: bool = ...,
        copy_X: bool = True,
        max_iter: int = 1000,
        tol: float = 1e-4,
        warm_start: bool = False,
        random_state: int | RandomState | None = None,
        selection: Literal["cyclic", "random"] = "cyclic",
    ): ...
    def fit(self, X: NDArray, y: NDArray) -> "MultiTaskLasso": ...
    def _more_tags(self): ...

class MultiTaskLasso(MultiTaskElasticNet):
    def __init__(
        self,
        alpha: float = 1.0,
        *,
        fit_intercept: bool = True,
        normalize: bool = ...,
        copy_X: bool = True,
        max_iter: int = 1000,
        tol: float = 1e-4,
        warm_start: bool = False,
        random_state: int | RandomState | None = None,
        selection: Literal["cyclic", "random"] = "cyclic",
    ) -> None: ...

class MultiTaskElasticNetCV(RegressorMixin, LinearModelCV):

    path = ...

    def __init__(
        self,
        *,
        l1_ratio: float | ArrayLike = 0.5,
        eps: float = 1e-3,
        n_alphas: int = 100,
        alphas: ArrayLike | None = None,
        fit_intercept: bool = True,
        normalize: bool = ...,
        max_iter: int = 1000,
        tol: float = 1e-4,
        cv: int | Generator | Iterable | None = None,
        copy_X: bool = True,
        verbose: bool | int = 0,
        n_jobs: int | None = None,
        random_state: int | RandomState | None = None,
        selection: Literal["cyclic", "random"] = "cyclic",
    ): ...
    def _get_estimator(self): ...
    def _is_multitask(self): ...
    def _more_tags(self): ...

    # This is necessary as LinearModelCV now supports sample_weight while
    # MultiTaskElasticNet does not (yet).
    def fit(self, X: NDArray, y: NDArray) -> Any: ...

class MultiTaskLassoCV(RegressorMixin, LinearModelCV):

    path = ...

    def __init__(
        self,
        *,
        eps: float = 1e-3,
        n_alphas: int = 100,
        alphas: ArrayLike | None = None,
        fit_intercept: bool = True,
        normalize: bool = ...,
        max_iter: int = 1000,
        tol: float = 1e-4,
        copy_X: bool = True,
        cv: int | Generator | Iterable | None = None,
        verbose: bool | int = False,
        n_jobs: int | None = None,
        random_state: int | RandomState | None = None,
        selection: Literal["cyclic", "random"] = "cyclic",
    ): ...
    def _get_estimator(self): ...
    def _is_multitask(self): ...
    def _more_tags(self): ...

    # This is necessary as LinearModelCV now supports sample_weight while
    # MultiTaskElasticNet does not (yet).
    def fit(self, X: NDArray, y: NDArray) -> Any: ...
