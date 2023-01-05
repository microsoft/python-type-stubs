from numpy import ndarray
from typing import Any
from numpy.typing import NDArray, ArrayLike

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Olivier Grisel <olivier.grisel@ensta.org>
#         Mathieu Blondel <mathieu@mblondel.org>
#         Denis A. Engemann <denis-alexander.engemann@inria.fr>
#         Kyle Kastner <kastnerkyle@gmail.com>
#
# License: BSD 3 clause

import numpy as np
from scipy import linalg

from ..base import BaseEstimator, TransformerMixin, _ClassNamePrefixFeaturesOutMixin
from ..utils.validation import check_is_fitted
from abc import ABCMeta, abstractmethod

class _BasePCA(_ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator, metaclass=ABCMeta):
    def get_covariance(self) -> NDArray: ...
    def get_precision(self) -> NDArray: ...
    @abstractmethod
    def fit(self, X: ArrayLike, y=None) -> Any: ...
    def transform(self, X: ArrayLike) -> ArrayLike: ...
    def inverse_transform(self, X: ArrayLike) -> ArrayLike: ...
    @property
    def _n_features_out(self): ...
