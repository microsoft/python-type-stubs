from typing import Any, ClassVar, Sequence, List, TypeVar
from abc import ABCMeta, abstractmethod
from ..tree import (
    DecisionTreeRegressor as DecisionTreeRegressor,
    BaseDecisionTree as BaseDecisionTree,
    DecisionTreeClassifier as DecisionTreeClassifier,
)
from ..base import BaseEstimator
from joblib import effective_n_jobs as effective_n_jobs
from ..utils.metaestimators import _BaseComposition
from ..base import (
    clone as clone,
    is_classifier as is_classifier,
    is_regressor as is_regressor,
    MetaEstimatorMixin,
)
from .._typing import Int
from ..utils import Bunch, deprecated, check_random_state as check_random_state

_BaseHeterogeneousEnsemble_Self = TypeVar(
    "_BaseHeterogeneousEnsemble_Self", bound="_BaseHeterogeneousEnsemble"
)

import warnings

import numpy as np


class BaseEnsemble(MetaEstimatorMixin, BaseEstimator, metaclass=ABCMeta):
    estimators_: list[BaseEstimator] = ...

    # overwrite _required_parameters from MetaEstimatorMixin
    _required_parameters: ClassVar[List[str]] = ...

    @abstractmethod
    def __init__(
        self,
        estimator: Any = None,
        *,
        n_estimators: Int = 10,
        estimator_params: Sequence[str] = ...,
        base_estimator: Any = "deprecated",
    ) -> None:
        ...

    # TODO(1.4): remove
    # mypy error: Decorated property not supported
    @deprecated(  # type: ignore
        "Attribute `base_estimator_` was deprecated in version 1.2 and will be removed "
        "in 1.4. Use `estimator_` instead."
    )
    @property
    def base_estimator_(self) -> BaseEstimator:
        ...

    # TODO(1.4): remove
    @property
    def estimator_(self) -> BaseEstimator:
        ...

    def __len__(self) -> int:
        ...

    def __getitem__(self, index):
        ...

    def __iter__(self):
        ...


class _BaseHeterogeneousEnsemble(
    MetaEstimatorMixin, _BaseComposition, metaclass=ABCMeta
):
    estimators_: list[BaseEstimator] = ...

    _required_parameters: ClassVar[list] = ...

    @property
    def named_estimators(self) -> Bunch:
        ...

    @abstractmethod
    def __init__(self, estimators: list[tuple[str, BaseEstimator]]) -> None:
        ...

    def set_params(
        self: _BaseHeterogeneousEnsemble_Self, **params
    ) -> _BaseHeterogeneousEnsemble_Self:
        ...

    def get_params(self, deep: bool = True) -> dict:
        ...
