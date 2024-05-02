from typing import Any, Sequence, TypeVar
from sympy.polys.matrices._typing import RingElement

T = TypeVar('T')
R = TypeVar('R', bound=RingElement)
def ddm_transpose(matrix: Sequence[Sequence[T]]) -> list[list[T]]:
    ...

def ddm_iadd(a: list[list[R]], b: Sequence[Sequence[R]]) -> None:
    ...

def ddm_isub(a: list[list[R]], b: Sequence[Sequence[R]]) -> None:
    ...

def ddm_ineg(a: list[list[R]]) -> None:
    ...

def ddm_imul(a: list[list[R]], b: R) -> None:
    ...

def ddm_irmul(a: list[list[R]], b: R) -> None:
    ...

def ddm_imatmul(a: list[list[R]], b: Sequence[Sequence[R]], c: Sequence[Sequence[R]]) -> None:
    ...

def ddm_irref(a, _partial_pivot=...) -> list[Any]:
    ...

def ddm_idet(a, K):
    ...

def ddm_iinv(ainv, a, K) -> None:
    ...

def ddm_ilu_split(L, U, K) -> list[Any]:
    ...

def ddm_ilu(a) -> list[Any]:
    ...

def ddm_ilu_solve(x, L, U, swaps, b) -> None:
    ...

def ddm_berk(M, K) -> list[list[Any]]:
    ...

