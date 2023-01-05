from numpy import float64, int64, ndarray
from collections.abc import Iterable, Generator
from typing import (
    DefaultDict,
    Dict,
    Iterator,
    List,
    Optional,
    Tuple,
    Union,
    Mapping,
    Sequence,
    Any,
    Callable,
    Literal,
)
from numpy.typing import ArrayLike, NDArray

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>,
#         Gael Varoquaux <gael.varoquaux@normalesup.org>
#         Andreas Mueller <amueller@ais.uni-bonn.de>
#         Olivier Grisel <olivier.grisel@ensta.org>
#         Raghav RV <rvraghav93@gmail.com>
# License: BSD 3 clause

from abc import ABCMeta, abstractmethod
from collections import defaultdict
from collections.abc import Mapping, Sequence, Iterable
from functools import partial, reduce
from itertools import product
import numbers
import operator
import time
import warnings

import numpy as np
from numpy.random import RandomState
from numpy.ma import MaskedArray
from scipy.stats import rankdata

from ..base import BaseEstimator, is_classifier, clone
from ..base import MetaEstimatorMixin
from ._split import check_cv
from ._validation import _fit_and_score
from ._validation import _aggregate_score_dicts
from ._validation import _insert_error_scores
from ._validation import _normalize_score_results
from ._validation import _warn_or_raise_about_fit_failures
from ..exceptions import NotFittedError
from ..utils import check_random_state
from ..utils._tags import _safe_tags
from ..utils.validation import indexable, check_is_fitted, _check_fit_params
from ..utils.metaestimators import available_if
from ..utils.fixes import delayed
from ..metrics._scorer import _check_multimetric_scoring
from ..metrics import check_scoring
from sklearn.base import BaseEstimator
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model._stochastic_gradient import SGDClassifier
from sklearn.metrics._scorer import _PredictScorer, _ThresholdScorer
from sklearn.model_selection._search_successive_halving import (
    HalvingGridSearchCV,
    HalvingRandomSearchCV,
)
from sklearn.pipeline import Pipeline
from sklearn.svm._classes import SVC

__all__ = ["GridSearchCV", "ParameterGrid", "ParameterSampler", "RandomizedSearchCV"]

class ParameterGrid:
    def __init__(self, param_grid: Mapping[str, Sequence] | Sequence[Mapping[str, Sequence]]) -> None: ...
    def __iter__(self) -> Iterator[dict[str, Any]]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, ind: int) -> dict[str, Any]: ...

class ParameterSampler:
    def __init__(
        self,
        param_distributions: Mapping,
        n_iter: int,
        *,
        random_state: int | RandomState | None = None,
    ): ...
    def _is_all_lists(self) -> bool: ...
    def __iter__(self) -> Iterator[Dict[str, Any]]: ...
    def __len__(self) -> int: ...

def _check_refit(search_cv: Union[RandomizedSearchCV, HalvingRandomSearchCV, GridSearchCV], attr: str) -> None: ...
def _estimator_has(attr: str) -> Callable: ...

class BaseSearchCV(MetaEstimatorMixin, BaseEstimator, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        estimator: BaseEstimator,
        *,
        scoring=None,
        n_jobs=None,
        refit=True,
        cv=None,
        verbose=0,
        pre_dispatch="2*n_jobs",
        error_score=...,
        return_train_score=True,
    ) -> None: ...
    @property
    def _estimator_type(self) -> str: ...
    def _more_tags(self) -> Dict[str, Union[bool, Dict[str, str]]]: ...
    def score(self, X: ArrayLike, y: ArrayLike | None = None) -> float: ...
    @available_if(_estimator_has("score_samples"))
    def score_samples(self, X: Iterable) -> NDArray: ...
    @available_if(_estimator_has("predict"))
    def predict(self, X: ndarray) -> NDArray: ...
    @available_if(_estimator_has("predict_proba"))
    def predict_proba(self, X) -> NDArray: ...
    @available_if(_estimator_has("predict_log_proba"))
    def predict_log_proba(self, X) -> NDArray: ...
    @available_if(_estimator_has("decision_function"))
    def decision_function(self, X: ndarray) -> ndarray: ...
    @available_if(_estimator_has("transform"))
    def transform(self, X) -> NDArray: ...
    @available_if(_estimator_has("inverse_transform"))
    def inverse_transform(self, Xt) -> NDArray: ...
    @property
    def n_features_in_(self): ...
    @property
    def classes_(self): ...
    def _run_search(self, evaluate_candidates): ...
    def _check_refit_for_multimetric(self, scores: Dict[str, Union[_ThresholdScorer, _PredictScorer]]) -> None: ...
    @staticmethod
    def _select_best_index(
        refit: Union[Callable, str, bool],
        refit_metric: Union[Callable, str],
        results: Dict[str, Any],
    ) -> int64: ...
    def fit(
        self,
        X: ArrayLike,
        y: ArrayLike | None = None,
        *,
        groups: ArrayLike | None = None,
        **fit_params,
    ) -> Union[HalvingRandomSearchCV, RandomizedSearchCV, HalvingGridSearchCV, GridSearchCV]: ...
    def _format_results(
        self,
        candidate_params: List[Dict[str, Any]],
        n_splits: int,
        out: List[Dict[str, Optional[Union[Dict[str, float], int, float]]]],
        more_results: Optional[DefaultDict[str, List[int]]] = None,
    ) -> Dict[str, Any]: ...

class GridSearchCV(BaseSearchCV):

    _required_parameters: list = ...

    def __init__(
        self,
        estimator: BaseEstimator,
        param_grid: Mapping | ArrayLike,
        *,
        scoring: str | Callable | ArrayLike | tuple | Mapping | None = None,
        n_jobs: int | None = None,
        refit: bool | str | Callable = True,
        cv: int | Generator | Iterable | None = None,
        verbose: int = 0,
        pre_dispatch: int | str = "2*n_jobs",
        error_score: float | Literal["raise"] = ...,
        return_train_score: bool = False,
    ) -> None: ...
    def _run_search(self, evaluate_candidates: Callable) -> None: ...

class RandomizedSearchCV(BaseSearchCV):

    _required_parameters: list = ...

    def __init__(
        self,
        estimator: BaseEstimator,
        param_distributions: dict | Sequence[dict],
        *,
        n_iter: int = 10,
        scoring: str | Callable | ArrayLike | tuple | Mapping | None = None,
        n_jobs: int | None = None,
        refit: bool | str | Callable = True,
        cv: int | Generator | Iterable | None = None,
        verbose: int = 0,
        pre_dispatch: int | str = "2*n_jobs",
        random_state: int | RandomState | None = None,
        error_score: float | Literal["raise"] = ...,
        return_train_score: bool = False,
    ) -> None: ...
    def _run_search(self, evaluate_candidates: Callable) -> None: ...
