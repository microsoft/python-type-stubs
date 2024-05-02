from typing import Any, Self
from sympy import MatrixBase
from sympy.core.expr import Expr
from sympy.matrices.expressions import MatrixExpr

class DiagonalMatrix(MatrixExpr):
    arg = ...
    shape = ...
    @property
    def diagonal_length(self) -> Expr | None:
        ...
    


class DiagonalOf(MatrixExpr):
    arg = ...
    @property
    def shape(self) -> tuple[Any | None, Any]:
        ...
    
    @property
    def diagonal_length(self) -> Any | None:
        ...
    


class DiagMatrix(MatrixExpr):
    def __new__(cls, vector) -> Self:
        ...
    
    @property
    def shape(self):
        ...
    
    def as_explicit(self):
        ...
    
    def doit(self, **hints) -> MatrixBase | DiagMatrix:
        ...
    


def diagonalize_vector(vector) -> MatrixBase | DiagMatrix:
    ...

