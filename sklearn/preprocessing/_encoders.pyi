from numpy import ndarray
from typing import Dict, List, Optional, Tuple, Union, Literal, Sequence, Any
from numpy.typing import ArrayLike, NDArray

# Authors: Andreas Mueller <amueller@ais.uni-bonn.de>
#          Joris Van den Bossche <jorisvandenbossche@gmail.com>
# License: BSD 3 clause

import numbers
import warnings

import numpy as np
from scipy import sparse

from ..base import BaseEstimator, TransformerMixin, _OneToOneFeatureMixin
from ..utils import check_array, is_scalar_nan
from ..utils.deprecation import deprecated
from ..utils.validation import check_is_fitted
from ..utils.validation import _check_feature_names_in
from ..utils._mask import _get_mask

from ..utils._encode import _encode, _check_unknown, _unique, _get_counts
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from scipy.sparse._csr import csr_matrix

__all__ = ["OneHotEncoder", "OrdinalEncoder"]

class _BaseEncoder(TransformerMixin, BaseEstimator):
    def _check_X(self, X: Union[DataFrame, ndarray], force_all_finite: str | bool = True) -> Tuple[List[ndarray], int, int]: ...
    def _get_feature(self, X: Union[DataFrame, ndarray], feature_idx: int) -> Union[ndarray, Series]: ...
    def _fit(
        self,
        X: Union[DataFrame, ndarray],
        handle_unknown: str = "error",
        force_all_finite: str | bool = True,
        return_counts: bool = False,
    ) -> Dict[str, int]: ...
    def _transform(
        self,
        X: Union[DataFrame, ndarray],
        handle_unknown: str = "error",
        force_all_finite: str | bool = True,
        warn_on_unknown: bool = False,
    ) -> Tuple[ndarray, ndarray]: ...
    def _more_tags(self): ...

class OneHotEncoder(_BaseEncoder):
    def __init__(
        self,
        *,
        categories: Sequence[ArrayLike] | Literal["auto"] = "auto",
        drop: Literal["first", "if_binary"] | ArrayLike | None = None,
        sparse: bool = True,
        dtype: int | float = ...,
        handle_unknown: Literal["error", "ignore", "infrequent_if_exist"] = "error",
        min_frequency: int | float | None = None,
        max_categories: int | None = None,
    ) -> None: ...
    @property
    def infrequent_categories_(self): ...
    def _validate_keywords(self) -> None: ...
    def _map_drop_idx_to_infrequent(self, feature_idx, drop_idx): ...
    def _compute_drop_idx(self) -> None: ...
    def _identify_infrequent(self, category_count, n_samples, col_idx): ...
    def _fit_infrequent_category_mapping(self, n_samples, category_counts): ...
    def _map_infrequent_categories(self, X_int: ndarray, X_mask: ndarray) -> None: ...
    def _compute_transformed_categories(self, i: int, remove_dropped: bool = True) -> ndarray: ...
    def _remove_dropped_categories(self, categories: ndarray, i: int) -> ndarray: ...
    def _compute_n_features_outs(self) -> List[int]: ...
    def fit(self, X: ArrayLike, y: Optional[Union[ndarray, List[int]]] = None) -> "OneHotEncoder": ...
    def fit_transform(self, X: ArrayLike, y: Optional[Union[List[int], ndarray]] = None) -> NDArray: ...
    def transform(self, X: ArrayLike) -> NDArray: ...
    def inverse_transform(self, X: NDArray | ArrayLike) -> NDArray: ...
    @deprecated("get_feature_names is deprecated in 1.0 and will be removed " "in 1.2. Please use get_feature_names_out instead.")
    def get_feature_names(self, input_features: Sequence[str] | None = None) -> np.ndarray: ...
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...

class OrdinalEncoder(_OneToOneFeatureMixin, _BaseEncoder):
    def __init__(
        self,
        *,
        categories: Sequence[ArrayLike] | Literal["auto"] = "auto",
        dtype: int | float = ...,
        handle_unknown: Literal["error", "use_encoded_value"] = "error",
        unknown_value: int | None = None,
        encoded_missing_value: int = ...,
    ): ...
    def fit(self, X: ArrayLike, y=None) -> Any: ...
    def transform(self, X: ArrayLike) -> NDArray: ...
    def inverse_transform(self, X: ArrayLike) -> NDArray: ...
