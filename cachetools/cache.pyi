from .abc import DefaultMapping as DefaultMapping
from typing import (
    Callable,
    Generic,
    Optional,
    TypeVar,
)

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class Cache(DefaultMapping[_KT, _VT]):
    def __init__(self, maxsize: int, getsizeof: Optional[Callable[[_VT], int]] = ...) -> None:
        """Mutable mapping to serve as a simple cache or cache base class.

        This class discards arbitrary items using popitem() to make space when necessary. 
        Derived classes may override popitem() to implement specific caching strategies. 
        If a subclass has to keep track of item access, insertion or deletion, 
        it may additionally need to override __getitem__(), __setitem__() and __delitem__().

        Parameters
        ----------
        maxsize: int
        The maximum size of the cache.

        getsizeof: callable, default None
        Return the size of a cache element’s value.

        """
        ...
    def __getitem__(self, key: _KT) -> _VT: ...
    def __setitem__(self, key: _KT, value: _VT) -> None: ...
    def __delitem__(self, key: _KT) -> None: ...
    def __contains__(self, key: _KT) -> bool: ...
    def __missing__(self, key: _KT) -> KeyError: ...
    def __iter__(self) -> _KT: ...
    def __len__(self) -> int: ...
    @property
    def maxsize(self) -> int:
        """
        The maximum size of the cache.
        """
        ...
    @property
    def currsize(self) -> int:
        """
        The current size of the cache.
        """
        ...
    @staticmethod
    def getsizeof(value: _VT) -> int:
        """
        Return the size of a cache element’s value.
        """
        ...

