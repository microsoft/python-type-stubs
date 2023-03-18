from typing import Literal
from ..base import BaseEstimator
from ._available_if import available_if as available_if
from .._config import get_config as get_config
from functools import wraps as wraps
from scipy.sparse import issparse as issparse
from . import check_pandas_support as check_pandas_support


class _SetOutputMixin:
    def __init_subclass__(
        cls, auto_wrap_output_keys: None | tuple[str] = ..., **kwargs
    ) -> None:
        ...

    def set_output(
        self, *, transform: None | Literal["default", "pandas"] = None
    ) -> BaseEstimator:
        ...
