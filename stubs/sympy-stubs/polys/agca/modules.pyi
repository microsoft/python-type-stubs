from types import NotImplementedType
from typing import Any, Literal, LiteralString, Self

from sympy.polys.agca.homomorphisms import FreeModuleHomomorphism
from sympy.polys.orderings import ProductOrder

class Module:
    def __init__(self, ring) -> None:
        ...
    
    def convert(self, elem, M=...):
        ...
    
    def submodule(self, *gens):
        ...
    
    def quotient_module(self, other):
        ...
    
    def __truediv__(self, e):
        ...
    
    def contains(self, elem) -> bool:
        ...
    
    def __contains__(self, elem) -> bool:
        ...
    
    def subset(self, other) -> bool:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def is_zero(self):
        ...
    
    def is_submodule(self, other):
        ...
    
    def multiply_ideal(self, other):
        ...
    
    def __mul__(self, e) -> NotImplementedType:
        ...
    
    __rmul__ = ...
    def identity_hom(self):
        ...
    


class ModuleElement:
    def __init__(self, module, data) -> None:
        ...
    
    def add(self, d1, d2):
        ...
    
    def mul(self, m, d):
        ...
    
    def div(self, m, d):
        ...
    
    def eq(self, d1, d2):
        ...
    
    def __add__(self, om) -> NotImplementedType | Self:
        ...
    
    __radd__ = ...
    def __neg__(self) -> Self:
        ...
    
    def __sub__(self, om) -> NotImplementedType | Self:
        ...
    
    def __rsub__(self, om) -> NotImplementedType | ModuleElement:
        ...
    
    def __mul__(self, o) -> NotImplementedType | Self:
        ...
    
    __rmul__ = ...
    def __truediv__(self, o) -> NotImplementedType | Self:
        ...
    
    def __eq__(self, om) -> bool:
        ...
    
    def __ne__(self, om) -> bool:
        ...
    


class FreeModuleElement(ModuleElement):
    def add(self, d1, d2) -> tuple[Any, ...]:
        ...
    
    def mul(self, d, p) -> tuple[Any, ...]:
        ...
    
    def div(self, d, p) -> tuple[Any, ...]:
        ...
    
    def __repr__(self) -> LiteralString:
        ...
    
    def __iter__(self):
        ...
    
    def __getitem__(self, idx):
        ...
    


class FreeModule(Module):
    dtype = FreeModuleElement
    def __init__(self, ring, rank) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def is_submodule(self, other) -> Literal[False]:
        ...
    
    def convert(self, elem, M=...) -> FreeModuleElement:
        ...
    
    def is_zero(self):
        ...
    
    def basis(self) -> tuple[FreeModuleElement, ...]:
        ...
    
    def quotient_module(self, submodule) -> QuotientModule:
        ...
    
    def multiply_ideal(self, other):
        ...
    
    def identity_hom(self) -> FreeModuleHomomorphism:
        ...
    


class FreeModulePolyRing(FreeModule):
    def __init__(self, ring, rank) -> None:
        ...
    
    def submodule(self, *gens, **opts) -> SubModulePolyRing:
        ...
    


class FreeModuleQuotientRing(FreeModule):
    def __init__(self, ring, rank) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def submodule(self, *gens, **opts) -> SubModuleQuotientRing:
        ...
    
    def lift(self, elem):
        ...
    
    def unlift(self, elem) -> FreeModuleElement:
        ...
    


class SubModule(Module):
    def __init__(self, gens, container) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def convert(self, elem, M=...):
        ...
    
    def intersect(self, other, **options):
        ...
    
    def module_quotient(self, other, **options):
        ...
    
    def union(self, other) -> Self:
        ...
    
    def is_zero(self) -> bool:
        ...
    
    def submodule(self, *gens) -> Self:
        ...
    
    def is_full_module(self) -> bool:
        ...
    
    def is_submodule(self, other) -> bool:
        ...
    
    def syzygy_module(self, **opts):
        ...
    
    def in_terms_of_generators(self, e):
        ...
    
    def reduce_element(self, x):
        ...
    
    def quotient_module(self, other, **opts) -> SubQuotientModule:
        ...
    
    def __add__(self, oth):
        ...
    
    __radd__ = ...
    def multiply_ideal(self, I) -> Self:
        ...
    
    def inclusion_hom(self):
        ...
    
    def identity_hom(self):
        ...
    


class SubQuotientModule(SubModule):
    def __init__(self, gens, container, **opts) -> None:
        ...
    
    def is_full_module(self):
        ...
    
    def quotient_hom(self):
        ...
    


_subs0 = ...
_subs1 = ...
class ModuleOrder(ProductOrder):
    def __init__(self, o1, o2, TOP) -> None:
        ...
    


class SubModulePolyRing(SubModule):
    def __init__(self, gens, container, order=..., TOP=...) -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def reduce_element(self, x, NF=...):
        ...
    


class SubModuleQuotientRing(SubModule):
    def __init__(self, gens, container) -> None:
        ...
    


class QuotientModuleElement(ModuleElement):
    def eq(self, d1, d2):
        ...
    
    def __repr__(self) -> str:
        ...
    


class QuotientModule(Module):
    dtype = QuotientModuleElement
    def __init__(self, ring, base, submodule) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def is_zero(self):
        ...
    
    def is_submodule(self, other) -> Literal[False]:
        ...
    
    def submodule(self, *gens, **opts) -> SubQuotientModule:
        ...
    
    def convert(self, elem, M=...) -> QuotientModuleElement:
        ...
    
    def identity_hom(self):
        ...
    
    def quotient_hom(self):
        ...
    


