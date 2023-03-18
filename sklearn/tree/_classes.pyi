from typing import ClassVar, Literal, Mapping, Sequence, TypeVar
from numpy.random import RandomState
from scipy.sparse import issparse as issparse, spmatrix
from ..utils._bunch import Bunch
from ._criterion import Criterion as Criterion
from ..utils.validation import check_is_fitted as check_is_fitted
from abc import ABCMeta, abstractmethod
from ._splitter import Splitter as Splitter
from ..utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from numpy import ndarray
from numbers import Integral as Integral, Real as Real
from ..base import (
    BaseEstimator,
    ClassifierMixin,
    clone as clone,
    RegressorMixin,
    is_classifier as is_classifier,
    MultiOutputMixin,
)
from ..utils import (
    check_random_state as check_random_state,
    compute_sample_weight as compute_sample_weight,
)
from ..utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from math import ceil as ceil
from .._typing import MatrixLike, ArrayLike, Int, Float
from ._tree import (
    DepthFirstTreeBuilder as DepthFirstTreeBuilder,
    BestFirstTreeBuilder as BestFirstTreeBuilder,
    Tree,
    ccp_pruning_path as ccp_pruning_path,
)

DecisionTreeRegressor_Self = TypeVar(
    "DecisionTreeRegressor_Self", bound="DecisionTreeRegressor"
)


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

import numpy as np

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
CRITERIA_REG: dict = ...

DENSE_SPLITTERS: dict = ...

SPARSE_SPLITTERS: dict = ...

# =============================================================================
# Base decision tree
# =============================================================================


class BaseDecisionTree(MultiOutputMixin, BaseEstimator, metaclass=ABCMeta):

    _parameter_constraints: ClassVar[dict] = ...

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
        ccp_alpha: float = 0.0,
    ) -> None:
        ...

    def get_depth(self) -> int:
        ...

    def get_n_leaves(self) -> int:
        ...

    def fit(
        self,
        X,
        y: ndarray,
        sample_weight: None | ndarray = None,
        check_input: bool = True,
    ):
        ...

    def predict(self, X: MatrixLike | ArrayLike, check_input: bool = True) -> ndarray:
        ...

    def apply(self, X: MatrixLike | ArrayLike, check_input: bool = True) -> ArrayLike:
        ...

    def decision_path(
        self, X: MatrixLike | ArrayLike, check_input: bool = True
    ) -> spmatrix:
        ...

    def cost_complexity_pruning_path(
        self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Bunch:
        ...

    @property
    def feature_importances_(self) -> ndarray:
        ...


# =============================================================================
# Public estimators
# =============================================================================


class DecisionTreeClassifier(ClassifierMixin, BaseDecisionTree):
    tree_: Tree = ...
    n_outputs_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_classes_: int | list[int] = ...
    max_features_: int = ...
    feature_importances_: ndarray = ...
    classes_: ndarray | list[ndarray] = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        criterion: Literal["gini", "entropy", "log_loss", "gini"] = "gini",
        splitter: Literal["best", "random", "best"] = "best",
        max_depth: None | Int = None,
        min_samples_split: float | int = 2,
        min_samples_leaf: float | int = 1,
        min_weight_fraction_leaf: Float = 0.0,
        max_features: float | None | Literal["auto", "sqrt", "log2"] | int = None,
        random_state: RandomState | None | Int = None,
        max_leaf_nodes: None | Int = None,
        min_impurity_decrease: Float = 0.0,
        class_weight: None | Mapping | str | Sequence[Mapping] = None,
        ccp_alpha: float = 0.0,
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
        check_input: bool = True,
    ) -> DecisionTreeClassifier | ExtraTreeClassifier:
        ...

    def predict_proba(
        self, X: MatrixLike | ArrayLike, check_input: bool = True
    ) -> ndarray | list[ndarray]:
        ...

    def predict_log_proba(self, X: MatrixLike | ArrayLike) -> ndarray | list[ndarray]:
        ...


class DecisionTreeRegressor(RegressorMixin, BaseDecisionTree):
    tree_: Tree = ...
    n_outputs_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    max_features_: int = ...
    feature_importances_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        criterion: Literal[
            "squared_error",
            "friedman_mse",
            "absolute_error",
            "poisson",
            "squared_error",
        ] = "squared_error",
        splitter: Literal["best", "random", "best"] = "best",
        max_depth: None | Int = None,
        min_samples_split: float | int = 2,
        min_samples_leaf: float | int = 1,
        min_weight_fraction_leaf: Float = 0.0,
        max_features: float | None | Literal["auto", "sqrt", "log2"] | int = None,
        random_state: RandomState | None | Int = None,
        max_leaf_nodes: None | Int = None,
        min_impurity_decrease: Float = 0.0,
        ccp_alpha: float = 0.0,
    ) -> None:
        ...

    def fit(
        self: DecisionTreeRegressor_Self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
        check_input: bool = True,
    ) -> DecisionTreeRegressor_Self:
        ...


class ExtraTreeClassifier(DecisionTreeClassifier):
    tree_: Tree = ...
    n_outputs_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    feature_importances_: ndarray = ...
    n_classes_: int | list[int] = ...
    max_features_: int = ...
    classes_: ndarray | list[ndarray] = ...

    def __init__(
        self,
        *,
        criterion: Literal["gini", "entropy", "log_loss", "gini"] = "gini",
        splitter: Literal["random", "best", "random"] = "random",
        max_depth: None | Int = None,
        min_samples_split: float | int = 2,
        min_samples_leaf: float | int = 1,
        min_weight_fraction_leaf: Float = 0.0,
        max_features: float
        | None
        | int
        | Literal["auto", "sqrt", "log2", "sqrt"] = "sqrt",
        random_state: RandomState | None | Int = None,
        max_leaf_nodes: None | Int = None,
        min_impurity_decrease: Float = 0.0,
        class_weight: None | Mapping | str | Sequence[Mapping] = None,
        ccp_alpha: float = 0.0,
    ) -> None:
        ...


class ExtraTreeRegressor(DecisionTreeRegressor):
    tree_: Tree = ...
    n_outputs_: int = ...
    feature_importances_: ndarray = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    max_features_: int = ...

    def __init__(
        self,
        *,
        criterion: Literal[
            "squared_error",
            "friedman_mse",
            "absolute_error",
            "poisson",
            "squared_error",
        ] = "squared_error",
        splitter: Literal["random", "best", "random"] = "random",
        max_depth: None | Int = None,
        min_samples_split: float | int = 2,
        min_samples_leaf: float | int = 1,
        min_weight_fraction_leaf: Float = 0.0,
        max_features: float | None | Literal["auto", "sqrt", "log2"] | int = 1.0,
        random_state: RandomState | None | Int = None,
        min_impurity_decrease: Float = 0.0,
        max_leaf_nodes: None | Int = None,
        ccp_alpha: float = 0.0,
    ) -> None:
        ...
