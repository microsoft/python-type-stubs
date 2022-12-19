from numpy import ndarray
from numpy.typing import ArrayLike, NDArray

# Authors: G. Varoquaux, A. Gramfort, L. Buitinck, J. Nothman
# License: BSD 3 clause

import warnings
from abc import ABCMeta, abstractmethod
from operator import attrgetter

import numpy as np
from scipy.sparse import issparse, csc_matrix

from ..base import TransformerMixin
from ..cross_decomposition._pls import _PLS
from ..utils import (
    check_array,
    safe_mask,
    safe_sqr,
)
from ..utils._tags import _safe_tags
from ..utils.validation import _check_feature_names_in
from sklearn.linear_model._logistic import LogisticRegression
from sklearn.linear_model._ridge import RidgeCV
from sklearn.svm._classes import SVC
from typing import Optional, Union

class SelectorMixin(TransformerMixin, metaclass=ABCMeta):
    def get_support(self, indices: bool = False) -> ArrayLike: ...
    @abstractmethod
    def _get_support_mask(self): ...
    def transform(self, X: ArrayLike) -> ArrayLike: ...
    def _transform(self, X: ndarray) -> ndarray: ...
    def inverse_transform(self, X: ArrayLike) -> NDArray: ...
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...

def _get_feature_importances(
    estimator: Union[RidgeCV, LogisticRegression, SVC],
    getter: str,
    transform_func: Optional[str] = None,
    norm_order: int = 1,
) -> ndarray: ...
