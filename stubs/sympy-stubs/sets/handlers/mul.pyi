from typing import Any
from sympy.core import Basic, Expr
from sympy.sets.fancysets import ImageSet
from sympy.sets.sets import FiniteSet, Interval, Set, Union

_set_mul = ...
_set_div = ...
@_set_mul.register(Basic, Basic)
def _(x, y) -> None:
    ...

@_set_mul.register(Set, Set)
def _(x, y) -> None:
    ...

@_set_mul.register(Expr, Expr)
def _(x, y):
    ...

@_set_mul.register(Interval, Interval)
def _(x, y) -> FiniteSet | Interval:
    ...

@_set_div.register(Basic, Basic)
def _(x, y) -> None:
    ...

@_set_div.register(Expr, Expr)
def _(x, y):
    ...

@_set_div.register(Set, Set)
def _(x, y) -> None:
    ...

@_set_div.register(Interval, Interval)
def _(x, y) -> FiniteSet | Interval | Any | ImageSet | Union:
    ...

