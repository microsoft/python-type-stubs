# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: timer, version: 0.2
# Module: timer, version: 0.2

'Extension that wraps Win32 Timer functions'

import typing
import builtins as _mod_builtins
from .lib import pywintypes as _mod_pywintypes

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
error = _mod_pywintypes.error
def kill_timer(timer_id) -> typing.Any:
    'boolean = kill_timer(timer_id)\nStops a timer'
    ...

def set_timer() -> typing.Any:
    'int = set_timer(milliseconds, callback}\nCreates a timer that executes a callback function'
    ...

def __getattr__(name) -> typing.Any:
    ...

