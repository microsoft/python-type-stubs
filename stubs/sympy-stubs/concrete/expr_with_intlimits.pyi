from typing import Self
from sympy.concrete.expr_with_limits import ExprWithLimits

class ReorderError(NotImplementedError):
    def __init__(self, expr, msg) -> None:
        ...
    


class ExprWithIntLimits(ExprWithLimits):
    __slots__ = ...
    def change_index(self, var, trafo, newvar=...) -> Self:
        ...
    
    def index(self, x) -> int:
        ...
    
    def reorder(self, *arg) -> Self:
        ...
    
    def reorder_limit(self, x, y) -> Self:
        ...
    
    @property
    def has_empty_sequence(self) -> bool | None:
        ...
    


