from typing import Any

from sympy.functions.elementary.piecewise import Piecewise
from sympy.utilities import public

z = ...
def roots_linear(f) -> list[Any]:
    ...

def roots_quadratic(f) -> list[Any]:
    ...

def roots_cubic(f, trig=...) -> list[Any]:
    ...

def roots_quartic(f) -> Any | list[Any] | list[Any | Piecewise]:
    ...

def roots_binomial(f) -> list[Any]:
    ...

def roots_cyclotomic(f, factor=...) -> list[Any]:
    ...

def roots_quintic(f) -> list[Any]:
    ...

def preprocess_roots(poly) -> tuple[Any, Any]:
    ...

@public
def roots(f, *gens, auto=..., cubics=..., trig=..., quartics=..., quintics=..., multiple=..., filter=..., predicate=..., strict=..., **flags):
    ...

def root_factors(f, *gens, filter=..., **args) -> list[Any]:
    ...

