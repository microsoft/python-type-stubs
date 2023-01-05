from typing import Optional, Any
from numpy.typing import ArrayLike, NDArray

# Author: Kyle Kastner <kastnerkyle@gmail.com>
#         Giorgio Patrini
# License: BSD 3 clause

import numpy as np
from scipy import linalg, sparse

from ._base import _BasePCA
from ..utils import gen_batches
from ..utils.extmath import svd_flip, _incremental_mean_and_var
from numpy import ndarray

class IncrementalPCA(_BasePCA):
    def __init__(
        self, n_components: int | None = None, *, whiten: bool = False, copy: bool = True, batch_size: int | None = None
    ) -> None: ...
    def fit(self, X: NDArray | ArrayLike, y: None = None) -> "IncrementalPCA": ...
    def partial_fit(self, X: ArrayLike, y: None = None, check_input: bool = True) -> "IncrementalPCA": ...
    def transform(self, X: NDArray | ArrayLike) -> NDArray: ...
