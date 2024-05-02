from functools import _Wrapped
from types import FunctionType
from typing import Any, Callable

def threaded_factory(func, use_add) -> _Wrapped[..., Any, ..., Any]:
    ...

def threaded(func) -> _Wrapped[..., Any, ..., Any]:
    ...

def xthreaded(func) -> _Wrapped[..., Any, ..., Any]:
    ...

def conserve_mpmath_dps(func) -> Callable[..., Any]:
    ...

class no_attrs_in_subclass:
    def __init__(self, cls, f) -> None:
        ...
    
    def __get__(self, instance, owner=...) -> Any:
        ...
    


def doctest_depends_on(exe=..., modules=..., disable_viewers=..., python_version=...) -> Callable[..., type[Any] | Any]:
    ...

def public(obj) -> type:
    ...

def memoize_property(propfunc) -> property:
    ...

def deprecated(message, *, deprecated_since_version, active_deprecations_target, stacklevel=...) -> Callable[..., Any | _Wrapped[..., Any, ..., Any]]:
    ...

