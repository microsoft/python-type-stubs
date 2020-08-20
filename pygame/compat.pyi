import sys
from io import BytesIO, StringIO
from typing import Tuple, Type, Union, overload
from cStringIO import StringIO
from itertools import imap as imap_
from types import TracebackType

"""Python 2.x/3.x compatibility tools"""
PY_MAJOR_VERSION = sys.version_info[0]

def geterror() -> Tuple[Type[BaseException], BaseException, TracebackType] | Tuple[None, None, None]: ...

if PY_MAJOR_VERSION >= 3:
    long_ = int
    xrange_ = range
    unichr_ = chr
    unicode_ = str
    bytes_ = bytes
    raw_input_ = input
    imap_ = map
    def as_bytes(string: str) -> bytes:
        """ '<binary literal>' => b'<binary literal>' """
        ...
    def as_unicode(rstring: str) -> bytes:
        """ r'<Unicode literal>' => '<Unicode literal>' """
        ...

else:
    long_ = long
    xrange_ = xrange
    BytesIO = StringIO
    unichr_ = unichr
    unicode_ = unicode
    bytes_ = str
    raw_input_ = raw_input
    def as_bytes(string: str) -> bytes:
        """ '<binary literal>' => '<binary literal>' """
        ...
    def as_unicode(rstring: str) -> bytes:
        """ r'<Unicode literal>' => u'<Unicode literal>' """
        ...

def get_BytesIO() -> Type[BytesIO]: ...
def get_StringIO() -> Type[StringIO]: ...
def ord_(o: Union[str, bytes]) -> int: ...

if sys.platform == "win32":
    filesystem_errors = "replace"
else: ...

def filesystem_encode(u: str) -> bytes: ...

