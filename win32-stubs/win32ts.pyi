# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32ts, version: unspecified
# Module: win32ts, version: unspecified

'Interface to the Terminal Services Api.'

import typing
import builtins as _mod_builtins

NOTIFY_FOR_ALL_SESSIONS: int
NOTIFY_FOR_THIS_SESSION: int
def ProcessIdToSessionId() -> typing.Any:
    'Finds the session under which a process is running'
    ...

WTSActive: int
WTSApplicationName: int
WTSClientAddress: int
WTSClientBuildNumber: int
WTSClientDirectory: int
WTSClientDisplay: int
WTSClientHardwareId: int
WTSClientName: int
WTSClientProductId: int
WTSClientProtocolType: int
def WTSCloseServer() -> typing.Any:
    'Closes a terminal server handle'
    ...

WTSConnectQuery: int
WTSConnectState: int
WTSConnected: int
def WTSDisconnectSession() -> typing.Any:
    'Disconnects a session without logging it off'
    ...

WTSDisconnected: int
WTSDomainName: int
WTSDown: int
def WTSEnumerateProcesses() -> typing.Any:
    'Lists processes on a terminal server'
    ...

def WTSEnumerateServers() -> typing.Any:
    'Lists terminal servers in a domain'
    ...

def WTSEnumerateSessions() -> typing.Any:
    'Lists sessions on a server'
    ...

def WTSGetActiveConsoleSessionId() -> typing.Any:
    'Returns the id of the console session'
    ...

WTSIdle: int
WTSInit: int
WTSInitialProgram: int
WTSListen: int
def WTSLogoffSession() -> typing.Any:
    'Logs off a user logged in through Terminal Services'
    ...

WTSOEMId: int
def WTSOpenServer() -> typing.Any:
    'Opens a handle to a terminal server'
    ...

def WTSQuerySessionInformation() -> typing.Any:
    'Retrieve information about a session'
    ...

def WTSQueryUserConfig() -> typing.Any:
    'Returns user configuration'
    ...

def WTSQueryUserToken() -> typing.Any:
    'Retrieves the access token for a session'
    ...

def WTSRegisterSessionNotification() -> typing.Any:
    'Registers a window to receive terminal service notifications'
    ...

WTSReset: int
def WTSSendMessage() -> typing.Any:
    'Sends a popup message to a terminal services session'
    ...

WTSSessionId: int
def WTSSetUserConfig() -> typing.Any:
    'Changes user configuration'
    ...

WTSShadow: int
def WTSShutdownSystem() -> typing.Any:
    'Issues a shutdown request to a terminal server'
    ...

def WTSTerminateProcess() -> typing.Any:
    'Kills a process on a terminal server'
    ...

def WTSUnRegisterSessionNotification() -> typing.Any:
    'Disables terminal service window messages'
    ...

WTSUserConfigBrokenTimeoutSettings: int
WTSUserConfigInitialProgram: int
WTSUserConfigModemCallbackPhoneNumber: int
WTSUserConfigModemCallbackSettings: int
WTSUserConfigReconnectSettings: int
WTSUserConfigShadowingSettings: int
WTSUserConfigTerminalServerHomeDir: int
WTSUserConfigTerminalServerHomeDirDrive: int
WTSUserConfigTerminalServerProfilePath: int
WTSUserConfigTimeoutSettingsConnections: int
WTSUserConfigTimeoutSettingsDisconnections: int
WTSUserConfigTimeoutSettingsIdle: int
WTSUserConfigWorkingDirectory: int
WTSUserConfigfAllowLogonTerminalServer: int
WTSUserConfigfDeviceClientDefaultPrinter: int
WTSUserConfigfDeviceClientDrives: int
WTSUserConfigfDeviceClientPrinters: int
WTSUserConfigfInheritInitialProgram: int
WTSUserConfigfTerminalServerRemoteHomeDir: int
WTSUserName: int
WTSVirtualClientData: int
WTSVirtualFileHandle: int
def WTSWaitSystemEvent() -> typing.Any:
    'Waits for an event to occur'
    ...

WTSWinStationName: int
WTSWorkingDirectory: int
WTS_CURRENT_SERVER: int
WTS_CURRENT_SERVER_HANDLE: int
WTS_CURRENT_SERVER_NAME: typing.Any
WTS_CURRENT_SESSION: int
WTS_EVENT_ALL: int
WTS_EVENT_CONNECT: int
WTS_EVENT_CREATE: int
WTS_EVENT_DELETE: int
WTS_EVENT_DISCONNECT: int
WTS_EVENT_FLUSH: int
WTS_EVENT_LICENSE: int
WTS_EVENT_LOGOFF: int
WTS_EVENT_LOGON: int
WTS_EVENT_NONE: int
WTS_EVENT_RENAME: int
WTS_EVENT_STATECHANGE: int
WTS_PROTOCOL_TYPE_CONSOLE: int
WTS_PROTOCOL_TYPE_ICA: int
WTS_PROTOCOL_TYPE_RDP: int
WTS_WSD_FASTREBOOT: int
WTS_WSD_LOGOFF: int
WTS_WSD_POWEROFF: int
WTS_WSD_REBOOT: int
WTS_WSD_SHUTDOWN: int
__doc__: str
__file__: str
__name__: str
__package__: str
def __getattr__(name) -> typing.Any:
    ...

