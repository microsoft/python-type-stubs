from typing import Self
from sympy.core.basic import Basic
from sympy.core.expr import Expr

class Trace(Expr):
    is_Trace = ...
    is_commutative = ...
    def __new__(cls, mat) -> Self:
        ...
    
    @property
    def arg(self) -> Basic:
        ...
    
    def doit(self, **hints) -> Trace:
        ...
    
    def as_explicit(self) -> Trace:
        ...
    


def trace(expr):
    ...

