# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32console, version: unspecified
# Module: win32console, version: unspecified

'Interface to the Windows Console functions for dealing with character-mode applications.'

import typing
import builtins as _mod_builtins
from .lib import pywintypes as _mod_pywintypes

ATTACH_PARENT_PROCESS: int
def AddConsoleAlias() -> typing.Any:
    'Creates a new console alias'
    ...

def AllocConsole() -> typing.Any:
    'Creates a new console for the calling process'
    ...

def AttachConsole() -> typing.Any:
    'Attaches calling process to console of another process'
    ...

BACKGROUND_BLUE: int
BACKGROUND_GREEN: int
BACKGROUND_INTENSITY: int
BACKGROUND_RED: int
COMMON_LVB_GRID_HORIZONTAL: int
COMMON_LVB_GRID_LVERTICAL: int
COMMON_LVB_GRID_RVERTICAL: int
COMMON_LVB_LEADING_BYTE: int
COMMON_LVB_REVERSE_VIDEO: int
COMMON_LVB_TRAILING_BYTE: int
COMMON_LVB_UNDERSCORE: int
CONSOLE_FULLSCREEN: int
CONSOLE_FULLSCREEN_HARDWARE: int
CONSOLE_FULLSCREEN_MODE: int
CONSOLE_MOUSE_DOWN: int
CONSOLE_MOUSE_SELECTION: int
CONSOLE_NO_SELECTION: int
CONSOLE_SELECTION_IN_PROGRESS: int
CONSOLE_SELECTION_NOT_EMPTY: int
CONSOLE_TEXTMODE_BUFFER: int
CONSOLE_WINDOWED_MODE: int
CTRL_BREAK_EVENT: int
CTRL_C_EVENT: int
def CreateConsoleScreenBuffer() -> typing.Any:
    'Creates a new console screen buffer'
    ...

ENABLE_ECHO_INPUT: int
ENABLE_LINE_INPUT: int
ENABLE_MOUSE_INPUT: int
ENABLE_PROCESSED_INPUT: int
ENABLE_PROCESSED_OUTPUT: int
ENABLE_WINDOW_INPUT: int
ENABLE_WRAP_AT_EOL_OUTPUT: int
FOCUS_EVENT: int
FOREGROUND_BLUE: int
FOREGROUND_GREEN: int
FOREGROUND_INTENSITY: int
FOREGROUND_RED: int
def FreeConsole() -> typing.Any:
    'Detaches process from its console'
    ...

def GenerateConsoleCtrlEvent() -> typing.Any:
    'Sends a control signal to a group of processes attached to a common console'
    ...

def GetConsoleAliasExes() -> typing.Any:
    'Lists all executables that have console aliases defined'
    ...

def GetConsoleAliases() -> typing.Any:
    'Retrieves aliases defined under specified executable'
    ...

def GetConsoleCP() -> typing.Any:
    "Returns the input code page for calling process's console"
    ...

def GetConsoleDisplayMode() -> typing.Any:
    "Returns the current console's display mode"
    ...

def GetConsoleOutputCP() -> typing.Any:
    "Returns the output code page for calling process's console"
    ...

def GetConsoleProcessList() -> typing.Any:
    'Returns pids of all processes attached to current console'
    ...

def GetConsoleSelectionInfo() -> typing.Any:
    'Returns info on text selection within the current console'
    ...

def GetConsoleTitle() -> typing.Any:
    'Returns the title of console to which calling process is attached'
    ...

def GetConsoleWindow() -> typing.Any:
    "Returns a handle to the console's window, or 0 if none exists"
    ...

def GetNumberOfConsoleFonts() -> typing.Any:
    'Returns the number of fonts available to the console'
    ...

def GetStdHandle() -> typing.Any:
    "Returns one of calling process's standard handles"
    ...

KEY_EVENT: int
LOCALE_USER_DEFAULT: int
MENU_EVENT: int
MOUSE_EVENT: int
PyCOORDType = _mod_builtins.PyCOORD
PyConsoleScreenBufferType = _mod_builtins.PyConsoleScreenBuffer
PyINPUT_RECORDType = _mod_builtins.PyINPUT_RECORD
PySMALL_RECTType = _mod_builtins.PySMALL_RECT
STD_ERROR_HANDLE: int
STD_INPUT_HANDLE: int
STD_OUTPUT_HANDLE: int
def SetConsoleCP() -> typing.Any:
    "Sets the input code page for calling process's console"
    ...

def SetConsoleOutputCP() -> typing.Any:
    "Sets the output code page for calling process's console"
    ...

def SetConsoleTitle() -> typing.Any:
    "Sets the title of calling process's console"
    ...

WINDOW_BUFFER_SIZE_EVENT: int
__doc__: str
__file__: str
__name__: str
__package__: str
error = _mod_pywintypes.error
def __getattr__(name) -> typing.Any:
    ...

