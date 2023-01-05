from sklearn.tree._classes import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.utils import Bunch
from numpy.typing import ArrayLike, NDArray
from numpy import ndarray
from numpy.random import RandomState
from typing import Optional, Union, Literal, Sequence

# Authors: Gilles Louppe <g.louppe@gmail.com>
#          Peter Prettenhofer <peter.prettenhofer@gmail.com>
#          Brian Holt <bdholt1@gmail.com>
#          Noel Dawe <noel@dawe.me>
#          Satrajit Gosh <satrajit.ghosh@gmail.com>
#          Joly Arnaud <arnaud.v.joly@gmail.com>
#          Fares Hedayati <fares.hedayati@gmail.com>
#          Nelson Liu <nelson@nelsonliu.me>
#
# License: BSD 3 clause

import numbers
import warnings
import copy
from abc import ABCMeta
from abc import abstractmethod
from math import ceil

import numpy as np
from scipy.sparse import issparse

from ..base import BaseEstimator
from ..base import ClassifierMixin
from ..base import clone
from ..base import RegressorMixin
from ..base import is_classifier
from ..base import MultiOutputMixin
from ..utils import Bunch
from ..utils import check_random_state
from ..utils import check_scalar
from ..utils.deprecation import deprecated
from ..utils.validation import _check_sample_weight
from ..utils import compute_sample_weight
from ..utils.multiclass import check_classification_targets
from ..utils.validation import check_is_fitted

import sklearn.utils._bunch
from pandas.core.frame import DataFrame
from scipy.sparse._csc import csc_matrix
from scipy.sparse._csr import csr_matrix

__all__ = [
    "DecisionTreeClassifier",
    "DecisionTreeRegressor",
    "ExtraTreeClassifier",
    "ExtraTreeRegressor",
]

# =============================================================================
# Types and constants
# =============================================================================

DTYPE = ...
DOUBLE = ...

CRITERIA_CLF: dict = ...
# TODO(1.2): Remove "mse" and "mae".
CRITERIA_REG: dict = ...

DENSE_SPLITTERS: dict = ...

SPARSE_SPLITTERS: dict = ...

# =============================================================================
# Base decision tree
# =============================================================================

class BaseDecisionTree(MultiOutputMixin, BaseEstimator, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        *,
        criterion,
        splitter,
        max_depth,
        min_samples_split,
        min_samples_leaf,
        min_weight_fraction_leaf,
        max_features,
        max_leaf_nodes,
        random_state,
        min_impurity_decrease,
        class_weight=None,
        ccp_alpha=0.0,
    ) -> None: ...
    def get_depth(self) -> int: ...
    def get_n_leaves(self) -> int: ...
    def fit(
        self,
        X: Union[DataFrame, ndarray, csr_matrix, csc_matrix],
        y: ndarray,
        sample_weight: Optional[ndarray] = None,
        check_input: bool = True,
    ) -> Union[DecisionTreeRegressor, DecisionTreeClassifier, ExtraTreeRegressor, ExtraTreeClassifier,]: ...
    def _validate_X_predict(self, X: Union[ndarray, csr_matrix], check_input: bool) -> Union[ndarray, csr_matrix]: ...
    def predict(self, X: NDArray | ArrayLike, check_input: bool = True) -> ArrayLike: ...
    def apply(self, X: NDArray | ArrayLike, check_input: bool = True) -> ArrayLike: ...
    def decision_path(self, X: NDArray | ArrayLike, check_input: bool = True) -> NDArray: ...
    def _prune_tree(self) -> None: ...
    def cost_complexity_pruning_path(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> Bunch: ...
    @property
    def feature_importances_(self) -> NDArray: ...

# =============================================================================
# Public estimators
# =============================================================================

class DecisionTreeClassifier(ClassifierMixin, BaseDecisionTree):
    def __init__(
        self,
        *,
        criterion: Literal["gini", "entropy", "log_loss"] = "gini",
        splitter: Literal["best", "random"] = "best",
        max_depth: int | None = None,
        min_samples_split: int | float = 2,
        min_samples_leaf: int | float = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_features: int | float | Literal["auto", "sqrt", "log2"] | None = None,
        random_state: int | RandomState | None = None,
        max_leaf_nodes: int | None = None,
        min_impurity_decrease: float = 0.0,
        class_weight: dict | Sequence[dict] | Literal["balanced"] | None = None,
        ccp_alpha: float = 0.0,
    ) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
        check_input: bool = True,
    ) -> DecisionTreeClassifier: ...
    def predict_proba(self, X: NDArray | ArrayLike, check_input: bool = True) -> NDArray | list[NDArray]: ...
    def predict_log_proba(self, X: NDArray | ArrayLike) -> NDArray | list[NDArray]: ...
    @deprecated(  # type: ignore
        "The attribute `n_features_` is deprecated in 1.0 and will be removed " "in 1.2. Use `n_features_in_` instead."
    )
    @property
    def n_features_(self): ...
    def _more_tags(self): ...

class DecisionTreeRegressor(RegressorMixin, BaseDecisionTree):
    def __init__(
        self,
        *,
        criterion: Literal["squared_error", "friedman_mse", "absolute_error", "poisson"] = "squared_error",
        splitter: Literal["best", "random"] = "best",
        max_depth: int | None = None,
        min_samples_split: int | float = 2,
        min_samples_leaf: int | float = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_features: int | float | Literal["auto", "sqrt", "log2"] | None = None,
        random_state: int | RandomState | None = None,
        max_leaf_nodes: int | None = None,
        min_impurity_decrease: float = 0.0,
        ccp_alpha: float = 0.0,
    ) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
        check_input: bool = True,
    ) -> DecisionTreeRegressor: ...
    def _compute_partial_dependence_recursion(self, grid: ndarray, target_features: ndarray) -> ndarray: ...
    @deprecated(  # type: ignore
        "The attribute `n_features_` is deprecated in 1.0 and will be removed " "in 1.2. Use `n_features_in_` instead."
    )
    @property
    def n_features_(self): ...

class ExtraTreeClassifier(DecisionTreeClassifier):
    def __init__(
        self,
        *,
        criterion: Literal["gini", "entropy", "log_loss"] = "gini",
        splitter: Literal["random", "best"] = "random",
        max_depth: int | None = None,
        min_samples_split: int | float = 2,
        min_samples_leaf: int | float = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_features: int | float | Literal["auto", "sqrt", "log2"] | None = "sqrt",
        random_state: int | RandomState | None = None,
        max_leaf_nodes: int | None = None,
        min_impurity_decrease: float = 0.0,
        class_weight: dict | Sequence[dict] | Literal["balanced"] | None = None,
        ccp_alpha: float = 0.0,
    ) -> None: ...

class ExtraTreeRegressor(DecisionTreeRegressor):
    def __init__(
        self,
        *,
        criterion: Literal["squared_error", "friedman_mse"] = "squared_error",
        splitter: Literal["random", "best"] = "random",
        max_depth: int | None = None,
        min_samples_split: int | float = 2,
        min_samples_leaf: int | float = 1,
        min_weight_fraction_leaf: float = 0.0,
        max_features: int | float | Literal["auto", "sqrt", "log2"] | None = 1.0,
        random_state: int | RandomState | None = None,
        min_impurity_decrease: float = 0.0,
        max_leaf_nodes: int | None = None,
        ccp_alpha: float = 0.0,
    ) -> None: ...
