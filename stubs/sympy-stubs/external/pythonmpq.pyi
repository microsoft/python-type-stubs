from types import NotImplementedType
from typing import Any, Self, Tuple as tTuple, Type

_PyHASH_MODULUS = ...
_PyHASH_INF = ...

class PythonMPQ:
    __slots__ = ...
    def __new__(cls, numerator, denominator=...) -> Self: ...
    def __int__(self) -> int: ...
    def __float__(self): ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __reduce__(self) -> tuple[type[Self], tuple[Any, Any]]: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __abs__(self) -> Self: ...
    def __pos__(self) -> Self: ...
    def __neg__(self) -> Self: ...
    def __add__(self, other) -> NotImplementedType | Self: ...
    def __radd__(self, other) -> Self | NotImplementedType: ...
    def __sub__(self, other) -> NotImplementedType | Self: ...
    def __rsub__(self, other) -> Self | NotImplementedType: ...
    def __mul__(self, other) -> NotImplementedType | Self: ...
    def __rmul__(self, other) -> Self | NotImplementedType: ...
    def __pow__(self, exp) -> Self: ...
    def __truediv__(self, other) -> NotImplementedType | Self: ...
    def __rtruediv__(self, other) -> Self | NotImplementedType: ...

    _compatible_types: tTuple[Type, ...] = ...
