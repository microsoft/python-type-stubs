from typing import Any, Generator, Self
from sympy.core.basic import Basic
from sympy.sets.sets import Set, SetKind

class PowerSet(Set):
    def __new__(cls, arg, evaluate=...) -> Self:
        ...
    
    @property
    def arg(self) -> Basic:
        ...
    
    def __len__(self) -> Any:
        ...
    
    def __iter__(self) -> Generator[Any, Any, None]:
        ...
    
    @property
    def kind(self) -> SetKind:
        ...
    


