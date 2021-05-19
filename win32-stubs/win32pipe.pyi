# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32pipe, version: unspecified
# Module: win32pipe, version: unspecified

''

import typing
import builtins as _mod_builtins
from .lib import pywintypes as _mod_pywintypes

def CallNamedPipe() -> typing.Any:
    ...

def ConnectNamedPipe() -> typing.Any:
    ...

def CreateNamedPipe() -> typing.Any:
    ...

def CreatePipe() -> typing.Any:
    ...

def DisconnectNamedPipe() -> typing.Any:
    ...

def FdCreatePipe() -> typing.Any:
    ...

def GetNamedPipeClientProcessId() -> typing.Any:
    ...

def GetNamedPipeClientSessionId() -> typing.Any:
    ...

def GetNamedPipeHandleState() -> typing.Any:
    ...

def GetNamedPipeInfo() -> typing.Any:
    ...

def GetNamedPipeServerProcessId() -> typing.Any:
    ...

def GetNamedPipeServerSessionId() -> typing.Any:
    ...

def GetOverlappedResult() -> typing.Any:
    ...

NMPWAIT_NOWAIT: int
NMPWAIT_USE_DEFAULT_WAIT: int
NMPWAIT_WAIT_FOREVER: int
PIPE_ACCESS_DUPLEX: int
PIPE_ACCESS_INBOUND: int
PIPE_ACCESS_OUTBOUND: int
PIPE_NOWAIT: int
PIPE_READMODE_BYTE: int
PIPE_READMODE_MESSAGE: int
PIPE_TYPE_BYTE: int
PIPE_TYPE_MESSAGE: int
PIPE_UNLIMITED_INSTANCES: int
PIPE_WAIT: int
def PeekNamedPipe() -> typing.Any:
    ...

def SetNamedPipeHandleState() -> typing.Any:
    ...

def TransactNamedPipe() -> typing.Any:
    ...

UNICODE: int
def WaitNamedPipe() -> typing.Any:
    ...

__doc__: str
__file__: str
__name__: str
__package__: str
error = _mod_pywintypes.error
def popen() -> typing.Any:
    ...

def popen2() -> typing.Any:
    ...

def popen3() -> typing.Any:
    ...

def popen4() -> typing.Any:
    ...

def __getattr__(name) -> typing.Any:
    ...

