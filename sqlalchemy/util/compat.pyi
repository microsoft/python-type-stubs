import base64
import collections
import contextlib
import itertools
from StringIO import StringIO as StringIO
from collections import namedtuple
from datetime import tzinfo
from functools import reduce
from itertools import izip_longest as zip_longest
from typing import Any, Optional
from urllib import quote as quote, quote_plus as quote_plus, unquote as unquote, unquote_plus as unquote_plus
from urlparse import parse_qsl as parse_qsl

py36: Any
py33: Any
py35: Any
py32: Any
py3k: Any
py2k: Any
py265: Any
jython: Any
pypy: Any
win32: Any
cpython: Any
contextmanager = contextlib.contextmanager
dottedgetter: Any
namedtuple = collections.namedtuple
next = next

FullArgSpec = namedtuple('FullArgSpec', ['args', 'varargs', 'varkw', 'defaults', 'kwonlyargs', 'kwonlydefaults', 'annotations'])
safe_kwarg: Any
safe_kwarg = str

def inspect_getfullargspec(func: Any): ...

string_types: Any
binary_types: Any
binary_type = bytes
text_type = str
int_types: Any
iterbytes = iter
itertools_filterfalse = itertools.filterfalse
itertools_filter = filter
itertools_imap = map
exec_: Any
import_: Any
print_: Any

def b(s: Any): ...
def b64decode(x: Any): ...
def b64encode(x: Any): ...
def decode_backslashreplace(text: Any, encoding: Any): ...
def cmp(a: Any, b: Any): ...
def raise_(exception: Any, with_traceback: Optional[Any] = ..., replace_context: Optional[Any] = ..., from_: bool = ...) -> None: ...
def u(s: Any): ...
def ue(s: Any): ...
callable = callable
binary_type = str
text_type = unicode
callable = callable
cmp = cmp
reduce = reduce
b64encode = base64.b64encode
b64decode = base64.b64decode

def safe_bytestring(text: Any): ...
def inspect_formatargspec(args: Any, varargs: Optional[Any] = ..., varkw: Optional[Any] = ..., defaults: Optional[Any] = ..., kwonlyargs: Any = ..., kwonlydefaults: Any = ..., annotations: Any = ..., formatarg: Any = ..., formatvarargs: Any = ..., formatvarkw: Any = ..., formatvalue: Any = ..., formatreturns: Any = ..., formatannotation: Any = ...): ...
def nested(*managers: Any) -> None: ...
def raise_from_cause(exception: Any, exc_info: Optional[Any] = ...) -> None: ...
def reraise(tp: Any, value: Any, tb: Optional[Any] = ..., cause: Optional[Any] = ...) -> None: ...
def with_metaclass(meta: Any, *bases: Any): ...

class timezone(tzinfo):
    def __init__(self, offset: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
    def utcoffset(self, dt: Any): ...
    def tzname(self, dt: Any): ...
    def dst(self, dt: Any) -> None: ...
    def fromutc(self, dt: Any): ...
