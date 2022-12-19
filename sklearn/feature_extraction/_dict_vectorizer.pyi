from numpy import ndarray
from typing import Dict, List, Optional, Any, Mapping
from numpy.typing import ArrayLike, NDArray, DTypeLike

# Authors: Lars Buitinck
#          Dan Blanchard <dblanchard@ets.org>
# License: BSD 3 clause

from array import array
from collections.abc import Mapping, Iterable
from operator import itemgetter
from numbers import Number

import numpy as np
import scipy.sparse as sp

from ..base import BaseEstimator, TransformerMixin
from ..utils import check_array, tosequence
from ..utils.deprecation import deprecated
from scipy.sparse._csr import csr_matrix

def _tosequence(X): ...

class DictVectorizer(TransformerMixin, BaseEstimator):
    def __init__(
        self,
        *,
        dtype: DTypeLike = ...,
        separator: str = "=",
        sparse: bool = True,
        sort: bool = True,
    ) -> None: ...
    def _add_iterable_element(
        self,
        f,
        v,
        feature_names,
        vocab,
        *,
        fitting=True,
        transforming=False,
        indices=None,
        values=None,
    ): ...
    def fit(self, X: Mapping | Iterable[Mapping], y=None) -> Any: ...
    def _transform(self, X: List[Dict[str, int]], fitting: bool) -> csr_matrix: ...
    def fit_transform(self, X: Mapping | Iterable[Mapping], y: Optional[ndarray] = None) -> NDArray: ...
    def inverse_transform(self, X: NDArray | ArrayLike, dict_type: type = ...) -> list[Mapping]: ...
    def transform(self, X: Mapping | Iterable[Mapping]) -> NDArray: ...
    @deprecated("get_feature_names is deprecated in 1.0 and will be removed " "in 1.2. Please use get_feature_names_out instead.")
    def get_feature_names(self) -> list: ...
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...
    def restrict(self, support: ArrayLike, indices: bool = False) -> Any: ...
    def _more_tags(self): ...
