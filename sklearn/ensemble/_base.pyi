from typing import Dict, Optional, Tuple, Union, Any, Sequence, Mapping
from sklearn.utils import Bunch
from numpy.typing import ArrayLike

# Authors: Gilles Louppe
# License: BSD 3 clause

from abc import ABCMeta, abstractmethod
import numbers
from typing import List

import numpy as np

from ..base import clone
from ..base import is_classifier, is_regressor
from ..base import BaseEstimator
from ..base import MetaEstimatorMixin
from ..tree import (
    DecisionTreeRegressor,
    ExtraTreeRegressor,
    BaseDecisionTree,
    DecisionTreeClassifier,
)
from ..utils import Bunch, _print_elapsed_time
from ..utils import check_random_state
from ..utils.metaestimators import _BaseComposition
from numpy import int64, ndarray
from numpy.random import RandomState
from sklearn.base import BaseEstimator
from sklearn.ensemble._forest import RandomForestClassifier, RandomForestRegressor
from sklearn.ensemble._gb import GradientBoostingRegressor
from sklearn.linear_model._base import LinearRegression
from sklearn.linear_model._logistic import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors._classification import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm._classes import SVC
from sklearn.tree._classes import (
    DecisionTreeClassifier,
    DecisionTreeRegressor,
    ExtraTreeClassifier,
    ExtraTreeRegressor,
)

def _fit_single_estimator(
    estimator: BaseEstimator,
    X: ndarray,
    y: ndarray,
    sample_weight: None = None,
    message_clsname: Optional[str] = None,
    message: None = None,
) -> BaseEstimator: ...
def _set_random_states(
    estimator: Union[
        DecisionTreeRegressor,
        DecisionTreeClassifier,
        ExtraTreeRegressor,
        ExtraTreeClassifier,
    ],
    random_state: Optional[Union[int64, RandomState]] = None,
) -> None: ...

class BaseEnsemble(MetaEstimatorMixin, BaseEstimator, metaclass=ABCMeta):

    # overwrite _required_parameters from MetaEstimatorMixin
    _required_parameters: List[str] = ...

    @abstractmethod
    def __init__(
        self,
        base_estimator: Optional[
            Union[
                ExtraTreeRegressor,
                ExtraTreeClassifier,
                DecisionTreeRegressor,
                DecisionTreeClassifier,
            ]
        ],
        *,
        n_estimators: int = 10,
        estimator_params: ArrayLike = ...,
    ) -> None: ...
    def _validate_estimator(
        self,
        default: Optional[Union[DecisionTreeRegressor, DecisionTreeClassifier]] = None,
    ) -> None: ...
    def _make_estimator(
        self,
        append: bool = True,
        random_state: Optional[Union[int64, RandomState]] = None,
    ) -> Union[DecisionTreeRegressor, DecisionTreeClassifier, ExtraTreeRegressor, ExtraTreeClassifier,]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index): ...
    def __iter__(self): ...

def _partition_estimators(n_estimators: int, n_jobs: Optional[int]) -> Tuple[int, List[int], List[int]]: ...

class _BaseHeterogeneousEnsemble(MetaEstimatorMixin, _BaseComposition, metaclass=ABCMeta):

    _required_parameters: list = ...

    @property
    def named_estimators(self) -> Bunch: ...
    @abstractmethod
    def __init__(self, estimators: Sequence[tuple[str, BaseEstimator]]) -> None: ...
    def _validate_estimators(
        self,
    ) -> Union[
        Tuple[
            Tuple[str, str, str],
            Tuple[DecisionTreeClassifier, KNeighborsClassifier, SVC],
        ],
        Tuple[Tuple[str, str], Tuple[RandomForestClassifier, Pipeline]],
        Tuple[
            Tuple[str, str, str],
            Tuple[GradientBoostingRegressor, RandomForestRegressor, LinearRegression],
        ],
        Tuple[
            Tuple[str, str, str],
            Tuple[LogisticRegression, RandomForestClassifier, GaussianNB],
        ],
    ]: ...
    def set_params(self, **params) -> Any: ...
    def get_params(self, deep: bool = True) -> Mapping: ...
