from typing import Self
from sympy.core.basic import Basic
from sympy.matrices.expressions.matpow import MatPow

class Inverse(MatPow):
    is_Inverse = ...
    exp = ...
    def __new__(cls, mat, exp=...) -> Self:
        ...
    
    @property
    def arg(self) -> Basic:
        ...
    
    @property
    def shape(self):
        ...
    
    def doit(self, **hints) -> Self:
        ...
    


def refine_Inverse(expr, assumptions):
    ...

