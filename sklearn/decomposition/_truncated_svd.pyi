from typing import Optional, Literal, Any
from numpy.typing import ArrayLike, NDArray

# Author: Lars Buitinck
#         Olivier Grisel <olivier.grisel@ensta.org>
#         Michael Becker <mike@beckerfuffle.com>
# License: 3-clause BSD.

from numbers import Integral
import numpy as np
from numpy.random import RandomState
import scipy.sparse as sp
from scipy.sparse.linalg import svds

from ..base import BaseEstimator, TransformerMixin, _ClassNamePrefixFeaturesOutMixin
from ..utils import check_array, check_random_state
from ..utils._arpack import _init_arpack_v0
from ..utils.extmath import randomized_svd, safe_sparse_dot, svd_flip
from ..utils.sparsefuncs import mean_variance_axis
from ..utils.validation import check_is_fitted, check_scalar
from numpy import ndarray
from scipy.sparse._csr import csr_matrix

__all__ = ["TruncatedSVD"]

class TruncatedSVD(_ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        n_components: int = 2,
        *,
        algorithm: Literal["arpack", "randomized"] = "randomized",
        n_iter: int = 5,
        n_oversamples: int = 10,
        power_iteration_normalizer: Literal["auto", "QR", "LU", "none"] = "auto",
        random_state: int | RandomState | None = None,
        tol: float = 0.0,
    ) -> None: ...
    def fit(self, X: NDArray | ArrayLike, y=None) -> Any: ...
    def fit_transform(self, X: NDArray | ArrayLike, y: Optional[ndarray] = None) -> NDArray: ...
    def transform(self, X: NDArray | ArrayLike) -> NDArray: ...
    def inverse_transform(self, X: ArrayLike) -> NDArray: ...
    def _more_tags(self): ...
    @property
    def _n_features_out(self): ...
