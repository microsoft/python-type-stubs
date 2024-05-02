from typing import Any

from numpy import ndarray as NDArray
from sympy.core.basic import Basic
from sympy.matrices.immutable import ImmutableDenseMatrix
from sympy.matrices.repmatrix import MutableRepMatrix, RepMatrix
from sympy.series.order import Order
from sympy.utilities.decorator import doctest_depends_on

class DenseMatrix(RepMatrix):
    is_MatrixExpr: bool = ...
    _op_priority = ...
    _class_priority = ...
    def as_immutable(self) -> ImmutableDenseMatrix:
        ...
    
    def as_mutable(self) -> Matrix:
        ...
    
    def cholesky(self, hermitian=...):
        ...
    
    def LDLdecomposition(self, hermitian=...) -> tuple[Any, Any]:
        ...
    
    def lower_triangular_solve(self, rhs):
        ...
    
    def upper_triangular_solve(self, rhs):
        ...
    


class MutableDenseMatrix(DenseMatrix, MutableRepMatrix):
    def simplify(self, **kwargs) -> None:
        ...
    


Matrix = MutableMatrix = MutableDenseMatrix
def list2numpy(l, dtype=...) -> NDArray[Any, Any]:
    ...

def matrix2numpy(m, dtype=...) -> NDArray[Any, Any]:
    ...

def rot_givens(i, j, theta, dim=...):
    ...

def rot_axis3(theta):
    ...

def rot_axis2(theta):
    ...

def rot_axis1(theta):
    ...

def rot_ccw_axis3(theta):
    ...

def rot_ccw_axis2(theta):
    ...

def rot_ccw_axis1(theta):
    ...

@doctest_depends_on(modules=('numpy', ))
def symarray(prefix, shape, **kwargs) -> NDArray[Any, Any]:
    ...

def casoratian(seqs, n, zero=...) -> tuple[Any | Basic, bool] | Any | Basic | Order:
    ...

def eye(*args, **kwargs):
    ...

def diag(*values, strict=..., unpack=..., **kwargs):
    ...

def GramSchmidt(vlist, orthonormal=...) -> list[Any]:
    ...

def hessian(f, varlist, constraints=...):
    ...

def jordan_cell(eigenval, n):
    ...

def matrix_multiply_elementwise(A, B):
    ...

def ones(*args, **kwargs):
    ...

def randMatrix(r, c=..., min=..., max=..., seed=..., symmetric=..., percent=..., prng=...):
    ...

def wronskian(functions, var, method=...) -> tuple[Any | Basic, bool] | Any | Basic | Order:
    ...

def zeros(*args, **kwargs):
    ...

