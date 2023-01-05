from numpy import int64, ndarray
from typing import Optional, Tuple, Union, Literal, Any
from numpy.typing import ArrayLike
from time import time
from collections import namedtuple
import warnings

from scipy import stats
import numpy as np

from ..base import clone
from ..exceptions import ConvergenceWarning
from ..preprocessing import normalize
from ..utils import check_array, check_random_state, _safe_indexing, is_scalar_nan
from ..utils.validation import FLOAT_DTYPES, check_is_fitted
from ..utils.validation import _check_feature_names_in
from ..utils._mask import _get_mask

from ._base import _BaseImputer
from ._base import SimpleImputer
from ._base import _check_inputs_dtype
from sklearn.ensemble._forest import RandomForestRegressor
from sklearn.linear_model._bayes import BayesianRidge
from sklearn.neighbors._regression import KNeighborsRegressor
from sklearn.pipeline import Pipeline

_ImputerTriplet = ...

class IterativeImputer(_BaseImputer):
    def __init__(
        self,
        estimator: Estimator | None = None,
        *,
        missing_values: int = ...,
        sample_posterior: bool = False,
        max_iter: int = 10,
        tol: float = 1e-3,
        n_nearest_features: int | None = None,
        initial_strategy: Literal["mean", "median", "most_frequent", "constant"] = "mean",
        imputation_order: Literal["ascending", "descending", "roman", "arabic", "random"] = "ascending",
        skip_complete: bool = False,
        min_value: float | ArrayLike = ...,
        max_value: float | ArrayLike = ...,
        verbose: int = 0,
        random_state: int | RandomState | None = None,
        add_indicator: bool = False,
    ) -> None: ...
    def _impute_one_feature(
        self,
        X_filled: ndarray,
        mask_missing_values: ndarray,
        feat_idx: int64,
        neighbor_feat_idx: ndarray,
        estimator: Optional[Union[KNeighborsRegressor, BayesianRidge, Pipeline, RandomForestRegressor]] = None,
        fit_mode: bool = True,
    ) -> Union[
        Tuple[ndarray, RandomForestRegressor],
        Tuple[ndarray, BayesianRidge],
        Tuple[ndarray, KNeighborsRegressor],
        Tuple[ndarray, Pipeline],
    ]: ...
    def _get_neighbor_feat_idx(self, n_features: int, feat_idx: int64, abs_corr_mat: Optional[ndarray]) -> ndarray: ...
    def _get_ordered_idx(self, mask_missing_values: ndarray) -> ndarray: ...
    def _get_abs_corr_mat(self, X_filled: ndarray, tolerance: float = 1e-6) -> Optional[ndarray]: ...
    def _initial_imputation(self, X: ndarray, in_fit: bool = False) -> Tuple[ndarray, ndarray, ndarray, ndarray]: ...
    @staticmethod
    def _validate_limit(limit: float, limit_type: str, n_features: int) -> ndarray: ...
    def fit_transform(self, X: ArrayLike, y: Optional[ndarray] = None) -> ArrayLike: ...
    def transform(self, X: ArrayLike) -> ArrayLike: ...
    def fit(self, X: ArrayLike, y=None) -> Any: ...
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...
