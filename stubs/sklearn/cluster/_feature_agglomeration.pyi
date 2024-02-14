import numpy as np
from numpy import ndarray
from scipy.sparse import issparse as issparse

from .._typing import ArrayLike, MatrixLike
from ..base import TransformerMixin
from ..utils.validation import check_is_fitted as check_is_fitted

# Author: V. Michel, A. Gramfort
# License: BSD 3 clause

###############################################################################
# Mixin class for feature agglomeration.

class AgglomerationTransform(TransformerMixin):
    def transform(self, X: MatrixLike) -> ndarray: ...
    def inverse_transform(self, Xred: MatrixLike | ArrayLike) -> ndarray: ...
