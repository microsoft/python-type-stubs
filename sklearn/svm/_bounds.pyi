from typing import Literal
from ..utils._param_validation import (
    StrOptions as StrOptions,
    Interval as Interval,
    validate_params as validate_params,
)
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from .._typing import ArrayLike, MatrixLike, Float
from ..preprocessing import LabelBinarizer as LabelBinarizer
from ..utils.validation import (
    check_consistent_length as check_consistent_length,
    check_array as check_array,
)
from numbers import Real as Real

import numpy as np


def l1_min_c(
    X: MatrixLike | ArrayLike,
    y: ArrayLike,
    *,
    loss: Literal["squared_hinge", "log", "squared_hinge"] = "squared_hinge",
    fit_intercept: bool = True,
    intercept_scaling: Float = 1.0
) -> Float:
    ...
