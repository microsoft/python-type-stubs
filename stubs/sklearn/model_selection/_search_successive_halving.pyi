from typing import (
    Callable,
    ClassVar,
    Iterable,
    Iterator,
    Literal,
    Mapping,
    Sequence,
    TypeVar,
)
from numpy.random import RandomState
from ..base import BaseEstimator
from ._split import BaseShuffleSplit
from ._split import check_cv as check_cv
from copy import deepcopy as deepcopy
from ..svm._classes import SVC
from abc import abstractmethod as abstractmethod
from numpy import ndarray
from numbers import Integral as Integral
from ..base import is_classifier as is_classifier
from ..utils import resample as resample
from . import ParameterGrid as ParameterGrid, ParameterSampler as ParameterSampler
from ..utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from math import ceil as ceil, floor as floor, log as log
from ._search import BaseSearchCV
from .._typing import MatrixLike, ArrayLike, Int, Float
from . import BaseCrossValidator

BaseSuccessiveHalving_Self = TypeVar(
    "BaseSuccessiveHalving_Self", bound="BaseSuccessiveHalving"
)


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
        estimator,
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
        self: BaseSuccessiveHalving_Self,
        X: MatrixLike,
        y: None | MatrixLike | ArrayLike = None,
        groups: None | ArrayLike = None,
        **fit_params,
    ) -> BaseSuccessiveHalving_Self:
        ...


class HalvingGridSearchCV(BaseSuccessiveHalving):
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
    best_estimator_: BaseEstimator | dict = ...
    cv_results_: dict[str, ndarray] = ...
    n_required_iterations_: int = ...
    n_possible_iterations_: int = ...
    n_iterations_: int = ...
    min_resources_: int = ...
    max_resources_: int = ...
    n_remaining_candidates_: int = ...
    n_candidates_: list[int] = ...
    n_resources_: list[int] = ...

    _required_parameters: ClassVar[list] = ...

    def __init__(
        self,
        estimator: BaseEstimator | SVC,
        param_grid: Mapping | dict[str, list[int | float]] | Sequence[dict],
        *,
        factor: float | int = 3,
        resource: str = "n_samples",
        max_resources: str | Int = "auto",
        min_resources: int | Literal["exhaust", "smallest", "exhaust"] = "exhaust",
        aggressive_elimination: bool = False,
        cv: Iterable | int | BaseShuffleSplit | BaseCrossValidator = 5,
        scoring: None | str | Callable = None,
        refit: bool = True,
        error_score: str | Float = ...,
        return_train_score: bool = True,
        random_state: RandomState | None | Int = None,
        n_jobs: None | int = None,
        verbose: Int = 0,
    ) -> None:
        ...


class HalvingRandomSearchCV(BaseSuccessiveHalving):
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
    best_estimator_: BaseEstimator | dict = ...
    cv_results_: dict[str, ndarray] = ...
    n_required_iterations_: int = ...
    n_possible_iterations_: int = ...
    n_iterations_: int = ...
    min_resources_: int = ...
    max_resources_: int = ...
    n_remaining_candidates_: int = ...
    n_candidates_: list[int] = ...
    n_resources_: list[int] = ...

    _required_parameters: ClassVar[list] = ...

    def __init__(
        self,
        estimator: BaseEstimator,
        param_distributions: dict,
        *,
        n_candidates: str | Int = "exhaust",
        factor: float | int = 3,
        resource: str = "n_samples",
        max_resources: str | Int = "auto",
        min_resources: Literal["exhaust", "smallest", "smallest"] | int = "smallest",
        aggressive_elimination: bool = False,
        cv: Iterable | int | BaseShuffleSplit | BaseCrossValidator = 5,
        scoring: None | str | Callable = None,
        refit: bool = True,
        error_score: str | Float = ...,
        return_train_score: bool = True,
        random_state: RandomState | None | Int = None,
        n_jobs: None | int = None,
        verbose: Int = 0,
    ) -> None:
        ...
