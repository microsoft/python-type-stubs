from typing import Type, Callable, Any
from numpy.typing import ArrayLike, NDArray

# Copyright (c) 2011, 2012
# Authors: Pietro Berkes,
#          Andreas Muller
#          Mathieu Blondel
#          Olivier Grisel
#          Arnaud Joly
#          Denis Engemann
#          Giorgio Patrini
#          Thierry Guillemot
# License: BSD 3 clause
import os
import os.path as op
import inspect
import warnings
import sys
import functools
import tempfile
from subprocess import check_output, STDOUT, CalledProcessError
from subprocess import TimeoutExpired
import re
import contextlib
from collections.abc import Iterable
from collections.abc import Sequence

import scipy as sp
from functools import wraps
from inspect import signature

import shutil
import atexit
import unittest
from unittest import TestCase

from numpy.testing import assert_allclose as np_assert_allclose
from numpy.testing import assert_almost_equal
from numpy.testing import assert_approx_equal
from numpy.testing import assert_array_equal
from numpy.testing import assert_array_almost_equal
from numpy.testing import assert_array_less
import numpy as np
import joblib

import sklearn
from sklearn.utils import (
    IS_PYPY,
    _IS_32BIT,
    deprecated,
    _in_unstable_openblas_configuration,
)
from sklearn.utils.multiclass import check_classification_targets
from sklearn.utils.validation import (
    check_array,
    check_is_fitted,
    check_X_y,
)
from sklearn.utils.fixes import threadpool_info

__all__ = [
    "assert_raises",
    "assert_raises_regexp",
    "assert_array_equal",
    "assert_almost_equal",
    "assert_array_almost_equal",
    "assert_array_less",
    "assert_approx_equal",
    "assert_allclose",
    "assert_run_python_script",
    "SkipTest",
]

_dummy = ...
assert_raises = ...
SkipTest = ...
assert_dict_equal = ...

assert_raises_regex = ...
# assert_raises_regexp is deprecated in Python 3.4 in favor of
# assert_raises_regex but lets keep the backward compat in scikit-learn with
# the old name for now
assert_raises_regexp = ...

# TODO: Remove in 1.2
@deprecated(  # type: ignore
    "`assert_warns` is deprecated in 1.0 and will be removed in 1.2."
    "Use `pytest.warns` instead."
)
def assert_warns(warning_class: Warning, func: Callable, *args, **kw) -> Any: ...

# TODO: Remove in 1.2
@deprecated(  # type: ignore
    "`assert_warns_message` is deprecated in 1.0 and will be removed in 1.2."
    "Use `pytest.warns` instead."
)
def assert_warns_message(
    warning_class: Warning, message: str | Callable, func: Callable, *args, **kw
) -> Any: ...

# To remove when we support numpy 1.7
def assert_no_warnings(func, *args, **kw): ...
def ignore_warnings(
    obj: Callable | None = None, category: Warning = ...
) -> "_IgnoreWarnings": ...

class _IgnoreWarnings:
    def __init__(self, category: tuple[Warning, ...]) -> None: ...
    def __call__(self, fn: Callable) -> Callable: ...
    def __repr__(self): ...
    def __enter__(self) -> None: ...
    def __exit__(self, *exc_info) -> None: ...

def assert_raise_message(
    exceptions: Exception | tuple[Exception, ...],
    message: str,
    function: Callable,
    *args,
    **kwargs
): ...
def assert_allclose(
    actual: ArrayLike,
    desired: ArrayLike,
    rtol: float | None = None,
    atol: float | None = 0.0,
    equal_nan: bool | None = True,
    err_msg: str | None = "",
    verbose: bool | None = True,
): ...
def assert_allclose_dense_sparse(
    x: NDArray | ArrayLike,
    y: NDArray | ArrayLike,
    rtol: float = 1e-07,
    atol: float = 1e-9,
    err_msg: str = "",
): ...
def set_random_state(estimator: Any, random_state: int | RandomState | None = 0): ...
def check_skip_network(): ...
def _delete_folder(folder_path, warn=False): ...

class TempMemmap:
    def __init__(self, data, mmap_mode: str = "r"): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...

def _create_memmap_backed_array(array, filename, mmap_mode): ...
def _create_aligned_memmap_backed_arrays(data, mmap_mode, folder): ...
def create_memmap_backed_data(
    data, mmap_mode: str = "r", return_folder: bool = False, aligned: bool = False
): ...

# Utils to test docstrings

def _get_args(function, varargs=False): ...
def _get_func_name(func): ...
def check_docstring_parameters(
    func: Callable, doc: str | None = None, ignore: ArrayLike | None = None
) -> ArrayLike: ...
def assert_run_python_script(source_code: str, timeout: int = 60): ...
def _convert_container(container, constructor_name, columns_name=None, dtype=None): ...
def raises(
    expected_exc_type,
    match: str | ArrayLike | None = None,
    may_pass: bool = False,
    err_msg: str | None = None,
): ...

class _Raises(contextlib.AbstractContextManager):
    # see raises() for parameters
    def __init__(self, expected_exc_type, match, may_pass, err_msg): ...
    def __exit__(self, exc_type, exc_value, _): ...

class MinimalClassifier:

    _estimator_type: str = ...

    def __init__(self, param=None): ...
    def get_params(self, deep=True): ...
    def set_params(self, **params): ...
    def fit(self, X, y): ...
    def predict_proba(self, X): ...
    def predict(self, X): ...
    def score(self, X, y): ...

class MinimalRegressor:

    _estimator_type: str = ...

    def __init__(self, param=None): ...
    def get_params(self, deep=True): ...
    def set_params(self, **params): ...
    def fit(self, X, y): ...
    def predict(self, X): ...
    def score(self, X, y): ...

class MinimalTransformer:
    def __init__(self, param=None): ...
    def get_params(self, deep=True): ...
    def set_params(self, **params): ...
    def fit(self, X, y=None): ...
    def transform(self, X, y=None): ...
    def fit_transform(self, X, y=None): ...
