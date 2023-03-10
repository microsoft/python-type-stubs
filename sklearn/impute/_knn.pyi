from typing import Any, Callable, Literal
from ..utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from .._typing import Int, MatrixLike, ArrayLike
from ..utils.validation import (
    FLOAT_DTYPES as FLOAT_DTYPES,
    check_is_fitted as check_is_fitted,
)
from ._base import _BaseImputer
from numpy import ndarray
from ..utils import is_scalar_nan as is_scalar_nan
from numbers import Integral as Integral
from ..metrics import pairwise_distances_chunked as pairwise_distances_chunked

# Authors: Ashim Bhattarai <ashimb9@gmail.com>
#          Thomas J Fan <thomasjpfan@gmail.com>
# License: BSD 3 clause

import numpy as np


class KNNImputer(_BaseImputer):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        missing_values: int | float | None | str = ...,
        n_neighbors: Int = 5,
        weights: Literal["uniform", "distance", "uniform"] | Callable = "uniform",
        metric: Literal["nan_euclidean", "nan_euclidean"] | Callable = "nan_euclidean",
        copy: bool = True,
        add_indicator: bool = False,
        keep_empty_features: bool = False,
    ) -> None:
        ...

    def fit(self, X: MatrixLike | list[list[int | float]], y: Any = None) -> Any:
        ...

    def transform(self, X: MatrixLike | list[list[int | float]]) -> ndarray:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...
