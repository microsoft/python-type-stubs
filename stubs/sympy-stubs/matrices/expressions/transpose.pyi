from typing import Any
from sympy.core.basic import Basic
from sympy.matrices.expressions.matexpr import MatrixExpr

class Transpose(MatrixExpr):
    is_Transpose = ...
    def doit(self, **hints) -> Any | Transpose:
        ...
    
    @property
    def arg(self) -> Basic:
        ...
    
    @property
    def shape(self):
        ...
    


def transpose(expr) -> Any | Transpose:
    ...

def refine_Transpose(expr, assumptions):
    ...

