from typing import Any
from sympy.utilities import public, xthreaded

@xthreaded
@public
def apart(f, x=..., full=..., **options) -> Any:
    ...

def apart_undetermined_coeffs(P, Q):
    ...

def apart_full_decomposition(P, Q) -> Any:
    ...

@public
def apart_list(f, x=..., dummies=..., **options) -> tuple[Any, Any, list[Any]]:
    ...

def apart_list_full_decomposition(P, Q, dummygen) -> list[Any]:
    ...

@public
def assemble_partfrac_list(partial_list):
    ...

