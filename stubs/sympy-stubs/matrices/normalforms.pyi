from typing import Any

from sympy.matrices.dense import MutableDenseMatrix

def smith_normal_form(m, domain=...) -> MutableDenseMatrix:
    ...

def invariant_factors(m, domain=...) -> tuple[Any, ...]:
    ...

def hermite_normal_form(A, *, D=..., check_rank=...) -> MutableDenseMatrix:
    ...

