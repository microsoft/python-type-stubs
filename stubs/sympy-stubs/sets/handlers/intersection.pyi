from sympy.sets.fancysets import CartesianComplexRegion, ComplexRegion, ImageSet, Integers, Naturals, PolarComplexRegion, Range, Rationals, Reals
from sympy.sets.sets import Complement, EmptySet, FiniteSet, Intersection, Interval, ProductSet, Set, Union, UniversalSet
from sympy.sets.conditionset import ConditionSet

intersection_sets = ...
@intersection_sets.register(ConditionSet, ConditionSet)
def _(a, b) -> None:
    ...

@intersection_sets.register(ConditionSet, Set)
def _(a, b) -> Set | FiniteSet | Intersection | Union | Complement | ConditionSet:
    ...

@intersection_sets.register(Naturals, Integers)
def _(a, b):
    ...

@intersection_sets.register(Naturals, Naturals)
def _(a, b):
    ...

@intersection_sets.register(Interval, Naturals)
def _(a, b):
    ...

@intersection_sets.register(ComplexRegion, Set)
def _(self, other) -> FiniteSet | CartesianComplexRegion | PolarComplexRegion | ComplexRegion | Intersection | Union | Complement | None:
    ...

@intersection_sets.register(Integers, Reals)
def _(a, b):
    ...

@intersection_sets.register(Range, Interval)
def _(a, b) -> None:
    ...

@intersection_sets.register(Range, Naturals)
def _(a, b):
    ...

@intersection_sets.register(Range, Range)
def _(a, b) -> Range | None:
    ...

@intersection_sets.register(Range, Integers)
def _(a, b):
    ...

@intersection_sets.register(Range, Rationals)
def _(a, b):
    ...

@intersection_sets.register(ImageSet, Set)
def _(self, other):
    ...

@intersection_sets.register(ProductSet, ProductSet)
def _(a, b) -> FiniteSet | ProductSet:
    ...

@intersection_sets.register(Interval, Interval)
def _(a, b) -> FiniteSet | Interval | None:
    ...

@intersection_sets.register(EmptySet, Set)
def _(a, b):
    ...

@intersection_sets.register(UniversalSet, Set)
def _(a, b):
    ...

@intersection_sets.register(FiniteSet, FiniteSet)
def _(a, b) -> FiniteSet:
    ...

@intersection_sets.register(FiniteSet, Set)
def _(a, b) -> FiniteSet | None:
    ...

@intersection_sets.register(Set, Set)
def _(a, b) -> None:
    ...

@intersection_sets.register(Integers, Rationals)
def _(a, b):
    ...

@intersection_sets.register(Naturals, Rationals)
def _(a, b):
    ...

@intersection_sets.register(Rationals, Reals)
def _(a, b):
    ...

@intersection_sets.register(Integers, Interval)
def _(a, b) -> None:
    ...

@intersection_sets.register(Naturals, Interval)
def _(a, b) -> None:
    ...

