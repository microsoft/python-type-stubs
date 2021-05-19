# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32ras, version: unspecified
# Module: win32ras, version: unspecified

'A module encapsulating the Windows Remote Access Service (RAS) API.'

import typing
import builtins as _mod_builtins
from .lib import pywintypes as _mod_pywintypes

def CreatePhonebookEntry() -> typing.Any:
    ...

def Dial() -> typing.Any:
    ...

def EditPhonebookEntry() -> typing.Any:
    ...

def EnumConnections() -> typing.Any:
    ...

def EnumEntries() -> typing.Any:
    ...

def GetConnectStatus() -> typing.Any:
    ...

def GetEntryDialParams() -> typing.Any:
    ...

def GetErrorString() -> typing.Any:
    ...

def HangUp() -> typing.Any:
    ...

def IsHandleValid() -> typing.Any:
    ...

RASCS_AllDevicesConnected: int
RASCS_AuthAck: int
RASCS_AuthCallback: int
RASCS_AuthChangePassword: int
RASCS_AuthLinkSpeed: int
RASCS_AuthNotify: int
RASCS_AuthProject: int
RASCS_AuthRetry: int
RASCS_Authenticate: int
RASCS_Authenticated: int
RASCS_CallbackComplete: int
RASCS_CallbackSetByCaller: int
RASCS_ConnectDevice: int
RASCS_Connected: int
RASCS_DeviceConnected: int
RASCS_Disconnected: int
RASCS_Interactive: int
RASCS_LogonNetwork: int
RASCS_OpenPort: int
RASCS_PasswordExpired: int
RASCS_PortOpened: int
RASCS_PrepareForCallback: int
RASCS_Projected: int
RASCS_ReAuthenticate: int
RASCS_RetryAuthentication: int
RASCS_StartAuthentication: int
RASCS_WaitForCallback: int
RASCS_WaitForModemReset: int
def RASDIALEXTENSIONS() -> typing.Any:
    ...

def SetEntryDialParams() -> typing.Any:
    ...

__doc__: str
__file__: str
__name__: str
__package__: str
error = _mod_pywintypes.error
def __getattr__(name) -> typing.Any:
    ...

