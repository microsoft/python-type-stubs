from abc import ABCMeta, abstractmethod
from typing import TypeVar

from numpy import ndarray
from scipy import linalg as linalg

from .._typing import MatrixLike
from ..base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin
from ..utils.validation import check_is_fitted as check_is_fitted

_BasePCA_Self = TypeVar("_BasePCA_Self", bound=_BasePCA)

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Olivier Grisel <olivier.grisel@ensta.org>
#         Mathieu Blondel <mathieu@mblondel.org>
#         Denis A. Engemann <denis-alexander.engemann@inria.fr>
#         Kyle Kastner <kastnerkyle@gmail.com>
#
# License: BSD 3 clause

import numpy as np

class _BasePCA(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator, metaclass=ABCMeta):
    def get_covariance(self) -> ndarray: ...
    def get_precision(self) -> ndarray: ...
    @abstractmethod
    def fit(self: _BasePCA_Self, X: MatrixLike, y=None) -> _BasePCA_Self: ...
    def transform(self, X: MatrixLike) -> ndarray: ...
    def inverse_transform(self, X: MatrixLike) -> ndarray: ...
