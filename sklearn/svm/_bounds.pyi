from typing import Literal
from numpy.typing import ArrayLike, NDArray

# Author: Paolo Losi
# License: BSD 3 clause

import numpy as np

from ..preprocessing import LabelBinarizer
from ..utils.validation import check_consistent_length, check_array
from ..utils.extmath import safe_sparse_dot

def l1_min_c(
    X: NDArray | ArrayLike,
    y: ArrayLike,
    *,
    loss: Literal["squared_hinge", "log"] = "squared_hinge",
    fit_intercept: bool = True,
    intercept_scaling: float = 1.0,
) -> float: ...
