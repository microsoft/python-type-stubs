from typing import Self
from sympy.series.order import Order
from sympy.vector.basisdependent import BasisDependent, BasisDependentAdd, BasisDependentMul, BasisDependentZero
from sympy.core.expr import AtomicExpr
from sympy.vector.vector import VectorZero

class Dyadic(BasisDependent):
    _op_priority = ...
    _expr_type: type[Dyadic]
    _mul_func: type[Dyadic]
    _add_func: type[Dyadic]
    _zero_func: type[Dyadic]
    _base_func: type[Dyadic]
    zero: DyadicZero
    @property
    def components(self):
        ...
    
    def dot(self, other) -> VectorZero | DyadicZero:
        ...
    
    def __and__(self, other) -> VectorZero | DyadicZero:
        ...
    
    def cross(self, other) -> DyadicZero:
        ...
    
    def __xor__(self, other) -> DyadicZero:
        ...
    
    def to_matrix(self, system, second_system=...):
        ...
    


class BaseDyadic(Dyadic, AtomicExpr):
    def __new__(cls, vector1, vector2) -> DyadicZero | Self:
        ...
    


class DyadicMul(BasisDependentMul, Dyadic):
    def __new__(cls, *args, **options) -> Order | BasisDependentZero:
        ...
    
    @property
    def base_dyadic(self):
        ...
    
    @property
    def measure_number(self):
        ...
    


class DyadicAdd(BasisDependentAdd, Dyadic):
    def __new__(cls, *args, **options) -> BasisDependentZero | Order:
        ...
    


class DyadicZero(BasisDependentZero, Dyadic):
    _op_priority = ...
    _pretty_form = ...
    _latex_form = ...
    def __new__(cls) -> Self:
        ...
    


