from .cache import Cache as Cache
from typing import Callable, Generic, Optional, TypeVar

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class LFUCache(Cache):
    """Least Frequently Used (LFU) cache implementation."""

    def __init__(self, maxsize: int, getsizeof: Optional[Callable[[_VT], int]] = ...) -> None: ...
    def __getitem__(self, key: _KT, cache_getitem: Callable[[_KT], _VT] = ...) -> _VT: ...
    def __setitem__(self, key: _KT, value: _VT, cache_setitem: Callable[[_KT, _VT], None] = ...) -> None: ...
    def __delitem__(self, key: _KT, cache_delitem: Callable[[_KT], None] = ...) -> None: ...
    def popitem(self) -> Generic[_KT, _VT]:
        """
        Remove and return the (key, value) pair least frequently used.
        """
        ...

