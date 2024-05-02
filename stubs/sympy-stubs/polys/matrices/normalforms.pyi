from typing import Any

from sympy.polys.matrices.domainmatrix import DomainMatrix
from sympy.polys.matrices.domainscalar import DomainScalar

def smith_normal_form(m) -> DomainMatrix:
    ...

def add_columns(m, i, j, a, b, c, d) -> None:
    ...

def invariant_factors(m) -> tuple[()] | tuple[Any, ...]:
    ...

def hermite_normal_form(A, *, D=..., check_rank=...) -> DomainMatrix | DomainScalar:
    ...

