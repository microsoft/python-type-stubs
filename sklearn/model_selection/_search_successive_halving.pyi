from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, Sequence
from .._typing import MatrixLike, ArrayLike, Estimator, Int, Float
from . import BaseCrossValidator
from ._search import BaseSearchCV
from abc import abstractmethod as abstractmethod
from . import ParameterGrid as ParameterGrid, ParameterSampler as ParameterSampler
from ..utils import resample as resample
from ..svm._classes import SVC
from copy import deepcopy as deepcopy
from numpy import ndarray
from ..ensemble._forest import RandomForestClassifier
from collections.abc import Iterable
from numpy.random import RandomState
from ._split import check_cv as check_cv
from math import ceil as ceil, floor as floor, log as log
from ..base import is_classifier as is_classifier
from ..utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from numbers import Integral as Integral
from ..ensemble._gb import GradientBoostingRegressor

import numpy as np


__all__ = ["HalvingGridSearchCV", "HalvingRandomSearchCV"]


class _SubsampleMetaSplitter:
    def __init__(self, *, base_cv, fraction, subsample_test, random_state) -> None:
        ...

    def split(
        self, X: ndarray, y: ndarray, groups=None
    ) -> Iterator[tuple[ndarray, ndarray]]:
        ...


class BaseSuccessiveHalving(BaseSearchCV):
    def __init__(
        self,
        estimator: SVC | GradientBoostingRegressor | RandomForestClassifier,
        *,
        scoring=None,
        n_jobs=None,
        refit: bool = True,
        cv: int = 5,
        verbose: int = 0,
        random_state=None,
        error_score=...,
        return_train_score: bool = True,
        max_resources: str = "auto",
        min_resources: str = "exhaust",
        resource: str = "n_samples",
        factor: int = 3,
        aggressive_elimination: bool = False,
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike,
        y: None | MatrixLike | ArrayLike = None,
        groups: None | ArrayLike = None,
        **fit_params,
    ) -> Any:
        ...


class HalvingGridSearchCV(BaseSuccessiveHalving):

    _required_parameters: list = ...

    def __init__(
        self,
        estimator: SVC | Estimator,
        param_grid: Sequence[dict] | dict[str, list[int | float]] | Mapping,
        *,
        factor: int | float = 3,
        resource: str = "n_samples",
        max_resources: str | Int = "auto",
        min_resources: int | Literal["exhaust", "smallest", "exhaust"] = "exhaust",
        aggressive_elimination: bool = False,
        cv: Iterable | BaseCrossValidator | int = 5,
        scoring: str | None | Callable = None,
        refit: bool = True,
        error_score: str | Float = ...,
        return_train_score: bool = True,
        random_state: RandomState | None | Int = None,
        n_jobs: int | None = None,
        verbose: Int = 0,
    ) -> None:
        ...


class HalvingRandomSearchCV(BaseSuccessiveHalving):

    _required_parameters: list = ...

    def __init__(
        self,
        estimator: Estimator | GradientBoostingRegressor | RandomForestClassifier,
        param_distributions: dict,
        *,
        n_candidates: str | Int = "exhaust",
        factor: int | float = 3,
        resource: str = "n_samples",
        max_resources: str | Int = "auto",
        min_resources: Literal["exhaust", "smallest", "smallest"] | int = "smallest",
        aggressive_elimination: bool = False,
        cv: Iterable | BaseCrossValidator | int = 5,
        scoring: str | None | Callable = None,
        refit: bool = True,
        error_score: str | Float = ...,
        return_train_score: bool = True,
        random_state: RandomState | None | Int = None,
        n_jobs: int | None = None,
        verbose: Int = 0,
    ) -> None:
        ...
