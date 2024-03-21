from typing import Any
from sympy.core.basic import Basic
from sympy.core.symbol import Dummy
from sympy.functions.elementary.piecewise import Piecewise

def components(f, x) -> set[Any]:
    ...

_symbols_cache: dict[str, list[Dummy]] = ...
def heurisch_wrapper(f, x, rewrite=..., hints=..., mappings=..., retries=..., degree_offset=..., unnecessary_permutations=..., _try_heurisch=...) -> Basic | Piecewise:
    ...

class BesselTable:
    def __init__(self) -> None:
        ...
    
    def diffs(self, f, n, z) -> tuple[Any, Any] | None:
        ...
    
    def has(self, f) -> bool:
        ...
    


_bessel_table = ...
class DiffCache:
    def __init__(self, x) -> None:
        ...
    
    def get_diff(self, f):
        ...
    


def heurisch(f, x, rewrite=..., hints=..., mappings=..., retries=..., degree_offset=..., unnecessary_permutations=..., _try_heurisch=...):
    ...

