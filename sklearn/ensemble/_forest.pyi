from numpy import ndarray
from typing import Dict, Optional, Tuple, Union, Any, Literal
from numpy.typing import ArrayLike, NDArray

# Authors: Gilles Louppe <g.louppe@gmail.com>
#          Brian Holt <bdholt1@gmail.com>
#          Joly Arnaud <arnaud.v.joly@gmail.com>
#          Fares Hedayati <fares.hedayati@gmail.com>
#
# License: BSD 3 clause

import numbers
from warnings import catch_warnings, simplefilter, warn
import threading

from abc import ABCMeta, abstractmethod
import numpy as np
from numpy.random import RandomState
from scipy.sparse import issparse
from scipy.sparse import hstack as sparse_hstack
from typing import Sequence

from ..base import is_classifier
from ..base import ClassifierMixin, MultiOutputMixin, RegressorMixin, TransformerMixin

from ..metrics import accuracy_score, r2_score
from ..preprocessing import OneHotEncoder
from ..tree import (
    DecisionTreeClassifier,
    DecisionTreeRegressor,
    ExtraTreeClassifier,
    ExtraTreeRegressor,
)
from ..utils import check_random_state, compute_sample_weight, deprecated
from ..exceptions import DataConversionWarning
from ._base import BaseEnsemble, _partition_estimators
from ..utils.fixes import delayed
from ..utils.multiclass import check_classification_targets, type_of_target
from ..utils.validation import (
    check_is_fitted,
    _check_sample_weight,
    _check_feature_names_in,
)
from ..utils.validation import _num_samples
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from scipy.sparse._csc import csc_matrix
from scipy.sparse._csr import csr_matrix
from sklearn.tree._classes import (
    DecisionTreeClassifier,
    DecisionTreeRegressor,
    ExtraTreeClassifier,
    ExtraTreeRegressor,
)

__all__ = [
    "RandomForestClassifier",
    "RandomForestRegressor",
    "ExtraTreesClassifier",
    "ExtraTreesRegressor",
    "RandomTreesEmbedding",
]

MAX_INT = ...

def _get_n_samples_bootstrap(n_samples: int, max_samples: Optional[float]) -> int: ...
def _generate_sample_indices(random_state: int, n_samples: int, n_samples_bootstrap: int) -> ndarray: ...
def _generate_unsampled_indices(random_state: int, n_samples: int, n_samples_bootstrap: int) -> ndarray: ...
def _parallel_build_trees(
    tree: Union[
        DecisionTreeRegressor,
        DecisionTreeClassifier,
        ExtraTreeRegressor,
        ExtraTreeClassifier,
    ],
    bootstrap: bool,
    X: Union[csc_matrix, ndarray],
    y: ndarray,
    sample_weight: None,
    tree_idx: int,
    n_trees: int,
    verbose: int = 0,
    class_weight: None = None,
    n_samples_bootstrap: Optional[int] = None,
) -> Union[DecisionTreeRegressor, DecisionTreeClassifier, ExtraTreeRegressor, ExtraTreeClassifier,]: ...

class BaseForest(MultiOutputMixin, BaseEnsemble, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        base_estimator: Union[
            DecisionTreeRegressor,
            DecisionTreeClassifier,
            ExtraTreeRegressor,
            ExtraTreeClassifier,
        ],
        n_estimators: int = 100,
        *,
        estimator_params=...,
        bootstrap=False,
        oob_score=False,
        n_jobs=None,
        random_state=None,
        verbose=0,
        warm_start=False,
        class_weight=None,
        max_samples=None,
    ) -> None: ...
    def apply(self, X: NDArray | ArrayLike) -> np.ndarray: ...
    def decision_path(self, X: NDArray | ArrayLike) -> tuple[NDArray, np.ndarray]: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> Union[
        RandomForestRegressor,
        ExtraTreesClassifier,
        ExtraTreesRegressor,
        RandomForestClassifier,
        RandomTreesEmbedding,
    ]: ...
    @abstractmethod
    def _set_oob_score_and_attributes(self, X, y): ...
    def _compute_oob_predictions(self, X: ndarray, y: ndarray) -> ndarray: ...
    def _validate_y_class_weight(self, y: ndarray) -> Tuple[ndarray, None]: ...
    def _validate_X_predict(self, X: Union[ndarray, csr_matrix]) -> Union[ndarray, csr_matrix]: ...
    @property
    def feature_importances_(self) -> NDArray: ...

    # TODO: Remove in 1.2
    # mypy error: Decorated property not supported
    @deprecated(  # type: ignore
        "Attribute `n_features_` was deprecated in version 1.0 and will be " "removed in 1.2. Use `n_features_in_` instead."
    )
    @property
    def n_features_(self): ...

def _accumulate_prediction(predict, X, out, lock): ...

class ForestClassifier(ClassifierMixin, BaseForest, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        base_estimator: Union[DecisionTreeClassifier, ExtraTreeClassifier],
        n_estimators: int = 100,
        *,
        estimator_params=...,
        bootstrap=False,
        oob_score=False,
        n_jobs=None,
        random_state=None,
        verbose=0,
        warm_start=False,
        class_weight=None,
        max_samples=None,
    ) -> None: ...
    @staticmethod
    def _get_oob_predictions(tree: DecisionTreeClassifier, X: ndarray) -> ndarray: ...
    def _set_oob_score_and_attributes(self, X: ndarray, y: ndarray) -> None: ...
    def _validate_y_class_weight(self, y: ndarray) -> Tuple[ndarray, None]: ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    def predict_proba(self, X: NDArray | ArrayLike) -> NDArray | list[ArrayLike]: ...
    def predict_log_proba(self, X: NDArray | ArrayLike) -> NDArray | list[ArrayLike]: ...
    def _more_tags(self) -> Dict[str, bool]: ...

class ForestRegressor(RegressorMixin, BaseForest, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        base_estimator: Union[DecisionTreeRegressor, ExtraTreeRegressor],
        n_estimators: int = 100,
        *,
        estimator_params=...,
        bootstrap=False,
        oob_score=False,
        n_jobs=None,
        random_state=None,
        verbose=0,
        warm_start=False,
        max_samples=None,
    ) -> None: ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    @staticmethod
    def _get_oob_predictions(tree, X): ...
    def _set_oob_score_and_attributes(self, X, y): ...
    def _compute_partial_dependence_recursion(self, grid, target_features): ...
    def _more_tags(self) -> Dict[str, bool]: ...

class RandomForestClassifier(ForestClassifier):
    def __init__(
        self,
        n_estimators: int = 100,
        *,
        criterion: Literal["gini", "entropy", "log_loss"] = "gini",
        max_depth: int | None = None,
        min_samples_split: int | float = 2,
        min_samples_leaf: int | float = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_features: None | Literal["sqrt", "log2"] | int | float = "sqrt",
        max_leaf_nodes: int | None = None,
        min_impurity_decrease: float = 0.0,
        bootstrap: bool = True,
        oob_score: bool = False,
        n_jobs: int | None = None,
        random_state: int | RandomState | None = None,
        verbose: int = 0,
        warm_start: bool = False,
        class_weight: Literal["balanced", "balanced_subsample"] | dict | Sequence[dict] | None = None,
        ccp_alpha: float = 0.0,
        max_samples: int | float | None = None,
    ) -> None: ...

class RandomForestRegressor(ForestRegressor):
    def __init__(
        self,
        n_estimators: int = 100,
        *,
        criterion: Literal["squared_error", "absolute_error", "poisson"] = "squared_error",
        max_depth: int | None = None,
        min_samples_split: int | float = 2,
        min_samples_leaf: int | float = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_features: None | Literal["sqrt", "log2"] | int | float = 1.0,
        max_leaf_nodes: int | None = None,
        min_impurity_decrease: float = 0.0,
        bootstrap: bool = True,
        oob_score: bool = False,
        n_jobs: int | None = None,
        random_state: int | RandomState | None = None,
        verbose: int = 0,
        warm_start: bool = False,
        ccp_alpha: float = 0.0,
        max_samples: int | float | None = None,
    ) -> None: ...

class ExtraTreesClassifier(ForestClassifier):
    def __init__(
        self,
        n_estimators: int = 100,
        *,
        criterion: Literal["gini", "entropy", "log_loss"] = "gini",
        max_depth: int | None = None,
        min_samples_split: int | float = 2,
        min_samples_leaf: int | float = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_features: None | Literal["sqrt", "log2"] | int | float = "sqrt",
        max_leaf_nodes: int | None = None,
        min_impurity_decrease: float = 0.0,
        bootstrap: bool = False,
        oob_score: bool = False,
        n_jobs: int | None = None,
        random_state: int | RandomState | None = None,
        verbose: int = 0,
        warm_start: bool = False,
        class_weight: Literal["balanced", "balanced_subsample"] | dict | Sequence[dict] | None = None,
        ccp_alpha: float = 0.0,
        max_samples: int | float | None = None,
    ) -> None: ...

class ExtraTreesRegressor(ForestRegressor):
    def __init__(
        self,
        n_estimators: int = 100,
        *,
        criterion: Literal["squared_error", "absolute_error"] = "squared_error",
        max_depth: int | None = None,
        min_samples_split: int | float = 2,
        min_samples_leaf: int | float = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_features: None | Literal["sqrt", "log2"] | int | float = 1.0,
        max_leaf_nodes: int | None = None,
        min_impurity_decrease: float = 0.0,
        bootstrap: bool = False,
        oob_score: bool = False,
        n_jobs: int | None = None,
        random_state: int | RandomState | None = None,
        verbose: int = 0,
        warm_start: bool = False,
        ccp_alpha: float = 0.0,
        max_samples: int | float | None = None,
    ) -> None: ...

class RandomTreesEmbedding(TransformerMixin, BaseForest):

    criterion: str = ...
    max_features: int = ...

    def __init__(
        self,
        n_estimators: int = 100,
        *,
        max_depth: int = 5,
        min_samples_split: int | float = 2,
        min_samples_leaf: int | float = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_leaf_nodes: int | None = None,
        min_impurity_decrease: float = 0.0,
        sparse_output: bool = True,
        n_jobs: int | None = None,
        random_state: int | RandomState | None = None,
        verbose: int = 0,
        warm_start: bool = False,
    ) -> None: ...
    def _set_oob_score_and_attributes(self, X, y): ...
    def fit(self, X: NDArray | ArrayLike, y=None, sample_weight: ArrayLike | None = None) -> Any: ...
    def fit_transform(
        self,
        X: NDArray | ArrayLike,
        y: Optional[ndarray] = None,
        sample_weight: ArrayLike | None = None,
    ) -> NDArray: ...
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...
    def transform(self, X: NDArray | ArrayLike) -> NDArray: ...
