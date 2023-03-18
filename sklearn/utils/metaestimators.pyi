from typing import Any, Callable, ClassVar, Sequence, List
from operator import attrgetter as attrgetter
from contextlib import suppress as suppress
from abc import ABCMeta, abstractmethod
from ._available_if import available_if, _AvailableIfDescriptor
from ..base import BaseEstimator
import warnings
import numpy as np

__all__ = ["available_if", "if_delegate_has_method"]


class _BaseComposition(BaseEstimator, metaclass=ABCMeta):

    steps: ClassVar[List[Any]] = ...

    @abstractmethod
    def __init__(self) -> None:
        ...


# TODO(1.3) remove
class _IffHasAttrDescriptor(_AvailableIfDescriptor):
    def __init__(self, fn, delegate_names, attribute_name) -> None:
        ...


# TODO(1.3) remove
def if_delegate_has_method(delegate: tuple[str, ...] | str | Sequence[str]) -> Callable:
    ...
