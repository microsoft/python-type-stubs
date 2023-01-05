from numpy import ndarray
from typing import Dict, List, Optional, Union, Callable, Literal, Mapping, Any
from numpy.typing import ArrayLike
import warnings

import numpy as np

from ..base import BaseEstimator, TransformerMixin
from ..utils.metaestimators import available_if
from ..utils.validation import (
    _allclose_dense_sparse,
    _check_feature_names_in,
    check_array,
)
from scipy.sparse._csr import csr_matrix
from sklearn.ensemble._forest import RandomForestClassifier
from sklearn.ensemble._gb import GradientBoostingClassifier

def _identity(X): ...

class FunctionTransformer(TransformerMixin, BaseEstimator):
    def __init__(
        self,
        func: Callable | None = None,
        inverse_func: Callable | None = None,
        *,
        validate: bool = False,
        accept_sparse: bool = False,
        check_inverse: bool = True,
        feature_names_out: Callable | Literal["one-to-one"] | None = None,
        kw_args: Mapping | None = None,
        inv_kw_args: Mapping | None = None,
    ) -> None: ...
    def _check_input(self, X: Union[ndarray, csr_matrix, List[str]], *, reset) -> Union[ndarray, csr_matrix, List[str]]: ...
    def _check_inverse_transform(self, X): ...
    def fit(self, X: ArrayLike, y: Optional[ndarray] = None) -> "FunctionTransformer": ...
    def transform(self, X: ArrayLike) -> ArrayLike: ...
    def inverse_transform(self, X: ArrayLike) -> ArrayLike: ...
    @available_if(lambda self: self.feature_names_out is not None)
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...
    def _transform(
        self,
        X: Union[csr_matrix, ndarray, List[str]],
        func: Optional[Callable] = None,
        kw_args: Optional[Union[Dict[str, RandomForestClassifier], Dict[str, GradientBoostingClassifier]]] = None,
    ) -> Union[ndarray, List[Dict[str, int]]]: ...
    def __sklearn_is_fitted__(self): ...
    def _more_tags(self): ...
