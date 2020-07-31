from .keys import hashkey as hashkey
from typing import Any, Optional


def cached(cache: Any, key: Any = ..., lock: Optional[Any] = ...):
    """Decorator to wrap a function with a memoizing callable that saves
    results in a cache.

    """
    ...


def cachedmethod(cache: Any, key: Any = ..., lock: Optional[Any] = ...):
    """Decorator to wrap a class or instance method with a memoizing
    callable that saves results in a cache.

    """
    ...
