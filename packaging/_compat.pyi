from ._typing import TYPE_CHECKING as TYPE_CHECKING
from typing import Any, Tuple, Type

PY2: Any
PY3: Any
string_types: Any

def with_metaclass(meta: Type[Any], *bases: Tuple[Type[Any], ...]) -> Any: ...
