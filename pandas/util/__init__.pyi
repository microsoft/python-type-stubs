from pandas import compat as compat
from pandas.core.util.hashing import hash_array as hash_array, hash_pandas_object as hash_pandas_object
from pandas.util._decorators import Appender as Appender, Substitution as Substitution, cache_readonly as cache_readonly
from typing import Any

def __getattr__(name: Any): ...

class _testing:
    def __getattr__(self, item: Any): ...

testing: Any
