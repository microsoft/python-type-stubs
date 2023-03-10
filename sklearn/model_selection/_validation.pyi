from typing import Callable, Iterable, Literal, Mapping
from ..linear_model._base import LinearRegression
from .._typing import Estimator, MatrixLike, ArrayLike, Int, Float
from ..preprocessing import LabelEncoder as LabelEncoder
from ..ensemble._hist_gradient_boosting.gradient_boosting import (
    HistGradientBoostingRegressor,
)
from . import BaseCrossValidator
from traceback import format_exc as format_exc
from contextlib import suppress as suppress
from joblib import logger as logger
from ..utils import indexable as indexable, check_random_state as check_random_state
from ..svm._classes import SVC, SVR, LinearSVC
from ..pipeline import Pipeline
from ..metrics import check_scoring as check_scoring
from ..naive_bayes import GaussianNB
from numpy import ndarray
from ..ensemble._stacking import StackingRegressor
from ..ensemble._forest import RandomForestClassifier
from collections.abc import Iterable
from numpy.random import RandomState
from ..exceptions import FitFailedWarning as FitFailedWarning
from ._split import check_cv as check_cv
from ..base import is_classifier as is_classifier, clone as clone
from functools import partial as partial
from collections import Counter as Counter
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from ..kernel_ridge import KernelRidge

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Gael Varoquaux <gael.varoquaux@normalesup.org>
#         Olivier Grisel <olivier.grisel@ensta.org>
#         Raghav RV <rvraghav93@gmail.com>
#         Michal Karbownik <michakarbownik@gmail.com>
# License: BSD 3 clause


import warnings
import numbers
import time

import numpy as np
import scipy.sparse as sp


__all__ = [
    "cross_validate",
    "cross_val_score",
    "cross_val_predict",
    "permutation_test_score",
    "learning_curve",
    "validation_curve",
]


def cross_validate(
    estimator: Estimator,
    X: MatrixLike,
    y: None | MatrixLike | ArrayLike = None,
    *,
    groups: None | ArrayLike = None,
    scoring: tuple | str | Callable | None | ArrayLike | Mapping = None,
    cv: Iterable | BaseCrossValidator | int | None = None,
    n_jobs: None | Int = None,
    verbose: Int = 0,
    fit_params: dict | None = None,
    pre_dispatch: str | Int = "2*n_jobs",
    return_train_score: bool = False,
    return_estimator: bool = False,
    error_score: str | Float = ...,
) -> dict[str, ndarray] | dict[str, ndarray | list[Pipeline]]:
    ...


def cross_val_score(
    estimator: Estimator,
    X: MatrixLike,
    y: None | MatrixLike | ArrayLike = None,
    *,
    groups: None | ArrayLike = None,
    scoring: str | None | Callable = None,
    cv: Iterable | BaseCrossValidator | int | None = None,
    n_jobs: None | Int = None,
    verbose: Int = 0,
    fit_params: dict | None = None,
    pre_dispatch: str | Int = "2*n_jobs",
    error_score: str | Float = ...,
) -> ndarray:
    ...


def cross_val_predict(
    estimator: Pipeline
    | Estimator
    | LinearRegression
    | RandomForestClassifier
    | StackingRegressor,
    X: MatrixLike,
    y: None | MatrixLike | ArrayLike = None,
    *,
    groups: None | ArrayLike = None,
    cv: Iterable | BaseCrossValidator | int | None = None,
    n_jobs: None | Int = None,
    verbose: Int = 0,
    fit_params: dict | None = None,
    pre_dispatch: str | Int = "2*n_jobs",
    method: Literal[
        "predict", "predict_proba", "predict_log_proba", "decision_function", "predict"
    ] = "predict",
) -> ndarray:
    ...


def permutation_test_score(
    estimator: SVC | Estimator,
    X: MatrixLike,
    y: None | MatrixLike | ArrayLike,
    *,
    groups: None | ArrayLike = None,
    cv: Iterable | BaseCrossValidator | int | None = None,
    n_permutations: Int = 100,
    n_jobs: None | Int = None,
    random_state: RandomState | None | Int = 0,
    verbose: Int = 0,
    scoring: str | None | Callable = None,
    fit_params: dict | None = None,
) -> tuple[float, ndarray, float] | tuple[Float, ndarray, Float]:
    ...


def learning_curve(
    estimator: SVC | KernelRidge | SVR | GaussianNB | HistGradientBoostingRegressor,
    X: MatrixLike,
    y: MatrixLike | ArrayLike,
    *,
    groups: None | ArrayLike = None,
    train_sizes: ArrayLike = ...,
    cv: Iterable | BaseCrossValidator | int | None = None,
    scoring: str | None | Callable = None,
    exploit_incremental_learning: bool = False,
    n_jobs: None | Int = None,
    pre_dispatch: str | Int = "all",
    verbose: Int = 0,
    shuffle: bool = False,
    random_state: RandomState | None | Int = None,
    error_score: str | Float = ...,
    return_times: bool = False,
    fit_params: dict | None = None,
) -> tuple[ndarray, ndarray, ndarray, ndarray, ndarray]:
    ...


def validation_curve(
    estimator: SVC | LinearSVC,
    X: MatrixLike,
    y: None | MatrixLike | ArrayLike,
    *,
    param_name: str,
    param_range: ArrayLike,
    groups: None | ArrayLike = None,
    cv: Iterable | BaseCrossValidator | int | None = None,
    scoring: str | None | Callable = None,
    n_jobs: None | Int = None,
    pre_dispatch: str | Int = "all",
    verbose: Int = 0,
    error_score: str | Float = ...,
    fit_params: dict | None = None,
) -> tuple[ndarray, ndarray]:
    ...
