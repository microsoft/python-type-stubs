# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32net, version: unspecified
# Module: win32net, version: unspecified

'A module encapsulating the Windows Network API.'

import typing
import builtins as _mod_builtins
from .lib import pywintypes as _mod_pywintypes

def NetFileClose() -> typing.Any:
    ...

def NetFileEnum() -> typing.Any:
    ...

def NetFileGetInfo() -> typing.Any:
    ...

def NetGetAnyDCName() -> typing.Any:
    ...

def NetGetDCName() -> typing.Any:
    ...

def NetGetJoinInformation() -> typing.Any:
    ...

def NetGroupAdd() -> typing.Any:
    ...

def NetGroupAddUser() -> typing.Any:
    ...

def NetGroupDel() -> typing.Any:
    ...

def NetGroupDelUser() -> typing.Any:
    ...

def NetGroupEnum() -> typing.Any:
    ...

def NetGroupGetInfo() -> typing.Any:
    ...

def NetGroupGetUsers() -> typing.Any:
    ...

def NetGroupSetInfo() -> typing.Any:
    ...

def NetGroupSetUsers() -> typing.Any:
    ...

def NetLocalGroupAdd() -> typing.Any:
    ...

def NetLocalGroupAddMembers() -> typing.Any:
    ...

def NetLocalGroupDel() -> typing.Any:
    ...

def NetLocalGroupDelMembers() -> typing.Any:
    ...

def NetLocalGroupEnum() -> typing.Any:
    ...

def NetLocalGroupGetInfo() -> typing.Any:
    ...

def NetLocalGroupGetMembers() -> typing.Any:
    ...

def NetLocalGroupSetInfo() -> typing.Any:
    ...

def NetLocalGroupSetMembers() -> typing.Any:
    ...

def NetMessageBufferSend() -> typing.Any:
    ...

def NetMessageNameAdd() -> typing.Any:
    ...

def NetMessageNameDel() -> typing.Any:
    ...

def NetMessageNameEnum() -> typing.Any:
    ...

def NetServerComputerNameAdd() -> typing.Any:
    ...

def NetServerComputerNameDel() -> typing.Any:
    ...

def NetServerDiskEnum() -> typing.Any:
    ...

def NetServerEnum() -> typing.Any:
    ...

def NetServerGetInfo() -> typing.Any:
    ...

def NetServerSetInfo() -> typing.Any:
    ...

def NetSessionDel() -> typing.Any:
    ...

def NetSessionEnum() -> typing.Any:
    ...

def NetSessionGetInfo() -> typing.Any:
    ...

def NetShareAdd() -> typing.Any:
    ...

def NetShareCheck() -> typing.Any:
    ...

def NetShareDel() -> typing.Any:
    ...

def NetShareEnum() -> typing.Any:
    'Obsolete Function,Level 1 call'
    ...

def NetShareGetInfo() -> typing.Any:
    ...

def NetShareSetInfo() -> typing.Any:
    ...

def NetStatisticsGet() -> typing.Any:
    ...

def NetUseAdd() -> typing.Any:
    ...

def NetUseDel() -> typing.Any:
    ...

def NetUseEnum() -> typing.Any:
    ...

def NetUseGetInfo() -> typing.Any:
    ...

def NetUserAdd() -> typing.Any:
    ...

def NetUserChangePassword() -> typing.Any:
    ...

def NetUserDel() -> typing.Any:
    ...

def NetUserEnum() -> typing.Any:
    ...

def NetUserGetGroups() -> typing.Any:
    'Updated - New Behavior'
    ...

def NetUserGetInfo() -> typing.Any:
    ...

def NetUserGetLocalGroups() -> typing.Any:
    'Updated - New Behavior'
    ...

def NetUserModalsGet() -> typing.Any:
    ...

def NetUserModalsSet() -> typing.Any:
    ...

def NetUserSetInfo() -> typing.Any:
    ...

def NetValidateName() -> typing.Any:
    ...

def NetValidatePasswordPolicy() -> typing.Any:
    ...

def NetWkstaGetInfo() -> typing.Any:
    ...

def NetWkstaSetInfo() -> typing.Any:
    ...

def NetWkstaTransportAdd() -> typing.Any:
    ...

def NetWkstaTransportDel() -> typing.Any:
    ...

def NetWkstaTransportEnum() -> typing.Any:
    ...

def NetWkstaUserEnum() -> typing.Any:
    ...

SERVICE_SERVER: str
SERVICE_WORKSTATION: str
USE_FORCE: int
USE_LOTS_OF_FORCE: int
USE_NOFORCE: int
__doc__: str
__file__: str
__name__: str
__package__: str
error = _mod_pywintypes.error
def __getattr__(name) -> typing.Any:
    ...

