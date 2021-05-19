# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32service, version: unspecified
# Module: win32service, version: unspecified

''

import typing
import builtins as _mod_builtins
from .lib import pywintypes as _mod_pywintypes

def ChangeServiceConfig() -> typing.Any:
    ...

def ChangeServiceConfig2() -> typing.Any:
    ...

def CloseServiceHandle() -> typing.Any:
    ...

def ControlService() -> typing.Any:
    ...

def CreateDesktop() -> typing.Any:
    ...

def CreateService() -> typing.Any:
    ...

def CreateWindowStation() -> typing.Any:
    ...

DBT_CONFIGCHANGECANCELED: int
DBT_CONFIGCHANGED: int
DBT_CUSTOMEVENT: int
DBT_DEVICEARRIVAL: int
DBT_DEVICEQUERYREMOVE: int
DBT_DEVICEQUERYREMOVEFAILED: int
DBT_DEVICEREMOVECOMPLETE: int
DBT_DEVICEREMOVEPENDING: int
DBT_DEVICETYPESPECIFIC: int
DBT_QUERYCHANGECONFIG: int
DF_ALLOWOTHERACCOUNTHOOK: int
def DeleteService() -> typing.Any:
    ...

def EnumDependentServices() -> typing.Any:
    ...

def EnumServicesStatus() -> typing.Any:
    ...

def EnumServicesStatusEx() -> typing.Any:
    ...

def EnumWindowStations() -> typing.Any:
    ...

def GetProcessWindowStation() -> typing.Any:
    ...

def GetServiceDisplayName() -> typing.Any:
    ...

def GetServiceKeyName() -> typing.Any:
    ...

def GetThreadDesktop() -> typing.Any:
    ...

def GetUserObjectInformation() -> typing.Any:
    ...

HDESKType = _mod_builtins.PyHDESK
HWINSTAType = _mod_builtins.PyHWINSTA
def LockServiceDatabase() -> typing.Any:
    ...

def OpenDesktop() -> typing.Any:
    ...

def OpenInputDesktop() -> typing.Any:
    ...

def OpenSCManager() -> typing.Any:
    ...

def OpenService() -> typing.Any:
    ...

def OpenWindowStation() -> typing.Any:
    ...

def QueryServiceConfig() -> typing.Any:
    ...

def QueryServiceConfig2() -> typing.Any:
    ...

def QueryServiceLockStatus() -> typing.Any:
    ...

def QueryServiceObjectSecurity() -> typing.Any:
    ...

def QueryServiceStatus() -> typing.Any:
    ...

def QueryServiceStatusEx() -> typing.Any:
    ...

SC_ACTION_NONE: int
SC_ACTION_REBOOT: int
SC_ACTION_RESTART: int
SC_ACTION_RUN_COMMAND: int
SC_ENUM_PROCESS_INFO: int
SC_GROUP_IDENTIFIER: int
SC_MANAGER_ALL_ACCESS: int
SC_MANAGER_CONNECT: int
SC_MANAGER_CREATE_SERVICE: int
SC_MANAGER_ENUMERATE_SERVICE: int
SC_MANAGER_LOCK: int
SC_MANAGER_MODIFY_BOOT_CONFIG: int
SC_MANAGER_QUERY_LOCK_STATUS: int
SERVICE_ACCEPT_HARDWAREPROFILECHANGE: int
SERVICE_ACCEPT_NETBINDCHANGE: int
SERVICE_ACCEPT_PARAMCHANGE: int
SERVICE_ACCEPT_PAUSE_CONTINUE: int
SERVICE_ACCEPT_POWEREVENT: int
SERVICE_ACCEPT_PRESHUTDOWN: int
SERVICE_ACCEPT_SESSIONCHANGE: int
SERVICE_ACCEPT_SHUTDOWN: int
SERVICE_ACCEPT_STOP: int
SERVICE_ACTIVE: int
SERVICE_ALL_ACCESS: int
SERVICE_AUTO_START: int
SERVICE_BOOT_START: int
SERVICE_CHANGE_CONFIG: int
SERVICE_CONFIG_DELAYED_AUTO_START_INFO: int
SERVICE_CONFIG_DESCRIPTION: int
SERVICE_CONFIG_FAILURE_ACTIONS: int
SERVICE_CONFIG_FAILURE_ACTIONS_FLAG: int
SERVICE_CONFIG_PRESHUTDOWN_INFO: int
SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO: int
SERVICE_CONFIG_SERVICE_SID_INFO: int
SERVICE_CONTINUE_PENDING: int
SERVICE_CONTROL_CONTINUE: int
SERVICE_CONTROL_DEVICEEVENT: int
SERVICE_CONTROL_HARDWAREPROFILECHANGE: int
SERVICE_CONTROL_INTERROGATE: int
SERVICE_CONTROL_NETBINDADD: int
SERVICE_CONTROL_NETBINDDISABLE: int
SERVICE_CONTROL_NETBINDENABLE: int
SERVICE_CONTROL_NETBINDREMOVE: int
SERVICE_CONTROL_PARAMCHANGE: int
SERVICE_CONTROL_PAUSE: int
SERVICE_CONTROL_POWEREVENT: int
SERVICE_CONTROL_PRESHUTDOWN: int
SERVICE_CONTROL_SESSIONCHANGE: int
SERVICE_CONTROL_SHUTDOWN: int
SERVICE_CONTROL_STOP: int
SERVICE_DEMAND_START: int
SERVICE_DISABLED: int
SERVICE_DRIVER: int
SERVICE_ENUMERATE_DEPENDENTS: int
SERVICE_ERROR_CRITICAL: int
SERVICE_ERROR_IGNORE: int
SERVICE_ERROR_NORMAL: int
SERVICE_ERROR_SEVERE: int
SERVICE_FILE_SYSTEM_DRIVER: int
SERVICE_INACTIVE: int
SERVICE_INTERACTIVE_PROCESS: int
SERVICE_INTERROGATE: int
SERVICE_KERNEL_DRIVER: int
SERVICE_NO_CHANGE: int
SERVICE_PAUSED: int
SERVICE_PAUSE_CONTINUE: int
SERVICE_PAUSE_PENDING: int
SERVICE_QUERY_CONFIG: int
SERVICE_QUERY_STATUS: int
SERVICE_RUNNING: int
SERVICE_SID_TYPE_NONE: int
SERVICE_SID_TYPE_RESTRICTED: int
SERVICE_SID_TYPE_UNRESTRICTED: int
SERVICE_SPECIFIC_ERROR: int
SERVICE_START: int
SERVICE_START_PENDING: int
SERVICE_STATE_ALL: int
SERVICE_STOP: int
SERVICE_STOPPED: int
SERVICE_STOP_PENDING: int
SERVICE_SYSTEM_START: int
SERVICE_USER_DEFINED_CONTROL: int
SERVICE_WIN32: int
SERVICE_WIN32_OWN_PROCESS: int
SERVICE_WIN32_SHARE_PROCESS: int
def SetServiceObjectSecurity() -> typing.Any:
    ...

def SetServiceStatus() -> typing.Any:
    ...

def SetUserObjectInformation() -> typing.Any:
    ...

def StartService() -> typing.Any:
    ...

UNICODE: int
UOI_FLAGS: int
UOI_NAME: int
UOI_TYPE: int
UOI_USER_SID: int
def UnlockServiceDatabase() -> typing.Any:
    ...

WSF_VISIBLE: int
__doc__: str
__file__: str
__name__: str
__package__: str
error = _mod_pywintypes.error
def __getattr__(name) -> typing.Any:
    ...

