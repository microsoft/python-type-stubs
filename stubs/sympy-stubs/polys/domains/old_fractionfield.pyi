from typing import Any, Self

from sympy.polys.domains.characteristiczero import CharacteristicZero
from sympy.polys.domains.compositedomain import CompositeDomain
from sympy.polys.domains.field import Field
from sympy.polys.polyclasses import DMF
from sympy.utilities import public

class FractionField(Field, CharacteristicZero, CompositeDomain):
    dtype = DMF
    is_Frac = ...
    has_assoc_Ring = ...
    has_assoc_Field = ...
    def __init__(self, dom, *gens) -> None: ...
    def new(self, element) -> dtype: ...
    def __str__(self) -> str: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    def to_sympy(self, a): ...
    def from_sympy(self, a): ...
    def from_ZZ(K1, a, K0): ...
    def from_ZZ_python(K1, a, K0): ...
    def from_QQ_python(K1, a, K0): ...
    def from_ZZ_gmpy(K1, a, K0): ...
    def from_QQ_gmpy(K1, a, K0): ...
    def from_RealField(K1, a, K0): ...
    def from_GlobalPolynomialRing(K1, a, K0): ...
    def from_FractionField(K1, a, K0) -> None: ...
    def get_ring(self) -> Any: ...
    def poly_ring(self, *gens): ...
    def frac_field(self, *gens): ...
    def is_positive(self, a): ...
    def is_negative(self, a): ...
    def is_nonpositive(self, a): ...
    def is_nonnegative(self, a): ...
    def numer(self, a): ...
    def denom(self, a): ...
    def factorial(self, a) -> dtype: ...
