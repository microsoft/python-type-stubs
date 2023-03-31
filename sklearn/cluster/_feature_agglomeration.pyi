from numpy import ndarray
from scipy.sparse import issparse as issparse
from ..base import TransformerMixin
from .._typing import MatrixLike, ArrayLike
from ..utils.validation import check_is_fitted as check_is_fitted

# Author: V. Michel, A. Gramfort
# License: BSD 3 clause

import numpy as np

###############################################################################
# Mixin class for feature agglomeration.


class AgglomerationTransform(TransformerMixin):
    def transform(self, X: MatrixLike) -> ndarray:
        ...

    def inverse_transform(self, Xred: MatrixLike | ArrayLike) -> ndarray:
        ...
