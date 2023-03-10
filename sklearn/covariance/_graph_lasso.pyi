from typing import Any, Iterable, Literal
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from collections.abc import Iterable
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from .._typing import MatrixLike, Float, Int, ArrayLike
from scipy import linalg as linalg
from ..model_selection import check_cv as check_cv, cross_val_score as cross_val_score
from ..linear_model import lars_path_gram as lars_path_gram
from ..utils.validation import (
    check_random_state as check_random_state,
    check_scalar as check_scalar,
)
from numpy import ndarray
from . import (
    empirical_covariance as empirical_covariance,
    EmpiricalCovariance,
    log_likelihood as log_likelihood,
)
from numbers import Integral as Integral, Real as Real
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from ..model_selection import BaseCrossValidator

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# License: BSD 3 clause
# Copyright: INRIA
import warnings
import operator
import sys
import time
import numpy as np


def alpha_max(emp_cov: MatrixLike) -> Float:
    ...


# The g-lasso algorithm
def graphical_lasso(
    emp_cov: MatrixLike,
    alpha: Float,
    *,
    cov_init: None | MatrixLike = None,
    mode: Literal["cd", "lars", "cd"] = "cd",
    tol: Float = 1e-4,
    enet_tol: Float = 1e-4,
    max_iter: Int = 100,
    verbose: bool = False,
    return_costs: bool = False,
    eps: Float = ...,
    return_n_iter: bool = False,
) -> tuple[ndarray, ndarray, int] | tuple[ndarray, ndarray, list[tuple], int] | tuple[
    ndarray, ndarray
]:
    ...


class BaseGraphicalLasso(EmpiricalCovariance):
    _parameter_constraints: dict = ...

    def __init__(
        self,
        tol: float = 1e-4,
        enet_tol: float = 1e-4,
        max_iter: int = 100,
        mode: str = "cd",
        verbose: bool = False,
        assume_centered: bool = False,
    ) -> None:
        ...


class GraphicalLasso(BaseGraphicalLasso):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        alpha: Float = 0.01,
        *,
        mode: Literal["cd", "lars", "cd"] = "cd",
        tol: Float = 1e-4,
        enet_tol: Float = 1e-4,
        max_iter: Int = 100,
        verbose: bool = False,
        assume_centered: bool = False,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...


# Cross-validation with GraphicalLasso
def graphical_lasso_path(
    X: ArrayLike,
    alphas: ArrayLike,
    cov_init: None | MatrixLike = None,
    X_test: None | MatrixLike = None,
    mode: Literal["cd", "lars", "cd"] = "cd",
    tol: Float = 1e-4,
    enet_tol: Float = 1e-4,
    max_iter: Int = 100,
    verbose: int | bool = False,
) -> tuple[list[ndarray], list[ndarray], list[float]] | tuple[
    list[ndarray], list[ndarray], list[Float]
]:
    ...


class GraphicalLassoCV(BaseGraphicalLasso):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        alphas: int | ArrayLike = 4,
        n_refinements: Int = 4,
        cv: Iterable | BaseCrossValidator | int | None = None,
        tol: Float = 1e-4,
        enet_tol: Float = 1e-4,
        max_iter: Int = 100,
        mode: Literal["cd", "lars", "cd"] = "cd",
        n_jobs: None | Int = None,
        verbose: bool = False,
        assume_centered: bool = False,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...
