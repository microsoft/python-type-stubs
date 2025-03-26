from numbers import Integral as Integral
from typing import Any, ClassVar
from typing_extensions import Self

import numpy as np
from numpy import ndarray
from scipy import linalg as linalg, sparse as sparse

from .._typing import ArrayLike, Int, MatrixLike
from ..utils import gen_batches as gen_batches
from ..utils._param_validation import Interval as Interval
from ..utils.extmath import svd_flip as svd_flip
from ._base import _BasePCA

class IncrementalPCA(_BasePCA):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    batch_size_: int = ...
    n_samples_seen_: int = ...
    n_components_: int = ...
    noise_variance_: float = ...
    var_: ndarray = ...
    mean_: ndarray = ...
    singular_values_: ndarray = ...
    explained_variance_ratio_: ndarray = ...
    explained_variance_: ndarray = ...
    components_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self, n_components: None | Int = None, *, whiten: bool = False, copy: bool = True, batch_size: None | Int = None
    ) -> None: ...
    def fit(self, X: MatrixLike | ArrayLike, y: Any = None) -> Self: ...
    def partial_fit(
        self,
        X: MatrixLike,
        y: Any = None,
        check_input: bool = True,
    ) -> Self: ...
    def transform(self, X: MatrixLike | ArrayLike) -> ndarray: ...
