from typing import ClassVar, TypeVar
from scipy import linalg as linalg, optimize as optimize, sparse
from ..utils.extmath import safe_sparse_dot as safe_sparse_dot
from numpy.random.mtrand import RandomState
from ..utils._array_api import get_namespace as get_namespace
from ..utils.sparsefuncs import (
    mean_variance_axis as mean_variance_axis,
    inplace_column_scale as inplace_column_scale,
)
from scipy.special import expit as expit
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from ..utils._seq_dataset import (
    ArrayDataset32 as ArrayDataset32,
    CSRDataset32 as CSRDataset32,
    ArrayDataset64,
    CSRDataset64,
)
from ..utils.validation import (
    FLOAT_DTYPES as FLOAT_DTYPES,
    check_is_fitted as check_is_fitted,
)
from scipy.sparse.linalg import lsqr as lsqr
from abc import ABCMeta, abstractmethod
from numpy import ndarray
from numbers import Integral as Integral
from ..base import BaseEstimator, ClassifierMixin, RegressorMixin, MultiOutputMixin
from ..utils import check_array as check_array, check_random_state as check_random_state
from ._stochastic_gradient import SGDClassifier
from .._typing import MatrixLike, ArrayLike, Int

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
) -> tuple[ArrayDataset64 | CSRDataset64, float]:
    ...


class LinearModel(BaseEstimator, metaclass=ABCMeta):
    @abstractmethod
    def fit(self, X, y):
        ...

    def predict(self, X: MatrixLike) -> ndarray:
        ...


# XXX Should this derive from LinearModel? It should be a mixin, not an ABC.
# Maybe the n_features checking can be moved to LinearModel.
class LinearClassifierMixin(ClassifierMixin):
    def decision_function(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...

    def predict(self, X: MatrixLike | ArrayLike) -> ndarray:
        ...


class SparseCoefMixin:
    def densify(self: SparseCoefMixin_Self) -> SparseCoefMixin_Self:
        ...

    def sparsify(self: SparseCoefMixin_Self) -> SGDClassifier | SparseCoefMixin_Self:
        ...


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
    ) -> None:
        ...

    def fit(
        self: LinearRegression_Self,
        X: MatrixLike | ArrayLike,
        y: MatrixLike | ArrayLike,
        sample_weight: None | ArrayLike = None,
    ) -> LinearRegression_Self:
        ...
