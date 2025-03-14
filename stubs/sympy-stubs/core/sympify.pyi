from typing import Any, Callable

from sympy.core.basic import Basic

class SympifyError(ValueError):
    def __init__(self, expr, base_exc=...) -> None: ...

converter: dict[type[Any], Callable[[Any], Basic]] = ...
_sympy_converter: dict[type[Any], Callable[[Any], Basic]] = ...
_external_converter = ...

class CantSympify:
    __slots__ = ...

def sympify(a, locals=..., convert_xor=..., strict=..., rational=..., evaluate=...): ...
def kernS(s) -> list[Any] | set[Any] | tuple[Any, ...]: ...
