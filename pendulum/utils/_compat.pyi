from typing import Any, Optional

PY2: Any
PY36: Any
PYPY: Any
long = long
unicode = unicode
basestring = basestring
long = int
unicode = str
basestring = str

def decode(string: Any, encodings: Optional[Any] = ...): ...
def encode(string: Any, encodings: Optional[Any] = ...): ...
