# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32transaction, version: unspecified
# Module: win32transaction, version: unspecified

'Module wrapping Kernal Transaction Manager functions, as used with transacted NTFS and transacted registry functions.'

import typing
import builtins as _mod_builtins
from .lib import pywintypes as _mod_pywintypes

def CommitTransaction() -> typing.Any:
    ...

def CommitTransactionAsync() -> typing.Any:
    ...

def CreateTransaction() -> typing.Any:
    ...

def GetTransactionId() -> typing.Any:
    ...

def OpenTransaction() -> typing.Any:
    ...

def RollbackTransaction() -> typing.Any:
    ...

def RollbackTransactionAsync() -> typing.Any:
    ...

__doc__: str
__file__: str
__name__: str
__package__: str
error = _mod_pywintypes.error
def __getattr__(name) -> typing.Any:
    ...

