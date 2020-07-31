from .ttl import TTLCache
from collections import namedtuple
from typing import Any

_CacheInfo = namedtuple("CacheInfo", ["hits", "misses", "maxsize", "currsize"])

class _UnboundCache(dict):
    @property
    def maxsize(self) -> int: ...
    @property
    def currsize(self) -> int: ...

class _UnboundTTLCache(TTLCache):
    def __init__(self, ttl: int, timer: int) -> None: ...
    @property
    def maxsize(self) -> int: ...

def lfu_cache(maxsize: int = ..., typed: bool = ...):
    """Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Frequently Used (LFU)
    algorithm.

    Parameters:
    maxsize: int, default=128

    typed: bool, default: False

    """
    ...

def lru_cache(maxsize: int = ..., typed: bool = ...):
    """Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU)
    algorithm.

    Parameters:
    maxsize: int, default=128

    typed: bool, default: False

    """
    ...

def rr_cache(maxsize: int = ..., choice: Any = ..., typed: bool = ...):
    """Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Random Replacement (RR)
    algorithm.

    Parameters:
    maxsize: int, default=128

    choice: Any, default=random.choice

    typed: bool, default: False


    """
    ...

def ttl_cache(maxsize: int = ..., ttl: int = ..., timer: Any = ..., typed: bool = ...):
    """Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU)
    algorithm with a per-item time-to-live (TTL) value.

    Parameters:
    maxsize: int, default=128

    ttl: int, default=600

    timer: float, default = timer.monotonic

    typed: bool, default: False

    """
    ...

