from abc import ABCMeta, abstractmethod as abstractmethod
from numbers import Integral as Integral, Real as Real
from typing import Callable, ClassVar, Literal, TypeVar

from numpy import ndarray
from scipy import sparse as sparse
from scipy.sparse import csgraph as csgraph

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, ClassifierMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..metrics.pairwise import rbf_kernel as rbf_kernel
from ..neighbors import NearestNeighbors as NearestNeighbors
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from ..utils.multiclass import check_classification_targets as check_classification_targets
from ..utils.validation import check_is_fitted as check_is_fitted

BaseLabelPropagation_Self = TypeVar("BaseLabelPropagation_Self", bound=BaseLabelPropagation)
LabelPropagation_Self = TypeVar("LabelPropagation_Self", bound=LabelPropagation)

# coding=utf8

import warnings

import numpy as np

class BaseLabelPropagation(ClassifierMixin, BaseEstimator, metaclass=ABCMeta):
    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        kernel: Callable | Literal["rbf", "knn"] = "rbf",
        *,
        gamma: Float = 20,
        n_neighbors: Int = 7,
        alpha: Float = 1,
        max_iter: Int = 30,
        tol: Float = 1e-3,
        n_jobs=None,
    ) -> None: ...
    def predict(self, X: MatrixLike) -> ndarray: ...
    def predict_proba(self, X: MatrixLike) -> ndarray: ...
    def fit(self: BaseLabelPropagation_Self, X: MatrixLike, y: ArrayLike) -> BaseLabelPropagation_Self | LabelSpreading: ...

class LabelPropagation(BaseLabelPropagation):
    n_iter_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    transduction_: ndarray = ...
    label_distributions_: ndarray = ...
    classes_: ndarray = ...
    X_: ndarray = ...

    _variant: ClassVar[str] = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        kernel: Callable | Literal["knn", "rbf"] = "rbf",
        *,
        gamma: Float = 20,
        n_neighbors: Int = 7,
        max_iter: Int = 1000,
        tol: float = 1e-3,
        n_jobs: None | Int = None,
    ) -> None: ...
    def fit(self: LabelPropagation_Self, X: MatrixLike, y: ArrayLike) -> LabelPropagation_Self: ...

class LabelSpreading(BaseLabelPropagation):
    n_iter_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    transduction_: ndarray = ...
    label_distributions_: ndarray = ...
    classes_: ndarray = ...
    X_: ndarray = ...

    _variant: ClassVar[str] = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        kernel: Callable | Literal["rbf", "knn"] = "rbf",
        *,
        gamma: Float = 20,
        n_neighbors: Int = 7,
        alpha: Float = 0.2,
        max_iter: Int = 30,
        tol: Float = 1e-3,
        n_jobs: None | Int = None,
    ) -> None: ...
