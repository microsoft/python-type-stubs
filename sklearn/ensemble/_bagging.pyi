from numpy import int64, ndarray
from typing import Callable, Dict, List, Optional, Tuple, Union, Any
from numpy.typing import ArrayLike, NDArray

# Author: Gilles Louppe <g.louppe@gmail.com>
# License: BSD 3 clause

import itertools
import numbers
import numpy as np
from abc import ABCMeta, abstractmethod
from warnings import warn
from functools import partial

from ._base import BaseEnsemble, _partition_estimators
from ..base import ClassifierMixin, RegressorMixin
from ..metrics import r2_score, accuracy_score
from ..tree import DecisionTreeClassifier, DecisionTreeRegressor
from ..utils import check_random_state, column_or_1d, deprecated
from ..utils import indices_to_mask
from ..utils.metaestimators import available_if
from ..utils.multiclass import check_classification_targets
from ..utils.validation import has_fit_parameter, check_is_fitted, _check_sample_weight
from ..utils.fixes import delayed
from numpy.random.mtrand import RandomState
from sklearn.ensemble._iforest import IsolationForest
from sklearn.tree._classes import DecisionTreeRegressor, ExtraTreeRegressor

__all__ = ["BaggingClassifier", "BaggingRegressor"]

MAX_INT = ...

def _generate_indices(random_state: RandomState, bootstrap: bool, n_population: int, n_samples: int) -> ndarray: ...
def _generate_bagging_indices(
    random_state: int64,
    bootstrap_features: bool,
    bootstrap_samples: bool,
    n_features: int,
    n_samples: int,
    max_features: int,
    max_samples: int,
) -> Tuple[ndarray, ndarray]: ...
def _parallel_build_estimators(
    n_estimators: int,
    ensemble: Union[IsolationForest, BaggingRegressor],
    X: ndarray,
    y: ndarray,
    sample_weight: None,
    seeds: ndarray,
    total_n_estimators: int,
    verbose: int,
    check_input: bool,
) -> Union[Tuple[List[DecisionTreeRegressor], List[ndarray]], Tuple[List[ExtraTreeRegressor], List[ndarray]],]: ...
def _parallel_predict_proba(estimators, estimators_features, X, n_classes): ...
def _parallel_predict_log_proba(estimators, estimators_features, X, n_classes): ...
def _parallel_decision_function(estimators, estimators_features, X): ...
def _parallel_predict_regression(
    estimators: List[DecisionTreeRegressor],
    estimators_features: List[ndarray],
    X: ndarray,
) -> ndarray: ...
def _estimator_has(attr: str) -> Callable: ...

class BaseBagging(BaseEnsemble, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        base_estimator: Optional[Union[DecisionTreeRegressor, ExtraTreeRegressor]] = None,
        n_estimators: int = 10,
        *,
        max_samples=1.0,
        max_features=1.0,
        bootstrap=True,
        bootstrap_features=False,
        oob_score=False,
        warm_start=False,
        n_jobs=None,
        random_state=None,
        verbose=0,
    ) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> "BaggingRegressor": ...
    def _parallel_args(self) -> Dict[Any, Any]: ...
    def _fit(
        self,
        X: ndarray,
        y: ndarray,
        max_samples: Optional[Union[int, float]] = None,
        max_depth: Optional[int] = None,
        sample_weight: None = None,
        check_input: bool = True,
    ) -> Union[IsolationForest, BaggingRegressor]: ...
    @abstractmethod
    def _set_oob_score(self, X, y): ...
    def _validate_y(self, y: ndarray) -> ndarray: ...
    def _get_estimators_indices(self): ...
    @property
    def estimators_samples_(self): ...

    # TODO: Remove in 1.2
    # mypy error: Decorated property not supported
    @deprecated(  # type: ignore
        "Attribute `n_features_` was deprecated in version 1.0 and will be " "removed in 1.2. Use `n_features_in_` instead."
    )
    @property
    def n_features_(self): ...

class BaggingClassifier(ClassifierMixin, BaseBagging):
    def __init__(
        self,
        base_estimator: Any = None,
        n_estimators: int = 10,
        *,
        max_samples: int | float = 1.0,
        max_features: int | float = 1.0,
        bootstrap: bool = True,
        bootstrap_features: bool = False,
        oob_score: bool = False,
        warm_start: bool = False,
        n_jobs: int | None = None,
        random_state: int | RandomState | None = None,
        verbose: int = 0,
    ): ...
    def _validate_estimator(self): ...
    def _set_oob_score(self, X, y): ...
    def _validate_y(self, y): ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    def predict_proba(self, X: NDArray | ArrayLike) -> np.ndarray: ...
    def predict_log_proba(self, X: NDArray | ArrayLike) -> np.ndarray: ...
    @available_if(_estimator_has("decision_function"))
    def decision_function(self, X: NDArray | ArrayLike) -> np.ndarray: ...

class BaggingRegressor(RegressorMixin, BaseBagging):
    def __init__(
        self,
        base_estimator: Optional[DecisionTreeRegressor] = None,
        n_estimators: int = 10,
        *,
        max_samples: int | float = 1.0,
        max_features: int | float = 1.0,
        bootstrap: bool = True,
        bootstrap_features: bool = False,
        oob_score: bool = False,
        warm_start: bool = False,
        n_jobs: int | None = None,
        random_state: int | RandomState | None = None,
        verbose: int = 0,
    ) -> None: ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    def _validate_estimator(self) -> None: ...
    def _set_oob_score(self, X, y): ...
