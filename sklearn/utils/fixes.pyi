# Authors: Emmanuelle Gouillart <emmanuelle.gouillart@normalesup.org>
#          Gael Varoquaux <gael.varoquaux@normalesup.org>
#          Fabian Pedregosa <fpedregosa@acm.org>
#          Lars Buitinck
#
# License: BSD 3 clause

from functools import update_wrapper
import functools

import sklearn
import numpy as np
import scipy
import scipy.stats
import threadpoolctl
from .._config import config_context, get_config
from ..externals._packaging.version import parse as parse_version
from numpy import ndarray
from scipy.stats._stats_py import ModeResult
from typing import Any, Callable, Dict, List, Optional, Union

np_version = ...
sp_version = ...

def _object_dtype_isnan(X): ...

class loguniform(scipy.stats.reciprocal):
    pass

# remove when https://github.com/joblib/joblib/issues/1071 is fixed
def delayed(function: Callable) -> Callable: ...

class _FuncWrapper:
    def __init__(self, function: Callable) -> None: ...
    def __call__(self, *args, **kwargs) -> Any: ...

# Rename the `method` kwarg to `interpolation` for NumPy < 1.22, because
# `interpolation` kwarg was deprecated in favor of `method` in NumPy >= 1.22.
def _percentile(a, q, *, method="linear", **kwargs): ...

# compatibility fix for threadpoolctl >= 3.0.0
# since version 3 it's possible to setup a global threadpool controller to avoid
# looping through all loaded shared libraries each time.
# the global controller is created during the first call to threadpoolctl.
def _get_threadpool_controller() -> threadpoolctl.ThreadpoolController: ...
def threadpool_limits(
    limits: int | dict | Literal["sequential_blas_under_openmp"] | None = None,
    user_api: Optional[str] = None,
) -> threadpoolctl._ThreadpoolLimiter: ...

threadpool_limits.__doc__ = ...

def threadpool_info() -> List[Dict[str, Optional[Union[str, int]]]]: ...

threadpool_info.__doc__ = ...

# TODO: Remove when SciPy 1.9 is the minimum supported version
def _mode(a: ndarray, axis: int = 0) -> ModeResult: ...
