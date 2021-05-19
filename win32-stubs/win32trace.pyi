# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32trace, version: unspecified
# Module: win32trace, version: unspecified

'Interface to the Windows Console functions for dealing with character-mode applications.'

import typing
import builtins as _mod_builtins
from .lib import pywintypes as _mod_pywintypes

def GetHandle() -> typing.Any:
    ...

def GetTracer() -> typing.Any:
    ...

def InitRead() -> typing.Any:
    ...

def InitWrite() -> typing.Any:
    ...

def TermRead() -> typing.Any:
    ...

def TermWrite() -> typing.Any:
    ...

__doc__: str
__file__: str
__name__: str
__package__: str
def blockingread() -> typing.Any:
    ...

error = _mod_pywintypes.error
def flush() -> typing.Any:
    ...

def read() -> typing.Any:
    ...

def setprint() -> typing.Any:
    ...

def write() -> typing.Any:
    ...

def __getattr__(name) -> typing.Any:
    ...

