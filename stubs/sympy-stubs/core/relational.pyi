from types import NotImplementedType
from typing import Any, Self

from sympy.core.basic import Basic
from sympy.core.evalf import EvalfMixin
from sympy.logic.boolalg import Boolean

__all__ = ('Rel', 'Eq', 'Ne', 'Lt', 'Le', 'Gt', 'Ge', 'Relational', 'Equality', 'Unequality', 'StrictLessThan', 'LessThan', 'StrictGreaterThan', 'GreaterThan')
class Relational(Boolean, EvalfMixin):
    __slots__ = ...
    ValidRelationOperator: dict[str | None, type[Relational]] = ...
    is_Relational = ...
    def __new__(cls, lhs, rhs, rop=..., **assumptions) -> Self | Eq | Relational | Ne:
        ...
    
    @property
    def lhs(self) -> Basic:
        ...
    
    @property
    def rhs(self) -> Basic:
        ...
    
    @property
    def reversed(self) -> Eq | Relational | Ne:
        ...
    
    @property
    def reversedsign(self) -> Eq | Relational | Ne | Self:
        ...
    
    @property
    def negated(self) -> Self | Eq | Relational | Ne:
        ...
    
    @property
    def weak(self) -> Self:
        ...
    
    @property
    def strict(self) -> Self:
        ...
    
    @property
    def canonical(self) -> Eq | Relational | Ne | Self:
        ...
    
    def equals(self, other, failing_expression=...) -> bool | None:
        ...
    
    def expand(self, **kwargs) -> Self:
        ...
    
    def __bool__(self):
        ...
    
    @property
    def binary_symbols(self) -> set[Any]:
        ...
    


Rel = Relational
class Equality(Relational):
    rel_op = ...
    __slots__ = ...
    is_Equality = ...
    def __new__(cls, lhs, rhs, **options) -> Self | Eq | Relational | Ne:
        ...
    
    @property
    def binary_symbols(self) -> set[Basic] | set[Any]:
        ...
    
    def integrate(self, *args, **kwargs) -> Equality | Relational | Ne:
        ...
    
    def as_poly(self, *gens, **kwargs):
        ...
    


Eq = Equality
class Unequality(Relational):
    rel_op = ...
    __slots__ = ...
    def __new__(cls, lhs, rhs, **options) -> Self:
        ...
    
    @property
    def binary_symbols(self) -> set[Basic] | set[Any]:
        ...
    


Ne = Unequality
class _Inequality(Relational):
    __slots__ = ...
    def __new__(cls, lhs, rhs, **options) -> NotImplementedType | Self | Eq | Relational | Ne:
        ...
    


class _Greater(_Inequality):
    __slots__ = ...
    @property
    def gts(self) -> Basic:
        ...
    
    @property
    def lts(self) -> Basic:
        ...
    


class _Less(_Inequality):
    __slots__ = ...
    @property
    def gts(self) -> Basic:
        ...
    
    @property
    def lts(self) -> Basic:
        ...
    


class GreaterThan(_Greater):
    __slots__ = ...
    rel_op = ...
    @property
    def strict(self) -> NotImplementedType | Gt | Eq | Relational | Ne:
        ...
    


Ge = GreaterThan
class LessThan(_Less):
    __doc__ = ...
    __slots__ = ...
    rel_op = ...
    @property
    def strict(self) -> NotImplementedType | Lt | Eq | Relational | Ne:
        ...
    


Le = LessThan
class StrictGreaterThan(_Greater):
    __doc__ = ...
    __slots__ = ...
    rel_op = ...
    @property
    def weak(self) -> NotImplementedType | Ge | Eq | Relational | Ne:
        ...
    


Gt = StrictGreaterThan
class StrictLessThan(_Less):
    __doc__ = ...
    __slots__ = ...
    rel_op = ...
    @property
    def weak(self) -> NotImplementedType | Le | Eq | Relational | Ne:
        ...
    


Lt = StrictLessThan
def is_lt(lhs, rhs, assumptions=...) -> bool | None:
    ...

def is_gt(lhs, rhs, assumptions=...) -> bool | None:
    ...

def is_le(lhs, rhs, assumptions=...) -> bool | None:
    ...

def is_ge(lhs, rhs, assumptions=...) -> bool | None:
    ...

def is_neq(lhs, rhs, assumptions=...) -> bool:
    ...

def is_eq(lhs, rhs, assumptions=...):
    ...

