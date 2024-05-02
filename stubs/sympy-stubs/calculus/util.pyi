from typing import Any
from sympy import Union
from sympy.sets.sets import FiniteSet, Set


def continuous_domain(f, symbol, domain):
    ...

def function_range(f, symbol, domain) -> FiniteSet:
    ...

def not_empty_in(finset_intersection, *syms) -> FiniteSet | Union | None:
    ...

def periodicity(f, symbol, check=...):
    ...

def lcim(numbers) -> Any | None:
    ...

def is_convex(f, *syms, domain=...) -> bool:
    ...

def stationary_points(f, symbol, domain=...) -> Set:
    ...

def maximum(f, symbol, domain=...):
    ...

def minimum(f, symbol, domain=...):
    ...

