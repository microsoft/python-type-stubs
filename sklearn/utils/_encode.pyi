from typing import Any, NamedTuple
from contextlib import suppress as suppress
from collections import Counter
from numpy import str_, ndarray
from . import is_scalar_nan as is_scalar_nan

import numpy as np


class MissingValues(NamedTuple):

    nan: bool = ...
    none: bool = ...

    def to_list(self) -> list[Any | float]:
        ...


class _nandict(dict):
    def __init__(
        self, mapping: dict[str, int] | dict[str | float, int] | dict[str_, int]
    ) -> None:
        ...

    def __missing__(self, key):
        ...


class _NaNCounter(Counter):
    def __init__(self, items: ndarray) -> None:
        ...

    def __missing__(self, key):
        ...
