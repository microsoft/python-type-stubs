from pandas import compat as compat
from pandas.core.util.hashing import hash_array as hash_array, hash_pandas_object as hash_pandas_object
from ._decorators import Appender as Appender, Substitution as Substitution, cache_readonly as cache_readonly

def __getattr__(name): ...

class _testing:
    def __getattr__(self, item): ...

testing = ...
