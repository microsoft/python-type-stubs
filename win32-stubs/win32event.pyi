# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32event, version: unspecified
# Module: win32event, version: unspecified

''

import typing
import builtins as _mod_builtins
from .lib import pywintypes as _mod_pywintypes

def CancelWaitableTimer() -> typing.Any:
    ...

def CreateEvent() -> typing.Any:
    ...

def CreateMutex() -> typing.Any:
    ...

def CreateSemaphore() -> typing.Any:
    ...

def CreateWaitableTimer() -> typing.Any:
    ...

EVENT_ALL_ACCESS: int
EVENT_MODIFY_STATE: int
INFINITE: int
MAXIMUM_WAIT_OBJECTS: int
def MsgWaitForMultipleObjects() -> typing.Any:
    ...

def MsgWaitForMultipleObjectsEx() -> typing.Any:
    ...

def OpenEvent() -> typing.Any:
    ...

def OpenMutex() -> typing.Any:
    ...

def OpenSemaphore() -> typing.Any:
    ...

def OpenWaitableTimer() -> typing.Any:
    ...

def PulseEvent() -> typing.Any:
    ...

QS_ALLEVENTS: int
QS_ALLINPUT: int
QS_HOTKEY: int
QS_INPUT: int
QS_KEY: int
QS_MOUSE: int
QS_MOUSEBUTTON: int
QS_MOUSEMOVE: int
QS_PAINT: int
QS_POSTMESSAGE: int
QS_SENDMESSAGE: int
QS_TIMER: int
def ReleaseMutex() -> typing.Any:
    ...

def ReleaseSemaphore() -> typing.Any:
    ...

def ResetEvent() -> typing.Any:
    ...

SYNCHRONIZE: int
def SetEvent() -> typing.Any:
    ...

def SetWaitableTimer() -> typing.Any:
    ...

def SignalObjectAndWait() -> typing.Any:
    ...

UNICODE: int
WAIT_ABANDONED: int
WAIT_ABANDONED_0: int
WAIT_FAILED: int
WAIT_IO_COMPLETION: int
WAIT_OBJECT_0: int
WAIT_TIMEOUT: int
def WaitForInputIdle() -> typing.Any:
    ...

def WaitForMultipleObjects() -> typing.Any:
    ...

def WaitForMultipleObjectsEx() -> typing.Any:
    ...

def WaitForSingleObject() -> typing.Any:
    ...

def WaitForSingleObjectEx() -> typing.Any:
    ...

__doc__: str
__file__: str
__name__: str
__package__: str
error = _mod_pywintypes.error
def __getattr__(name) -> typing.Any:
    ...

