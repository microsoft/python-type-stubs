from types import NotImplementedType
from typing import Self
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.logic import And
from sympy.core.numbers import _sympifyit
from sympy.core.power import Pow
from sympy.series.order import Order

class AccumulationBounds(Expr):
    is_extended_real = ...
    is_number = ...
    def __new__(cls, min, max) -> Self:
        ...
    
    _op_priority = ...
    @property
    def min(self) -> Basic:
        ...
    
    @property
    def max(self) -> Basic:
        ...
    
    @property
    def delta(self):
        ...
    
    @property
    def mid(self):
        ...
    
    @_sympifyit('other', NotImplemented)
    def __add__(self, other) -> AccumBounds | Order | NotImplementedType:
        ...
    
    __radd__ = ...
    def __neg__(self) -> AccumBounds:
        ...
    
    @_sympifyit('other', NotImplemented)
    def __sub__(self, other) -> AccumBounds | Order | NotImplementedType:
        ...
    
    @_sympifyit('other', NotImplemented)
    def __rsub__(self, other):
        ...
    
    @_sympifyit('other', NotImplemented)
    def __mul__(self, other) -> Self | AccumBounds | Order | NotImplementedType:
        ...
    
    __rmul__ = ...
    @_sympifyit('other', NotImplemented)
    def __truediv__(self, other):
        ...
    
    @_sympifyit('other', NotImplemented)
    def __rtruediv__(self, other) -> AccumBounds | Order | NotImplementedType:
        ...
    
    @_sympifyit('other', NotImplemented)
    def __pow__(self, other):
        ...
    
    @_sympifyit('other', NotImplemented)
    def __rpow__(self, other) -> Self | Pow:
        ...
    
    def __abs__(self) -> AccumBounds | Self:
        ...
    
    def __contains__(self, other) -> And | bool:
        ...
    
    def intersection(self, other) -> AccumBounds | Self | None:
        ...
    
    def union(self, other) -> AccumBounds | None:
        ...
    


AccumBounds = AccumulationBounds
