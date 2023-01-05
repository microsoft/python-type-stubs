from numpy import float64, ndarray
from typing import Dict, List, Optional, Tuple, Union, Any
from numpy.typing import ArrayLike, NDArray

# Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
# Fabian Pedregosa <fabian.pedregosa@inria.fr>
# Olivier Grisel <olivier.grisel@ensta.org>
#         Vincent Michel <vincent.michel@inria.fr>
#         Peter Prettenhofer <peter.prettenhofer@gmail.com>
#         Mathieu Blondel <mathieu@mblondel.org>
#         Lars Buitinck
#         Maryan Morel <maryan.morel@polytechnique.edu>
#         Giorgio Patrini <giorgio.patrini@anu.edu.au>
#         Maria Telenczuk <https://github.com/maikia>
# License: BSD 3 clause

from abc import ABCMeta, abstractmethod
import numbers
import warnings

import numpy as np
import scipy.sparse as sp
from scipy import linalg
from scipy import optimize
from scipy import sparse
from scipy.sparse.linalg import lsqr
from scipy.special import expit

from ..base import BaseEstimator, ClassifierMixin, RegressorMixin, MultiOutputMixin
from ..preprocessing._data import _is_constant_feature
from ..utils import check_array
from ..utils.validation import FLOAT_DTYPES
from ..utils import check_random_state
from ..utils.extmath import safe_sparse_dot
from ..utils.extmath import _incremental_mean_and_var
from ..utils.sparsefuncs import mean_variance_axis, inplace_column_scale

from ..utils.validation import check_is_fitted, _check_sample_weight
from ..utils.fixes import delayed
from numpy.random import RandomState
from scipy.sparse._csc import csc_matrix
from scipy.sparse._csr import csr_matrix
from sklearn.linear_model._stochastic_gradient import SGDClassifier

# TODO: bayesian_ridge_regression and bayesian_regression_ard
# should be squashed into its respective objects.

SPARSE_INTERCEPT_DECAY: float = ...
# For sparse data intercept updates are scaled by this decay factor to avoid
# intercept oscillation.

# FIXME in 1.2: parameter 'normalize' should be removed from linear models
# in cases where now normalize=False. The default value of 'normalize' should
# be changed to False in linear models where now normalize=True
def _deprecate_normalize(normalize: Union[str, bool], default: bool, estimator_name: str) -> bool: ...
def make_dataset(
    X: ArrayLike,
    y: ArrayLike,
    sample_weight: NDArray,
    random_state: int | RandomState | None = None,
) -> float: ...
def _preprocess_data(
    X: Union[ndarray, csr_matrix, csc_matrix],
    y: ndarray,
    fit_intercept: bool,
    normalize: bool = False,
    copy: bool = True,
    sample_weight: Optional[ndarray] = None,
    check_input: bool = True,
) -> Union[
    Tuple[csc_matrix, ndarray, ndarray, float64, ndarray],
    Tuple[csr_matrix, ndarray, ndarray, ndarray, ndarray],
    Tuple[ndarray, ndarray, ndarray, float64, ndarray],
    Tuple[csr_matrix, ndarray, ndarray, float64, ndarray],
    Tuple[ndarray, ndarray, ndarray, ndarray, ndarray],
]: ...

# TODO: _rescale_data should be factored into _preprocess_data.
# Currently, the fact that sag implements its own way to deal with
# sample_weight makes the refactoring tricky.

def _rescale_data(
    X: Union[ndarray, csr_matrix], y: ndarray, sample_weight: ndarray
) -> Union[Tuple[csr_matrix, ndarray, ndarray], Tuple[ndarray, ndarray, ndarray]]: ...

class LinearModel(BaseEstimator, metaclass=ABCMeta):
    @abstractmethod
    def fit(self, X, y): ...
    def _decision_function(self, X: Union[ndarray, csr_matrix]) -> ndarray: ...
    def predict(self, X: ArrayLike | NDArray) -> NDArray: ...
    def _set_intercept(self, X_offset: ndarray, y_offset: Union[ndarray, float64], X_scale: ndarray) -> None: ...
    def _more_tags(self) -> Dict[str, bool]: ...

# XXX Should this derive from LinearModel? It should be a mixin, not an ABC.
# Maybe the n_features checking can be moved to LinearModel.
class LinearClassifierMixin(ClassifierMixin):
    def decision_function(self, X: NDArray | ArrayLike) -> NDArray: ...
    def predict(self, X: NDArray | ArrayLike) -> NDArray: ...
    def _predict_proba_lr(self, X: Union[ndarray, csr_matrix]) -> ndarray: ...

class SparseCoefMixin:
    def densify(self): ...
    def sparsify(self) -> SGDClassifier: ...

class LinearRegression(MultiOutputMixin, RegressorMixin, LinearModel):
    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        normalize: bool | str = "deprecated",
        copy_X: bool = True,
        n_jobs: int | None = None,
        positive: bool = False,
    ) -> None: ...
    def fit(
        self,
        X: NDArray | ArrayLike,
        y: ArrayLike,
        sample_weight: ArrayLike | None = None,
    ) -> "LinearRegression": ...

def _check_precomputed_gram_matrix(
    X: ndarray,
    precompute: ndarray,
    X_offset: ndarray,
    X_scale: ndarray,
    rtol: None = None,
    atol: float = 1e-5,
) -> None: ...
def _pre_fit(
    X: Union[csc_matrix, ndarray],
    y: ndarray,
    Xy: Optional[ndarray],
    precompute: Union[ndarray, str, bool],
    normalize: bool,
    fit_intercept: bool,
    copy: bool,
    check_input: bool = True,
    sample_weight: Optional[ndarray] = None,
) -> Union[
    Tuple[csc_matrix, ndarray, ndarray, float64, ndarray, bool, None],
    Tuple[ndarray, ndarray, ndarray, float64, ndarray, bool, None],
    Tuple[ndarray, ndarray, ndarray, float64, ndarray, ndarray, ndarray],
]: ...
