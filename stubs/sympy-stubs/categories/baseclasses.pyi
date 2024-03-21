from typing import Any, Self
from sympy.core import Basic, Symbol
from sympy.sets import Set

class Class(Set):
    is_proper = ...


class Object(Symbol):
    ...


class Morphism(Basic):
    def __new__(cls, domain, codomain):
        ...
    
    @property
    def domain(self) -> Basic:
        ...
    
    @property
    def codomain(self) -> Basic:
        ...
    
    def compose(self, other) -> Morphism | CompositeMorphism:
        ...
    
    def __mul__(self, other) -> Morphism | CompositeMorphism:
        ...
    


class IdentityMorphism(Morphism):
    def __new__(cls, domain) -> Self:
        ...
    
    @property
    def codomain(self) -> Basic:
        ...
    


class NamedMorphism(Morphism):
    def __new__(cls, domain, codomain, name) -> Self:
        ...
    
    @property
    def name(self):
        ...
    


class CompositeMorphism(Morphism):
    def __new__(cls, *components) -> Morphism | Self:
        ...
    
    @property
    def components(self) -> Basic:
        ...
    
    @property
    def domain(self):
        ...
    
    @property
    def codomain(self):
        ...
    
    def flatten(self, new_name) -> NamedMorphism:
        ...
    


class Category(Basic):
    def __new__(cls, name, objects=..., commutative_diagrams=...) -> Self:
        ...
    
    @property
    def name(self):
        ...
    
    @property
    def objects(self) -> Basic:
        ...
    
    @property
    def commutative_diagrams(self) -> Basic:
        ...
    
    def hom(self, A, B):
        ...
    
    def all_morphisms(self):
        ...
    


class Diagram(Basic):
    def __new__(cls, *args) -> Self:
        ...
    
    @property
    def premises(self) -> Basic:
        ...
    
    @property
    def conclusions(self) -> Basic:
        ...
    
    @property
    def objects(self) -> Basic:
        ...
    
    def hom(self, A, B) -> tuple[Any, Any]:
        ...
    
    def is_subdiagram(self, diagram) -> bool:
        ...
    
    def subdiagram_from_objects(self, objects) -> Diagram:
        ...
    


