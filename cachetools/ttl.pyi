from .cache import Cache as Cache
from typing import Any, Optional


class _Link:
    key: Any = ...
    expire: Any = ...

    def __init__(self, key: Optional[Any] = ..., expire: Optional[Any] = ...) -> None:
        ...

    def __reduce__(self):
        ...

    def unlink(self) -> None:
        ...


class _Timer:
    def __init__(self, timer: Any) -> None:
        ...

    def __call__(self):
        ...

    def __enter__(self):
        ...

    def __exit__(self, *exc: Any) -> None:
        ...

    def __reduce__(self):
        ...

    def __getattr__(self, name: Any):
        ...


class TTLCache(Cache):
    """LRU Cache implementation with per-item time-to-live (TTL) value."""

    def __init__(self, maxsize: Any, ttl: Any, timer: Any = ..., getsizeof: Optional[Any] = ...) -> None:
        ...

    def __contains__(self, key: Any):
        ...

    def __getitem__(self, key: Any, cache_getitem: Any = ...):
        ...

    def __setitem__(self, key: Any, value: Any, cache_setitem: Any = ...) -> None:
        ...

    def __delitem__(self, key: Any, cache_delitem: Any = ...) -> None:
        ...

    def __iter__(self) -> Any:
        ...

    def __len__(self):
        ...

    @property
    def currsize(self):
        """The current size of the cache."""
        ...

    @property
    def timer(self):
        """ The timer function used by the cache. """
        ...

    @property
    def ttl(self) -> int:
        """ The time-to-live value of the cache's items. """
        ...

    def expire(self, time: Optional[Any] = ...) -> None:
        """ Remove expired items from the cache. """
        ...

    def clear(self) -> None:
        ...

    def get(self, *args: Any, **kwargs: Any):
        ...

    def pop(self, *args: Any, **kwargs: Any):
        ...

    def setdefault(self, *args: Any, **kwargs: Any):
        ...

    def popitem(self):
        """Remove and return the `(key, value)` pair least recently used that
        has not already expired.

        """
        ...

