# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: dde, version: unspecified
# Module: dde, version: unspecified

'A module for Dynamic Data Exchange support'

import typing
import builtins as _mod_builtins

APPCLASS_MONITOR: int
APPCLASS_STANDARD: int
APPCMD_CLIENTONLY: int
APPCMD_FILTERINITS: int
CBF_FAIL_ADVISES: int
CBF_FAIL_ALLSVRXACTIONS: int
CBF_FAIL_CONNECTIONS: int
CBF_FAIL_EXECUTES: int
CBF_FAIL_POKES: int
CBF_FAIL_REQUESTS: int
CBF_FAIL_SELFCONNECTIONS: int
CBF_SKIP_ALLNOTIFICATIONS: int
CBF_SKIP_CONNECT_CONFIRMS: int
CBF_SKIP_DISCONNECTS: int
CBF_SKIP_REGISTRATIONS: int
def CreateConversation() -> typing.Any:
    ...

def CreateServer() -> typing.Any:
    ...

def CreateServerSystemTopic() -> typing.Any:
    ...

def CreateStringItem() -> typing.Any:
    ...

def CreateTopic() -> typing.Any:
    ...

MF_CALLBACKS: int
MF_CONV: int
MF_ERRORS: int
MF_HSZ_INFO: int
MF_LINKS: int
MF_POSTMSGS: int
MF_SENDMSGS: int
__doc__: str
__file__: str
__name__: str
__package__: str
class error(_mod_builtins.Exception):
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

