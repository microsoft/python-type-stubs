from typing import Self
from sympy.core.function import Function, UndefinedFunction
from sympy.core.mul import Mul

class MathieuBase(Function):
    unbranched = ...


class mathieus(MathieuBase):
    def fdiff(self, argindex=...) -> type[UndefinedFunction]:
        ...
    
    @classmethod
    def eval(cls, a, q, z) -> type[UndefinedFunction] | Mul | None:
        ...
    


class mathieuc(MathieuBase):
    def fdiff(self, argindex=...) -> type[UndefinedFunction]:
        ...
    
    @classmethod
    def eval(cls, a, q, z) -> type[UndefinedFunction] | Self | None:
        ...
    


class mathieusprime(MathieuBase):
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, a, q, z) -> Self | None:
        ...
    


class mathieucprime(MathieuBase):
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, a, q, z) -> Mul | None:
        ...
    


