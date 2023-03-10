from typing import Any
from ..utils._param_validation import Interval as Interval
from ..utils.extmath import svd_flip as svd_flip
from .._typing import Int, ArrayLike, MatrixLike
from scipy import linalg as linalg, sparse as sparse
from ._base import _BasePCA
from numpy import ndarray
from ..utils import gen_batches as gen_batches
from numbers import Integral as Integral
import numpy as np


class IncrementalPCA(_BasePCA):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        n_components: None | Int = None,
        *,
        whiten: bool = False,
        copy: bool = True,
        batch_size: None | Int = None
    ) -> None:
        ...

    def fit(self, X: MatrixLike | ArrayLike, y: Any = None) -> Any:
        ...

    def partial_fit(
        self, X: MatrixLike, y: Any = None, check_input: bool = True
    ) -> Any:
        ...

    def transform(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...
