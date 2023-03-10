from typing import Any, Iterable, Literal, Sequence
from .utils._bunch import Bunch
from ._typing import Estimator, Int, MatrixLike, ArrayLike, Float
from .base import clone as clone
from scipy.sparse import spmatrix
from .base import TransformerMixin
from .exceptions import NotFittedError as NotFittedError
from joblib import Memory
from itertools import islice as islice
from .utils.metaestimators import available_if as available_if, _BaseComposition
from pandas.core.series import Series
from .utils import check_pandas_support as check_pandas_support
from scipy import sparse as sparse
from scipy.sparse._csr import csr_matrix
from numpy import ndarray
from .utils.parallel import delayed as delayed, Parallel as Parallel
from .preprocessing import FunctionTransformer as FunctionTransformer
from collections.abc import Iterable
from pandas.core.frame import DataFrame
from collections import defaultdict as defaultdict
from .utils.validation import (
    check_memory as check_memory,
    check_is_fitted as check_is_fitted,
)

import numpy as np

__all__ = ["Pipeline", "FeatureUnion", "make_pipeline", "make_union"]


class Pipeline(_BaseComposition):

    # BaseEstimator interface
    _required_parameters: list = ...

    def __init__(
        self,
        steps: Sequence[tuple],
        *,
        memory: Memory | str | None = None,
        verbose: bool = False
    ) -> None:
        ...

    def set_output(
        self, *, transform: Literal["default", "pandas"] | None = None
    ) -> Pipeline | Estimator:
        ...

    def get_params(self, deep: bool = True) -> dict[str, Any]:
        ...

    def set_params(self, **kwargs) -> Any:
        ...

    def __len__(self) -> int:
        ...

    def __getitem__(self, ind: slice | int):
        ...

    @property
    def named_steps(self) -> Bunch:
        ...

    def fit(
        self,
        X: Iterable | DataFrame | list[str] | ndarray,
        y: list[Int] | list[int] | Iterable | ndarray | None | Series = None,
        **fit_params
    ) -> Any:
        ...

    def fit_transform(
        self,
        X: csr_matrix | list[str] | DataFrame | Iterable | ndarray,
        y: Iterable | Series | None | ndarray = None,
        **fit_params
    ) -> csr_matrix | DataFrame | ndarray:
        ...

    def predict(
        self, X: Iterable | DataFrame | list[str] | ndarray, **predict_params
    ) -> tuple[ndarray, ndarray] | ndarray:
        ...

    def fit_predict(
        self, X: Iterable, y: Iterable | None = None, **fit_params
    ) -> ndarray:
        ...

    def predict_proba(
        self, X: Iterable | DataFrame | ndarray, **predict_proba_params
    ) -> ndarray:
        ...

    def decision_function(self, X: Iterable | DataFrame | ndarray) -> ndarray:
        ...

    def score_samples(self, X: Iterable) -> ndarray:
        ...

    def predict_log_proba(self, X: Iterable, **predict_log_proba_params) -> ndarray:
        ...

    def transform(
        self, X: Iterable | DataFrame | ndarray
    ) -> csr_matrix | DataFrame | ndarray:
        ...

    def inverse_transform(self, Xt: MatrixLike) -> ndarray:
        ...

    def score(
        self,
        X: Iterable | DataFrame | list[str] | ndarray,
        y: Iterable | Series | None | ndarray = None,
        sample_weight: None | ArrayLike = None,
    ) -> Float:
        ...

    @property
    def classes_(self) -> ndarray:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...

    @property
    def n_features_in_(self) -> int:
        ...

    @property
    def feature_names_in_(self) -> ndarray:
        ...

    def __sklearn_is_fitted__(self) -> bool:
        ...


def make_pipeline(
    *steps, memory: Memory | str | None = None, verbose: bool = False
) -> Pipeline:
    ...


class FeatureUnion(TransformerMixin, _BaseComposition):

    _required_parameters: list = ...

    def __init__(
        self,
        transformer_list: Sequence[tuple[str, TransformerMixin]],
        *,
        n_jobs: None | Int = None,
        transformer_weights: dict | None = None,
        verbose: bool = False
    ) -> None:
        ...

    def set_output(
        self, *, transform: Literal["default", "pandas"] | None = None
    ) -> Estimator:
        ...

    @property
    def named_transformers(self) -> Bunch:
        ...

    def get_params(self, deep: bool = True) -> dict[str, Any]:
        ...

    def set_params(self, **kwargs) -> Any:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...

    def fit(
        self, X: Iterable | ArrayLike, y: None | MatrixLike = None, **fit_params
    ) -> Any:
        ...

    def fit_transform(
        self,
        X: Iterable | DataFrame | ArrayLike,
        y: None | MatrixLike | Series = None,
        **fit_params
    ) -> spmatrix | ndarray:
        ...

    def transform(self, X: Iterable | DataFrame | ArrayLike) -> spmatrix | ndarray:
        ...

    @property
    def n_features_in_(self) -> int:
        ...

    def __sklearn_is_fitted__(self):
        ...


def make_union(
    *transformers, n_jobs: None | Int = None, verbose: bool = False
) -> FeatureUnion:
    ...
