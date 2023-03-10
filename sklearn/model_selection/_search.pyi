from typing import Any, Callable, Iterable, Iterator, Mapping, Sequence
from .._typing import Int, MatrixLike, ArrayLike, Float, Estimator
from ..utils.random import sample_without_replacement as sample_without_replacement
from scipy.sparse import spmatrix
from . import BaseCrossValidator
from abc import ABCMeta, abstractmethod
from itertools import product as product
from ..utils import check_random_state as check_random_state
from ..svm._classes import SVC
from ..pipeline import Pipeline
from ..metrics import check_scoring as check_scoring
from ..utils.validation import (
    indexable as indexable,
    check_is_fitted as check_is_fitted,
)
from numpy import ndarray
from ..linear_model._stochastic_gradient import SGDClassifier
from collections.abc import Iterable
from numpy.random import RandomState
from ..exceptions import NotFittedError as NotFittedError
from ._split import check_cv as check_cv
from ..base import (
    BaseEstimator,
    is_classifier as is_classifier,
    clone as clone,
    MetaEstimatorMixin,
)
from functools import partial as partial, reduce as reduce
from scipy.stats import rankdata as rankdata
from collections import defaultdict as defaultdict
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from ..utils.metaestimators import available_if as available_if
from numpy.ma import MaskedArray as MaskedArray
from ..kernel_ridge import KernelRidge
import numbers
import operator
import time
import warnings

import numpy as np

__all__ = ["GridSearchCV", "ParameterGrid", "ParameterSampler", "RandomizedSearchCV"]


class ParameterGrid:
    def __init__(self, param_grid) -> None:
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
        self, X: MatrixLike | list[str], y: None | MatrixLike | ArrayLike = None
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

    def transform(self, X: ArrayLike) -> spmatrix:
        ...

    def inverse_transform(self, Xt: ArrayLike) -> spmatrix:
        ...

    @property
    def n_features_in_(self):
        ...

    @property
    def classes_(self):
        ...

    def fit(
        self,
        X: MatrixLike | list[str],
        y: None | MatrixLike | ArrayLike = None,
        *,
        groups: None | ArrayLike = None,
        **fit_params,
    ) -> Any:
        ...


class GridSearchCV(BaseSearchCV):

    _required_parameters: list = ...

    def __init__(
        self,
        estimator: Estimator,
        param_grid: Sequence[dict] | Mapping,
        *,
        scoring: tuple | str | Callable | None | ArrayLike | Mapping = None,
        n_jobs: None | Int = None,
        refit: bool | str | Callable = True,
        cv: Iterable | BaseCrossValidator | int | None = None,
        verbose: Int = 0,
        pre_dispatch: int | str = "2*n_jobs",
        error_score: str | Float = ...,
        return_train_score: bool = False,
    ) -> None:
        ...


class RandomizedSearchCV(BaseSearchCV):

    _required_parameters: list = ...

    def __init__(
        self,
        estimator: Pipeline | SVC | Estimator | KernelRidge | SGDClassifier,
        param_distributions: Sequence[Mapping] | Mapping,
        *,
        n_iter: Int = 10,
        scoring: tuple | str | Callable | None | ArrayLike | Mapping = None,
        n_jobs: None | Int = None,
        refit: bool | str | Callable = True,
        cv: Iterable | BaseCrossValidator | int | None = None,
        verbose: Int = 0,
        pre_dispatch: int | str = "2*n_jobs",
        random_state: RandomState | None | Int = None,
        error_score: str | Float = ...,
        return_train_score: bool = False,
    ) -> None:
        ...
