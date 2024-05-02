from types import NotImplementedType
from typing import Any

from sympy.matrices.immutable import ImmutableSparseMatrix
from sympy.matrices.repmatrix import MutableRepMatrix, RepMatrix

class SparseRepMatrix(RepMatrix):
    def applyfunc(self, f):
        ...
    
    def as_immutable(self) -> ImmutableSparseMatrix:
        ...
    
    def as_mutable(self) -> MutableSparseMatrix:
        ...
    
    def col_list(self) -> list[tuple[Any, ...]]:
        ...
    
    def nnz(self) -> int:
        ...
    
    def row_list(self) -> list[tuple[Any, ...]]:
        ...
    
    def scalar_multiply(self, scalar):
        "Scalar element-wise multiplication"
        ...
    
    def solve_least_squares(self, rhs, method=...):
        ...
    
    def solve(self, rhs, method=...) -> NotImplementedType | None:
        ...
    
    RL = ...
    CL = ...
    def liupc(self) -> tuple[list[list[Any]], Any]:
        ...
    
    def row_structure_symbolic_cholesky(self):
        ...
    
    def cholesky(self, hermitian=...):
        ...
    
    def LDLdecomposition(self, hermitian=...) -> tuple[Any, Any]:
        ...
    
    def lower_triangular_solve(self, rhs):
        ...
    
    def upper_triangular_solve(self, rhs):
        ...
    


class MutableSparseMatrix(SparseRepMatrix, MutableRepMatrix):
    ...


SparseMatrix = MutableSparseMatrix
