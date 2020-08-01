from abc import ABCMeta, abstractmethod
from collections.abc import MutableMapping
from typing import (
    Optional,
    TypeVar,
)

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class DefaultMapping(MutableMapping[_KT, _VT], metaclass=ABCMeta):
    @abstractmethod
    def __contains__(self, key: _KT) -> bool: ...
    @abstractmethod
    def __getitem__(self, key: _KT,) -> _VT: ...
    def get(self, key: _KT, default: Optional[_VT] = ...,) -> _VT: ...
    def pop(self, key: _KT, default: _VT = ...,) -> _VT: ...
    def setdefault(self, key: _KT, default: Optional[_KT] = ...,) -> _VT: ...

