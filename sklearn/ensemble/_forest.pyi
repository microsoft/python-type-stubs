from typing import Any, Literal, Mapping, Sequence
from .._typing import ArrayLike, MatrixLike, Int, Float
from ..preprocessing import OneHotEncoder as OneHotEncoder
from scipy.sparse import issparse as issparse, hstack as sparse_hstack, spmatrix
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from abc import ABCMeta, abstractmethod
from ._base import BaseEnsemble
from ..utils import (
    check_random_state as check_random_state,
    compute_sample_weight as compute_sample_weight,
)
from ..tree._classes import (
    DecisionTreeClassifier,
    DecisionTreeRegressor,
    ExtraTreeClassifier,
    ExtraTreeRegressor,
)
from ..metrics import accuracy_score as accuracy_score, r2_score as r2_score
from ..utils.validation import check_is_fitted as check_is_fitted
from ..tree._tree import DTYPE as DTYPE, DOUBLE as DOUBLE
from scipy.sparse._csr import csr_matrix
from numpy import ndarray
from warnings import (
    catch_warnings as catch_warnings,
    simplefilter as simplefilter,
    warn as warn,
)
from numpy.random import RandomState
from ..exceptions import DataConversionWarning as DataConversionWarning
from ..utils.multiclass import (
    check_classification_targets as check_classification_targets,
    type_of_target as type_of_target,
)
from ..base import (
    is_classifier as is_classifier,
    ClassifierMixin,
    MultiOutputMixin,
    RegressorMixin,
    TransformerMixin,
)
from ..tree import BaseDecisionTree as BaseDecisionTree
from numbers import Integral as Integral, Real as Real
from ..utils.parallel import delayed as delayed, Parallel as Parallel
import threading
import numpy as np


__all__ = [
    "RandomForestClassifier",
    "RandomForestRegressor",
    "ExtraTreesClassifier",
    "ExtraTreesRegressor",
    "RandomTreesEmbedding",
]

MAX_INT = ...


class BaseForest(MultiOutputMixin, BaseEnsemble, metaclass=ABCMeta):

    _parameter_constraints: dict = ...

    @abstractmethod
    def __init__(
        self,
        estimator,
        n_estimators: int = 100,
        *,
        estimator_params=...,
        bootstrap: bool = False,
        oob_score: bool = False,
        n_jobs=None,
        random_state=None,
        verbose: int = 0,
        warm_start: bool = False,
        class_weight=None,
        max_samples=None,
        base_estimator: str = "deprecated",
    ) -> None:
        ...

    def apply(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def decision_path(self, X: MatrixLike | ArrayLike) -> tuple[spmatrix, ndarray]:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    @property
    def feature_importances_(self) -> ndarray:
        ...


class ForestClassifier(ClassifierMixin, BaseForest, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        estimator: ExtraTreeClassifier | DecisionTreeClassifier,
        n_estimators: int = 100,
        *,
        estimator_params=...,
        bootstrap: bool = False,
        oob_score: bool = False,
        n_jobs=None,
        random_state=None,
        verbose: int = 0,
        warm_start: bool = False,
        class_weight=None,
        max_samples=None,
        base_estimator: str = "deprecated",
    ) -> None:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def predict_log_proba(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...


class ForestRegressor(RegressorMixin, BaseForest, metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        estimator: ExtraTreeRegressor | DecisionTreeRegressor,
        n_estimators: int = 100,
        *,
        estimator_params=...,
        bootstrap: bool = False,
        oob_score: bool = False,
        n_jobs=None,
        random_state=None,
        verbose: int = 0,
        warm_start: bool = False,
        max_samples=None,
        base_estimator: str = "deprecated",
    ) -> None:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...


class RandomForestClassifier(ForestClassifier):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_estimators: Int = 100,
        *,
        criterion: Literal["gini", "entropy", "log_loss", "gini"] = "gini",
        max_depth: None | Int = None,
        min_samples_split: int | float = 2,
        min_samples_leaf: int | float = 1,
        min_weight_fraction_leaf: Float = 0.0,
        max_features: int | float | Literal["sqrt", "log2", "sqrt"] = "sqrt",
        max_leaf_nodes: None | Int = None,
        min_impurity_decrease: Float = 0.0,
        bootstrap: bool = True,
        oob_score: bool = False,
        n_jobs: None | Int = None,
        random_state: RandomState | None | Int = None,
        verbose: Int = 0,
        warm_start: bool = False,
        class_weight: Literal["balanced", "balanced_subsample"]
        | Sequence[Mapping]
        | Mapping
        | None = None,
        ccp_alpha: float = 0.0,
        max_samples: int | float | None = None,
    ) -> None:
        ...


class RandomForestRegressor(ForestRegressor):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_estimators: Int = 100,
        *,
        criterion: Literal[
            "squared_error",
            "absolute_error",
            "friedman_mse",
            "poisson",
            "squared_error",
        ] = "squared_error",
        max_depth: None | Int = None,
        min_samples_split: int | float = 2,
        min_samples_leaf: int | float = 1,
        min_weight_fraction_leaf: Float = 0.0,
        max_features: Literal["sqrt", "log2"] | int | float = 1.0,
        max_leaf_nodes: None | Int = None,
        min_impurity_decrease: Float = 0.0,
        bootstrap: bool = True,
        oob_score: bool = False,
        n_jobs: None | Int = None,
        random_state: RandomState | None | Int = None,
        verbose: Int = 0,
        warm_start: bool = False,
        ccp_alpha: float = 0.0,
        max_samples: int | float | None = None,
    ) -> None:
        ...


class ExtraTreesClassifier(ForestClassifier):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_estimators: Int = 100,
        *,
        criterion: Literal["gini", "entropy", "log_loss", "gini"] = "gini",
        max_depth: None | Int = None,
        min_samples_split: int | float = 2,
        min_samples_leaf: int | float = 1,
        min_weight_fraction_leaf: Float = 0.0,
        max_features: int | float | Literal["sqrt", "log2", "sqrt"] = "sqrt",
        max_leaf_nodes: None | Int = None,
        min_impurity_decrease: Float = 0.0,
        bootstrap: bool = False,
        oob_score: bool = False,
        n_jobs: None | Int = None,
        random_state: RandomState | None | Int = None,
        verbose: Int = 0,
        warm_start: bool = False,
        class_weight: Literal["balanced", "balanced_subsample"]
        | Sequence[Mapping]
        | Mapping
        | None = None,
        ccp_alpha: float = 0.0,
        max_samples: int | float | None = None,
    ) -> None:
        ...


class ExtraTreesRegressor(ForestRegressor):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_estimators: Int = 100,
        *,
        criterion: Literal[
            "squared_error",
            "absolute_error",
            "friedman_mse",
            "poisson",
            "squared_error",
        ] = "squared_error",
        max_depth: None | Int = None,
        min_samples_split: int | float = 2,
        min_samples_leaf: int | float = 1,
        min_weight_fraction_leaf: Float = 0.0,
        max_features: Literal["sqrt", "log2"] | int | float = 1.0,
        max_leaf_nodes: None | Int = None,
        min_impurity_decrease: Float = 0.0,
        bootstrap: bool = False,
        oob_score: bool = False,
        n_jobs: None | Int = None,
        random_state: RandomState | None | Int = None,
        verbose: Int = 0,
        warm_start: bool = False,
        ccp_alpha: float = 0.0,
        max_samples: int | float | None = None,
    ) -> None:
        ...


class RandomTreesEmbedding(TransformerMixin, BaseForest):

    _parameter_constraints: dict = ...
    for param in ("max_features", "ccp_alpha", "splitter"):
        pass

    criterion: str = ...
    max_features: int = ...

    def __init__(
        self,
        n_estimators: Int = 100,
        *,
        max_depth: Int = 5,
        min_samples_split: int | float = 2,
        min_samples_leaf: int | float = 1,
        min_weight_fraction_leaf: Float = 0.0,
        max_leaf_nodes: None | Int = None,
        min_impurity_decrease: Float = 0.0,
        sparse_output: bool = True,
        n_jobs: None | Int = None,
        random_state: RandomState | None | Int = None,
        verbose: Int = 0,
        warm_start: bool = False,
    ) -> None:
        ...

    def fit(
        self,
        X: MatrixLike | ArrayLike,
        y: Any = None,
        sample_weight: None | ArrayLike = None,
    ) -> Any:
        ...

    def fit_transform(
        self,
        X: MatrixLike | ArrayLike,
        y: Any = None,
        sample_weight: None | ArrayLike = None,
    ) -> spmatrix | csr_matrix:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> spmatrix | csr_matrix:
        ...
