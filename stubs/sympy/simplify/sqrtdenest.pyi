from typing import Literal
from sympy.core.add import Add
from sympy.core.mul import Mul
from sympy.core.power import Pow
from sympy.series.order import Order
def is_sqrt(expr) -> bool:
    ...

def sqrt_depth(p) -> Literal[1, 0]:
    ...

def is_algebraic(p) -> bool:
    ...

def sqrtdenest(expr, max_iter=...) -> Mul | Pow | Order | Add | None:
    ...

class SqrtdenestStopIteration(StopIteration):
    ...


def sqrt_biquadratic_denest(expr, a, b, r, d2) -> None:
    ...

