from numpy import ndarray
from typing import Optional, Tuple, Literal, Any
from numpy.typing import ArrayLike, NDArray

# Authors: Fabian Pedregosa <fabian@fseoane.net>
#          Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Nelle Varoquaux <nelle.varoquaux@gmail.com>
# License: BSD 3 clause

import numpy as np
from scipy import interpolate
from scipy.stats import spearmanr
import warnings
import math

from .base import BaseEstimator, TransformerMixin, RegressorMixin
from .utils import check_array, check_consistent_length
from .utils.validation import _check_sample_weight
from ._isotonic import _inplace_contiguous_isotonic_regression, _make_unique

__all__ = ["check_increasing", "isotonic_regression", "IsotonicRegression"]

def check_increasing(x: ArrayLike, y: ArrayLike) -> bool: ...
def isotonic_regression(
    y: ArrayLike,
    *,
    sample_weight: ArrayLike | None = None,
    y_min: float | None = None,
    y_max: float | None = None,
    increasing: bool = True,
) -> list[float]: ...

class IsotonicRegression(RegressorMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        *,
        y_min: float | None = None,
        y_max: float | None = None,
        increasing: bool | Literal["auto"] = True,
        out_of_bounds: Literal["nan", "clip", "raise"] = "nan",
    ) -> None: ...
    def _check_input_data_shape(self, X: ndarray) -> None: ...
    def _build_f(self, X: ndarray, y: ndarray) -> None: ...
    def _build_y(
        self,
        X: ndarray,
        y: ndarray,
        sample_weight: Optional[ndarray],
        trim_duplicates: bool = True,
    ) -> Tuple[ndarray, ndarray]: ...
    def fit(self, X: ArrayLike, y: ArrayLike, sample_weight: ArrayLike | None = None) -> "IsotonicRegression": ...
    def transform(self, T: ArrayLike) -> NDArray: ...
    def predict(self, T: ArrayLike) -> NDArray: ...

    # We implement get_feature_names_out here instead of using
    # `_ClassNamePrefixFeaturesOutMixin`` because `input_features` are ignored.
    # `input_features` are ignored because `IsotonicRegression` accepts 1d
    # arrays and the semantics of `feature_names_in_` are not clear for 1d arrays.
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...
    def __getstate__(self): ...
    def __setstate__(self, state): ...
    def _more_tags(self): ...
