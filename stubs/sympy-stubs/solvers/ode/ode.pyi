from collections.abc import Generator
from typing import Any, Literal, NoReturn

from sympy.core.add import Add
from sympy.core.basic import Basic
from sympy.core.multidimensional import vectorize
from sympy.core.relational import Eq, Equality, Ne, Relational
from sympy.core.symbol import Symbol

allhints = ...

def get_numbered_constants(eq, num=..., start=..., prefix=...) -> Symbol | tuple[Symbol | Any, ...]: ...
def iter_numbered_constants(eq, start=..., prefix=...) -> Generator[Symbol | Any, Any, NoReturn]: ...
def dsolve(
    eq, func=..., hint=..., simplify=..., ics=..., xi=..., eta=..., x0=..., n=..., **kwargs
) -> (
    list[Any]
    | Any
    | dict[Any, Any]
    | Equality
    | Basic
    | list[list[Any] | Any]
    | list[list[list[Any] | Any] | Any]
    | list[Equality]
): ...
def solve_ics(sols, funcs, constants, ics): ...
def classify_ode(eq, func=..., dict=..., ics=..., *, prep=..., xi=..., eta=..., n=..., **kwargs): ...
def classify_sysode(eq, funcs=..., **kwargs) -> dict[str, int]: ...
def check_linear_2eq_order1(eq, func, func_coef) -> Literal["type6", "type7"] | None: ...
def check_nonlinear_2eq_order1(eq, func, func_coef) -> Literal["type5", "type1", "type2", "type3", "type4"] | None: ...
def check_nonlinear_2eq_order2(eq, func, func_coef) -> None: ...
def check_nonlinear_3eq_order1(eq, func, func_coef): ...
def check_nonlinear_3eq_order2(eq, func, func_coef) -> None: ...
@vectorize(0)
def odesimp(
    ode, eq, func, hint
) -> (
    list[Eq | Any | Relational | Ne]
    | list[list[Any] | Any]
    | Eq
    | Relational
    | Ne
    | list[list[Eq | Any | Relational | Ne] | list[list[Any] | Any] | Any]
): ...
def ode_sol_simplicity(sol, func, trysolving=...) -> int: ...
@vectorize(0)
def constantsimp(expr, constants) -> list[list[Any] | Any] | Eq | Relational | Ne | Add | Basic | Any: ...
def constant_renumber(
    expr, variables=..., newconstants=...
) -> list[Any] | set[Any] | tuple[Any, ...] | tuple | Basic | Eq | Relational | Ne: ...
def homogeneous_order(eq, *symbols) -> Any | None: ...
def ode_2nd_power_series_ordinary(eq, func, order, match) -> Eq | Relational | Ne: ...
def ode_2nd_power_series_regular(eq, func, order, match) -> Eq | Relational | Ne | None: ...
def ode_1st_power_series(eq, func, order, match) -> Eq | Relational | Ne: ...
def checkinfsol(eq, infinitesimals, func=..., order=...) -> list[Any]: ...
def sysode_linear_2eq_order1(match_) -> list[Eq | Any | Relational | Ne]: ...
def sysode_nonlinear_2eq_order1(match_) -> set[Eq] | list[Any] | set[Any]: ...
def sysode_nonlinear_3eq_order1(
    match_,
) -> (
    list[Any | Basic]
    | list[
        Any
        | list[Any]
        | dict[Any, Any]
        | Equality
        | Basic
        | list[list[Any] | Any]
        | list[list[list[Any] | Any] | Any]
        | list[Equality]
    ]
): ...
