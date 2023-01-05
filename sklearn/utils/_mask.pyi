import numpy as np
from scipy import sparse as sp
from contextlib import suppress

from . import is_scalar_nan
from .fixes import _object_dtype_isnan
from numpy import ndarray

def _get_dense_mask(X: ndarray, value_to_mask: float) -> ndarray: ...
def _get_mask(X: ndarray, value_to_mask: float) -> ndarray: ...
