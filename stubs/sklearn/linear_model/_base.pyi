from abc import ABCMeta, abstractmethod
from numbers import Integral as Integral
from typing import ClassVar, TypeVar

from numpy import ndarray
from numpy.random.mtrand import RandomState
from scipy import linalg as linalg, optimize as optimize, sparse
from scipy.sparse.linalg import lsqr as lsqr
from scipy.special import expit as expit

from .._typing import ArrayLike, Int, MatrixLike
from ..base import BaseEstimator, ClassifierMixin, MultiOutputMixin, RegressorMixin
from ..utils import check_array as check_array, check_random_state as check_random_state
from ..utils._array_api import get_namespace as get_namespace
from ..utils._seq_dataset import ArrayDataset32 as ArrayDataset32, ArrayDataset64, CSRDataset32 as CSRDataset32, CSRDataset64
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from ..utils.parallel import Parallel as Parallel, delayed as delayed
from ..utils.sparsefuncs import inplace_column_scale as inplace_column_scale, mean_variance_axis as mean_variance_axis
from ..utils.validation import FLOAT_DTYPES as FLOAT_DTYPES, check_is_fitted as check_is_fitted
from ._stochastic_gradient import SGDClassifier

LinearRegression_Self = TypeVar("LinearRegression_Self", bound="LinearRegression")
SparseCoefMixin_Self = TypeVar("SparseCoefMixin_Self", bound="SparseCoefMixin")

import numbers
import warnings

import numpy as np
import scipy.sparse as sp

# TODO: bayesian_ridge_regression and bayesian_regression_ard
# should be squashed into its respective objects.

SPARSE_INTERCEPT_DECAY: float = ...

def make_dataset(
    X: MatrixLike,
    y: ArrayLike,
    sample_weight: ArrayLike,
    random_state: None | Int | RandomState = None,
) -> tuple[ArrayDataset64 | CSRDataset64, float]: ...

class LinearModel(BaseEstimator, metaclass=ABCMeta):
    @abstractmethod
    def fit(self, X, y): ...
    def predict(self, X: MatrixLike) -> ndarray: ...

# XXX Should this derive from LinearModel? It should be a mixin, not an ABC.
# Maybe the n_features checking can be moved to LinearModel.
class LinearClassifierMixin(ClassifierMixin):
    def decision_function(self, X: MatrixLike | ArrayLike) -> ndarray: ...
    def predict(self, X: MatrixLike | ArrayLike) -> ndarray: ...

class SparseCoefMixin:
    def densify(self: SparseCoefMixin_Self) -> SparseCoefMixin_Self: ...
    def sparsify(self: SparseCoefMixin_Self) -> SGDClassifier | SparseCoefMixin_Self: ...

class LinearRegression(MultiOutputMixin, RegressorMixin, LinearModel):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    intercept_: float | ndarray = ...
    singular_: ndarray = ...
    rank_: int = ...
    coef_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        copy_X: bool = True,
        n_jobs: None | Int = None,
        positive: bool = False,
    ) -> None: ...
    def fit(
        self: LinearRegression_Self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> LinearRegression_Self: ...
