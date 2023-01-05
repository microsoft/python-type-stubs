from numpy import ndarray
from numpy.typing import ArrayLike

# Author: V. Michel, A. Gramfort
# License: BSD 3 clause

import numpy as np

from ..base import TransformerMixin
from ..utils.validation import check_is_fitted
from scipy.sparse import issparse

###############################################################################
# Mixin class for feature agglomeration.

class AgglomerationTransform(TransformerMixin):
    def transform(self, X: ArrayLike) -> np.ndarray: ...
    def inverse_transform(self, Xred: ArrayLike) -> np.ndarray: ...
