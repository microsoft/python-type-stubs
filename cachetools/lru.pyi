from .cache import Cache as Cache
from typing import Any, Optional


class LRUCache(Cache):
    """Least Recently Used (LRU) cache implementation."""

    def __init__(self, maxsize: Any, getsizeof: Optional[Any] = ...) -> None:
        ...

    def __getitem__(self, key: Any, cache_getitem: Any = ...):
        ...

    def __setitem__(self, key: Any, value: Any, cache_setitem: Any = ...) -> None:
        ...

    def __delitem__(self, key: Any, cache_delitem: Any = ...) -> None:
        ...

    def popitem(self):
        """
        Remove and return the (key, value) pair least recently used.
        """
        ...

