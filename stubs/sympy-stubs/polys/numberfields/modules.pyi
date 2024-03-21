from types import NotImplementedType
from typing import Any, Literal, Self
from sympy.polys.matrices.domainmatrix import DomainMatrix
from sympy.polys.polyclasses import ANP
from sympy.polys.polyutils import IntegerPowerable

def to_col(coeffs) -> DomainMatrix:
    ...

class Module:
    @property
    def n(self):
        ...
    
    def mult_tab(self):
        ...
    
    @property
    def parent(self) -> None:
        ...
    
    def represent(self, elt):
        ...
    
    def ancestors(self, include_self=...) -> list[Any]:
        ...
    
    def power_basis_ancestor(self) -> PowerBasis | None:
        ...
    
    def nearest_common_ancestor(self, other) -> None:
        ...
    
    @property
    def number_field(self) -> Any | None:
        ...
    
    def is_compat_col(self, col) -> Literal[False]:
        ...
    
    def __call__(self, spec, denom=...) -> PowerBasisElement | ModuleElement:
        ...
    
    def starts_with_unity(self):
        ...
    
    def basis_elements(self) -> list[PowerBasisElement | ModuleElement]:
        ...
    
    def zero(self) -> PowerBasisElement | NotImplementedType | ModuleElement:
        ...
    
    def one(self):
        ...
    
    def element_from_rational(self, a):
        ...
    
    def submodule_from_gens(self, gens, hnf=..., hnf_modulus=...) -> Submodule:
        ...
    
    def submodule_from_matrix(self, B, denom=...) -> Submodule:
        ...
    
    def whole_submodule(self) -> Submodule:
        ...
    
    def endomorphism_ring(self) -> EndomorphismRing:
        ...
    


class PowerBasis(Module):
    def __init__(self, T) -> None:
        ...
    
    @property
    def number_field(self) -> Any | None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    @property
    def n(self):
        ...
    
    def mult_tab(self) -> dict[Any, Any] | None:
        ...
    
    def compute_mult_tab(self) -> None:
        ...
    
    def represent(self, elt):
        ...
    
    def starts_with_unity(self) -> Literal[True]:
        ...
    
    def element_from_rational(self, a):
        ...
    
    def element_from_poly(self, f) -> PowerBasisElement | NotImplementedType | ModuleElement:
        ...
    
    def element_from_ANP(self, a) -> PowerBasisElement | NotImplementedType | ModuleElement:
        ...
    
    def element_from_alg_num(self, a) -> PowerBasisElement | NotImplementedType | ModuleElement:
        ...
    


class Submodule(Module, IntegerPowerable):
    def __init__(self, parent, matrix, denom=..., mult_tab=...) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def reduced(self) -> Self:
        ...
    
    def discard_before(self, r) -> Submodule:
        ...
    
    @property
    def n(self):
        ...
    
    def mult_tab(self) -> dict[Any, Any] | None:
        ...
    
    def compute_mult_tab(self) -> None:
        ...
    
    @property
    def parent(self) -> Any:
        ...
    
    @property
    def matrix(self) -> Any:
        ...
    
    @property
    def coeffs(self):
        ...
    
    @property
    def denom(self) -> int:
        ...
    
    @property
    def QQ_matrix(self):
        ...
    
    def starts_with_unity(self) -> bool:
        ...
    
    def is_sq_maxrank_HNF(self) -> bool:
        ...
    
    def is_power_basis_submodule(self) -> bool:
        ...
    
    def element_from_rational(self, a):
        ...
    
    def basis_element_pullbacks(self) -> list[PowerBasisElement | ModuleElement]:
        ...
    
    def represent(self, elt):
        ...
    
    def is_compat_submodule(self, other) -> Literal[False]:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def add(self, other, hnf=..., hnf_modulus=...):
        ...
    
    def __add__(self, other) -> NotImplementedType:
        ...
    
    __radd__ = ...
    def mul(self, other, hnf=..., hnf_modulus=...) -> Self | Submodule | NotImplementedType:
        ...
    
    def __mul__(self, other) -> Self | Submodule | NotImplementedType:
        ...
    
    __rmul__ = ...
    def reduce_element(self, elt):
        ...
    


def is_sq_maxrank_HNF(dm) -> bool:
    ...

def make_mod_elt(module, col, denom=...) -> PowerBasisElement | ModuleElement:
    ...

class ModuleElement(IntegerPowerable):
    def __init__(self, module, col, denom=...) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def reduced(self) -> Self:
        ...
    
    def reduced_mod_p(self, p) -> PowerBasisElement | ModuleElement:
        ...
    
    @classmethod
    def from_int_list(cls, module, coeffs, denom=...) -> Self:
        ...
    
    @property
    def n(self):
        ...
    
    def __len__(self):
        ...
    
    def column(self, domain=...):
        ...
    
    @property
    def coeffs(self):
        ...
    
    @property
    def QQ_col(self):
        ...
    
    def to_parent(self) -> PowerBasisElement | ModuleElement:
        ...
    
    def to_ancestor(self, anc) -> Self:
        ...
    
    def over_power_basis(self) -> Self | PowerBasisElement | ModuleElement:
        ...
    
    def is_compat(self, other) -> Literal[False]:
        ...
    
    def unify(self, other) -> tuple[Self, Any] | tuple[Self | Any, Any]:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def equiv(self, other) -> bool:
        ...
    
    def __add__(self, other) -> Self | NotImplementedType:
        ...
    
    __radd__ = ...
    def __neg__(self) -> Self | NotImplementedType | PowerBasisElement | ModuleElement:
        ...
    
    def __sub__(self, other):
        ...
    
    def __rsub__(self, other):
        ...
    
    def __mul__(self, other) -> Self | NotImplementedType | PowerBasisElement | ModuleElement:
        ...
    
    __rmul__ = ...
    def __floordiv__(self, a) -> Any | NotImplementedType:
        ...
    
    def __rfloordiv__(self, a):
        ...
    
    def __mod__(self, m) -> NotImplementedType:
        ...
    


class PowerBasisElement(ModuleElement):
    @property
    def T(self):
        ...
    
    def numerator(self, x=...) -> Any:
        ...
    
    def poly(self, x=...) -> Any:
        ...
    
    @property
    def is_rational(self):
        ...
    
    @property
    def generator(self):
        ...
    
    def as_expr(self, x=...) -> Any:
        ...
    
    def norm(self, T=...):
        ...
    
    def inverse(self):
        ...
    
    def __rfloordiv__(self, a):
        ...
    
    def to_ANP(self) -> ANP:
        ...
    
    def to_alg_num(self):
        ...
    


class ModuleHomomorphism:
    def __init__(self, domain, codomain, mapping) -> None:
        ...
    
    def matrix(self, modulus=...) -> DomainMatrix:
        ...
    
    def kernel(self, modulus=...):
        ...
    


class ModuleEndomorphism(ModuleHomomorphism):
    def __init__(self, domain, mapping) -> None:
        ...
    


class InnerEndomorphism(ModuleEndomorphism):
    def __init__(self, domain, multiplier) -> None:
        ...
    


class EndomorphismRing:
    def __init__(self, domain) -> None:
        ...
    
    def inner_endomorphism(self, multiplier) -> InnerEndomorphism:
        ...
    
    def represent(self, element) -> DomainMatrix:
        ...
    


def find_min_poly(alpha, domain, x=..., powers=...) -> Any | None:
    ...

