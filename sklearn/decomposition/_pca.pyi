from typing import Dict, List, Optional, Tuple, Type, Union, Literal, Any
from numpy.typing import ArrayLike, NDArray

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
#         Olivier Grisel <olivier.grisel@ensta.org>
#         Mathieu Blondel <mathieu@mblondel.org>
#         Denis A. Engemann <denis-alexander.engemann@inria.fr>
#         Michael Eickenberg <michael.eickenberg@inria.fr>
#         Giorgio Patrini <giorgio.patrini@anu.edu.au>
#
# License: BSD 3 clause

from math import log, sqrt
import numbers

import numpy as np
from numpy.random import RandomState
from scipy import linalg
from scipy.special import gammaln
from scipy.sparse import issparse
from scipy.sparse.linalg import svds

from ._base import _BasePCA
from ..utils import check_random_state, check_scalar
from ..utils._arpack import _init_arpack_v0
from ..utils.extmath import fast_logdet, randomized_svd, svd_flip
from ..utils.extmath import stable_cumsum
from ..utils.validation import check_is_fitted
from numpy import float64, int64, ndarray

def _assess_dimension(spectrum: ndarray, rank: int, n_samples: int) -> float64: ...
def _infer_dimension(spectrum: ndarray, n_samples: int) -> int64: ...

class PCA(_BasePCA):
    def __init__(
        self,
        n_components: int | float | Literal["mle"] | None = None,
        *,
        copy: bool = True,
        whiten: bool = False,
        svd_solver: Literal["auto", "full", "arpack", "randomized"] = "auto",
        tol: float = 0.0,
        iterated_power: int | Literal["auto"] = "auto",
        n_oversamples: int = 10,
        power_iteration_normalizer: Literal["auto", "QR", "LU", "none"] = "auto",
        random_state: int | RandomState | None = None,
    ) -> None: ...
    def fit(self, X: ArrayLike, y: Optional[ndarray] = None) -> "PCA": ...
    def fit_transform(self, X: ArrayLike, y: Optional[ndarray] = None) -> NDArray: ...
    def _fit(self, X: ndarray) -> Tuple[ndarray, ndarray, ndarray]: ...
    def _fit_full(self, X: ndarray, n_components: Union[int64, str, int]) -> Tuple[ndarray, ndarray, ndarray]: ...
    def _fit_truncated(self, X: ndarray, n_components: int, svd_solver: str) -> Tuple[ndarray, ndarray, ndarray]: ...
    def score_samples(self, X: ArrayLike) -> NDArray: ...
    def score(self, X: ArrayLike, y: None = None) -> float: ...
    def _more_tags(self) -> Dict[str, List[Union[Type[float64], Type[np.float32]]]]: ...
