from typing import Any, ClassVar, Iterable, Literal, Sequence, TypeVar
from scipy import sparse as sparse
from .utils.validation import (
    check_memory as check_memory,
    check_is_fitted as check_is_fitted,
)
from itertools import islice as islice
from .base import BaseEstimator
from joblib import Memory
from .utils.metaestimators import available_if as available_if, _BaseComposition
from pandas.core.frame import DataFrame
from scipy.sparse import spmatrix
from .utils._bunch import Bunch
from collections import defaultdict as defaultdict
from .base import clone as clone, TransformerMixin
from numpy import ndarray
from .exceptions import NotFittedError as NotFittedError
from ._typing import Int, MatrixLike, ArrayLike, Float
from .preprocessing import FunctionTransformer as FunctionTransformer
from pandas.core.series import Series
from .utils import check_pandas_support as check_pandas_support
from .utils.parallel import delayed as delayed, Parallel as Parallel

FeatureUnion_Self = TypeVar("FeatureUnion_Self", bound="FeatureUnion")
Pipeline_Self = TypeVar("Pipeline_Self", bound="Pipeline")


import numpy as np

__all__ = ["Pipeline", "FeatureUnion", "make_pipeline", "make_union"]


class Pipeline(_BaseComposition):

    # BaseEstimator interface
    _required_parameters: ClassVar[list] = ...

    def __init__(
        self,
        steps: Sequence[tuple],
        *,
        memory: None | Memory | str = None,
        verbose: bool = False
    ) -> None:
        ...

    def set_output(
        self, *, transform: None | Literal["default", "pandas"] = None
    ) -> BaseEstimator:
        ...

    def get_params(self, deep: bool = True) -> dict[str, Any]:
        ...

    def set_params(self: Pipeline_Self, **kwargs) -> Pipeline_Self:
        ...

    def __len__(self) -> int:
        ...

    def __getitem__(self, ind: slice | int):
        ...

    @property
    def named_steps(self) -> Bunch:
        ...

    def fit(
        self: Pipeline_Self,
        X: list[str] | ndarray | Iterable | DataFrame,
        y: list[Int] | list[int] | Iterable | None | Series | ndarray = None,
        **fit_params
    ) -> Pipeline_Self:
        ...

    def fit_transform(
        self, X: Iterable, y: Iterable | Series | None | ndarray = None, **fit_params
    ) -> ndarray:
        ...

    def predict(
        self, X: list[str] | ndarray | Iterable | DataFrame, **predict_params
    ) -> ndarray | tuple[ndarray, ndarray]:
        ...

    def fit_predict(
        self, X: Iterable, y: Iterable | None = None, **fit_params
    ) -> ndarray:
        ...

    def predict_proba(
        self, X: Iterable | ndarray | DataFrame, **predict_proba_params
    ) -> ndarray:
        ...

    def decision_function(self, X: Iterable | ndarray | DataFrame) -> ndarray:
        ...

    def score_samples(self, X: Iterable) -> ndarray:
        ...

    def predict_log_proba(self, X: Iterable, **predict_log_proba_params) -> ndarray:
        ...

    def transform(self, X: Iterable | ndarray | DataFrame) -> ndarray:
        ...

    def inverse_transform(self, Xt: MatrixLike) -> ndarray:
        ...

    def score(
        self,
        X: list[str] | ndarray | Iterable | DataFrame,
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
    *steps, memory: None | Memory | str = None, verbose: bool = False
) -> Pipeline:
    ...


class FeatureUnion(TransformerMixin, _BaseComposition):

    _required_parameters: ClassVar[list] = ...

    def __init__(
        self,
        transformer_list: Sequence[tuple[str, TransformerMixin | Pipeline]],
        *,
        n_jobs: None | Int = None,
        transformer_weights: None | dict = None,
        verbose: bool = False
    ) -> None:
        ...

    def set_output(
        self, *, transform: None | Literal["default", "pandas"] = None
    ) -> BaseEstimator:
        ...

    @property
    def named_transformers(self) -> Bunch:
        ...

    def get_params(self, deep: bool = True) -> dict[str, Any]:
        ...

    def set_params(self: FeatureUnion_Self, **kwargs) -> FeatureUnion_Self:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...

    def fit(
        self: FeatureUnion_Self,
        X: Iterable | ArrayLike,
        y: None | MatrixLike = None,
        **fit_params
    ) -> FeatureUnion_Self:
        ...

    def fit_transform(
        self,
        X: Iterable | ArrayLike | DataFrame,
        y: Series | None | MatrixLike = None,
        **fit_params
    ) -> ndarray | spmatrix:
        ...

    def transform(self, X: Iterable | ArrayLike | DataFrame) -> ndarray | spmatrix:
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
