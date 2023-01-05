from numpy import float32, float64, int64, ndarray
from typing import Dict, List, Optional, Tuple, Type, Union, Any, Mapping, Sequence
from numpy.typing import ArrayLike, NDArray

# Author: Gael Varoquaux <gael.varoquaux@normalesup.org>
# License: BSD 3 clause

import copy
import warnings
from collections import defaultdict
import platform
import inspect
import re

import numpy as np

from . import __version__
from ._config import get_config
from .utils import _IS_32BIT
from .utils._tags import (
    _DEFAULT_TAGS,
)
from .utils.validation import check_X_y
from .utils.validation import check_array
from .utils.validation import _check_y
from .utils.validation import _num_features
from .utils.validation import _check_feature_names_in
from .utils.validation import _generate_get_feature_names_out
from .utils.validation import check_is_fitted
from .utils._estimator_html_repr import estimator_html_repr
from .utils.validation import _get_feature_names
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from scipy.sparse._csc import csc_matrix
from scipy.sparse._csr import csr_matrix

def clone(
    estimator: BaseEstimator | Sequence[BaseEstimator] | tuple[BaseEstimator, ...] | set[BaseEstimator],
    *,
    safe: bool = True,
) -> Any: ...
def _pprint(params, offset=0, printer=repr): ...

class BaseEstimator:
    @classmethod
    def _get_param_names(cls) -> List[str]: ...
    def get_params(self, deep: bool = True) -> Mapping: ...
    def set_params(self, **params) -> BaseEstimator: ...
    def __repr__(self, N_CHAR_MAX: int = 700) -> str: ...
    def __getstate__(self) -> Dict[str, Optional[Union[int, str, ndarray]]]: ...
    def __setstate__(self, state: Dict[str, Optional[Union[int, str, ndarray]]]) -> None: ...
    def _more_tags(self) -> Dict[str, Union[bool, List[str], List[Type[float64]]]]: ...
    def _get_tags(
        self,
    ) -> Dict[str, Union[bool, List[str], Dict[str, str], List[Type[float64]], List[Union[Type[float64], Type[float32]]],],]: ...
    def _check_n_features(self, X: Union[DataFrame, ndarray, csr_matrix, csc_matrix], reset: bool) -> None: ...
    def _check_feature_names(self, X: Any, *, reset) -> None: ...
    def _validate_data(
        self,
        X: Any = "no_validation",
        y: Any = "no_validation",
        reset: bool = True,
        validate_separately: Union[
            bool,
            Tuple[
                Dict[str, Union[str, List[Union[Type[float64], Type[float32]]], bool]],
                Dict[str, Union[bool, List[Union[Type[float64], Type[float32]]]]],
            ],
            Tuple[Dict[str, Union[Type[float32], str]], Dict[str, Optional[bool]]],
            Tuple[
                Dict[str, Union[str, List[Union[Type[float64], Type[float32]]], bool]],
                Dict[str, Union[bool, str]],
            ],
            Tuple[Dict[str, Union[bool, str]], Dict[str, bool]],
        ] = False,
        **check_params,
    ) -> Union[Tuple[ndarray, ndarray], Tuple[csr_matrix, ndarray], ndarray, csr_matrix, Tuple[csc_matrix, ndarray],]: ...
    @property
    def _repr_html_(self): ...
    def _repr_html_inner(self): ...
    def _repr_mimebundle_(self, **kwargs): ...

class ClassifierMixin:

    _estimator_type: str = ...

    def score(self, X: ArrayLike, y: ArrayLike, sample_weight: ArrayLike | None = None) -> float: ...
    def _more_tags(self) -> Dict[str, bool]: ...

class RegressorMixin:

    _estimator_type: str = ...

    def score(self, X: ArrayLike, y: ArrayLike, sample_weight: ArrayLike | None = None) -> float: ...
    def _more_tags(self) -> Dict[str, bool]: ...

class ClusterMixin:

    _estimator_type: str = ...

    def fit_predict(self, X: ArrayLike, y: None = None) -> np.ndarray: ...
    def _more_tags(self) -> Dict[str, List[Any]]: ...

class BiclusterMixin:
    @property
    def biclusters_(self) -> Tuple[ndarray, ndarray]: ...
    def get_indices(self, i: int) -> tuple[NDArray, NDArray]: ...
    def get_shape(self, i: int) -> tuple[int, int]: ...
    def get_submatrix(self, i: int, data: ArrayLike) -> np.ndarray: ...

class TransformerMixin:
    def fit_transform(self, X: ArrayLike, y: ArrayLike | None = None, **fit_params) -> NDArray: ...

class _OneToOneFeatureMixin:
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...

class _ClassNamePrefixFeaturesOutMixin:
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...

class DensityMixin:

    _estimator_type: str = ...

    def score(self, X: ArrayLike, y=None) -> float: ...

class OutlierMixin:

    _estimator_type: str = ...

    def fit_predict(self, X: NDArray | ArrayLike, y=None) -> NDArray: ...

class MetaEstimatorMixin:
    _required_parameters: list = ...

class MultiOutputMixin:
    def _more_tags(self) -> Dict[str, bool]: ...

class _UnstableArchMixin:
    def _more_tags(self): ...

def is_classifier(estimator: BaseEstimator) -> bool: ...
def is_regressor(estimator: BaseEstimator) -> bool: ...
def is_outlier_detector(estimator: BaseEstimator) -> bool: ...
