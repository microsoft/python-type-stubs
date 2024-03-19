from typing import Any
from sympy.polys.numberfields.galois_resolvents import GaloisGroupException
from sympy.utilities import public

class MaxTriesException(GaloisGroupException):
    ...


def tschirnhausen_transformation(T, max_coeff=..., max_tries=..., history=..., fixed_order=...) -> tuple[Any, Any]:
    ...

def has_square_disc(T) -> bool:
    ...

@public
def galois_group(f, *gens, by_name=..., max_tries=..., randomize=..., **args) -> Any:
    ...

