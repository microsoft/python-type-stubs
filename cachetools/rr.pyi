from .cache import Cache as Cache
from typing import Callable, Generic, Optional, Sequence, TypeVar

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_T = TypeVar("_T")

class RRCache(Cache):
    """Random Replacement (RR) cache implementation."""

    def __init__(
        self, maxsize: int, choice: Optional[Callable[[Sequence[_T]], _T]] = ..., getsizeof: Optional[Callable[[_VT], int]] = ...
    ) -> None: ...
    @property
    def choice(self) -> _T:
        """
        The `choice` function used by the cache.
        """
        ...
    def popitem(self) -> _VT:
        """
        Remove and return a random `(key, value)` pair.
        """
        ...
