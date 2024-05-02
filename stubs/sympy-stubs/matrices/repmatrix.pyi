from typing import Any, Self
from sympy.matrices.dense import MutableDenseMatrix
from sympy.matrices.expressions.matexpr import MatrixElement
from sympy.polys.matrices import DomainMatrix
from sympy import MatrixBase
from sympy.matrices.common import MatrixKind

class RepMatrix(MatrixBase):
    _rep: DomainMatrix
    def __eq__(self, other) -> bool:
        ...
    
    def flat(self) -> list[Any]:
        ...
    
    def copy(self):
        ...
    
    @property
    def kind(self) -> MatrixKind:
        ...
    
    def __getitem__(self, key) -> MatrixElement | list[Any]:
        ...
    
    def equals(self, other, failing_expression=...) -> bool:
        ...
    


class MutableRepMatrix(RepMatrix):
    is_zero = ...
    def __new__(cls, *args, **kwargs) -> Self:
        ...
    
    def copy(self) -> Self:
        ...
    
    def as_mutable(self) -> Self:
        ...
    
    def __setitem__(self, key, value) -> None:
        ...
    
    def col_op(self, j, f) -> None:
        ...
    
    def col_swap(self, i, j) -> None:
        ...
    
    def row_op(self, i, f) -> None:
        ...
    
    def row_swap(self, i, j) -> None:
        ...
    
    def zip_row_op(self, i, k, f) -> None:
        ...
    
    def copyin_list(self, key, value) -> None:
        ...
    
    def copyin_matrix(self, key, value) -> None:
        ...
    
    def fill(self, value) -> None:
        ...
    


