import warnings
from abc import ABCMeta, abstractmethod
from contextlib import suppress as suppress
from operator import attrgetter as attrgetter
from typing import Any, Callable, ClassVar, List, Sequence

import numpy as np

from ..base import BaseEstimator
from ._available_if import _AvailableIfDescriptor, available_if

__all__ = ["available_if", "if_delegate_has_method"]

class _BaseComposition(BaseEstimator, metaclass=ABCMeta):
    steps: ClassVar[List[Any]] = ...

    @abstractmethod
    def __init__(self) -> None: ...

# TODO(1.3) remove
class _IffHasAttrDescriptor(_AvailableIfDescriptor):
    def __init__(self, fn, delegate_names, attribute_name) -> None: ...

# TODO(1.3) remove
def if_delegate_has_method(delegate: tuple[str, ...] | str | Sequence[str]) -> Callable: ...
