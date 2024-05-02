from sympy.core import Basic, Expr
from sympy.core.numbers import Infinity, Integer, NegativeInfinity, Zero
from sympy.sets.fancysets import ImageSet
from sympy.sets.sets import FiniteSet, Interval, Set, Union

_set_pow = ...
@_set_pow.register(Basic, Basic)
def _(x, y) -> None:
    ...

@_set_pow.register(Set, Set)
def _(x, y) -> FiniteSet | ImageSet:
    ...

@_set_pow.register(Expr, Expr)
def _(x, y):
    ...

@_set_pow.register(Interval, Zero)
def _(x, z) -> FiniteSet:
    ...

@_set_pow.register(Interval, Integer)
def _(x, exponent) -> FiniteSet | Interval | Union | None:
    ...

@_set_pow.register(Interval, Infinity)
def _(b, e) -> FiniteSet | Interval:
    ...

@_set_pow.register(Interval, NegativeInfinity)
def _(b, e):
    ...

