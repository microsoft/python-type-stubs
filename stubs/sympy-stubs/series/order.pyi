from typing import Any, Self
from sympy.core import Expr
from sympy.core.basic import Basic
from sympy.core.cache import cacheit

class Order(Expr):
    is_Order = ...
    __slots__ = ...
    @cacheit
    def __new__(cls, expr, *args, **kwargs):
        ...
    
    @property
    def expr(self) -> Basic:
        ...
    
    @property
    def variables(self) -> tuple[Any, ...] | tuple[()]:
        ...
    
    @property
    def point(self) -> tuple[Any, ...] | tuple[()]:
        ...
    
    @property
    def free_symbols(self) -> set[Basic]:
        ...
    
    def as_expr_variables(self, order_symbols) -> tuple[Basic, tuple[tuple[Any, Any] | Basic, ...]]:
        ...
    
    def removeO(self):
        ...
    
    def getO(self) -> Self:
        ...
    
    @cacheit
    def contains(self, expr):
        ...
    
    def __contains__(self, other):
        ...
    
    def __neg__(self) -> Self:
        ...
    


O = Order
