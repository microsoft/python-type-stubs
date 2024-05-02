from typing import Any, Literal

from sympy.polys.polymatrix import PolyMatrix

def order_at(a, p, t) -> Literal[0]:
    ...

def order_at_oo(a, d, t):
    ...

def weak_normalizer(a, d, DE, z=...) -> tuple[Any, tuple[Any, Any]]:
    ...

def normal_denom(fa, fd, ga, gd, DE) -> tuple[Any, tuple[Any, Any], tuple[Any, Any], Any]:
    ...

def special_denom(a, ba, bd, ca, cd, DE, case=...) -> tuple[Any, Any, Any, Any]:
    ...

def bound_degree(a, b, cQ, DE, case=..., parametric=...):
    ...

def spde(a, b, c, n, DE) -> tuple[Any, Any, Literal[0], Any, Any] | tuple[Any, Any, Any, Any, Any]:
    ...

def no_cancel_b_large(b, c, n, DE) -> Any:
    ...

def no_cancel_b_small(b, c, n, DE) -> tuple[Any, Any, Any] | Any:
    ...

def no_cancel_equal(b, c, n, DE) -> tuple[Any, Any | int, Any] | Any:
    ...

def cancel_primitive(b, c, n, DE) -> Any:
    ...

def cancel_exp(b, c, n, DE) -> Any:
    ...

def solve_poly_rde(b, cQ, n, DE, parametric=...) -> tuple[list[Any], Any] | Any | tuple[list[Any], PolyMatrix | Any] | tuple[Any, Any, Any] | tuple[Any, Any | int, Any]:
    ...

def rischDE(fa, fd, ga, gd, DE) -> tuple[Any, Any]:
    ...

