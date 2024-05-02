from typing import Any

from sympy.polys.polyutils import IntegerPowerable
from sympy.utilities.decorator import public

class PrimeIdeal(IntegerPowerable):
    def __init__(self, ZK, p, alpha, f, e=...) -> None:
        ...
    
    def __str__(self) -> str:
        ...
    
    @property
    def is_inert(self):
        ...
    
    def repr(self, field_gen=..., just_gens=...) -> str:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def as_submodule(self):
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __add__(self, other):
        ...
    
    __radd__ = ...
    def __mul__(self, other):
        ...
    
    __rmul__ = ...
    def test_factor(self):
        ...
    
    def valuation(self, I) -> Any:
        ...
    
    def reduce_element(self, elt):
        ...
    
    def reduce_ANP(self, a):
        ...
    
    def reduce_alg_num(self, a):
        ...
    


@public
def prime_valuation(I, P) -> int:
    ...

@public
def prime_decomp(p, T=..., ZK=..., dK=..., radical=...) -> list[PrimeIdeal] | list[Any]:
    ...

