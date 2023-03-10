from typing import Any, Callable, Literal
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from .._typing import Float, Int, MatrixLike, ArrayLike
from ..utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from scipy import sparse as sparse
from ..base import BaseEstimator, ClassifierMixin
from ..neighbors import NearestNeighbors as NearestNeighbors
from ..utils.validation import check_is_fitted as check_is_fitted
from abc import ABCMeta, abstractmethod as abstractmethod
from ..metrics.pairwise import rbf_kernel as rbf_kernel
from numpy import ndarray
from numbers import Integral as Integral, Real as Real
from scipy.sparse import csgraph as csgraph

# coding=utf8

import warnings
import numpy as np


class BaseLabelPropagation(ClassifierMixin, BaseEstimator, metaclass=ABCMeta):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        kernel: Callable | Literal["rbf", "knn", "rbf"] = "rbf",
        *,
        gamma: Float = 20,
        n_neighbors: Int = 7,
        alpha: Float = 1,
        max_iter: Int = 30,
        tol: Float = 1e-3,
        n_jobs=None,
    ) -> None:
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...

    def predict_proba(self, X: MatrixLike) -> ndarray:
        ...

    def fit(self, X: MatrixLike, y: ArrayLike) -> Any:
        ...


class LabelPropagation(BaseLabelPropagation):

    _variant: str = ...

    _parameter_constraints: dict = ...

    def __init__(
        self,
        kernel: Callable | Literal["knn", "rbf", "rbf"] = "rbf",
        *,
        gamma: Float = 20,
        n_neighbors: Int = 7,
        max_iter: Int = 1000,
        tol: float = 1e-3,
        n_jobs: None | Int = None,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: ArrayLike) -> Any:
        ...


class LabelSpreading(BaseLabelPropagation):

    _variant: str = ...

    _parameter_constraints: dict = ...

    def __init__(
        self,
        kernel: Callable | Literal["rbf", "knn", "rbf"] = "rbf",
        *,
        gamma: Float = 20,
        n_neighbors: Int = 7,
        alpha: Float = 0.2,
        max_iter: Int = 30,
        tol: Float = 1e-3,
        n_jobs: None | Int = None,
    ) -> None:
        ...
