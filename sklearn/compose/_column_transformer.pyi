from typing import ClassVar, Literal, Sequence, TypeVar
from scipy import sparse as sparse
from itertools import chain as chain
from ..base import BaseEstimator
from ..preprocessing import FunctionTransformer as FunctionTransformer
from scipy.sparse import spmatrix
from ..utils._bunch import Bunch
from ..utils.parallel import delayed as delayed, Parallel as Parallel
from ..utils.validation import (
    check_array as check_array,
    check_is_fitted as check_is_fitted,
)
from collections import Counter as Counter
from numpy import ndarray, dtype
from ..base import clone as clone, TransformerMixin
from ..utils import check_pandas_support as check_pandas_support
from ..utils.metaestimators import _BaseComposition
from .._typing import Float, Int, ArrayLike, MatrixLike

ColumnTransformer_Self = TypeVar("ColumnTransformer_Self", bound="ColumnTransformer")


import numpy as np


__all__ = ["ColumnTransformer", "make_column_transformer", "make_column_selector"]


_ERR_MSG_1DCOLUMN: str = ...


class ColumnTransformer(TransformerMixin, _BaseComposition):
    n_features_in_: int = ...
    output_indices_: dict = ...
    sparse_output_: bool = ...
    transformers_: list = ...

    _required_parameters: ClassVar[list] = ...

    def __init__(
        self,
        transformers: Sequence[tuple],
        *,
        remainder: Literal["drop", "passthrough", "drop"] | BaseEstimator = "drop",
        sparse_threshold: Float = 0.3,
        n_jobs: None | Int = None,
        transformer_weights: None | dict = None,
        verbose: bool = False,
        verbose_feature_names_out: bool = True,
    ) -> None:
        ...

    def set_output(
        self, *, transform: None | Literal["default", "pandas"] = None
    ) -> BaseEstimator:
        ...

    def get_params(self, deep: bool = True) -> dict:
        ...

    def set_params(self: ColumnTransformer_Self, **kwargs) -> ColumnTransformer_Self:
        ...

    @property
    def named_transformers_(self) -> Bunch:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...

    def fit(
        self: ColumnTransformer_Self, X: MatrixLike, y: None | ArrayLike = None
    ) -> ColumnTransformer_Self:
        ...

    def fit_transform(
        self, X: MatrixLike, y: None | ArrayLike = None
    ) -> ndarray | spmatrix:
        ...

    def transform(self, X: MatrixLike) -> ndarray | spmatrix:
        ...


def make_column_transformer(
    *transformers,
    remainder: Literal["drop", "passthrough", "drop"] | BaseEstimator = "drop",
    sparse_threshold: Float = 0.3,
    n_jobs: None | Int = None,
    verbose: bool = False,
    verbose_feature_names_out: bool = True,
) -> ColumnTransformer:
    ...


class make_column_selector:
    def __init__(
        self,
        pattern: None | str = None,
        *,
        dtype_include: Sequence[dtype] | None | dtype = None,
        dtype_exclude: Sequence[dtype] | None | dtype = None,
    ) -> None:
        ...

    def __call__(self, df: MatrixLike) -> list[str]:
        ...
