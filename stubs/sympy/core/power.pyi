from typing import Any, Literal, Self
from sympy.core.basic import Basic
from sympy.core.cache import cacheit
from sympy.core.expr import Expr
from sympy.core.function import UndefinedFunction
from sympy.core.kind import _UndefinedKind, Kind
from sympy.core.mul import Mul
from sympy.core.numbers import Number
from sympy.functions.elementary.exponential import log
from sympy.series.order import Order

def isqrt(n) -> int:
    ...

def integer_nthroot(y, n) -> tuple[int, bool] | tuple[Any, Literal[True]] | tuple[Literal[1], Literal[False]] | tuple[int, Any]:
    ...

def integer_log(y, x) -> tuple[int, Any] | tuple[Any, Any | bool] | tuple[int, bool]:
    ...

class Pow(Expr):
    is_Pow = ...
    __slots__ = ...
    args: tuple[Expr, Expr]
    _args: tuple[Expr, Expr]
    @cacheit
    def __new__(cls, b, e, evaluate=...):
        ...
    
    def inverse(self, argindex=...) -> type[log] | None:
        ...
    
    @property
    def base(self) -> Expr:
        ...
    
    @property
    def exp(self) -> Expr:
        ...
    
    @property
    def kind(self) -> Kind | _UndefinedKind:
        ...
    
    @classmethod
    def class_key(cls) -> tuple[Literal[3], Literal[2], str]:
        ...
    
    def as_base_exp(self) -> tuple[Any, Any | Mul] | tuple[Expr, Expr]:
        ...
    
    def as_real_imag(self, deep=..., **hints) -> tuple[Self, Any] | tuple[Any | Order | Basic, Any] | tuple[Any, Any | Expr] | tuple[Any, Any] | tuple[type[UndefinedFunction] | Any, type[UndefinedFunction] | Any] | None:
        ...
    
    def as_numer_denom(self) -> tuple[Self, Any] | tuple[Any | Mul | Expr, Self] | tuple[Self, Any | Mul | Expr] | tuple[Self, Self]:
        ...
    
    def matches(self, expr, repl_dict=..., old=...) -> dict[Any, Any] | None:
        ...
    
    def taylor_term(self, n, x, *previous_terms):
        ...
    
    def as_content_primitive(self, radical=..., clear=...) -> tuple[Self, Self] | tuple[Number, Self] | tuple[Any, Self]:
        ...
    
    def is_constant(self, *wrt, **flags) -> bool | None:
        ...
    


power = ...
