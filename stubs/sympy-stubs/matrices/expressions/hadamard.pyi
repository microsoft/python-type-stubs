from typing import Self

from sympy.core.basic import Basic
from sympy.matrices.expressions.matexpr import MatrixExpr

def hadamard_product(*matrices):
    ...

class HadamardProduct(MatrixExpr):
    is_HadamardProduct = ...
    def __new__(cls, *args, evaluate=..., check=...) -> Self:
        ...
    
    @property
    def shape(self):
        ...
    
    def doit(self, **hints):
        ...
    


def canonicalize(x):
    ...

def hadamard_power(base, exp) -> HadamardPower:
    ...

class HadamardPower(MatrixExpr):
    def __new__(cls, base, exp) -> Self:
        ...
    
    @property
    def base(self) -> Basic:
        ...
    
    @property
    def exp(self) -> Basic:
        ...
    
    @property
    def shape(self):
        ...
    


