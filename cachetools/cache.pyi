from .abc import DefaultMapping as DefaultMapping
from typing import (
    Any,
    Optional,
)

class _DefaultSize:
    def __getitem__(self, _: Any): ...
    def __setitem__(self, _: Any, value: Any,) -> None: ...
    def pop(self, _: Any): ...

class Cache(DefaultMapping):
    def __init__(self, maxsize: int, getsizeof: Optional[Any] = ...,) -> None:
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
    def __getitem__(self, key: Any,): ...
    def __setitem__(self, key: Any, value: Any,) -> None: ...
    def __delitem__(self, key: Any,) -> None: ...
    def __contains__(self, key: Any,): ...
    def __missing__(self, key: Any,) -> None: ...
    def __iter__(self,) -> Any: ...
    def __len__(self,) -> int: ...
    @property
    def maxsize(self,) -> int:
        """
        The maximum size of the cache.
        """
        ...
    @property
    def currsize(self,) -> int:
        """
        The current size of the cache.
        """
        ...
    @staticmethod
    def getsizeof(value: Any,) -> int:
        """
        Return the size of a cache element’s value.
        """
        ...

