from typing import Callable, Optional, Sequence, Tuple, TypeVar

from .cache import Cache

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class RRCache(Cache[_KT, _VT]):
    """Random Replacement (RR) cache implementation."""

    def __init__(
        self,
        maxsize: int,
        choice: Optional[Callable[[Sequence[_KT]], _KT]] = ...,
        getsizeof: Optional[Callable[[_VT], int]] = ...,
    ) -> None: ...
    @property
    def choice(self) -> Callable[[Sequence[_KT]], _KT]:
        """
        The `choice` function used by the cache.
        """
        ...
    def popitem(self) -> Tuple[_KT, _VT]:
        """
        Remove and return a random `(key, value)` pair.
        """
        ...
