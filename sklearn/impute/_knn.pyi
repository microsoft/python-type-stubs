from numpy import ndarray
from typing import List, Optional, Union, Callable, Literal, Any
from numpy.typing import ArrayLike

# Authors: Ashim Bhattarai <ashimb9@gmail.com>
#          Thomas J Fan <thomasjpfan@gmail.com>
# License: BSD 3 clause

import numpy as np

from ._base import _BaseImputer
from ..utils.validation import FLOAT_DTYPES
from ..metrics import pairwise_distances_chunked
from ..metrics.pairwise import _NAN_METRICS
from ..neighbors._base import _get_weights
from ..neighbors._base import _check_weights
from ..utils import is_scalar_nan
from ..utils._mask import _get_mask
from ..utils.validation import check_is_fitted
from ..utils.validation import _check_feature_names_in

class KNNImputer(_BaseImputer):
    def __init__(
        self,
        *,
        missing_values: int | float | str | None = ...,
        n_neighbors: int = 5,
        weights: Literal["uniform", "distance"] | Callable = "uniform",
        metric: Literal["nan_euclidean"] | Callable = "nan_euclidean",
        copy: bool = True,
        add_indicator: bool = False,
    ) -> None: ...
    def _calc_impute(
        self,
        dist_pot_donors: ndarray,
        n_neighbors: int,
        fit_X_col: ndarray,
        mask_fit_X_col: ndarray,
    ) -> ndarray: ...
    def fit(self, X: ArrayLike, y: Optional[ndarray] = None) -> "KNNImputer": ...
    def transform(self, X: ArrayLike) -> ArrayLike: ...
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...
