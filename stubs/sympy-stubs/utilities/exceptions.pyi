import contextlib
from typing import Any, Callable, Generator, Self

class SymPyDeprecationWarning(DeprecationWarning):
    def __init__(self, message, *, deprecated_since_version, active_deprecations_target) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __reduce__(self) -> tuple[Callable[..., Self], tuple[Any, str, Any]]:
        ...
    


def sympy_deprecation_warning(message, *, deprecated_since_version, active_deprecations_target, stacklevel=...) -> None:
    ...

@contextlib.contextmanager
def ignore_warnings(warningcls) -> Generator[None, Any, None]:
    ...

