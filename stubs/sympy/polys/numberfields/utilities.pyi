from typing import Any, Generator, Literal, NoReturn
from sympy.utilities.decorator import public

def is_rat(c) -> Any | Literal[True]:
    ...

def is_int(c) -> Any | Literal[True]:
    ...

def get_num_denom(c) -> tuple[Any, Any]:
    ...

@public
def extract_fundamental_discriminant(a) -> tuple[dict[Any, Any], dict[int, int]] | tuple[dict[Any, Any], dict[Any, Any]]:
    ...

@public
class AlgIntPowers:
    def __init__(self, T, modulus=...) -> None:
        ...
    
    def red(self, exp):
        ...
    
    def __rmod__(self, other):
        ...
    
    def compute_up_through(self, e) -> None:
        ...
    
    def get(self, e) -> list[int] | list[Any]:
        ...
    
    def __getitem__(self, item) -> list[int] | list[Any]:
        ...
    


@public
def coeff_search(m, R) -> Generator[Any, Any, NoReturn]:
    ...

def supplement_a_subspace(M):
    ...

@public
def isolate(alg, eps=..., fast=...) -> tuple[Any, Any]:
    ...

