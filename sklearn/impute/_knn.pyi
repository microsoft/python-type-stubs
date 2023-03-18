from typing import Any, Callable, ClassVar, Literal, TypeVar
from ._base import MissingIndicator
from ..utils import is_scalar_nan as is_scalar_nan
from ._base import _BaseImputer
from numpy import ndarray
from ..utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    StrOptions as StrOptions,
)
from numbers import Integral as Integral
from .._typing import Int, MatrixLike, ArrayLike
from ..metrics import pairwise_distances_chunked as pairwise_distances_chunked
from ..utils.validation import (
    FLOAT_DTYPES as FLOAT_DTYPES,
    check_is_fitted as check_is_fitted,
)

KNNImputer_Self = TypeVar("KNNImputer_Self", bound="KNNImputer")

# Authors: Ashim Bhattarai <ashimb9@gmail.com>
#          Thomas J Fan <thomasjpfan@gmail.com>
# License: BSD 3 clause

import numpy as np


class KNNImputer(_BaseImputer):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    indicator_: MissingIndicator = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        missing_values: float | None | str | int = ...,
        n_neighbors: Int = 5,
        weights: Literal["uniform", "distance", "uniform"] | Callable = "uniform",
        metric: Callable | Literal["nan_euclidean", "nan_euclidean"] = "nan_euclidean",
        copy: bool = True,
        add_indicator: bool = False,
        keep_empty_features: bool = False,
    ) -> None:
        ...

    def fit(
        self: KNNImputer_Self, X: list[list[int | float]] | MatrixLike, y: Any = None
    ) -> KNNImputer_Self:
        ...

    def transform(self, X: list[list[int | float]] | MatrixLike) -> ndarray:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...
