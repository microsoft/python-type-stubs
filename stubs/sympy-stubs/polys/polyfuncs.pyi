from typing import Any

from sympy.utilities import public

@public
def symmetrize(F, *gens, **args) -> list[Any] | tuple[Any | list[Any], list[tuple[Any, Any]]]:
    ...

@public
def horner(f, *gens, **args):
    ...

@public
def interpolate(data, x) -> Any:
    ...

@public
def rational_interpolate(data, degnum, X=...) -> float:
    ...

@public
def viete(f, roots=..., *gens, **args) -> list[Any]:
    ...

