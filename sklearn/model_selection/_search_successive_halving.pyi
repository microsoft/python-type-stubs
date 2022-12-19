from collections.abc import Generator, Iterable
from typing import (
    Dict,
    Iterator,
    List,
    Optional,
    Tuple,
    Union,
    Any,
    Mapping,
    Literal,
    Callable,
)
from numpy.typing import ArrayLike
from copy import deepcopy
from math import ceil, floor, log
from abc import abstractmethod
from numbers import Integral

import numpy as np
from numpy.random import RandomState
from ._search import BaseSearchCV
from . import ParameterGrid, ParameterSampler
from ..base import BaseEstimator, is_classifier
from ._split import check_cv, _yields_constant_splits
from ..utils import resample
from ..utils.multiclass import check_classification_targets
from ..utils.validation import _num_samples
from numpy.ma.core import MaskedArray
from numpy import int64, ndarray
from scipy.stats._distn_infrastructure import rv_discrete_frozen
from sklearn.ensemble._forest import RandomForestClassifier
from sklearn.ensemble._gb import GradientBoostingRegressor
from sklearn.model_selection._search import ParameterGrid, ParameterSampler
from sklearn.svm._classes import SVC

__all__ = ["HalvingGridSearchCV", "HalvingRandomSearchCV"]

class _SubsampleMetaSplitter:
    def __init__(self, *, base_cv, fraction, subsample_test, random_state) -> None: ...
    def split(self, X: ndarray, y: ndarray, groups: None = None) -> Iterator[Tuple[ndarray, ndarray]]: ...

def _top_k(
    results: Dict[
        str,
        Union[
            ndarray,
            MaskedArray,
            List[Union[Dict[str, Union[int, float]], Dict[str, float]]],
            List[Dict[str, Union[int, float]]],
            List[
                Union[
                    Dict[str, Union[bool, int, str]],
                    Dict[str, Optional[Union[int, bool, str]]],
                ]
            ],
        ],
    ],
    k: int,
    itr: int,
) -> ndarray: ...

class BaseSuccessiveHalving(BaseSearchCV):
    def __init__(
        self,
        estimator: Union[RandomForestClassifier, GradientBoostingRegressor, SVC],
        *,
        scoring=None,
        n_jobs=None,
        refit=True,
        cv=5,
        verbose=0,
        random_state=None,
        error_score=...,
        return_train_score=True,
        max_resources="auto",
        min_resources="exhaust",
        resource="n_samples",
        factor=3,
        aggressive_elimination=False,
    ) -> None: ...
    def _check_input_parameters(self, X: ndarray, y: ndarray, groups: None) -> None: ...
    @staticmethod
    def _select_best_index(
        refit: bool,
        refit_metric: str,
        results: Dict[
            str,
            Union[
                ndarray,
                MaskedArray,
                List[Union[Dict[str, Union[int, float]], Dict[str, float]]],
                List[Dict[str, Union[int, float]]],
                List[
                    Union[
                        Dict[str, Union[bool, int, str]],
                        Dict[str, Optional[Union[int, bool, str]]],
                    ]
                ],
            ],
        ],
    ) -> int64: ...
    def fit(
        self,
        X: ArrayLike,
        y: ArrayLike | None = None,
        groups: ArrayLike | None = None,
        **fit_params,
    ) -> Union[HalvingGridSearchCV, HalvingRandomSearchCV]: ...
    def _run_search(self, evaluate_candidates: Callable) -> None: ...
    @abstractmethod
    def _generate_candidate_params(self): ...
    def _more_tags(self): ...

class HalvingGridSearchCV(BaseSuccessiveHalving):

    _required_parameters: list = ...

    def __init__(
        self,
        estimator: BaseEstimator,
        param_grid: Mapping | ArrayLike,
        *,
        factor: int | float = 3,
        resource: str | Literal["n_samples"] = "n_samples",
        max_resources: int | str = "auto",
        min_resources: Literal["exhaust", "smallest"] | int = "exhaust",
        aggressive_elimination: bool = False,
        cv: int | Generator | Iterable = 5,
        scoring: str | Callable | None = None,
        refit: bool = True,
        error_score: float | Literal["raise"] = ...,
        return_train_score: bool = True,
        random_state: int | RandomState | None = None,
        n_jobs: int | None = None,
        verbose: int = 0,
    ) -> None: ...
    def _generate_candidate_params(self) -> ParameterGrid: ...

class HalvingRandomSearchCV(BaseSuccessiveHalving):

    _required_parameters: list = ...

    def __init__(
        self,
        estimator: BaseEstimator,
        param_distributions: Mapping,
        *,
        n_candidates: int | str = "exhaust",
        factor: int | float = 3,
        resource: str | Literal["n_samples"] = "n_samples",
        max_resources: int | str = "auto",
        min_resources: Literal["exhaust", "smallest"] | int = "smallest",
        aggressive_elimination: bool = False,
        cv: int | Generator | Iterable = 5,
        scoring: str | Callable | None = None,
        refit: bool = True,
        error_score: float | Literal["raise"] = ...,
        return_train_score: bool = True,
        random_state: int | RandomState | None = None,
        n_jobs: int | None = None,
        verbose: int = 0,
    ) -> None: ...
    def _generate_candidate_params(self) -> ParameterSampler: ...
