from typing import Any, Literal, Self
from sympy import ImmutableDenseNDimArray
from sympy.core import Basic
from sympy.matrices import Matrix

class ArrayComprehension(Basic):
    def __new__(cls, function, *symbols, **assumptions) -> Self:
        ...
    
    @property
    def function(self) -> Basic:
        ...
    
    @property
    def limits(self):
        ...
    
    @property
    def free_symbols(self) -> set[Basic] | set[Basic | Any]:
        ...
    
    @property
    def variables(self) -> list[Any]:
        ...
    
    @property
    def bound_symbols(self) -> list[Any]:
        ...
    
    @property
    def shape(self):
        ...
    
    @property
    def is_shape_numeric(self) -> bool:
        ...
    
    def rank(self):
        ...
    
    def __len__(self):
        ...
    
    def doit(self, **hints) -> Self | ImmutableDenseNDimArray:
        ...
    
    def tolist(self) -> list[Any]:
        ...
    
    def tomatrix(self) -> Matrix:
        ...
    


def isLambda(v) -> Literal[False]:
    ...

class ArrayComprehensionMap(ArrayComprehension):
    def __new__(cls, function, *symbols, **assumptions) -> Self:
        ...
    
    @property
    def func(self) -> type[Any]:
        class _(ArrayComprehensionMap):
            ...
        
        
    


