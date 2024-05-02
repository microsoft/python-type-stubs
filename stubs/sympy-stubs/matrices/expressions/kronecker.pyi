from types import NotImplementedType
from typing import Any, Self

from sympy.matrices.expressions.matadd import MatAdd
from sympy.matrices.expressions.matexpr import MatrixExpr
from sympy.matrices.expressions.special import GenericIdentity, GenericZeroMatrix, Identity
from sympy.matrices.immutable import ImmutableDenseMatrix
from sympy.series.order import Order

def kronecker_product(*matrices) -> NotImplementedType | GenericIdentity | Order | object | Identity:
    ...

class KroneckerProduct(MatrixExpr):
    is_KroneckerProduct = ...
    def __new__(cls, *args, check=...) -> ImmutableDenseMatrix | Identity | Self:
        ...
    
    @property
    def shape(self) -> tuple[Any, Any]:
        ...
    
    def structurally_equal(self, other) -> bool:
        ...
    
    def has_matching_shape(self, other) -> bool | NotImplementedType:
        ...
    
    def doit(self, **hints) -> NotImplementedType | GenericIdentity | Order | object:
        ...
    


def validate(*args) -> None:
    ...

def extract_commutative(kron) -> NotImplementedType | GenericIdentity | Order | object:
    ...

def matrix_kronecker_product(*matrices):
    ...

def explicit_kronecker_product(kron):
    ...

rules = ...
canonicalize = ...
def kronecker_mat_add(expr) -> GenericZeroMatrix | MatAdd:
    ...

def kronecker_mat_mul(expr):
    ...

def kronecker_mat_pow(expr) -> ImmutableDenseMatrix | Identity | KroneckerProduct:
    ...

def combine_kronecker(expr) -> Any:
    ...

