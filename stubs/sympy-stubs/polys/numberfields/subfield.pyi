from typing import Any
from sympy.core.numbers import AlgebraicNumber
from sympy.utilities import public

def is_isomorphism_possible(a, b) -> bool:
    ...

def field_isomorphism_pslq(a, b) -> list[Any] | None:
    ...

def field_isomorphism_factor(a, b) -> Any | None:
    ...

@public
def field_isomorphism(a, b, *, fast=...) -> list[Any] | Any | None:
    ...

@public
def primitive_element(extension, x=..., *, ex=..., polys=...) -> tuple[Any, list[int]] | tuple[Any, list[int], list[Any]]:
    ...

@public
def to_number_field(extension, theta=..., *, gen=..., alias=...) -> AlgebraicNumber:
    ...

