from typing import Any, Literal, LiteralString, Self

from sympy.core import Basic
from sympy.core.function import UndefinedFunction
from sympy.sets.sets import FiniteSet

class Partition(FiniteSet):
    _rank = ...
    _partition = ...
    def __new__(cls, *partition) -> Self: ...
    def sort_key(self, order=...) -> tuple[
        tuple[tuple[Literal[5], Literal[0], str], tuple[int, tuple[Any, ...]], Any, Any]
        | Any
        | tuple[
            tuple[Literal[10, 0], Literal[0], str | Any], tuple[int, tuple[Any, ...]] | tuple[Literal[1], tuple[str]], Any, Any
        ],
        ...,
    ]: ...
    @property
    def partition(self) -> list[Any]: ...
    def __add__(self, other) -> Partition: ...
    def __sub__(self, other) -> Partition: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    @property
    def rank(self) -> int: ...
    @property
    def RGS(self) -> tuple[Any, ...]: ...
    @classmethod
    def from_rgs(cls, rgs, elements) -> Partition: ...

class IntegerPartition(Basic):
    _dict = ...
    _keys = ...
    def __new__(cls, partition, integer=...) -> Self: ...
    def prev_lex(self) -> IntegerPartition: ...
    def next_lex(self) -> IntegerPartition: ...
    def as_dict(self) -> dict[str, str]: ...
    @property
    def conjugate(self): ...
    def __lt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def as_ferrers(self, char=...) -> LiteralString: ...
    def __str__(self) -> str: ...

def random_integer_partition(n, seed=...) -> list[Any]: ...
def RGS_generalized(m): ...
def RGS_enum(m) -> type[UndefinedFunction] | Literal[0, 1]: ...
def RGS_unrank(rank, m) -> list[Any]: ...
def RGS_rank(rgs) -> Literal[0]: ...
