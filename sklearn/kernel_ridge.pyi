from typing import Dict, Optional, Union, Callable, Any, Mapping
from numpy.typing import ArrayLike, NDArray

# Authors: Mathieu Blondel <mathieu@mblondel.org>
#          Jan Hendrik Metzen <jhm@informatik.uni-bremen.de>
# License: BSD 3 clause

import numpy as np

from .base import BaseEstimator, RegressorMixin, MultiOutputMixin
from .metrics.pairwise import pairwise_kernels
from .linear_model._ridge import _solve_cholesky_kernel
from .utils.validation import check_is_fitted, _check_sample_weight
from numpy import float64, ndarray

class KernelRidge(MultiOutputMixin, RegressorMixin, BaseEstimator):
    def __init__(
        self,
        alpha: float | ArrayLike = 1,
        *,
        kernel: str | Callable = "linear",
        gamma: float | None = None,
        degree: float = 3,
        coef0: float = 1,
        kernel_params: Mapping[str, Any] | None = None,
    ) -> None: ...
    def _get_kernel(self, X: ndarray, Y: Optional[ndarray] = None) -> ndarray: ...
    def _more_tags(self) -> Dict[str, bool]: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: float | ArrayLike | None = None,
    ) -> "KernelRidge": ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
