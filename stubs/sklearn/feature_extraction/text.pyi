from typing import Any, Callable, ClassVar, Iterable, Literal, Mapping, TypeVar
from operator import itemgetter as itemgetter
from collections import defaultdict as defaultdict
from ..utils.validation import (
    check_is_fitted as check_is_fitted,
    check_array as check_array,
    FLOAT_DTYPES as FLOAT_DTYPES,
)
from ..exceptions import NotFittedError as NotFittedError
from numpy import ndarray
from ..utils._param_validation import (
    StrOptions as StrOptions,
    Interval as Interval,
    HasMethods as HasMethods,
)
from numbers import Integral as Integral, Real as Real
from functools import partial
from ._stop_words import ENGLISH_STOP_WORDS
from ..base import BaseEstimator, TransformerMixin, OneToOneFeatureMixin
from scipy.sparse import spmatrix
from ._hash import FeatureHasher as FeatureHasher
from .._typing import ArrayLike, Int, MatrixLike, Float
from collections.abc import Mapping
from ..preprocessing import normalize as normalize

TfidfVectorizer_Self = TypeVar("TfidfVectorizer_Self", bound="TfidfVectorizer")
HashingVectorizer_Self = TypeVar("HashingVectorizer_Self", bound="HashingVectorizer")
CountVectorizer_Self = TypeVar("CountVectorizer_Self", bound="CountVectorizer")
TfidfTransformer_Self = TypeVar("TfidfTransformer_Self", bound="TfidfTransformer")

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

    def build_preprocessor(self) -> Callable | partial:
        ...

    def build_tokenizer(self) -> Callable:
        ...

    def get_stop_words(self) -> frozenset | None | list:
        ...

    def build_analyzer(self) -> Callable | partial:
        ...


class HashingVectorizer(
    TransformerMixin, _VectorizerMixin, BaseEstimator, auto_wrap_output_keys=None
):

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        input: Literal["filename", "file", "content", "content"] = "content",
        encoding: str = "utf-8",
        decode_error: Literal["strict", "ignore", "replace", "strict"] = "strict",
        strip_accents: None | Literal["ascii", "unicode"] | Callable = None,
        lowercase: bool = True,
        preprocessor: None | Callable = None,
        tokenizer: None | Callable = None,
        stop_words: None | str | ArrayLike = None,
        token_pattern: None | str = r"(?u)\b\w\w+\b",
        ngram_range: tuple[float, float] = ...,
        analyzer: Literal["word", "char", "char_wb", "word"] | Callable = "word",
        n_features: Int = ...,
        binary: bool = False,
        norm: Literal["l1", "l2", "l2"] = "l2",
        alternate_sign: bool = True,
        dtype=...,
    ) -> None:
        ...

    def partial_fit(
        self: HashingVectorizer_Self, X: MatrixLike, y: Any = None
    ) -> HashingVectorizer_Self:
        ...

    def fit(
        self: HashingVectorizer_Self, X: list[str] | MatrixLike, y: Any = None
    ) -> HashingVectorizer_Self:
        ...

    def transform(self, X: Iterable[str]) -> spmatrix:
        ...

    def fit_transform(self, X: list[str] | Iterable[str], y: Any = None) -> spmatrix:
        ...


class CountVectorizer(_VectorizerMixin, BaseEstimator):
    stop_words_: set = ...
    fixed_vocabulary_: bool = ...
    vocabulary_: dict = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        input: Literal["filename", "file", "content", "content"] = "content",
        encoding: str = "utf-8",
        decode_error: Literal["strict", "ignore", "replace", "strict"] = "strict",
        strip_accents: None | Literal["ascii", "unicode"] | Callable = None,
        lowercase: bool = True,
        preprocessor: None | Callable = None,
        tokenizer: None | Callable = None,
        stop_words: None | str | ArrayLike = None,
        token_pattern: None | str = r"(?u)\b\w\w+\b",
        ngram_range: tuple[float, float] = ...,
        analyzer: Literal["word", "char", "char_wb", "word"] | Callable = "word",
        max_df: float | int = 1.0,
        min_df: float | int = 1,
        max_features: None | Int = None,
        vocabulary: Iterable | None | Mapping = None,
        binary: bool = False,
        dtype=...,
    ) -> None:
        ...

    def fit(
        self: CountVectorizer_Self, raw_documents: Iterable, y=None
    ) -> CountVectorizer_Self:
        ...

    def fit_transform(
        self,
        raw_documents: list[str] | ndarray | Iterable,
        y: None | ndarray | list[Int] = None,
    ) -> ndarray | spmatrix:
        ...

    def transform(self, raw_documents: list[str] | ndarray | Iterable) -> spmatrix:
        ...

    def inverse_transform(self, X: MatrixLike | ArrayLike) -> list[ndarray]:
        ...

    def get_feature_names_out(self, input_features: None | ArrayLike = None) -> ndarray:
        ...


class TfidfTransformer(
    OneToOneFeatureMixin, TransformerMixin, BaseEstimator, auto_wrap_output_keys=None
):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        norm: None | Literal["l1", "l2", "l2"] = "l2",
        use_idf: bool = True,
        smooth_idf: bool = True,
        sublinear_tf: bool = False,
    ) -> None:
        ...

    def fit(
        self: TfidfTransformer_Self, X: MatrixLike, y: None | ndarray | list[Int] = None
    ) -> TfidfTransformer_Self:
        ...

    def transform(self, X: MatrixLike, copy: bool = True) -> spmatrix:
        ...

    @property
    def idf_(self) -> ndarray:
        ...

    @idf_.setter
    def idf_(self, value) -> ndarray:
        ...


class TfidfVectorizer(CountVectorizer):
    stop_words_: set = ...
    fixed_vocabulary_: bool = ...
    vocabulary_: dict = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        input: Literal["filename", "file", "content", "content"] = "content",
        encoding: str = "utf-8",
        decode_error: Literal["strict", "ignore", "replace", "strict"] = "strict",
        strip_accents: None | Literal["ascii", "unicode"] | Callable = None,
        lowercase: bool = True,
        preprocessor: None | Callable = None,
        tokenizer: None | Callable = None,
        analyzer: Literal["word", "char", "char_wb", "word"] | Callable = "word",
        stop_words: None | str | ArrayLike = None,
        token_pattern: str = r"(?u)\b\w\w+\b",
        ngram_range: tuple[float, float] = ...,
        max_df: Float = 1.0,
        min_df: Float = 1,
        max_features: None | Int = None,
        vocabulary: Iterable | None | Mapping = None,
        binary: bool = False,
        dtype=...,
        norm: None | Literal["l1", "l2", "l2"] = "l2",
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

    def fit(
        self: TfidfVectorizer_Self, raw_documents: Iterable, y=None
    ) -> TfidfVectorizer_Self:
        ...

    def fit_transform(
        self, raw_documents: list[str] | ndarray | Iterable, y: None | ndarray = None
    ) -> spmatrix:
        ...

    def transform(self, raw_documents: list[str] | ndarray | Iterable) -> spmatrix:
        ...
