from numpy import float64, ndarray
from collections.abc import Generator, Iterable
from typing import Any, Dict, List, Optional, Tuple, Union, Callable, Mapping, Literal
from numpy.typing import ArrayLike, NDArray

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Gael Varoquaux <gael.varoquaux@normalesup.org>
#         Olivier Grisel <olivier.grisel@ensta.org>
#         Raghav RV <rvraghav93@gmail.com>
#         Michal Karbownik <michakarbownik@gmail.com>
# License: BSD 3 clause

import warnings
import numbers
import time
from functools import partial
from traceback import format_exc
from contextlib import suppress
from collections import Counter

import numpy as np
import scipy.sparse as sp

from ..base import is_classifier, clone
from ..utils import indexable, check_random_state, _safe_indexing
from ..utils.validation import _check_fit_params
from ..utils.validation import _num_samples
from ..utils.fixes import delayed
from ..utils.metaestimators import _safe_split
from ..metrics import check_scoring
from ..metrics._scorer import _check_multimetric_scoring, _MultimetricScorer
from ..exceptions import FitFailedWarning
from ._split import check_cv
from ..preprocessing import LabelEncoder
from pandas.core.series import Series
from numpy.random import RandomState
from sklearn.base import BaseEstimator
from sklearn.ensemble._forest import RandomForestClassifier
from sklearn.linear_model._base import LinearRegression
from sklearn.metrics._scorer import _PredictScorer, _ThresholdScorer
from sklearn.model_selection._split import StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.svm._classes import LinearSVC, SVC

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
    X: ArrayLike,
    y: ArrayLike | None = None,
    *,
    groups: ArrayLike | None = None,
    scoring: str | Callable | ArrayLike | tuple | Mapping | None = None,
    cv: int | Generator | Iterable | None = None,
    n_jobs: int | None = None,
    verbose: int = 0,
    fit_params: Mapping | None = None,
    pre_dispatch: int | str = "2*n_jobs",
    return_train_score: bool = False,
    return_estimator: bool = False,
    error_score: float | Literal["raise"] = ...,
) -> dict: ...
def _insert_error_scores(results: List[Dict[str, Optional[Union[float, int]]]], error_score: float) -> None: ...
def _normalize_score_results(
    scores: Union[List[Dict[str, float]], ndarray], scaler_score_key: str = "score"
) -> Dict[str, ndarray]: ...
def _warn_or_raise_about_fit_failures(
    results: List[Dict[str, Optional[Union[Dict[str, float], int, float]]]],
    error_score: float,
) -> None: ...
def cross_val_score(
    estimator: BaseEstimator,
    X: ArrayLike,
    y: ArrayLike | None = None,
    *,
    groups: ArrayLike | None = None,
    scoring: str | Callable | None = None,
    cv: int | Generator | Iterable | None = None,
    n_jobs: int | None = None,
    verbose: int = 0,
    fit_params: Mapping | None = None,
    pre_dispatch: int | str = "2*n_jobs",
    error_score: float | Literal["raise"] = ...,
) -> NDArray: ...
def _fit_and_score(
    estimator: BaseEstimator,
    X: ndarray,
    y: Optional[Union[ndarray, Series]],
    scorer: Union[
        Dict[str, Callable],
        Callable,
        _ThresholdScorer,
        _PredictScorer,
        Dict[str, _PredictScorer],
    ],
    train: ndarray,
    test: ndarray,
    verbose: int,
    parameters: Any,
    fit_params: None,
    return_train_score: bool = False,
    return_parameters: bool = False,
    return_n_test_samples: bool = False,
    return_times: bool = False,
    return_estimator: bool = False,
    split_progress: Optional[Tuple[int, int]] = None,
    candidate_progress: Optional[Tuple[int, int]] = None,
    error_score: float = np.nan,
) -> Dict[str, Optional[Union[Dict[str, float], int, float]]]: ...
def _score(
    estimator: BaseEstimator,
    X_test: ndarray,
    y_test: Optional[Union[ndarray, Series]],
    scorer: Union[
        Dict[str, Callable],
        Callable,
        _ThresholdScorer,
        _PredictScorer,
        Dict[str, _PredictScorer],
    ],
    error_score: float | str = "raise",
) -> Union[Dict[str, float], float]: ...
def cross_val_predict(
    estimator: BaseEstimator,
    X: ArrayLike,
    y: ArrayLike | None = None,
    *,
    groups: ArrayLike | None = None,
    cv: int | Generator | Iterable | None = None,
    n_jobs: int | None = None,
    verbose: int = 0,
    fit_params: Mapping | None = None,
    pre_dispatch: int | str = "2*n_jobs",
    method: Literal["predict", "predict_proba", "predict_log_proba", "decision_function"] = "predict",
) -> NDArray: ...
def _fit_and_predict(
    estimator: Union[Pipeline, LinearRegression, RandomForestClassifier],
    X: ndarray,
    y: ndarray,
    train: ndarray,
    test: ndarray,
    verbose: int,
    fit_params: None,
    method: str,
) -> ndarray: ...
def _enforce_prediction_order(classes: ndarray, predictions: ndarray, n_classes: int, method: str) -> ndarray: ...
def _check_is_permutation(indices: ndarray, n_samples: int) -> bool: ...
def permutation_test_score(
    estimator: BaseEstimator,
    X: ArrayLike,
    y: ArrayLike | None,
    *,
    groups: ArrayLike | None = None,
    cv: int | Generator | Iterable | None = None,
    n_permutations: int = 100,
    n_jobs: int | None = None,
    random_state: int | RandomState | None = 0,
    verbose: int = 0,
    scoring: str | Callable | None = None,
    fit_params: Mapping | None = None,
) -> tuple[float, NDArray, float]: ...
def _permutation_test_score(
    estimator: SVC,
    X: ndarray,
    y: ndarray,
    groups: None,
    cv: StratifiedKFold,
    scorer: _PredictScorer,
    fit_params: None,
) -> float64: ...
def _shuffle(y: ndarray, groups: None, random_state: RandomState) -> ndarray: ...
def learning_curve(
    estimator,
    X: ArrayLike,
    y: ArrayLike,
    *,
    groups: ArrayLike | None = None,
    train_sizes: ArrayLike = ...,
    cv: int | Generator | Iterable | None = None,
    scoring: str | Callable | None = None,
    exploit_incremental_learning: bool = False,
    n_jobs: int | None = None,
    pre_dispatch: int | str = "all",
    verbose: int = 0,
    shuffle: bool = False,
    random_state: int | RandomState | None = None,
    error_score: float | Literal["raise"] = ...,
    return_times: bool = False,
    fit_params: Mapping | None = None,
) -> tuple[NDArray, NDArray, NDArray, NDArray, NDArray]: ...
def _translate_train_sizes(train_sizes, n_max_training_samples): ...
def _incremental_fit_estimator(
    estimator,
    X,
    y,
    classes,
    train,
    test,
    train_sizes,
    scorer,
    verbose,
    return_times,
    error_score,
    fit_params,
): ...
def validation_curve(
    estimator: Union[LinearSVC, SVC],
    X: ArrayLike,
    y: ArrayLike | None,
    *,
    param_name: str,
    param_range: ArrayLike,
    groups: ArrayLike | None = None,
    cv: int | Generator | Iterable | None = None,
    scoring: str | Callable | None = None,
    n_jobs: int | None = None,
    pre_dispatch: int | str = "all",
    verbose: int = 0,
    error_score: float | Literal["raise"] = ...,
    fit_params: Mapping | None = None,
) -> tuple[NDArray, NDArray]: ...
def _aggregate_score_dicts(
    scores: List[Dict[str, Optional[Union[Dict[str, float], int, float]]]]
) -> Dict[str, Union[List[None], List[Dict[str, float]], ndarray]]: ...
