from numbers import Real as Real
from typing import Literal

import numpy as np

from .._typing import ArrayLike, Float, MatrixLike
from ..preprocessing import LabelBinarizer as LabelBinarizer
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions, validate_params as validate_params
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from ..utils.validation import check_array as check_array, check_consistent_length as check_consistent_length

def l1_min_c(
    X: MatrixLike | ArrayLike,
    y: ArrayLike,
    *,
    loss: Literal["squared_hinge", "log", "squared_hinge"] = "squared_hinge",
    fit_intercept: bool = True,
    intercept_scaling: Float = 1.0,
) -> Float: ...
