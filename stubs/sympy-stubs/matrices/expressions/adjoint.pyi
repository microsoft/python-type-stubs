from sympy.core.basic import Basic
from sympy.core.function import UndefinedFunction
from sympy.matrices.expressions.matexpr import MatrixExpr

class Adjoint(MatrixExpr):
    is_Adjoint = ...
    def doit(self, **hints) -> type[UndefinedFunction]:
        ...
    
    @property
    def arg(self) -> Basic:
        ...
    
    @property
    def shape(self):
        ...
    


