# coding=utf8

# Authors: Clay Woolam <clay@woolam.org>
#          Utkarsh Upadhyay <mail@musicallyut.in>
# License: BSD
from abc import ABCMeta, abstractmethod

import warnings
import numpy as np
from scipy import sparse
from scipy.sparse import csgraph

from ..base import BaseEstimator, ClassifierMixin
from ..metrics.pairwise import rbf_kernel
from ..neighbors import NearestNeighbors
from ..utils.extmath import safe_sparse_dot
from ..utils.multiclass import check_classification_targets
from ..utils.validation import check_is_fitted
from ..exceptions import ConvergenceWarning
from numpy import ndarray
from scipy.sparse._coo import coo_matrix
from scipy.sparse._csr import csr_matrix
from typing import Optional, Union

class BaseLabelPropagation(ClassifierMixin, BaseEstimator, metaclass=ABCMeta):
    def __init__(
        self,
        kernel: str = "rbf",
        *,
        gamma=20,
        n_neighbors=7,
        alpha=1,
        max_iter=30,
        tol=1e-3,
        n_jobs=None,
    ) -> None: ...
    def _get_kernel(self, X: ndarray, y: Optional[ndarray] = None) -> Union[ndarray, csr_matrix]: ...
    @abstractmethod
    def _build_graph(self): ...
    def predict(self, X: ndarray) -> ndarray: ...
    def predict_proba(self, X: ndarray) -> ndarray: ...
    def fit(self, X: ndarray, y: ndarray) -> "LabelSpreading": ...

class LabelPropagation(BaseLabelPropagation):

    _variant: str = ...

    def __init__(
        self,
        kernel="rbf",
        *,
        gamma=20,
        n_neighbors=7,
        max_iter=1000,
        tol=1e-3,
        n_jobs=None,
    ): ...
    def _build_graph(self): ...
    def fit(self, X, y): ...

class LabelSpreading(BaseLabelPropagation):

    _variant: str = ...

    def __init__(
        self,
        kernel: str = "rbf",
        *,
        gamma=20,
        n_neighbors=7,
        alpha=0.2,
        max_iter=30,
        tol=1e-3,
        n_jobs=None,
    ) -> None: ...
    def _build_graph(self) -> Union[ndarray, coo_matrix]: ...
