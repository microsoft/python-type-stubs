from typing import Any

class SolveFailed(Exception):
    ...


def solve_poly_system(seq, *gens, strict=..., **args) -> list[tuple[Any, Any]] | list[tuple[Any]] | None:
    ...

def solve_biquadratic(f, g, opt) -> list[tuple[Any, Any]] | None:
    ...

def solve_generic(polys, opt, strict=...) -> list[tuple[Any]] | None:
    ...

def solve_triangulated(polys, *gens, **args) -> list[Any]:
    ...

