from typing import Callable

from sympy.core import Expr
from sympy.core.basic import Basic
from sympy.core.function import UndefinedFunction
from sympy.logic.boolalg import Boolean
from sympy.matrices.expressions.matexpr import MatrixElement

def refine(expr, assumptions=...) -> Basic:
    ...

def refine_abs(expr, assumptions) -> None:
    ...

def refine_Pow(expr, assumptions):
    ...

def refine_atan2(expr, assumptions) -> type[UndefinedFunction]:
    ...

def refine_re(expr, assumptions) -> Basic | None:
    ...

def refine_im(expr, assumptions) -> Basic | None:
    ...

def refine_arg(expr, assumptions) -> None:
    ...

def refine_sign(expr, assumptions):
    ...

def refine_matrixelement(expr, assumptions) -> MatrixElement | None:
    ...

handlers_dict: dict[str, Callable[[Expr, Boolean], Expr]] = ...
