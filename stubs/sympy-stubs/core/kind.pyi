from typing import Callable, Literal, LiteralString, Self

from sympy.core.cache import cacheit

class KindMeta(type):
    def __new__(cls, clsname, bases, dct) -> Self: # type: ignore
        ...
    


class Kind(metaclass=KindMeta):
    def __new__(cls, *args) -> Self:
        ...
    


class _UndefinedKind(Kind):
    def __new__(cls) -> Self:
        ...
    
    def __repr__(self) -> Literal['UndefinedKind']:
        ...
    


UndefinedKind = ...
class _NumberKind(Kind):
    def __new__(cls) -> Self:
        ...
    
    def __repr__(self) -> Literal['NumberKind']:
        ...
    


NumberKind = ...
class _BooleanKind(Kind):
    def __new__(cls) -> Self:
        ...
    
    def __repr__(self) -> Literal['BooleanKind']:
        ...
    


BooleanKind = ...
class KindDispatcher:
    def __init__(self, name, commutative=..., doc=...) -> None:
        ...
    
    def __repr__(self) -> LiteralString:
        ...
    
    def register(self, *types, **kwargs) -> Callable[..., None]:
        ...
    
    def __call__(self, *args, **kwargs) -> Kind | _UndefinedKind:
        ...
    
    @cacheit
    def dispatch_kinds(self, kinds, **kwargs) -> Kind | _UndefinedKind:
        ...
    
    @property
    def __doc__(self) -> str:
        ...
    


