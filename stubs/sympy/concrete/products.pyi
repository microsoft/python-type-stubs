from typing import Any, Self, Tuple as tTuple
from sympy.concrete.expr_with_intlimits import ExprWithIntLimits
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.relational import Equality, Ne, Relational
from sympy.core.symbol import Symbol
from sympy.series.order import Order

class Product(ExprWithIntLimits):
    __slots__ = ...
    limits: tTuple[tTuple[Symbol, Expr, Expr]]
    def __new__(cls, function, *symbols, **assumptions) -> Equality | Relational | Ne | Self:
        ...
    
    @property
    def term(self) -> Basic:
        ...
    
    function = ...
    def doit(self, **hints) -> tuple[Any, ...] | Self | Basic | Equality | Order | Relational | Ne | Any:
        ...
    
    def is_convergent(self):
        ...
    
    def reverse_order(self, *indices) -> Product:
        ...
    


def product(*args, **kwargs) -> Equality | Relational | Ne:
    ...

