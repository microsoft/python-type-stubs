import sys as _sys

"""
Compatibility wrappers providing uniform behaviour for Python code required to
run under both Python 2.x and 3.x.

All operations emulate 2.x behaviour where applicable.
"""
if _sys.version_info[0] == 3:
    _sys_maxint = _sys.maxsize
    _int_type = int
    _str_type = str
    _bytes_type = lambda x: bytes(x, "UTF-8")
    _is_str = lambda x: isinstance(x, (str, type("".encode())))
    _is_int = lambda x: isinstance(x, int)
    _callable = lambda x: hasattr(x, "__call__")
    _dict_keys = lambda x: list(x.keys())
    _dict_items = lambda x: list(x.items())
    _iter_dict_keys = lambda x: x.keys()
    _iter_range = range
else:
    _sys_maxint = _sys.maxint
    _int_type = (int, long)
    _str_type = basestring
    _bytes_type = str
    _is_str = lambda x: isinstance(x, basestring)
    _is_int = lambda x: isinstance(x, (int, long))
    _callable = lambda x: callable(x)
    _dict_keys = lambda x: x.keys()
    _dict_items = lambda x: x.items()
    _iter_dict_keys = lambda x: iter(x.keys())
    _iter_range = xrange
