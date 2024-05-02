from types import NotImplementedType
from typing import Any, Self

from sympy.external.gmpy import GROUND_TYPES
from sympy.series.order import Order

_gens_order = ...
_max_order = ...
_re_gen = ...
illegal_types = ...
finf = ...

def parallel_dict_from_expr(exprs, **args) -> tuple[list[Any], Any]: ...
def dict_from_expr(expr, **args) -> tuple[Any, Any]: ...
def expr_from_dict(rep, *gens) -> Order: ...

parallel_dict_from_basic = ...
dict_from_basic = ...
basic_from_dict = ...

class PicklableWithSlots:
    __slots__ = ...
    def __getstate__(self, cls=...) -> dict[Any, Any]: ...
    def __setstate__(self, d) -> None: ...

class IntegerPowerable:
    def __pow__(self, e, modulo=...) -> NotImplementedType | Self: ...
