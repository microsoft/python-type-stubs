import atexit
import contextlib
import functools
import inspect

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
import re
import shutil
import sys
import tempfile
import unittest
import warnings
from collections.abc import Iterable as Iterable, Sequence
from functools import wraps as wraps
from inspect import signature as signature
from subprocess import (
    STDOUT as STDOUT,
    CalledProcessError as CalledProcessError,
    TimeoutExpired as TimeoutExpired,
    check_output as check_output,
)
from typing import Any, Callable, ClassVar, Sequence
from unittest import TestCase as TestCase

import joblib
import numpy as np
import scipy as sp
import sklearn
from numpy import ndarray
from numpy.random import RandomState
from numpy.testing import (
    assert_allclose as np_assert_allclose,
    assert_almost_equal,
    assert_approx_equal,
    assert_array_almost_equal,
    assert_array_equal,
    assert_array_less,
)
from numpydoc import docscrape as docscrape

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..metrics import accuracy_score as accuracy_score, r2_score as r2_score
from . import IS_PYPY as IS_PYPY
from .fixes import threadpool_info as threadpool_info
from .multiclass import check_classification_targets as check_classification_targets
from .validation import check_array as check_array, check_is_fitted as check_is_fitted, check_X_y as check_X_y

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

# To remove when we support numpy 1.7
def assert_no_warnings(func, *args, **kw): ...
def ignore_warnings(obj: None | Callable = None, category: Warning = ...) -> _IgnoreWarnings | Callable: ...

class _IgnoreWarnings:
    def __init__(self, category: tuple[Warning]) -> None: ...
    def __call__(self, fn: Callable) -> Callable: ...
    def __repr__(self) -> str: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *exc_info) -> None: ...

def assert_raise_message(exceptions: tuple[Exception, ...] | Exception, message: str, function: Callable, *args, **kwargs): ...
def assert_allclose(
    actual: ArrayLike,
    desired: ArrayLike,
    rtol: float | None = None,
    atol: float | None = 0.0,
    equal_nan: None | bool = True,
    err_msg: None | str = "",
    verbose: None | bool = True,
): ...
def assert_allclose_dense_sparse(
    x: MatrixLike | ArrayLike,
    y: MatrixLike | ArrayLike,
    rtol: Float = 1e-07,
    atol: Float = 1e-9,
    err_msg: str = "",
): ...
def set_random_state(estimator: Any, random_state: RandomState | None | Int = 0): ...
def check_skip_network(): ...

class TempMemmap:
    def __init__(self, data, mmap_mode: str = "r") -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...

def create_memmap_backed_data(data, mmap_mode: str = "r", return_folder: bool = False, aligned: bool = False): ...
def check_docstring_parameters(func: Callable, doc: None | str = None, ignore: Sequence | None = None) -> ndarray: ...
def assert_run_python_script(source_code: str, timeout: Int = 60): ...
def raises(
    expected_exc_type,
    match: None | str | Sequence[str] = None,
    may_pass: bool = False,
    err_msg: None | str = None,
): ...

class _Raises(contextlib.AbstractContextManager):
    # see raises() for parameters
    def __init__(self, expected_exc_type, match, may_pass, err_msg) -> None: ...
    def __exit__(self, exc_type, exc_value, _): ...

class MinimalClassifier:
    _estimator_type: ClassVar[str] = ...

    def __init__(self, param=None) -> None: ...
    def get_params(self, deep: bool = True): ...
    def set_params(self, **params): ...
    def fit(self, X, y): ...
    def predict_proba(self, X): ...
    def predict(self, X): ...
    def score(self, X, y): ...

class MinimalRegressor:
    _estimator_type: ClassVar[str] = ...

    def __init__(self, param=None) -> None: ...
    def get_params(self, deep: bool = True): ...
    def set_params(self, **params): ...
    def fit(self, X, y): ...
    def predict(self, X): ...
    def score(self, X, y): ...

class MinimalTransformer:
    def __init__(self, param=None) -> None: ...
    def get_params(self, deep: bool = True): ...
    def set_params(self, **params): ...
    def fit(self, X, y=None): ...
    def transform(self, X, y=None): ...
    def fit_transform(self, X, y=None): ...
