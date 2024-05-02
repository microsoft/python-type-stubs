from typing import Any
from sympy.matrices.dense import MutableDenseMatrix
from sympy.polys.matrices.domainmatrix import DomainMatrix

class PolyNonlinearError(Exception):
    ...


class RawMatrix(MutableDenseMatrix):
    _sympify = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    


def eqs_to_matrix(eqs_coeffs, eqs_rhs, gens, domain) -> DomainMatrix:
    ...

def sympy_eqs_to_ring(eqs, symbols) -> tuple[Any, Any]:
    ...

def solve_lin_sys(eqs, ring, _raw=...) -> dict[Any, Any] | None:
    ...

