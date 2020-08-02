import abc
from typing import Mapping, MutableMapping, TypeVar

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class MultiMapping(Mapping[_KT, _VT]):
    @abc.abstractmethod
    def getall(self, key, default=...): ...
    @abc.abstractmethod
    def getone(self, key, default=...): ...

class MutableMultiMapping(MultiMapping[_KT, _VT], MutableMapping[_KT, _VT], metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, key, value): ...
    @abc.abstractmethod
    def extend(self, *args, **kwargs): ...
    @abc.abstractmethod
    def popone(self, key, default=...): ...
    @abc.abstractmethod
    def popall(self, key, default=...): ...

