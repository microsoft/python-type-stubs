from typing import Any, Callable
import warnings
import functools


__all__ = ["deprecated"]


class deprecated:

    # Adapted from https://wiki.python.org/moin/PythonDecoratorLibrary,
    # but with many changes.

    def __init__(self, extra: str = "") -> None:
        ...

    def __call__(self, obj: Any) -> property | Callable:
        ...
