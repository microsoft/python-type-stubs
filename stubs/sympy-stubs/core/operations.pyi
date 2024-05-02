from typing import Any, LiteralString, Self
from sympy.core.basic import Basic
from sympy.core.cache import cacheit
from sympy.series.order import Order

class AssocOp(Basic):
    __slots__: tuple[str, ...] = ...
    _args_type: type[Basic] | None = ...
    @cacheit
    def __new__(cls, *args, evaluate=..., _sympify=...) -> Order:
        ...
    
    @classmethod
    def flatten(cls, seq) -> tuple[list[Any], list[Any], None]:
        ...
    
    @classmethod
    def make_args(cls, expr) -> tuple[Basic, ...] | tuple[Any]:
        ...
    
    def doit(self, **hints) -> Self:
        ...
    


class ShortCircuit(Exception):
    ...


class LatticeOp(AssocOp):
    is_commutative = ...
    def __new__(cls, *args, **options) -> Self:
        ...
    
    @classmethod
    def make_args(cls, expr) -> frozenset[Any]:
        ...
    


class AssocOpDispatcher:
    def __init__(self, name, doc=...) -> None:
        ...
    
    def __repr__(self) -> LiteralString:
        ...
    
    def register_handlerclass(self, classes, typ, on_ambiguity=...) -> None:
        ...
    
    @cacheit
    def __call__(self, *args, _sympify=..., **kwargs) -> Any:
        ...
    
    @cacheit
    def dispatch(self, handlers) -> type:
        ...
    
    @property
    def __doc__(self) -> str:
        ...
    


