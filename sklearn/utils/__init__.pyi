from typing import Any, Iterable, Iterator, Sequence, SupportsIndex
from numpy.random import RandomState
from .fixes import parse_version as parse_version, threadpool_info as threadpool_info
from ._bunch import Bunch as Bunch
from .murmurhash import murmurhash3_32 as murmurhash3_32
from itertools import compress as compress, islice as islice
from ..exceptions import DataConversionWarning as DataConversionWarning
from .validation import (
    as_float_array as as_float_array,
    assert_all_finite as assert_all_finite,
    check_random_state as check_random_state,
    column_or_1d as column_or_1d,
    check_array as check_array,
    check_consistent_length as check_consistent_length,
    check_X_y as check_X_y,
    indexable as indexable,
    check_symmetric as check_symmetric,
    check_scalar as check_scalar,
)
from contextlib import contextmanager as contextmanager, suppress as suppress
from .discovery import all_estimators as all_estimators
from scipy.sparse import issparse as issparse
from .. import get_config as get_config
from collections.abc import Sequence as Sequence
from .deprecation import deprecated as deprecated
from numpy import ndarray
from .class_weight import (
    compute_class_weight as compute_class_weight,
    compute_sample_weight as compute_sample_weight,
)
from ._estimator_html_repr import estimator_html_repr as estimator_html_repr
from .._typing import MatrixLike, ArrayLike, Int
import math as math
import numbers as numbers
import platform as platform
import struct as struct
import timeit as timeit

import warnings as warnings
import numpy as np


# Do not deprecate parallel_backend and register_parallel_backend as they are
# needed to tune `scikit-learn` behavior and have different effect if called
# from the vendored version or or the site-package version. The other are
# utilities that are independent of scikit-learn so they are not part of
# scikit-learn public API.
parallel_backend = ...
register_parallel_backend = ...

__all__ = [
    "murmurhash3_32",
    "as_float_array",
    "assert_all_finite",
    "check_array",
    "check_random_state",
    "compute_class_weight",
    "compute_sample_weight",
    "column_or_1d",
    "check_consistent_length",
    "check_X_y",
    "check_scalar",
    "indexable",
    "check_symmetric",
    "indices_to_mask",
    "deprecated",
    "parallel_backend",
    "register_parallel_backend",
    "resample",
    "shuffle",
    "check_matplotlib_support",
    "all_estimators",
    "DataConversionWarning",
    "estimator_html_repr",
    "Bunch",
]

IS_PYPY = ...
_IS_32BIT = ...


def safe_mask(X: MatrixLike | ArrayLike, mask: ArrayLike) -> ndarray:
    ...


def axis0_safe_slice(
    X: MatrixLike | ArrayLike, mask: ArrayLike, len_mask: Int
) -> ndarray:
    ...


def resample(
    *arrays,
    replace: bool = True,
    n_samples: None | Int = None,
    random_state: RandomState | None | Int = None,
    stratify: None | MatrixLike | ArrayLike = None
) -> list[ndarray]:
    ...


def shuffle(
    *arrays, random_state: RandomState | None | Int = None, n_samples: None | Int = None
) -> list[SupportsIndex]:
    ...


def safe_sqr(X: MatrixLike | ArrayLike, *, copy: bool = True) -> ndarray:
    ...


def gen_batches(n: Int, batch_size: Int, *, min_batch_size: Int = 0) -> Iterator[slice]:
    ...


def gen_even_slices(
    n: Int, n_packs: Int, *, n_samples: None | Int = None
) -> Iterator[slice]:
    ...


def tosequence(x: Iterable) -> list:
    ...


def indices_to_mask(indices: Sequence | ndarray, mask_length: Int) -> ndarray:
    ...


def get_chunk_n_rows(
    row_bytes: Int,
    *,
    max_n_rows: None | Int = None,
    working_memory: float | None | int = None
) -> int:
    ...


def is_scalar_nan(x: Any) -> bool:
    ...


def check_matplotlib_support(caller_name: str) -> None:
    ...


def check_pandas_support(caller_name: str):
    ...
