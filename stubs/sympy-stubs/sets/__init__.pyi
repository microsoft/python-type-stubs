from sympy.core.singleton import S
from sympy.sets.conditionset import ConditionSet
from sympy.sets.contains import Contains
from sympy.sets.fancysets import (
    Complexes as _Complexes,
    ComplexRegion,
    ImageSet,
    Integers as _Integers,
    Naturals as _Naturals,
    Naturals0 as _Naturals0,
    Range,
    Rationals as _Rationals,
    Reals as _Reals,
)
from sympy.sets.handlers.comparison import _eval_is_eq
from sympy.sets.ordinals import OmegaPower, Ordinal, ord0
from sympy.sets.powerset import PowerSet
from sympy.sets.sets import (
    Complement,
    DisjointUnion,
    EmptySet as _EmptySet,
    FiniteSet,
    Intersection,
    Interval,
    ProductSet,
    Set,
    SymmetricDifference,
    Union,
    UniversalSet as _UniversalSet,
    imageset,
)

Complexes: _Complexes
EmptySet: _EmptySet
Integers: _Integers
Naturals: _Naturals
Naturals0: _Naturals0
Rationals: _Rationals
Reals: _Reals
UniversalSet: _UniversalSet
__all__ = [
    "Set",
    "Interval",
    "Union",
    "EmptySet",
    "FiniteSet",
    "ProductSet",
    "Intersection",
    "imageset",
    "Complement",
    "SymmetricDifference",
    "DisjointUnion",
    "ImageSet",
    "Range",
    "ComplexRegion",
    "Reals",
    "Contains",
    "ConditionSet",
    "Ordinal",
    "OmegaPower",
    "ord0",
    "PowerSet",
    "Reals",
    "Naturals",
    "Naturals0",
    "UniversalSet",
    "Integers",
    "Rationals",
]
