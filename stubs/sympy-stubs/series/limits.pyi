from typing import Self
from sympy.core import Expr
from sympy.core.basic import Basic
from sympy.core.function import UndefinedFunction

def limit(e, z, z0, dir=...):
    ...

def heuristics(e, z, z0, dir):
    ...

class Limit(Expr):
    def __new__(cls, e, z, z0, dir=...) -> Self:
        ...
    
    @property
    def free_symbols(self) -> set[Basic]:
        ...
    
    def pow_heuristics(self, e) -> type[UndefinedFunction] | None:
        ...
    
    def doit(self, **hints):
        ...
    


