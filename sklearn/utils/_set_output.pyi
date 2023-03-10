from typing import Literal
from .._typing import Estimator
from functools import wraps as wraps
from . import check_pandas_support as check_pandas_support
from ._available_if import available_if as available_if
from scipy.sparse import issparse as issparse
from .._config import get_config as get_config


class _SetOutputMixin:
    def __init_subclass__(
        cls, auto_wrap_output_keys: None | tuple[str] = ..., **kwargs
    ) -> None:
        ...

    def set_output(
        self, *, transform: Literal["default", "pandas"] | None = None
    ) -> Estimator:
        ...
