from typing import Any
from sympy.core.logic import And
from sympy.sets.sets import FiniteSet, Union

def solve_poly_inequality(poly, rel) -> list[Any]:
    ...

def solve_poly_inequalities(polys) -> FiniteSet | Union:
    ...

def solve_rational_inequalities(eqs):
    ...

def reduce_rational_inequalities(exprs, gen, relational=...):
    ...

def reduce_abs_inequality(expr, rel, gen):
    ...

def reduce_abs_inequalities(exprs, gen) -> And:
    ...

def solve_univariate_inequality(expr, gen, relational=..., domain=..., continuous=...):
    ...

def reduce_inequalities(inequalities, symbols=...) -> And:
    ...

