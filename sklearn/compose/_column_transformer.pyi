from sklearn.compose._column_transformer import ColumnTransformer
from typing import Any, Dict, Iterator, List, Optional, Tuple, Union, Mapping, Callable
from numpy.typing import ArrayLike, NDArray, DTypeLike
from numpy import ndarray

# Author: Andreas Mueller
#         Joris Van den Bossche
# License: BSD
from itertools import chain
from collections import Counter
from typing import Literal, Callable, Sequence

import numpy as np
from scipy import sparse

from ..base import BaseEstimator, clone, TransformerMixin
from ..utils._estimator_html_repr import _VisualBlock
from ..pipeline import _fit_transform_one, _transform_one, _name_estimators
from ..preprocessing import FunctionTransformer
from ..utils import Bunch
from ..utils import _safe_indexing
from ..utils import _get_column_indices
from ..utils.deprecation import deprecated
from ..utils.metaestimators import _BaseComposition
from ..utils.validation import check_array, check_is_fitted, _check_feature_names_in
from ..utils.fixes import delayed
from pandas.core.frame import DataFrame
from scipy.sparse._csr import csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing._data import StandardScaler
from sklearn.preprocessing._encoders import OneHotEncoder

__all__ = ["ColumnTransformer", "make_column_transformer", "make_column_selector"]

_ERR_MSG_1DCOLUMN: str = ...

class ColumnTransformer(TransformerMixin, _BaseComposition):

    _required_parameters: list = ...

    def __init__(
        self,
        transformers: ArrayLike,
        *,
        remainder: Literal["drop", "passthrough"] | BaseEstimator = "drop",
        sparse_threshold: float = 0.3,
        n_jobs: int | None = None,
        transformer_weights: Mapping | None = None,
        verbose: bool = False,
        verbose_feature_names_out: bool = True,
    ) -> None: ...
    @property
    def _transformers(self): ...
    @_transformers.setter
    def _transformers(self, value): ...
    def get_params(self, deep: bool = True) -> Mapping: ...
    def set_params(self, **kwargs) -> ColumnTransformer: ...
    def _iter(
        self,
        fitted: bool = False,
        replace_strings: bool = False,
        column_as_strings: bool = False,
    ) -> Iterator[
        Union[
            Tuple[str, StandardScaler, List[str], None],
            Tuple[str, OneHotEncoder, List[str], None],
            Tuple[str, TfidfVectorizer, int, float],
            Tuple[str, Pipeline, int, float],
        ]
    ]: ...
    def _validate_transformers(self) -> None: ...
    def _validate_column_callables(self, X: Union[DataFrame, ndarray]) -> None: ...
    def _validate_remainder(self, X: Union[DataFrame, ndarray]) -> None: ...
    @property
    def named_transformers_(self): ...
    @deprecated("get_feature_names is deprecated in 1.0 and will be removed " "in 1.2. Please use get_feature_names_out instead.")
    def get_feature_names(self) -> ArrayLike: ...
    def _get_feature_name_out_for_transformer(
        self,
        name: str,
        trans: Union[OneHotEncoder, StandardScaler],
        column: List[str],
        feature_names_in: ndarray,
    ) -> ndarray: ...
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...
    def _update_fitted_transformers(
        self,
        transformers: Union[
            Tuple[StandardScaler, OneHotEncoder],
            Tuple[TfidfVectorizer, Pipeline, Pipeline],
        ],
    ) -> None: ...
    def _validate_output(
        self,
        result: Union[
            Tuple[ndarray, csr_matrix],
            Tuple[csr_matrix, ndarray, csr_matrix],
            List[Union[csr_matrix, ndarray]],
        ],
    ) -> None: ...
    def _record_output_indices(
        self,
        Xs: Union[Tuple[ndarray, csr_matrix], Tuple[csr_matrix, ndarray, csr_matrix]],
    ) -> None: ...
    def _log_message(self, name: str, idx: int, total: int) -> None: ...
    def _fit_transform(
        self,
        X: Union[DataFrame, ndarray],
        y: Optional[Union[ndarray, List[int]]],
        func: Callable,
        fitted: bool = False,
        column_as_strings: bool = False,
    ) -> List[Any]: ...
    def fit(self, X: ArrayLike | DataFrame, y: ArrayLike | None = None) -> ColumnTransformer: ...
    def fit_transform(self, X: ArrayLike | DataFrame, y: ArrayLike | None = None) -> NDArray | ArrayLike: ...
    def transform(self, X: ArrayLike | DataFrame) -> NDArray | ArrayLike: ...
    def _hstack(self, Xs: List[Union[csr_matrix, ndarray]]) -> ndarray: ...
    def _sk_visual_block_(self): ...

def _check_X(X: Union[DataFrame, ndarray]) -> Union[DataFrame, ndarray]: ...
def _is_empty_column_selection(column: Union[int, List[str]]) -> bool: ...
def _get_transformer_list(
    estimators: Tuple[Tuple[Pipeline, Tuple[str, str]], Tuple[Pipeline, Tuple[str, str]]]
) -> List[Tuple[str, Pipeline, Tuple[str, str]]]: ...
def make_column_transformer(
    *transformers,
    remainder: Literal["drop", "passthrough"] | BaseEstimator = "drop",
    sparse_threshold: float = 0.3,
    n_jobs: int | None = None,
    verbose: bool = False,
    verbose_feature_names_out: bool = True,
) -> ColumnTransformer: ...

class make_column_selector:
    def __init__(
        self,
        pattern: str | None = None,
        *,
        dtype_include: DTypeLike | Sequence[DTypeLike] | None = None,
        dtype_exclude: DTypeLike | Sequence[DTypeLike] | None = None,
    ): ...
    def __call__(self, df: DataFrame): ...
