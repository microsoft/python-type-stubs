from . import compat as compat
from .. import exc as exc
from .langhelpers import decorator as decorator, inject_docstring_text as inject_docstring_text, inject_param_text as inject_param_text
from typing import Any, Optional

def warn_deprecated(msg: Any, stacklevel: int = ...) -> None: ...
def warn_deprecated_limited(msg: Any, args: Any, stacklevel: int = ...) -> None: ...
def warn_pending_deprecation(msg: Any, stacklevel: int = ...) -> None: ...
def deprecated_cls(version: Any, message: Any, constructor: str = ...): ...
def deprecated(version: Any, message: Optional[Any] = ..., add_deprecation_to_docstring: bool = ...): ...
def deprecated_params(**specs: Any): ...
def pending_deprecation(version: Any, message: Optional[Any] = ..., add_deprecation_to_docstring: bool = ...): ...
def deprecated_option_value(parameter_value: Any, default_value: Any, warning_text: Any): ...
