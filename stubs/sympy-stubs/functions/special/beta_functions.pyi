from typing import Self

from sympy.core.function import Function, UndefinedFunction

def betainc_mpmath_fix(a, b, x1, x2, reg=...):
    ...

class beta(Function):
    unbranched = ...
    def fdiff(self, argindex):
        ...
    
    @classmethod
    def eval(cls, x, y=...) -> type[UndefinedFunction] | None:
        ...
    
    def doit(self, **hints) -> Self | type[UndefinedFunction]:
        ...
    


class betainc(Function):
    nargs = ...
    unbranched = ...
    def fdiff(self, argindex):
        ...
    


class betainc_regularized(Function):
    nargs = ...
    unbranched = ...
    def __new__(cls, a, b, x1, x2) -> type[UndefinedFunction]:
        ...
    
    def fdiff(self, argindex):
        ...
    


