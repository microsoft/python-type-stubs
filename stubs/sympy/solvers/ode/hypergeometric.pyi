from typing import Any, Literal
from sympy.core.relational import Eq, Ne, Relational
def match_2nd_hypergeometric(eq, func) -> list[Any]:
    ...

def equivalence_hypergeometric(A, B, func) -> dict[str, Any] | None:
    ...

def match_2nd_2F1_hypergeometric(I, k, sing_point, func) -> dict[str, Any]:
    ...

def equivalence(max_num_pow, dem_pow) -> Literal['2F1'] | None:
    ...

def get_sol_2F1_hypergeometric(eq, func, match_object) -> Eq | Relational | Ne | None:
    ...

