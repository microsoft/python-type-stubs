from typing import Literal, Sequence
from ..utils._bunch import Bunch
from .._typing import Estimator, Float, Int, ArrayLike, MatrixLike
from ..preprocessing import FunctionTransformer as FunctionTransformer
from scipy.sparse import spmatrix
from itertools import chain as chain
from ..utils import check_pandas_support as check_pandas_support
from scipy import sparse as sparse
from ..utils.validation import (
    check_array as check_array,
    check_is_fitted as check_is_fitted,
)
from scipy.sparse._csr import csr_matrix
from numpy import ndarray, dtype
from ..base import clone as clone, TransformerMixin
from pandas.core.frame import DataFrame
from collections import Counter as Counter
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from ..utils.metaestimators import _BaseComposition

import numpy as np


__all__ = ["ColumnTransformer", "make_column_transformer", "make_column_selector"]


_ERR_MSG_1DCOLUMN: str = ...


class ColumnTransformer(TransformerMixin, _BaseComposition):

    _required_parameters: list = ...

    def __init__(
        self,
        transformers: Sequence[tuple],
        *,
        remainder: Estimator | Literal["drop", "passthrough", "drop"] = "drop",
        sparse_threshold: Float = 0.3,
        n_jobs: None | Int = None,
        transformer_weights: dict | None = None,
        verbose: bool = False,
        verbose_feature_names_out: bool = True,
    ) -> None:
        ...

    def set_output(
        self, *, transform: Literal["default", "pandas"] | None = None
    ) -> Estimator | ColumnTransformer:
        ...

    def get_params(self, deep: bool = True) -> dict:
        ...

    def set_params(self, **kwargs) -> ColumnTransformer:
        ...

    @property
    def named_transformers_(self) -> Bunch:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...

    def fit(self, X: MatrixLike, y: None | ArrayLike = None) -> ColumnTransformer:
        ...

    def fit_transform(
        self, X: MatrixLike, y: None | ArrayLike = None
    ) -> csr_matrix | spmatrix | DataFrame | ndarray:
        ...

    def transform(self, X: MatrixLike) -> csr_matrix | spmatrix | DataFrame | ndarray:
        ...


def make_column_transformer(
    *transformers,
    remainder: Estimator | Literal["drop", "passthrough", "drop"] = "drop",
    sparse_threshold: Float = 0.3,
    n_jobs: None | Int = None,
    verbose: bool = False,
    verbose_feature_names_out: bool = True,
) -> ColumnTransformer:
    ...


class make_column_selector:
    def __init__(
        self,
        pattern: str | None = None,
        *,
        dtype_include: dtype | Sequence[np.dtype] | None = None,
        dtype_exclude: dtype | Sequence[np.dtype] | None = None,
    ) -> None:
        ...

    def __call__(self, df: MatrixLike) -> list[str]:
        ...
