from typing import Any, Self

from sympy.matrices.dense import DenseMatrix
from sympy.matrices.expressions import MatrixExpr
from sympy.matrices.repmatrix import RepMatrix
from sympy.matrices.sparse import SparseRepMatrix

def sympify_matrix(arg):
    ...

def sympify_mpmath_matrix(arg) -> ImmutableDenseMatrix:
    ...

class ImmutableRepMatrix(RepMatrix, MatrixExpr):
    def __new__(cls, *args, **kwargs):
        ...
    
    __hash__ = ...
    def copy(self) -> Self:
        ...
    
    @property
    def cols(self):
        ...
    
    @property
    def rows(self):
        ...
    
    @property
    def shape(self) -> tuple[Any, Any]:
        ...
    
    def as_immutable(self) -> Self:
        ...
    
    def __setitem__(self, *args):
        ...
    
    def is_diagonalizable(self, reals_only=..., **kwargs) -> bool:
        ...
    
    is_diagonalizable = ...


class ImmutableDenseMatrix(DenseMatrix, ImmutableRepMatrix):
    _iterable = ...
    _class_priority = ...
    _op_priority = ...


ImmutableMatrix = ImmutableDenseMatrix
class ImmutableSparseMatrix(SparseRepMatrix, ImmutableRepMatrix):
    is_Matrix = ...
    _class_priority = ...


