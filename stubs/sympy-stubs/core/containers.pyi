from collections.abc import MutableSet
from types import NotImplementedType
from typing import Any, Callable, Generator, Iterator, Self

from sympy.core.basic import Basic
from sympy.core.kind import Kind

class Tuple(Basic):
    def __new__(cls, *args, **kwargs) -> Self:
        ...
    
    def __getitem__(self, i) -> Tuple:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __contains__(self, item) -> bool:
        ...
    
    def __iter__(self) -> Iterator[Basic]:
        ...
    
    def __add__(self, other) -> Tuple | NotImplementedType:
        ...
    
    def __radd__(self, other) -> Tuple | NotImplementedType:
        ...
    
    def __mul__(self, other) -> Self:
        ...
    
    __rmul__ = ...
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def tuple_count(self, value) -> int:
        ...
    
    def index(self, value, start=..., stop=...) -> int:
        ...
    
    @property
    def kind(self) -> TupleKind:
        ...
    


def tuple_wrapper(method) -> Callable[..., Any]:
    ...

class Dict(Basic):
    def __new__(cls, *args) -> Self:
        ...
    
    def __getitem__(self, key):
        ...
    
    def __setitem__(self, key, value):
        ...
    
    def items(self):
        ...
    
    def keys(self):
        ...
    
    def values(self):
        ...
    
    def __iter__(self):
        ...
    
    def __len__(self):
        ...
    
    def get(self, key, default=...) -> None:
        ...
    
    def __contains__(self, key) -> bool:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    __hash__: Callable[[Basic], Any] = ...


class OrderedSet(MutableSet):
    def __init__(self, iterable=...) -> None:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __contains__(self, key) -> bool:
        ...
    
    def add(self, key) -> None:
        ...
    
    def discard(self, key) -> None:
        ...
    
    def pop(self, last=...):
        ...
    
    def __iter__(self) -> Generator[Any, Any, None]:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def intersection(self, other) -> Self:
        ...
    
    def difference(self, other) -> Self:
        ...
    
    def update(self, iterable) -> None:
        ...
    


class TupleKind(Kind):
    def __new__(cls, *args) -> Self:
        ...
    
    def __repr__(self) -> str:
        ...
    


