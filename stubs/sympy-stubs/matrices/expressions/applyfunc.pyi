from typing import Self

from sympy.core.basic import Basic
from sympy.matrices.expressions import MatrixExpr

class ElementwiseApplyFunction(MatrixExpr):
    def __new__(cls, function, expr) -> MatrixExpr | Self:
        ...
    
    @property
    def function(self) -> Basic:
        ...
    
    @property
    def expr(self) -> Basic:
        ...
    
    @property
    def shape(self):
        ...
    
    def doit(self, **hints) -> Basic | Self:
        ...
    


