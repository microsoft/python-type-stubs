from types import NotImplementedType
from typing import Self

class ModuleHomomorphism:
    def __init__(self, domain, codomain) -> None:
        ...
    
    def kernel(self):
        ...
    
    def image(self):
        ...
    
    def restrict_domain(self, sm) -> Self:
        ...
    
    def restrict_codomain(self, sm) -> Self:
        ...
    
    def quotient_domain(self, sm) -> Self:
        ...
    
    def quotient_codomain(self, sm) -> Self:
        ...
    
    def __call__(self, elem):
        ...
    
    def __mul__(self, oth) -> NotImplementedType:
        ...
    
    __rmul__ = ...
    def __truediv__(self, oth) -> NotImplementedType:
        ...
    
    def __add__(self, oth) -> NotImplementedType:
        ...
    
    def __sub__(self, oth) -> NotImplementedType:
        ...
    
    def is_injective(self):
        ...
    
    def is_surjective(self):
        ...
    
    def is_isomorphism(self):
        ...
    
    def is_zero(self):
        ...
    
    def __eq__(self, oth) -> bool:
        ...
    
    def __ne__(self, oth) -> bool:
        ...
    


class MatrixHomomorphism(ModuleHomomorphism):
    def __init__(self, domain, codomain, matrix) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    


class FreeModuleHomomorphism(MatrixHomomorphism):
    ...


class SubModuleHomomorphism(MatrixHomomorphism):
    ...


def homomorphism(domain, codomain, matrix) -> FreeModuleHomomorphism:
    ...

