from numpy import float64, ndarray
from collections.abc import Generator, Iterable
from typing import List, Optional, Tuple, Union, Literal, Any
from numpy.typing import NDArray, ArrayLike

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# License: BSD 3 clause
# Copyright: INRIA
import warnings
import operator
import sys
import time

import numpy as np
from scipy import linalg

from . import empirical_covariance, EmpiricalCovariance, log_likelihood

from ..exceptions import ConvergenceWarning
from ..utils.validation import _is_arraylike_not_scalar, check_random_state
from ..utils.fixes import delayed

# mypy error: Module 'sklearn.linear_model' has no attribute '_cd_fast'
from ..linear_model import _cd_fast as cd_fast  # type: ignore
from ..linear_model import lars_path_gram
from ..model_selection import check_cv, cross_val_score

# Helper functions to compute the objective and dual objective functions
# of the l1-penalized estimator
def _objective(mle: ndarray, precision_: ndarray, alpha: float64) -> float64: ...
def _dual_gap(emp_cov: ndarray, precision_: ndarray, alpha: float64) -> float64: ...
def alpha_max(emp_cov: NDArray) -> float64: ...

class _DictWithDeprecatedKeys(dict):
    def __init__(self, **kwargs) -> None: ...
    def __getitem__(self, key: str) -> ndarray: ...
    def _set_deprecated(self, value: ndarray, *, new_key, deprecated_key) -> None: ...

# The g-lasso algorithm
def graphical_lasso(
    emp_cov: NDArray,
    alpha: float,
    *,
    cov_init: ArrayLike | None = None,
    mode: Literal["cd", "lars"] = "cd",
    tol: float = 1e-4,
    enet_tol: float = 1e-4,
    max_iter: int = 100,
    verbose: bool = False,
    return_costs: bool = False,
    eps: float = ...,
    return_n_iter: bool = False,
) -> tuple[NDArray, NDArray, list[tuple[float, float]], int]: ...

class GraphicalLasso(EmpiricalCovariance):
    def __init__(
        self,
        alpha: float = 0.01,
        *,
        mode: Literal["cd", "lars"] = "cd",
        tol: float = 1e-4,
        enet_tol: float = 1e-4,
        max_iter: int = 100,
        verbose: bool = False,
        assume_centered: bool = False,
    ) -> None: ...
    def fit(self, X: ArrayLike, y=None) -> Any: ...

# Cross-validation with GraphicalLasso
def graphical_lasso_path(
    X: NDArray,
    alphas: ArrayLike,
    cov_init: ArrayLike | None = None,
    X_test: ArrayLike | None = None,
    mode: Literal["cd", "lars"] = "cd",
    tol: float = 1e-4,
    enet_tol: float = 1e-4,
    max_iter: int = 100,
    verbose: int | bool = False,
) -> tuple[list[NDArray], list[NDArray], list[float]]: ...

class GraphicalLassoCV(GraphicalLasso):
    def __init__(
        self,
        *,
        alphas: int | ArrayLike = 4,
        n_refinements: int = 4,
        cv: int | Generator | Iterable | None = None,
        tol: float = 1e-4,
        enet_tol: float = 1e-4,
        max_iter: int = 100,
        mode: Literal["cd", "lars"] = "cd",
        n_jobs: int | None = None,
        verbose: bool = False,
        assume_centered: bool = False,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: None = None) -> "GraphicalLassoCV": ...
