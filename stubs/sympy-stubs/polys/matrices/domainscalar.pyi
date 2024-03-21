from types import NotImplementedType
from typing import Any, Self

class DomainScalar:
    def __new__(cls, element, domain) -> Self:
        ...
    
    @classmethod
    def new(cls, element, domain) -> Self:
        ...
    
    def __repr__(self) -> str:
        ...
    
    @classmethod
    def from_sympy(cls, expr) -> Self:
        ...
    
    def to_sympy(self):
        ...
    
    def to_domain(self, domain) -> Self:
        ...
    
    def convert_to(self, domain) -> Self:
        ...
    
    def unify(self, other) -> tuple[Self, Any]:
        ...
    
    def __add__(self, other) -> NotImplementedType | Self:
        ...
    
    def __sub__(self, other) -> NotImplementedType | Self:
        ...
    
    def __mul__(self, other) -> NotImplementedType | Self:
        ...
    
    def __floordiv__(self, other) -> NotImplementedType | Self:
        ...
    
    def __mod__(self, other) -> NotImplementedType | Self:
        ...
    
    def __divmod__(self, other) -> NotImplementedType | tuple[Self, Self]:
        ...
    
    def __pow__(self, n) -> NotImplementedType | Self:
        ...
    
    def __pos__(self) -> Self:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def is_zero(self):
        ...
    
    def is_one(self):
        ...
    


