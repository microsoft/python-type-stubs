# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32profile, version: unspecified
# Module: win32profile, version: unspecified

'Interface to the User Profile Api.'

import typing
import builtins as _mod_builtins

def CreateEnvironmentBlock() -> typing.Any:
    'Retrieves environment variables for a user'
    ...

def DeleteProfile() -> typing.Any:
    "Remove a user's profile"
    ...

def ExpandEnvironmentStringsForUser() -> typing.Any:
    'Replaces environment variables in a string with per-user values'
    ...

def GetAllUsersProfileDirectory() -> typing.Any:
    'Retrieve All Users profile directory'
    ...

def GetDefaultUserProfileDirectory() -> typing.Any:
    'Retrieve profile path for Default user'
    ...

def GetEnvironmentStrings() -> typing.Any:
    'Retrieves environment variables for current process'
    ...

def GetProfileType() -> typing.Any:
    "Returns type of current user's profile"
    ...

def GetProfilesDirectory() -> typing.Any:
    'Retrieves directory where user profiles are stored'
    ...

def GetUserProfileDirectory() -> typing.Any:
    'Returns profile directory for a logon token'
    ...

def LoadUserProfile() -> typing.Any:
    'Load user settings for a login token'
    ...

PI_APPLYPOLICY: int
PI_NOUI: int
PT_MANDATORY: int
PT_ROAMING: int
PT_TEMPORARY: int
def UnloadUserProfile() -> typing.Any:
    'Unload profile loaded by LoadUserProfile'
    ...

__doc__: str
__file__: str
__name__: str
__package__: str
def __getattr__(name) -> typing.Any:
    ...

