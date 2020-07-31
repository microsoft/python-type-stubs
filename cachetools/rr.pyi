from .cache import Cache as Cache
from typing import Any, Optional


class RRCache(Cache):
    """Random Replacement (RR) cache implementation."""

    def __init__(self, maxsize: Any, choice: Any = ..., getsizeof: Optional[Any] = ...) -> None:
        ...

    @property
    def choice(self):
        """
        The `choice` function used by the cache.
        """
        ...

    def popitem(self):
        """
        Remove and return a random `(key, value)` pair.
        """
        ...

