from numpy import int64, ndarray
from collections.abc import Iterable
from typing import Iterator, List, Optional, Tuple, Union, Sequence, Any
from numpy.typing import ArrayLike, NDArray
import pkgutil as pkgutil
import inspect as inspect
from importlib import import_module as import_module
from operator import itemgetter as itemgetter
from collections.abc import Sequence as Sequence
from contextlib import contextmanager as contextmanager
from itertools import compress as compress
from itertools import islice as islice
import math as math
import numbers as numbers
import platform as platform
import struct as struct
import timeit as timeit
from pathlib import Path as Path
from contextlib import suppress as suppress

import warnings as warnings
import numpy as np
from scipy.sparse import issparse as issparse

from .murmurhash import murmurhash3_32 as murmurhash3_32
from .class_weight import (
    compute_class_weight as compute_class_weight,
    compute_sample_weight as compute_sample_weight,
)
from . import _joblib as _joblib
from ..exceptions import DataConversionWarning as DataConversionWarning
from .deprecation import deprecated as deprecated
from .fixes import parse_version as parse_version, threadpool_info as threadpool_info
from ._estimator_html_repr import estimator_html_repr as estimator_html_repr
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
from .. import get_config as get_config
from ._bunch import Bunch as Bunch
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from random.mtrand import RandomState
from scipy.sparse._csr import csr_matrix

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

def _in_unstable_openblas_configuration() -> bool: ...
def safe_mask(X: NDArray | ArrayLike, mask: NDArray) -> ndarray: ...
def axis0_safe_slice(X: NDArray | ArrayLike, mask: NDArray, len_mask: int) -> ndarray: ...
def _array_indexing(
    array: Union[ndarray, csr_matrix],
    key: Union[ndarray, Tuple[int], int],
    key_dtype: str,
    axis: int,
) -> Union[int64, ndarray, csr_matrix]: ...
def _pandas_indexing(
    X: Union[DataFrame, Series],
    key: Union[ndarray, List[str], int],
    key_dtype: str,
    axis: int,
) -> Union[DataFrame, Series]: ...
def _list_indexing(X: List[str], key: ndarray, key_dtype: str) -> List[str]: ...
def _determine_key_type(key: Union[ndarray, str, Tuple[int], int, List[str]], accept_slice: bool = True) -> str: ...
def _safe_indexing(
    X: Union[Series, ndarray, csr_matrix, DataFrame, List[str]], indices: Union[ndarray, List[str], Tuple[int], int], *, axis=0
) -> Any: ...
def _get_column_indices(X: Union[DataFrame, ndarray], key: Union[int, List[str], Tuple[int]]) -> List[int]: ...
def resample(
    *arrays,
    replace: bool = True,
    n_samples: int | None = None,
    random_state: int | RandomState | None = None,
    stratify: ArrayLike | None = None,
) -> Sequence[ArrayLike]: ...
def shuffle(*arrays, random_state: int | RandomState | None = None, n_samples: int | None = None) -> Sequence: ...
def safe_sqr(X: NDArray | ArrayLike, *, copy: bool = True) -> NDArray: ...
def _chunk_generator(gen, chunksize): ...
def gen_batches(n: int, batch_size: int, *, min_batch_size: int = 0) -> Iterator[slice]: ...
def gen_even_slices(n: int, n_packs: int, *, n_samples: int | None = None) -> Iterator[slice]: ...
def tosequence(x: Iterable) -> Sequence: ...
def _to_object_array(sequence): ...
def indices_to_mask(indices: Sequence, mask_length: int) -> NDArray: ...
def _message_with_time(source: str, message: str, time: float) -> str: ...
@contextmanager
def _print_elapsed_time(source: Optional[str], message: Optional[str] = None) -> Iterator[None]: ...
def get_chunk_n_rows(row_bytes: int, *, max_n_rows: int | None = None, working_memory: int | float | None = None) -> int: ...
def _is_pandas_na(x: float) -> bool: ...
def is_scalar_nan(x: Any) -> bool: ...
def _approximate_mode(class_counts: ndarray, n_draws: int, rng: RandomState) -> ndarray: ...
def check_matplotlib_support(caller_name: str) -> None: ...
def check_pandas_support(caller_name: str): ...
def all_estimators(
    type_filter: Literal["classifier", "regressor", "cluster", "transformer"] | Sequence[str] | None = None
) -> ArrayLike: ...
