from typing import Any, Sequence, List
from ..utils._bunch import Bunch
from .._typing import Int, Estimator
from ..base import (
    clone as clone,
    is_classifier as is_classifier,
    is_regressor as is_regressor,
    BaseEstimator,
    MetaEstimatorMixin,
)
from joblib import effective_n_jobs as effective_n_jobs
from ..tree import (
    DecisionTreeRegressor as DecisionTreeRegressor,
    BaseDecisionTree as BaseDecisionTree,
    DecisionTreeClassifier as DecisionTreeClassifier,
)
from abc import ABCMeta, abstractmethod
from ..utils import deprecated, check_random_state as check_random_state
from ..utils.metaestimators import _BaseComposition
import warnings

import numpy as np


class BaseEnsemble(MetaEstimatorMixin, BaseEstimator, metaclass=ABCMeta):

    # overwrite _required_parameters from MetaEstimatorMixin
    _required_parameters: List[str] = ...

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
    def base_estimator_(self):
        ...

    # TODO(1.4): remove
    @property
    def estimator_(self):
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

    _required_parameters: list = ...

    @property
    def named_estimators(self) -> Bunch:
        ...

    @abstractmethod
    def __init__(self, estimators: list[tuple[str, Estimator]]) -> None:
        ...

    def set_params(self, **params) -> Any:
        ...

    def get_params(self, deep: bool = True) -> dict:
        ...
