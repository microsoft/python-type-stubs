from typing import Callable
from types import MethodType as MethodType
from functools import wraps as wraps, update_wrapper as update_wrapper


class _AvailableIfDescriptor:
    def __init__(self, fn: Callable, check: Callable, attribute_name: str) -> None:
        ...

    def __get__(self, obj, owner=None) -> Callable:
        ...


def available_if(check: Callable) -> Callable:
    ...
