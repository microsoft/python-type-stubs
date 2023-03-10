from typing import Any, Callable, Iterable, Literal, Mapping
from .._typing import ArrayLike, Int, MatrixLike, Float
from operator import itemgetter as itemgetter
from ..preprocessing import normalize as normalize
from scipy.sparse import spmatrix
from ..utils._param_validation import (
    StrOptions as StrOptions,
    Interval as Interval,
    HasMethods as HasMethods,
)
from ._stop_words import ENGLISH_STOP_WORDS
from ._hash import FeatureHasher as FeatureHasher
from ..utils.validation import (
    check_is_fitted as check_is_fitted,
    check_array as check_array,
    FLOAT_DTYPES as FLOAT_DTYPES,
)
from scipy.sparse._csr import csr_matrix
from numpy import ndarray
from collections.abc import Iterable
from ..exceptions import NotFittedError as NotFittedError
from ..base import BaseEstimator, TransformerMixin, OneToOneFeatureMixin
from functools import partial
from collections import defaultdict as defaultdict
from numbers import Integral as Integral, Real as Real

# Authors: Olivier Grisel <olivier.grisel@ensta.org>
#          Mathieu Blondel <mathieu@mblondel.org>
#          Lars Buitinck
#          Robert Layton <robertlayton@gmail.com>
#          Jochen Wersdörfer <jochen@wersdoerfer.de>
#          Roman Sinayev <roman.sinayev@gmail.com>
#
# License: BSD 3 clause

import array
import re
import unicodedata
import warnings

import numpy as np
import scipy.sparse as sp


__all__ = [
    "HashingVectorizer",
    "CountVectorizer",
    "ENGLISH_STOP_WORDS",
    "TfidfTransformer",
    "TfidfVectorizer",
    "strip_accents_ascii",
    "strip_accents_unicode",
    "strip_tags",
]


def strip_accents_unicode(s: str) -> str:
    ...


def strip_accents_ascii(s: str) -> str:
    ...


def strip_tags(s: str) -> str:
    ...


class _VectorizerMixin:

    _white_spaces = ...

    def decode(self, doc: bytes | str) -> str:
        ...

    def build_preprocessor(self) -> partial | Callable:
        ...

    def build_tokenizer(self) -> Callable:
        ...

    def get_stop_words(self) -> frozenset | None | list:
        ...

    def build_analyzer(self) -> partial | Callable:
        ...


class HashingVectorizer(
    TransformerMixin, _VectorizerMixin, BaseEstimator, auto_wrap_output_keys=None
):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        input: Literal["filename", "file", "content", "content"] = "content",
        encoding: str = "utf-8",
        decode_error: Literal["strict", "ignore", "replace", "strict"] = "strict",
        strip_accents: None | Callable | Literal["ascii", "unicode"] = None,
        lowercase: bool = True,
        preprocessor: None | Callable = None,
        tokenizer: None | Callable = None,
        stop_words: str | None | ArrayLike = None,
        token_pattern: str | None = r"(?u)\b\w\w+\b",
        ngram_range: tuple[float, float] = ...,
        analyzer: Literal["word", "char", "char_wb", "word"] | Callable = "word",
        n_features: Int = ...,
        binary: bool = False,
        norm: Literal["l1", "l2", "l2"] = "l2",
        alternate_sign: bool = True,
        dtype=...,
    ) -> None:
        ...

    def partial_fit(self, X: MatrixLike, y: Any = None) -> Any:
        ...

    def fit(self, X: MatrixLike | list[str], y: Any = None) -> Any:
        ...

    def transform(self, X: Iterable[str]) -> spmatrix | csr_matrix:
        ...

    def fit_transform(
        self, X: Iterable[str] | list[str], y: Any = None
    ) -> spmatrix | csr_matrix:
        ...


class CountVectorizer(_VectorizerMixin, BaseEstimator):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        input: Literal["filename", "file", "content", "content"] = "content",
        encoding: str = "utf-8",
        decode_error: Literal["strict", "ignore", "replace", "strict"] = "strict",
        strip_accents: None | Callable | Literal["ascii", "unicode"] = None,
        lowercase: bool = True,
        preprocessor: None | Callable = None,
        tokenizer: None | Callable = None,
        stop_words: str | None | ArrayLike = None,
        token_pattern: str | None = r"(?u)\b\w\w+\b",
        ngram_range: tuple[float, float] = ...,
        analyzer: Literal["word", "char", "char_wb", "word"] | Callable = "word",
        max_df: int | float = 1.0,
        min_df: int | float = 1,
        max_features: None | Int = None,
        vocabulary: Iterable | Mapping | None = None,
        binary: bool = False,
        dtype=...,
    ) -> None:
        ...

    def fit(self, raw_documents: Iterable, y=None) -> Any:
        ...

    def fit_transform(
        self,
        raw_documents: Iterable | list[str] | ndarray,
        y: list[Int] | None | ndarray = None,
    ) -> spmatrix | ndarray | csr_matrix:
        ...

    def transform(
        self, raw_documents: Iterable | list[str] | ndarray
    ) -> spmatrix | csr_matrix:
        ...

    def inverse_transform(self, X: MatrixLike | ArrayLike) -> list[ndarray]:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...


class TfidfTransformer(
    OneToOneFeatureMixin, TransformerMixin, BaseEstimator, auto_wrap_output_keys=None
):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        norm: Literal["l1", "l2", "l2"] | None = "l2",
        use_idf: bool = True,
        smooth_idf: bool = True,
        sublinear_tf: bool = False,
    ) -> None:
        ...

    def fit(self, X: MatrixLike, y: list[Int] | None | ndarray = None) -> Any:
        ...

    def transform(self, X: MatrixLike, copy: bool = True) -> spmatrix | csr_matrix:
        ...

    @property
    def idf_(self) -> ndarray:
        ...

    @idf_.setter
    def idf_(self, value) -> ndarray:
        ...


class TfidfVectorizer(CountVectorizer):

    _parameter_constraints: dict = ...

    def __init__(
        self,
        *,
        input: Literal["filename", "file", "content", "content"] = "content",
        encoding: str = "utf-8",
        decode_error: Literal["strict", "ignore", "replace", "strict"] = "strict",
        strip_accents: None | Callable | Literal["ascii", "unicode"] = None,
        lowercase: bool = True,
        preprocessor: None | Callable = None,
        tokenizer: None | Callable = None,
        analyzer: Literal["word", "char", "char_wb", "word"] | Callable = "word",
        stop_words: str | None | ArrayLike = None,
        token_pattern: str = r"(?u)\b\w\w+\b",
        ngram_range: tuple[float, float] = ...,
        max_df: Float = 1.0,
        min_df: Float = 1,
        max_features: None | Int = None,
        vocabulary: Iterable | Mapping | None = None,
        binary: bool = False,
        dtype=...,
        norm: Literal["l1", "l2", "l2"] | None = "l2",
        use_idf: bool = True,
        smooth_idf: bool = True,
        sublinear_tf: bool = False,
    ) -> None:
        ...

    # Broadcast the TF-IDF parameters to the underlying transformer instance
    # for easy grid search and repr

    @property
    def idf_(self) -> ndarray:
        ...

    @idf_.setter
    def idf_(self, value) -> ndarray:
        ...

    def fit(self, raw_documents: Iterable, y=None) -> Any:
        ...

    def fit_transform(
        self, raw_documents: Iterable | list[str] | ndarray, y: None | ndarray = None
    ) -> spmatrix | csr_matrix:
        ...

    def transform(
        self, raw_documents: Iterable | list[str] | ndarray
    ) -> spmatrix | csr_matrix:
        ...
