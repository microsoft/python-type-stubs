# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32wnet, version: unspecified
# Module: win32wnet, version: unspecified

'A module that exposes the Windows Networking API.'

import typing
import builtins as _mod_builtins
from .lib import pywintypes as _mod_pywintypes

NCB = _mod_builtins.PyNCB
def NCBBuffer() -> typing.Any:
    'Creates a memory buffer'
    ...

NCBType = _mod_builtins.PyNCB
NETRESOURCE = _mod_builtins.PyNETRESOURCE
NETRESOURCEType = _mod_builtins.PyNETRESOURCE
def Netbios() -> typing.Any:
    'Calls the windows Netbios function'
    ...

def WNetAddConnection2(NetResource, Password, UserName, Flags) -> typing.Any:
    'WNetAddConnection2(NetResource, Password, UserName, Flags)'
    ...

def WNetAddConnection3(HwndParent, NetResource, Password, UserName, Flags) -> typing.Any:
    'WNetAddConnection3(HwndParent, NetResource, Password, UserName, Flags)'
    ...

def WNetCancelConnection2() -> typing.Any:
    'localname,dwflags,bforce'
    ...

def WNetCloseEnum() -> typing.Any:
    'PyHANDLE from WNetOpenEnum()'
    ...

def WNetEnumResource() -> typing.Any:
    'Enum'
    ...

def WNetGetConnection() -> typing.Any:
    'Retrieves the name of the network resource associated with a local device'
    ...

def WNetGetLastError() -> typing.Any:
    'Retrieves extended error information set by a network provider when one of the WNet* functions fails'
    ...

def WNetGetResourceInformation() -> typing.Any:
    'Finds the type and provider of a network resource'
    ...

def WNetGetResourceParent() -> typing.Any:
    'Finds the parent resource of a network resource'
    ...

def WNetGetUniversalName() -> typing.Any:
    'localPath, infoLevel=UNIVERSAL_NAME_INFO_LEVEL'
    ...

def WNetGetUser() -> typing.Any:
    'connectionName=None'
    ...

def WNetOpenEnum() -> typing.Any:
    'dwScope,dwType,dwUsage,NETRESOURCE - returns PyHANDLE'
    ...

__doc__: str
__file__: str
__name__: str
__package__: str
error = _mod_pywintypes.error
def __getattr__(name) -> typing.Any:
    ...

