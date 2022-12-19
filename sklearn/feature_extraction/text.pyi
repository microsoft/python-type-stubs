from numpy import int64, ndarray
from collections.abc import Iterable
from typing import (
    Dict,
    List,
    Optional,
    Set,
    Tuple,
    Union,
    Callable,
    Literal,
    Any,
    Mapping,
)
from numpy.typing import ArrayLike, NDArray

# Authors: Olivier Grisel <olivier.grisel@ensta.org>
#          Mathieu Blondel <mathieu@mblondel.org>
#          Lars Buitinck
#          Robert Layton <robertlayton@gmail.com>
#          Jochen Wersdörfer <jochen@wersdoerfer.de>
#          Roman Sinayev <roman.sinayev@gmail.com>
#
# License: BSD 3 clause

import array
from collections import defaultdict
from collections.abc import Mapping
from functools import partial
import numbers
from operator import itemgetter
import re
import unicodedata
import warnings

import numpy as np
import scipy.sparse as sp

from ..base import BaseEstimator, TransformerMixin, _OneToOneFeatureMixin
from ..preprocessing import normalize
from ._hash import FeatureHasher
from ._stop_words import ENGLISH_STOP_WORDS
from ..utils.validation import check_is_fitted, check_array, FLOAT_DTYPES, check_scalar
from ..utils.deprecation import deprecated
from ..utils import _IS_32BIT
from ..exceptions import NotFittedError
from scipy.sparse._csr import csr_matrix
from sklearn.feature_extraction._hash import FeatureHasher

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

def _preprocess(doc: str, accent_function: None = None, lower: bool = False) -> str: ...
def _analyze(
    doc: str,
    analyzer: None = None,
    tokenizer: Optional[Callable] = None,
    ngrams: Optional[Callable] = None,
    preprocessor: Optional[partial] = None,
    decoder: Optional[Callable] = None,
    stop_words: Optional[frozenset] = None,
) -> List[Union[str, Any]]: ...
def strip_accents_unicode(s: str): ...
def strip_accents_ascii(s: str) -> str: ...
def strip_tags(s: str) -> str: ...
def _check_stop_list(stop: Optional[str]) -> Optional[frozenset]: ...

class _VectorizerMixin:

    _white_spaces = ...

    def decode(self, doc: bytes | str) -> str: ...
    def _word_ngrams(self, tokens: List[Union[str, Any]], stop_words: Optional[frozenset] = None) -> List[Union[str, Any]]: ...
    def _char_ngrams(self, text_document): ...
    def _char_wb_ngrams(self, text_document): ...
    def build_preprocessor(self) -> Callable: ...
    def build_tokenizer(self) -> Callable: ...
    def get_stop_words(self) -> list | None: ...
    def _check_stop_words_consistency(
        self, stop_words: Optional[frozenset], preprocess: partial, tokenize: Callable
    ) -> Optional[bool]: ...
    def build_analyzer(self) -> Callable: ...
    def _validate_vocabulary(self) -> None: ...
    def _check_vocabulary(self) -> None: ...
    def _validate_params(self) -> None: ...
    def _warn_for_unused_params(self) -> None: ...

class HashingVectorizer(TransformerMixin, _VectorizerMixin, BaseEstimator):
    def __init__(
        self,
        *,
        input: Literal["filename", "file", "content"] = "content",
        encoding: str = "utf-8",
        decode_error: Literal["strict", "ignore", "replace"] = "strict",
        strip_accents: Literal["ascii", "unicode"] | None = None,
        lowercase: bool = True,
        preprocessor: Callable | None = None,
        tokenizer: Callable | None = None,
        stop_words: Literal["english"] | ArrayLike | None = None,
        token_pattern: str = r"(?u)\b\w\w+\b",
        ngram_range: tuple[float, float] = ...,
        analyzer: Literal["word", "char", "char_wb"] | Callable = "word",
        n_features: int = ...,
        binary: bool = False,
        norm: Literal["l1", "l2"] = "l2",
        alternate_sign: bool = True,
        dtype: type = ...,
    ) -> None: ...
    def partial_fit(self, X: NDArray, y=None) -> Any: ...
    def fit(self, X: NDArray, y: None = None) -> "HashingVectorizer": ...
    def transform(self, X: Iterable) -> NDArray: ...
    def fit_transform(self, X: Iterable, y: None = None) -> NDArray: ...
    def _get_hasher(self) -> FeatureHasher: ...
    def _more_tags(self): ...

def _document_frequency(X: csr_matrix) -> ndarray: ...

class CountVectorizer(_VectorizerMixin, BaseEstimator):
    def __init__(
        self,
        *,
        input: Literal["filename", "file", "content"] = "content",
        encoding: str = "utf-8",
        decode_error: Literal["strict", "ignore", "replace"] = "strict",
        strip_accents: Literal["ascii", "unicode"] | None = None,
        lowercase: bool = True,
        preprocessor: Callable | None = None,
        tokenizer: Callable | None = None,
        stop_words: Literal["english"] | ArrayLike | None = None,
        token_pattern: str = r"(?u)\b\w\w+\b",
        ngram_range: tuple[float, float] = ...,
        analyzer: Literal["word", "char", "char_wb"] | Callable = "word",
        max_df: float | int = 1.0,
        min_df: float | int = 1,
        max_features: int | None = None,
        vocabulary: Mapping | Iterable | None = None,
        binary: bool = False,
        dtype: type = ...,
    ) -> None: ...
    def _sort_features(self, X: csr_matrix, vocabulary: Dict[str, Union[int, int64]]) -> csr_matrix: ...
    def _limit_features(
        self,
        X: csr_matrix,
        vocabulary: Dict[str, int],
        high: Optional[float] = None,
        low: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> Union[Tuple[csr_matrix, Set[str]], Tuple[csr_matrix, Set[Any]]]: ...
    def _count_vocab(self, raw_documents: Union[ndarray, List[str]], fixed_vocab: bool) -> Tuple[Dict[str, int], csr_matrix]: ...
    def _validate_params(self) -> None: ...
    def fit(self, raw_documents: Iterable, y=None) -> Any: ...
    def fit_transform(self, raw_documents: Iterable, y: Optional[Union[ndarray, List[int64]]] = None) -> NDArray: ...
    def transform(self, raw_documents: Iterable) -> NDArray: ...
    def inverse_transform(self, X: NDArray | ArrayLike) -> list[ArrayLike]: ...
    @deprecated("get_feature_names is deprecated in 1.0 and will be removed " "in 1.2. Please use get_feature_names_out instead.")
    def get_feature_names(self) -> ArrayLike: ...
    def get_feature_names_out(self, input_features: ArrayLike | None = None) -> np.ndarray: ...
    def _more_tags(self): ...

def _make_int_array() -> array.array: ...

class TfidfTransformer(_OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    def __init__(
        self,
        *,
        norm: Literal["l1", "l2"] = "l2",
        use_idf: bool = True,
        smooth_idf: bool = True,
        sublinear_tf: bool = False,
    ) -> None: ...
    def fit(self, X: NDArray, y: Optional[Union[List[int64], ndarray]] = None) -> "TfidfTransformer": ...
    def transform(self, X: NDArray, copy: bool = True) -> NDArray: ...
    @property
    def idf_(self) -> NDArray: ...
    @idf_.setter
    def idf_(self, value) -> NDArray: ...
    def _more_tags(self): ...

class TfidfVectorizer(CountVectorizer):
    def __init__(
        self,
        *,
        input: Literal["filename", "file", "content"] = "content",
        encoding: str = "utf-8",
        decode_error: Literal["strict", "ignore", "replace"] = "strict",
        strip_accents: Literal["ascii", "unicode"] | None = None,
        lowercase: bool = True,
        preprocessor: Callable | None = None,
        tokenizer: Callable | None = None,
        analyzer: Literal["word", "char", "char_wb"] | Callable = "word",
        stop_words: Literal["english"] | ArrayLike | None = None,
        token_pattern: str = r"(?u)\b\w\w+\b",
        ngram_range: tuple[float, float] = ...,
        max_df: float | int = 1.0,
        min_df: float | int = 1,
        max_features: int | None = None,
        vocabulary: Mapping | Iterable | None = None,
        binary: bool = False,
        dtype: DType = ...,
        norm: Literal["l1", "l2"] = "l2",
        use_idf: bool = True,
        smooth_idf: bool = True,
        sublinear_tf: bool = False,
    ) -> None: ...

    # Broadcast the TF-IDF parameters to the underlying transformer instance
    # for easy grid search and repr

    @property
    def idf_(self) -> NDArray: ...
    @idf_.setter
    def idf_(self, value) -> NDArray: ...
    def _check_params(self) -> None: ...
    def fit(self, raw_documents: Iterable, y=None) -> Any: ...
    def fit_transform(self, raw_documents: Iterable, y: Optional[ndarray] = None) -> NDArray: ...
    def transform(self, raw_documents: Iterable) -> NDArray: ...
    def _more_tags(self): ...
