from functools import wraps as wraps
from typing import Literal

from scipy.sparse import issparse as issparse

from .._config import get_config as get_config
from ..base import BaseEstimator
from . import check_pandas_support as check_pandas_support
from ._available_if import available_if as available_if

class _SetOutputMixin:
    def __init_subclass__(cls, auto_wrap_output_keys: None | tuple[str] = ..., **kwargs) -> None: ...
    def set_output(self, *, transform: None | Literal["default", "pandas"] = None) -> BaseEstimator: ...
