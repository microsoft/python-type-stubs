from collections.abc import Generator
from typing import Any

from sympy.combinatorics.permutations import Permutation

def symmetric(n) -> Generator[Permutation, Any, None]: ...
def cyclic(n) -> Generator[Permutation, Any, None]: ...
def alternating(n) -> Generator[Permutation, Any, None]: ...
def dihedral(n) -> Generator[Permutation, Any, None]: ...
def rubik_cube_generators() -> list[Permutation]: ...
def rubik(n) -> list[Any]: ...
