from typing import Any, Self

from sympy.core.expr import Expr
from sympy.core.mul import Mul
from sympy.matrices.expressions.matadd import MatAdd
from sympy.matrices.expressions.matexpr import MatrixExpr
from sympy.matrices.expressions.special import GenericIdentity, GenericZeroMatrix, ZeroMatrix
from sympy.series.order import Order

class MatMul(MatrixExpr, Mul):
    is_MatMul = ...
    identity = ...
    def __new__(cls, *args, evaluate=..., check=..., _sympify=...) -> GenericIdentity | Order | object | Self:
        ...
    
    @property
    def shape(self) -> tuple[Any, Any]:
        ...
    
    def as_coeff_matrices(self) -> tuple[Any | Order, list[Expr]]:
        ...
    
    def as_coeff_mmul(self) -> tuple[Any | Order, GenericIdentity | Any | Order | object | MatMul]:
        ...
    
    def expand(self, **kwargs) -> object:
        ...
    
    def doit(self, **hints) -> object:
        ...
    
    def args_cnc(self, cset=..., warn=..., **kwargs) -> list[Any]:
        ...
    


def newmul(*args) -> MatMul:
    ...

def any_zeros(mul) -> ZeroMatrix:
    ...

def merge_explicit(matmul) -> MatMul:
    ...

def remove_ids(mul) -> MatMul:
    ...

def factor_in_front(mul) -> MatMul:
    ...

def combine_powers(mul) -> MatMul:
    ...

def combine_permutations(mul) -> MatMul:
    ...

def combine_one_matrices(mul) -> MatMul:
    ...

def distribute_monom(mul) -> GenericZeroMatrix | MatAdd:
    ...

rules = ...
canonicalize = ...
def only_squares(*matrices) -> list[Any]:
    ...

def refine_MatMul(expr, assumptions) -> GenericIdentity | Order | object | MatMul:
    ...

