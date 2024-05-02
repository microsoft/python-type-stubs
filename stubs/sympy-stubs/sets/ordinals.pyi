from types import NotImplementedType
from typing import Literal, Self
from sympy.core import Basic

class OmegaPower(Basic):
    def __new__(cls, a, b) -> Self:
        ...
    
    @property
    def exp(self) -> Basic:
        ...
    
    @property
    def mult(self) -> Basic:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    


class Ordinal(Basic):
    def __new__(cls, *terms) -> Self:
        ...
    
    @property
    def terms(self) -> tuple[Basic, ...]:
        ...
    
    @property
    def leading_term(self) -> Basic:
        ...
    
    @property
    def trailing_term(self) -> Basic:
        ...
    
    @property
    def is_successor_ordinal(self) -> Literal[False]:
        ...
    
    @property
    def is_limit_ordinal(self) -> bool:
        ...
    
    @property
    def degree(self):
        ...
    
    @classmethod
    def convert(cls, integer_value) -> OrdinalZero | Ordinal:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __gt__(self, other) -> bool:
        ...
    
    def __ge__(self, other) -> bool:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    def __add__(self, other) -> NotImplementedType | Self | Ordinal:
        ...
    
    def __radd__(self, other) -> NotImplementedType | OrdinalZero | Ordinal:
        ...
    
    def __mul__(self, other) -> NotImplementedType | OrdinalZero | Ordinal:
        ...
    
    def __rmul__(self, other) -> NotImplementedType | OrdinalZero | Ordinal:
        ...
    
    def __pow__(self, other) -> NotImplementedType | Ordinal:
        ...
    


class OrdinalZero(Ordinal):
    ...


class OrdinalOmega(Ordinal):
    def __new__(cls) -> Self:
        ...
    
    @property
    def terms(self) -> tuple[OmegaPower]:
        ...
    


ord0 = ...
omega = ...
