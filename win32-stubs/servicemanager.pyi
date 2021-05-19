# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: servicemanager, version: unspecified
# Module: servicemanager, version: unspecified

'A module that interfaces with the Windows Service Control Manager.'

import typing
import builtins as _mod_builtins

COINIT_APARTMENTTHREADED: int
COINIT_DISABLE_OLE1DDE: int
COINIT_MULTITHREADED: int
COINIT_SPEED_OVER_MEMORY: int
def CoInitializeEx() -> typing.Any:
    ...

def CoUninitialize() -> typing.Any:
    ...

def Debugging() -> typing.Any:
    ...

EVENTLOG_AUDIT_FAILURE: int
EVENTLOG_AUDIT_SUCCESS: int
EVENTLOG_ERROR_TYPE: int
EVENTLOG_INFORMATION_TYPE: int
EVENTLOG_WARNING_TYPE: int
def Finalize() -> typing.Any:
    ...

def Initialize() -> typing.Any:
    ...

def LogErrorMsg() -> typing.Any:
    ...

def LogInfoMsg() -> typing.Any:
    ...

def LogMsg() -> typing.Any:
    ...

def LogWarningMsg() -> typing.Any:
    ...

PYS_SERVICE_STARTED: int
PYS_SERVICE_STARTING: int
PYS_SERVICE_STOPPED: int
PYS_SERVICE_STOPPING: int
def PrepareToHostMultiple() -> typing.Any:
    ...

def PrepareToHostSingle() -> typing.Any:
    ...

def PumpWaitingMessages() -> typing.Any:
    ...

def RegisterServiceCtrlHandler() -> typing.Any:
    ...

def RunningAsService() -> typing.Any:
    ...

def SetEventSourceName() -> typing.Any:
    ...

def StartServiceCtrlDispatcher() -> typing.Any:
    ...

__doc__: str
__file__: str
__name__: str
__package__: str
class startup_error(_mod_builtins.Exception):
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __module__: str
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def __weakref__(self) -> typing.Any:
        'list of weak references to the object (if defined)'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

def __getattr__(name) -> typing.Any:
    ...

