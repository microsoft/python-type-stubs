from typing import Any, Optional, Self

FuzzyBool = Optional[bool]
def fuzzy_bool(x) -> bool | None:
    ...

def fuzzy_and(args) -> bool | None:
    ...

def fuzzy_not(v) -> bool:
    ...

def fuzzy_or(args) -> bool | None:
    ...

def fuzzy_xor(args) -> bool | None:
    ...

def fuzzy_nand(args) -> bool | None:
    ...

class Logic:
    op_2class: dict[str, type[Logic]] = ...
    def __new__(cls, *args) -> Self:
        ...
    
    def __getnewargs__(self):
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, b) -> bool:
        ...
    
    def __ne__(self, b) -> bool:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __cmp__(self, other) -> int:
        ...
    
    def __str__(self) -> str:
        ...
    
    __repr__ = ...
    @staticmethod
    def fromstring(text) -> Not | bool | Logic:
        ...
    


class AndOr_Base(Logic):
    def __new__(cls, *args) -> bool | Self:
        ...
    
    @classmethod
    def flatten(cls, args) -> tuple[Any, ...]:
        ...
    


class And(AndOr_Base):
    op_x_notx = ...
    def expand(self) -> bool | Or | Self:
        ...
    


class Or(AndOr_Base):
    op_x_notx = ...


class Not(Logic):
    def __new__(cls, arg) -> Self | bool:
        ...
    
    @property
    def arg(self):
        ...
    


