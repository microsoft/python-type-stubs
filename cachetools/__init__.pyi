from typing import TypeVar
from .cache import Cache
from .decorators import cached, cachedmethod
from .lfu import LFUCache
from .lru import LRUCache
from .rr import RRCache
from .ttl import TTLCache
