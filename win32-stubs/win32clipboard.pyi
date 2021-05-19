# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32clipboard, version: unspecified
# Module: win32clipboard, version: unspecified

'A module which supports the Windows Clipboard API.'

import typing
import builtins as _mod_builtins
from .lib import pywintypes as _mod_pywintypes

CF_BITMAP: int
CF_DIB: int
CF_DIBV5: int
CF_DIF: int
CF_DSPBITMAP: int
CF_DSPENHMETAFILE: int
CF_DSPMETAFILEPICT: int
CF_DSPTEXT: int
CF_ENHMETAFILE: int
CF_HDROP: int
CF_LOCALE: int
CF_MAX: int
CF_METAFILEPICT: int
CF_OEMTEXT: int
CF_OWNERDISPLAY: int
CF_PALETTE: int
CF_PENDATA: int
CF_RIFF: int
CF_SYLK: int
CF_TEXT: int
CF_TIFF: int
CF_UNICODETEXT: int
CF_WAVE: int
def ChangeClipboardChain() -> typing.Any:
    ...

def CloseClipboard() -> typing.Any:
    ...

def CountClipboardFormats() -> typing.Any:
    ...

def EmptyClipboard() -> typing.Any:
    ...

def EnumClipboardFormats() -> typing.Any:
    ...

def GetClipboardData() -> typing.Any:
    ...

def GetClipboardDataHandle() -> typing.Any:
    ...

def GetClipboardFormatName() -> typing.Any:
    ...

def GetClipboardOwner() -> typing.Any:
    ...

def GetClipboardSequenceNumber() -> typing.Any:
    ...

def GetClipboardViewer() -> typing.Any:
    ...

def GetGlobalMemory() -> typing.Any:
    ...

def GetOpenClipboardWindow() -> typing.Any:
    ...

def GetPriorityClipboardFormat() -> typing.Any:
    ...

def IsClipboardFormatAvailable() -> typing.Any:
    ...

def OpenClipboard() -> typing.Any:
    ...

def RegisterClipboardFormat() -> typing.Any:
    ...

def SetClipboardData() -> typing.Any:
    ...

def SetClipboardText() -> typing.Any:
    ...

def SetClipboardViewer() -> typing.Any:
    ...

UNICODE: bool
__doc__: str
__file__: str
__name__: str
__package__: str
error = _mod_pywintypes.error
def __getattr__(name) -> typing.Any:
    ...

