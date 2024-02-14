import numbers
import time
import warnings
from collections import Counter as Counter
from contextlib import suppress as suppress
from functools import partial as partial
from traceback import format_exc as format_exc
from typing import Callable, Iterable, Literal, Mapping

import numpy as np
import scipy.sparse as sp
from joblib import logger as logger
from numpy import ndarray
from numpy.random import RandomState

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, clone as clone, is_classifier as is_classifier
from ..exceptions import FitFailedWarning as FitFailedWarning
from ..metrics import check_scoring as check_scoring
from ..preprocessing import LabelEncoder as LabelEncoder
from ..svm._classes import SVC, LinearSVC
from ..utils import check_random_state as check_random_state, indexable as indexable
from ..utils.parallel import Parallel as Parallel, delayed as delayed
from . import BaseCrossValidator
from ._split import BaseShuffleSplit, check_cv as check_cv

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Gael Varoquaux <gael.varoquaux@normalesup.org>
#         Olivier Grisel <olivier.grisel@ensta.org>
#         Raghav RV <rvraghav93@gmail.com>
#         Michal Karbownik <michakarbownik@gmail.com>
# License: BSD 3 clause

__all__ = [
    "cross_validate",
    "cross_val_score",
    "cross_val_predict",
    "permutation_test_score",
    "learning_curve",
    "validation_curve",
]

def cross_validate(
    estimator: BaseEstimator,
    X: MatrixLike,
    y: None | MatrixLike | ArrayLike = None,
    *,
    groups: None | ArrayLike = None,
    scoring: ArrayLike | None | tuple | Callable | Mapping | str = None,
    cv: int | BaseCrossValidator | Iterable | None | BaseShuffleSplit = None,
    n_jobs: None | Int = None,
    verbose: Int = 0,
    fit_params: None | dict = None,
    pre_dispatch: str | Int = "2*n_jobs",
    return_train_score: bool = False,
    return_estimator: bool = False,
    error_score: str | Float = ...,
): ...
def cross_val_score(
    estimator: BaseEstimator,
    X: MatrixLike,
    y: None | MatrixLike | ArrayLike = None,
    *,
    groups: None | ArrayLike = None,
    scoring: None | str | Callable = None,
    cv: int | BaseCrossValidator | Iterable | None | BaseShuffleSplit = None,
    n_jobs: None | Int = None,
    verbose: Int = 0,
    fit_params: None | dict = None,
    pre_dispatch: str | Int = "2*n_jobs",
    error_score: str | Float = ...,
) -> ndarray: ...
def cross_val_predict(
    estimator: BaseEstimator,
    X: MatrixLike,
    y: None | MatrixLike | ArrayLike = None,
    *,
    groups: None | ArrayLike = None,
    cv: int | BaseCrossValidator | Iterable | None | BaseShuffleSplit = None,
    n_jobs: None | Int = None,
    verbose: Int = 0,
    fit_params: None | dict = None,
    pre_dispatch: str | Int = "2*n_jobs",
    method: Literal["predict", "predict_proba", "predict_log_proba", "decision_function", "predict"] = "predict",
) -> ndarray: ...
def permutation_test_score(
    estimator: BaseEstimator | SVC,
    X: MatrixLike,
    y: None | MatrixLike | ArrayLike,
    *,
    groups: None | ArrayLike = None,
    cv: int | BaseCrossValidator | Iterable | None | BaseShuffleSplit = None,
    n_permutations: Int = 100,
    n_jobs: None | Int = None,
    random_state: RandomState | None | Int = 0,
    verbose: Int = 0,
    scoring: None | str | Callable = None,
    fit_params: None | dict = None,
) -> tuple[Float, ndarray, Float] | tuple[float, ndarray, float]: ...
def learning_curve(
    estimator,
    X: MatrixLike,
    y: MatrixLike | ArrayLike,
    *,
    groups: None | ArrayLike = None,
    train_sizes: ArrayLike = ...,
    cv: int | BaseCrossValidator | Iterable | None | BaseShuffleSplit = None,
    scoring: None | str | Callable = None,
    exploit_incremental_learning: bool = False,
    n_jobs: None | Int = None,
    pre_dispatch: str | Int = "all",
    verbose: Int = 0,
    shuffle: bool = False,
    random_state: RandomState | None | Int = None,
    error_score: str | Float = ...,
    return_times: bool = False,
    fit_params: None | dict = None,
) -> tuple[ndarray, ndarray, ndarray, ndarray, ndarray]: ...
def validation_curve(
    estimator: SVC | LinearSVC,
    X: MatrixLike,
    y: None | MatrixLike | ArrayLike,
    *,
    param_name: str,
    param_range: ArrayLike,
    groups: None | ArrayLike = None,
    cv: int | BaseCrossValidator | Iterable | None | BaseShuffleSplit = None,
    scoring: None | str | Callable = None,
    n_jobs: None | Int = None,
    pre_dispatch: str | Int = "all",
    verbose: Int = 0,
    error_score: str | Float = ...,
    fit_params: None | dict = None,
) -> tuple[ndarray, ndarray]: ...
