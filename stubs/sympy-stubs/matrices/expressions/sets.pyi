from typing import Self

from sympy.core.basic import Basic
from sympy.sets.sets import Set

class MatrixSet(Set):
    is_empty = ...
    def __new__(cls, n, m, set) -> Self:
        ...
    
    @property
    def shape(self) -> tuple[Basic, ...]:
        ...
    
    @property
    def set(self) -> Basic:
        ...
    


