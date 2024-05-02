from types import NotImplementedType
from typing import Any, Self

from sympy.core.sympify import CantSympify
from sympy.polys.domains.domainelement import DomainElement
from sympy.polys.rings import PolyElement, PolyRing
from sympy.printing.defaults import DefaultPrinting
from sympy.utilities import public

@public
def field(symbols, domain, order=...) -> Any:
    ...

@public
def xfield(symbols, domain, order=...) -> tuple[FracField | Any, Any]:
    ...

@public
def vfield(symbols, domain, order=...) -> FracField | Any:
    ...

@public
def sfield(exprs, *symbols, **options) -> tuple[FracField | Any, Any] | tuple[FracField | Any, list[Any]]:
    ...

_field_cache: dict[Any, Any] = ...
class FracField(DefaultPrinting):
    def __new__(cls, symbols, domain, order=...) -> Self | Any:
        ...
    
    def __getnewargs__(self) -> tuple[Any, Any, Any]:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def index(self, gen):
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def raw_new(self, numer, denom=...):
        ...
    
    def new(self, numer, denom=...):
        ...
    
    def domain_new(self, element):
        ...
    
    def ground_new(self, element):
        ...
    
    def field_new(self, element) -> FracElement:
        ...
    
    __call__ = ...
    def from_expr(self, expr):
        ...
    
    def to_domain(self) -> Any:
        ...
    
    def to_ring(self) -> PolyRing | Any:
        ...
    


class FracElement(DomainElement, DefaultPrinting, CantSympify): # type: ignore
    def __init__(self, numer, denom=...) -> None:
        ...
    
    def raw_new(f, numer, denom) -> Self:
        ...
    
    def new(f, numer, denom) -> Self:
        ...
    
    def to_poly(f) -> Any:
        ...
    
    def parent(self):
        ...
    
    def __getnewargs__(self) -> tuple[Any, Any, Any]:
        ...
    
    _hash = ...
    def __hash__(self) -> int:
        ...
    
    def copy(self) -> Self:
        ...
    
    def set_field(self, new_field) -> Self:
        ...
    
    def as_expr(self, *symbols):
        ...
    
    def __eq__(f, g) -> bool:
        ...
    
    def __ne__(f, g) -> bool:
        ...
    
    def __bool__(f) -> bool:
        ...
    
    def sort_key(self) -> tuple[Any, Any]:
        ...
    
    def __lt__(f1, f2) -> bool:
        ...
    
    def __le__(f1, f2) -> bool:
        ...
    
    def __gt__(f1, f2) -> bool:
        ...
    
    def __ge__(f1, f2) -> bool:
        ...
    
    def __pos__(f) -> Self:
        ...
    
    def __neg__(f) -> Self:
        ...
    
    def __add__(f, g) -> Self | FracElement | NotImplementedType | PolyElement:
        ...
    
    def __radd__(f, c) -> Self | NotImplementedType:
        ...
    
    def __sub__(f, g) -> Self | FracElement | NotImplementedType:
        ...
    
    def __rsub__(f, c) -> Self | NotImplementedType:
        ...
    
    def __mul__(f, g) -> Self | FracElement | NotImplementedType:
        ...
    
    def __rmul__(f, c) -> Self | NotImplementedType:
        ...
    
    def __truediv__(f, g) -> Self | FracElement | NotImplementedType:
        ...
    
    def __rtruediv__(f, c) -> Self | NotImplementedType:
        ...
    
    def __pow__(f, n) -> Self:
        ...
    
    def diff(f, x) -> Self:
        ...
    
    def __call__(f, *values):
        ...
    
    def evaluate(f, x, a=...):
        ...
    
    def subs(f, x, a=...) -> Self:
        ...
    
    def compose(f, x, a=...):
        ...
    


