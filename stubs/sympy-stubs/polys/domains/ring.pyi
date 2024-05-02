from typing import Self

from sympy.polys.agca.ideals import ModuleImplementedIdeal
from sympy.polys.domains.domain import Domain
from sympy.polys.domains.quotientring import QuotientRing
from sympy.utilities import public

class Ring(Domain):
    is_Ring = ...
    def get_ring(self) -> Self:
        ...
    
    def exquo(self, a, b):
        ...
    
    def quo(self, a, b):
        ...
    
    def rem(self, a, b):
        ...
    
    def div(self, a, b):
        ...
    
    def invert(self, a, b):
        ...
    
    def revert(self, a):
        ...
    
    def is_unit(self, a) -> bool:
        ...
    
    def numer(self, a):
        ...
    
    def denom(self, a):
        ...
    
    def free_module(self, rank):
        ...
    
    def ideal(self, *gens) -> ModuleImplementedIdeal:
        ...
    
    def quotient_ring(self, e) -> QuotientRing:
        ...
    
    def __truediv__(self, e) -> QuotientRing:
        ...
    


