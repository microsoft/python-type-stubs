# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32pdh, version: unspecified
# Module: win32pdh, version: unspecified

'A module, encapsulating the Windows Performance Data Helpers API'

import typing
import builtins as _mod_builtins
from .lib import pywintypes as _mod_pywintypes

def AddCounter() -> typing.Any:
    ...

def AddEnglishCounter() -> typing.Any:
    ...

def BrowseCounters() -> typing.Any:
    ...

def CloseQuery() -> typing.Any:
    ...

def CollectQueryData() -> typing.Any:
    ...

def ConnectMachine() -> typing.Any:
    ...

def EnumObjectItems() -> typing.Any:
    ...

def EnumObjects() -> typing.Any:
    ...

def ExpandCounterPath() -> typing.Any:
    ...

def GetCounterInfo() -> typing.Any:
    ...

def GetFormattedCounterArray() -> typing.Any:
    ...

def GetFormattedCounterValue() -> typing.Any:
    ...

def LookupPerfIndexByName() -> typing.Any:
    ...

def LookupPerfNameByIndex() -> typing.Any:
    ...

def MakeCounterPath() -> typing.Any:
    ...

def OpenQuery() -> typing.Any:
    ...

PDH_FMT_1000: int
PDH_FMT_ANSI: int
PDH_FMT_DOUBLE: int
PDH_FMT_LARGE: int
PDH_FMT_LONG: int
PDH_FMT_NODATA: int
PDH_FMT_NOSCALE: int
PDH_FMT_RAW: int
PDH_FMT_UNICODE: int
PDH_MAX_SCALE: int
PDH_MIN_SCALE: int
PDH_PATH_WBEM_INPUT: int
PDH_PATH_WBEM_RESULT: int
PDH_VERSION: int
PERF_DETAIL_ADVANCED: int
PERF_DETAIL_EXPERT: int
PERF_DETAIL_NOVICE: int
PERF_DETAIL_WIZARD: int
def ParseCounterPath() -> typing.Any:
    ...

def ParseInstanceName() -> typing.Any:
    ...

def RemoveCounter() -> typing.Any:
    ...

def SetCounterScaleFactor() -> typing.Any:
    ...

def ValidatePath() -> typing.Any:
    ...

__doc__: str
__file__: str
__name__: str
__package__: str
class counter_status_error(_mod_builtins.Exception):
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
    

error = _mod_pywintypes.error
def __getattr__(name) -> typing.Any:
    ...

