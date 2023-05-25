from typing import (
    Any,
    Callable,
    ClassVar,
    Iterable,
    Iterator,
    Mapping,
    Sequence,
    TypeVar,
)
from numpy.random import RandomState
from itertools import product as product
from ..base import BaseEstimator
from ..exceptions import NotFittedError as NotFittedError
from ._split import BaseShuffleSplit
from ..utils.random import sample_without_replacement as sample_without_replacement
from ..metrics import check_scoring as check_scoring
from ._split import check_cv as check_cv
from scipy.sparse import spmatrix
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from collections.abc import Mapping, Sequence, Iterable
from ..utils.validation import (
    indexable as indexable,
    check_is_fitted as check_is_fitted,
)
from scipy.stats import rankdata as rankdata
from collections import defaultdict as defaultdict
from abc import ABCMeta, abstractmethod
from numpy import ndarray
from functools import partial as partial, reduce as reduce
from ..base import is_classifier as is_classifier, clone as clone, MetaEstimatorMixin
from ..utils import check_random_state as check_random_state
from ..utils.metaestimators import available_if as available_if
from numpy.ma import MaskedArray as MaskedArray
from .._typing import Int, MatrixLike, ArrayLike, Float
from . import BaseCrossValidator

BaseSearchCV_Self = TypeVar("BaseSearchCV_Self", bound="BaseSearchCV")

import numbers
import operator
import time
import warnings

import numpy as np

__all__ = ["GridSearchCV", "ParameterGrid", "ParameterSampler", "RandomizedSearchCV"]


class ParameterGrid:
    def __init__(
        self, param_grid: Sequence[Mapping[str, Sequence]] | Mapping[str, Sequence]
    ) -> None:
        ...

    def __iter__(self) -> Iterator[dict[str, Any]]:
        ...

    def __len__(self) -> int:
        ...

    def __getitem__(self, ind: Int) -> dict[str, Any]:
        ...


class ParameterSampler:
    def __init__(
        self,
        param_distributions: dict,
        n_iter: Int,
        *,
        random_state: RandomState | None | Int = None,
    ) -> None:
        ...

    def __iter__(self):
        ...

    def __len__(self) -> int:
        ...


class BaseSearchCV(MetaEstimatorMixin, BaseEstimator, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        estimator,
        *,
        scoring=None,
        n_jobs=None,
        refit: bool = True,
        cv=None,
        verbose: int = 0,
        pre_dispatch: str = "2*n_jobs",
        error_score=...,
        return_train_score: bool = True,
    ) -> None:
        ...

    def score(
        self, X: list[str] | MatrixLike, y: None | MatrixLike | ArrayLike = None
    ) -> Float:
        ...

    def score_samples(self, X: Iterable) -> ndarray:
        ...

    def predict(self, X: ArrayLike) -> ndarray:
        ...

    def predict_proba(self, X: ArrayLike) -> ndarray:
        ...

    def predict_log_proba(self, X: ArrayLike) -> ndarray:
        ...

    def decision_function(self, X: ArrayLike) -> ndarray:
        ...

    def transform(self, X: ArrayLike) -> ndarray | spmatrix:
        ...

    def inverse_transform(self, Xt: ArrayLike) -> ndarray | spmatrix:
        ...

    def n_features_in_(self):
        ...

    def classes_(self):
        ...

    def fit(
        self: BaseSearchCV_Self,
        X: list[str] | MatrixLike,
        y: None | MatrixLike | ArrayLike = None,
        *,
        groups: None | ArrayLike = None,
        **fit_params,
    ) -> BaseSearchCV_Self:
        ...


class GridSearchCV(BaseSearchCV):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    classes_: ndarray = ...
    multimetric_: bool = ...
    refit_time_: float = ...
    n_splits_: int = ...
    scorer_: Callable | dict = ...
    best_index_: int = ...
    best_params_: dict = ...
    best_score_: float = ...
    best_estimator_: BaseEstimator = ...
    cv_results_: dict[str, ndarray] = ...

    _required_parameters: ClassVar[list] = ...

    def __init__(
        self,
        estimator: BaseEstimator,
        param_grid: Mapping | Sequence[dict],
        *,
        scoring: ArrayLike | None | tuple | Callable | Mapping | str = None,
        n_jobs: None | Int = None,
        refit: str | Callable | bool = True,
        cv: int | BaseCrossValidator | Iterable | None | BaseShuffleSplit = None,
        verbose: Int = 0,
        pre_dispatch: str | int = "2*n_jobs",
        error_score: str | Float = ...,
        return_train_score: bool = False,
    ) -> None:
        ...


class RandomizedSearchCV(BaseSearchCV):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    classes_: ndarray = ...
    multimetric_: bool = ...
    refit_time_: float = ...
    n_splits_: int = ...
    scorer_: Callable | dict = ...
    best_index_: int = ...
    best_params_: dict = ...
    best_score_: float = ...
    best_estimator_: BaseEstimator = ...
    cv_results_: dict[str, ndarray] = ...

    _required_parameters: ClassVar[list] = ...

    def __init__(
        self,
        estimator: BaseEstimator,
        param_distributions: Sequence[Mapping] | Mapping,
        *,
        n_iter: Int = 10,
        scoring: ArrayLike | None | tuple | Callable | Mapping | str = None,
        n_jobs: None | Int = None,
        refit: str | Callable | bool = True,
        cv: int | BaseCrossValidator | Iterable | None | BaseShuffleSplit = None,
        verbose: Int = 0,
        pre_dispatch: str | int = "2*n_jobs",
        random_state: RandomState | None | Int = None,
        error_score: str | Float = ...,
        return_train_score: bool = False,
    ) -> None:
        ...
