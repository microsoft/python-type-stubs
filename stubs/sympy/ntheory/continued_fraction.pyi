from typing import Any, Generator
from sympy.core.add import Add
from sympy.core.basic import Basic
from sympy.core.function import UndefinedFunction
from sympy.core.mul import Mul
from sympy.series.order import Order
def continued_fraction(a) -> list:
    ...

def continued_fraction_periodic(p, q, d=..., s=...) -> list:
    ...

def continued_fraction_reduce(cf) -> Order | Basic | Any | Add | Mul:
    ...

def continued_fraction_iterator(x) -> Generator[type[UndefinedFunction] | Any, Any, None]:
    ...

def continued_fraction_convergents(cf) -> Generator[Any, Any, None]:
    ...

