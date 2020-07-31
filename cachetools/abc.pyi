import abc
from abc import abstractmethod
from collections.abc import MutableMapping
from typing import (
    Any,
    Optional,
)

class DefaultMapping(
    MutableMapping, metaclass=abc.ABCMeta,
):
    @abstractmethod
    def __contains__(self, key: Any,) -> bool: ...
    @abstractmethod
    def __getitem__(self, key: Any,) -> Any: ...
    def get(self, key: Any, default: Optional[Any] = ...,): ...
    def pop(self, key: Any, default: Any = ...,): ...
    def setdefault(self, key: Any, default: Optional[Any] = ...,): ...

