# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32process, version: unspecified
# Module: win32process, version: unspecified

''

import typing
import builtins as _mod_builtins
from .lib import pywintypes as _mod_pywintypes

ABOVE_NORMAL_PRIORITY_CLASS: int
def AttachThreadInput() -> typing.Any:
    ...

BELOW_NORMAL_PRIORITY_CLASS: int
CREATE_BREAKAWAY_FROM_JOB: int
CREATE_DEFAULT_ERROR_MODE: int
CREATE_NEW_CONSOLE: int
CREATE_NEW_PROCESS_GROUP: int
CREATE_NO_WINDOW: int
CREATE_PRESERVE_CODE_AUTHZ_LEVEL: int
CREATE_SEPARATE_WOW_VDM: int
CREATE_SHARED_WOW_VDM: int
CREATE_SUSPENDED: int
CREATE_UNICODE_ENVIRONMENT: int
def CreateProcess() -> typing.Any:
    ...

def CreateProcessAsUser() -> typing.Any:
    ...

def CreateRemoteThread() -> typing.Any:
    ...

DEBUG_ONLY_THIS_PROCESS: int
DEBUG_PROCESS: int
DETACHED_PROCESS: int
def EnumProcessModules() -> typing.Any:
    ...

def EnumProcessModulesEx() -> typing.Any:
    ...

def EnumProcesses() -> typing.Any:
    ...

def ExitProcess() -> typing.Any:
    ...

def GetCurrentProcess() -> typing.Any:
    ...

def GetCurrentProcessId() -> typing.Any:
    ...

def GetExitCodeProcess() -> typing.Any:
    ...

def GetExitCodeThread() -> typing.Any:
    ...

def GetGuiResources() -> typing.Any:
    ...

def GetModuleFileNameEx() -> typing.Any:
    ...

def GetPriorityClass() -> typing.Any:
    ...

def GetProcessAffinityMask() -> typing.Any:
    ...

def GetProcessId() -> typing.Any:
    ...

def GetProcessIoCounters() -> typing.Any:
    ...

def GetProcessMemoryInfo() -> typing.Any:
    ...

def GetProcessPriorityBoost() -> typing.Any:
    ...

def GetProcessShutdownParameters() -> typing.Any:
    ...

def GetProcessTimes() -> typing.Any:
    ...

def GetProcessVersion() -> typing.Any:
    ...

def GetProcessWindowStation() -> typing.Any:
    ...

def GetProcessWorkingSetSize() -> typing.Any:
    ...

def GetStartupInfo() -> typing.Any:
    ...

def GetThreadIOPendingFlag() -> typing.Any:
    ...

def GetThreadPriority() -> typing.Any:
    ...

def GetThreadPriorityBoost() -> typing.Any:
    ...

def GetThreadTimes() -> typing.Any:
    ...

def GetWindowThreadProcessId() -> typing.Any:
    ...

HIGH_PRIORITY_CLASS: int
IDLE_PRIORITY_CLASS: int
def IsWow64Process() -> typing.Any:
    ...

LIST_MODULES_32BIT: int
LIST_MODULES_64BIT: int
LIST_MODULES_ALL: int
LIST_MODULES_DEFAULT: int
MAXIMUM_PROCESSORS: int
NORMAL_PRIORITY_CLASS: int
REALTIME_PRIORITY_CLASS: int
def ReadProcessMemory() -> typing.Any:
    ...

def ResumeThread() -> typing.Any:
    ...

STARTF_FORCEOFFFEEDBACK: int
STARTF_FORCEONFEEDBACK: int
STARTF_RUNFULLSCREEN: int
STARTF_USECOUNTCHARS: int
STARTF_USEFILLATTRIBUTE: int
STARTF_USEPOSITION: int
STARTF_USESHOWWINDOW: int
STARTF_USESIZE: int
STARTF_USESTDHANDLES: int
def STARTUPINFO() -> typing.Any:
    ...

def SetPriorityClass() -> typing.Any:
    ...

def SetProcessAffinityMask() -> typing.Any:
    ...

def SetProcessPriorityBoost() -> typing.Any:
    ...

def SetProcessShutdownParameters() -> typing.Any:
    ...

def SetProcessWorkingSetSize() -> typing.Any:
    ...

def SetThreadAffinityMask() -> typing.Any:
    ...

def SetThreadIdealProcessor() -> typing.Any:
    ...

def SetThreadPriority() -> typing.Any:
    ...

def SetThreadPriorityBoost() -> typing.Any:
    ...

def SuspendThread() -> typing.Any:
    ...

THREAD_MODE_BACKGROUND_BEGIN: int
THREAD_MODE_BACKGROUND_END: int
THREAD_PRIORITY_ABOVE_NORMAL: int
THREAD_PRIORITY_BELOW_NORMAL: int
THREAD_PRIORITY_HIGHEST: int
THREAD_PRIORITY_IDLE: int
THREAD_PRIORITY_LOWEST: int
THREAD_PRIORITY_NORMAL: int
THREAD_PRIORITY_TIME_CRITICAL: int
def TerminateProcess() -> typing.Any:
    ...

UNICODE: int
def VirtualAllocEx() -> typing.Any:
    ...

def VirtualFreeEx() -> typing.Any:
    ...

def WriteProcessMemory() -> typing.Any:
    ...

__doc__: str
__file__: str
__name__: str
__package__: str
def beginthreadex() -> typing.Any:
    ...

error = _mod_pywintypes.error
def __getattr__(name) -> typing.Any:
    ...

