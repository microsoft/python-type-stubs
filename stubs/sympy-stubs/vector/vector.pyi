from typing import Any, Callable, Literal, Self
from sympy import ImmutableDenseMatrix, Pow
from sympy.core.add import Add
from sympy.core.expr import AtomicExpr, Expr
from sympy.series.order import Order
from sympy.vector.basisdependent import BasisDependent, BasisDependentAdd, BasisDependentMul, BasisDependentZero
from sympy.vector.dyadic import DyadicZero

class Vector(BasisDependent):
    is_scalar = ...
    is_Vector = ...
    _op_priority = ...
    _expr_type: type[Vector]
    _mul_func: type[Vector]
    _add_func: type[Vector]
    _zero_func: type[Vector]
    _base_func: type[Vector]
    zero: VectorZero
    @property
    def components(self):
        ...
    
    def magnitude(self) -> Pow:
        ...
    
    def normalize(self):
        ...
    
    def dot(self, other) -> VectorZero | Callable[..., VectorZero | Any | Literal[0]] | Add | Dot:
        ...
    
    def __and__(self, other) -> VectorZero | Callable[..., VectorZero | Any | Literal[0]] | Add | Dot:
        ...
    
    def cross(self, other) -> DyadicZero | VectorAdd | VectorZero | Cross:
        ...
    
    def __xor__(self, other) -> DyadicZero | VectorAdd | VectorZero | Cross:
        ...
    
    def outer(self, other) -> DyadicZero | BasisDependentZero | Order:
        ...
    
    def projection(self, other, scalar=...) -> VectorZero:
        ...
    
    def __or__(self, other) -> DyadicZero | BasisDependentZero | Order:
        ...
    
    def to_matrix(self, system) -> ImmutableDenseMatrix:
        ...
    
    def separate(self) -> dict[Any, Any]:
        ...
    


class BaseVector(Vector, AtomicExpr):
    def __new__(cls, index, system, pretty_str=..., latex_str=...) -> Self:
        ...
    
    @property
    def system(self):
        ...
    
    @property
    def free_symbols(self) -> set[Self]:
        ...
    


class VectorAdd(BasisDependentAdd, Vector):
    def __new__(cls, *args, **options) -> BasisDependentZero | Order:
        ...
    


class VectorMul(BasisDependentMul, Vector):
    def __new__(cls, *args, **options) -> Order | BasisDependentZero:
        ...
    
    @property
    def base_vector(self):
        ...
    
    @property
    def measure_number(self):
        ...
    


class VectorZero(BasisDependentZero, Vector):
    _op_priority = ...
    _pretty_form = ...
    _latex_form = ...
    def __new__(cls) -> Self:
        ...
    


class Cross(Vector):
    def __new__(cls, expr1, expr2) -> Self:
        ...
    
    def doit(self, **hints) -> VectorAdd | VectorZero | Cross:
        ...
    


class Dot(Expr):
    def __new__(cls, expr1, expr2) -> Self:
        ...
    
    def doit(self, **hints) -> Add | Dot:
        ...
    


def cross(vect1, vect2) -> VectorAdd | VectorZero | Cross:
    ...

def dot(vect1, vect2) -> Add | Dot:
    ...

