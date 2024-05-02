from typing import Any, Self
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.kind import Kind
from sympy.core.relational import Equality, Ne, Relational

class ExprWithLimits(Expr):
    __slots__ = ...
    def __new__(cls, function, *symbols, **assumptions) -> Equality | Relational | Ne | Self:
        ...
    
    @property
    def function(self) -> Basic:
        ...
    
    @property
    def kind(self) -> Kind:
        ...
    
    @property
    def limits(self) -> tuple[Basic, ...]:
        ...
    
    @property
    def variables(self) -> list[Any]:
        ...
    
    @property
    def bound_symbols(self) -> list[Any]:
        ...
    
    @property
    def free_symbols(self) -> set[Any]:
        ...
    
    @property
    def is_number(self) -> bool:
        ...
    
    @property
    def has_finite_limits(self) -> bool | None:
        ...
    
    @property
    def has_reversed_limits(self) -> bool | None:
        ...
    


class AddWithLimits(ExprWithLimits):
    __slots__ = ...
    def __new__(cls, function, *symbols, **assumptions) -> Equality | Relational | Ne | Self:
        ...
    


