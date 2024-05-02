from typing import Any, Literal, Self
from sympy.core import Expr
from sympy.core.numbers import Integer
from sympy.series.order import Order
from sympy.utilities import public

__all__ = ['CRootOf']
class _pure_key_dict:
    def __init__(self) -> None:
        ...
    
    def __getitem__(self, k):
        ...
    
    def __setitem__(self, k, v) -> None:
        ...
    
    def __contains__(self, k) -> bool:
        ...
    


_reals_cache = ...
_complexes_cache = ...
@public
def rootof(f, x, index=..., radicals=..., expand=...) -> Any:
    ...

@public
class RootOf(Expr):
    __slots__ = ...
    def __new__(cls, f, x, index=..., radicals=..., expand=...) -> Any:
        ...
    


@public
class ComplexRootOf(RootOf):
    __slots__ = ...
    is_complex = ...
    is_number = ...
    is_finite = ...
    def __new__(cls, f, x, index=..., radicals=..., expand=...) -> Any:
        ...
    
    @property
    def expr(self):
        ...
    
    @property
    def args(self) -> tuple[Any, Any | Integer]:
        ...
    
    @property
    def free_symbols(self) -> set[Any]:
        ...
    
    @classmethod
    def real_roots(cls, poly, radicals=...) -> list[Any]:
        ...
    
    @classmethod
    def all_roots(cls, poly, radicals=...) -> list[Any]:
        ...
    
    @classmethod
    def clear_cache(cls) -> None:
        ...
    
    def eval_approx(self, n, return_mpmath=...):
        ...
    
    def eval_rational(self, dx=..., dy=..., n=...):
        ...
    


CRootOf = ...
@public
class RootSum(Expr):
    __slots__ = ...
    def __new__(cls, expr, func=..., x=..., auto=..., quadratic=...):
        ...
    
    @classmethod
    def new(cls, poly, func, auto=...) -> Self | Any:
        ...
    
    @property
    def expr(self):
        ...
    
    @property
    def args(self) -> tuple[Any, Any, Any]:
        ...
    
    @property
    def free_symbols(self):
        ...
    
    @property
    def is_commutative(self) -> Literal[True]:
        ...
    
    def doit(self, **hints) -> Self | Order:
        ...
    


