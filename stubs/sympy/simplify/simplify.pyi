from typing import Any
from sympy.concrete.products import Product
from sympy.core.add import Add
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.function import UndefinedFunction
from sympy.core.mul import Mul
from sympy.core.power import Pow
from sympy.core.relational import Eq, Equality, Ne, Relational
from sympy.core.symbol import Dummy
from sympy.functions.elementary.complexes import Abs
from sympy.series.order import Order
def separatevars(expr, symbols=..., dict=..., force=...) -> dict[str, Any] | dict[Any, list[Any]] | Order | Abs | type[UndefinedFunction] | Any | None:
    ...

def posify(eq) -> tuple[Any, dict[Any, Any]] | tuple[Any, dict[Dummy, Any]]:
    ...

def hypersimp(f, k) -> None:
    ...

def hypersimilar(f, g, k):
    ...

def signsimp(expr, evaluate=...) -> Expr | Relational | Order | Eq | Ne | Add | tuple[Any, dict[Any, Any]]:
    ...

def simplify(expr, ratio=..., measure=..., rational=..., inverse=..., doit=..., **kwargs):
    ...

def sum_simplify(s, **kwargs) -> Order:
    ...

def sum_combine(s_t) -> Order:
    ...

def factor_sum(self, limits=..., radical=..., clear=..., fraction=..., sign=...) -> Basic | Any | Add | Order | Mul:
    ...

def sum_add(self, other, method=...) -> Basic | Any | Add | Order | Mul:
    ...

def product_simplify(s, **kwargs) -> Order:
    ...

def product_mul(self, other, method=...) -> Equality | Relational | Ne | Product | Order:
    ...

def logcombine(expr, force=...):
    ...

def inversecombine(expr):
    ...

def kroneckersimp(expr) -> None:
    ...

def besselsimp(expr):
    ...

def nthroot(expr, n, max_len=..., prec=...) -> Mul | Pow | Order | Add | None:
    ...

def nsimplify(expr, constants=..., tolerance=..., full=..., rational=..., rational_conversion=...):
    ...

def clear_coefficients(expr, rhs=...) -> tuple[Any, Any] | tuple[Any | Expr | Relational | Order | Eq | Ne | Add | tuple[Any, dict[Any, Any]], Any]:
    ...

def nc_simplify(expr, deep=...):
    ...

def dotprodsimp(expr, withsimp=...) -> tuple[Any | Basic, bool] | Any | Basic:
    ...

bottom_up = ...
walk = ...
