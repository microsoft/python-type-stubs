from typing import Any
from sympy.core.function import Function, UndefinedFunction

_x = ...
class Ynm(Function):
    @classmethod
    def eval(cls, n, m, theta, phi) -> type[UndefinedFunction] | None:
        ...
    
    def fdiff(self, argindex=...):
        ...
    
    def as_real_imag(self, deep=..., **hints) -> tuple[Any, Any]:
        ...
    


def Ynm_c(n, m, theta, phi) -> type[UndefinedFunction]:
    ...

class Znm(Function):
    @classmethod
    def eval(cls, n, m, theta, phi) -> type[UndefinedFunction] | None:
        ...
    


