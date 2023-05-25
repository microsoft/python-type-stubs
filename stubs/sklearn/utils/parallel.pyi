from typing import Any, Callable, Iterable, Iterator
from numpy import ndarray
from .._config import config_context as config_context, get_config as get_config
from functools import update_wrapper as update_wrapper

import functools
import warnings

import joblib


class Parallel(joblib.Parallel):
    def __call__(self, iterable: Iterable | Iterator[Any]) -> ndarray:
        ...


# remove when https://github.com/joblib/joblib/issues/1071 is fixed
def delayed(function: Callable) -> tuple | Callable:
    ...


class _FuncWrapper:
    def __init__(self, function: Callable) -> None:
        ...

    def with_config(self, config: dict[str, bool | int | str]) -> _FuncWrapper:
        ...

    def __call__(self, *args, **kwargs):
        ...
