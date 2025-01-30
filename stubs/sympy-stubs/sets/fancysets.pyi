from typing import Any, Generator, Iterator, Literal, NoReturn
from typing_extensions import Self

from sympy.core.basic import Basic
from sympy.core.logic import And
from sympy.core.numbers import Integer, Rational
from sympy.core.singleton import Singleton
from sympy.sets.sets import FiniteSet, Interval, ProductSet, Set, Union

class Rationals(Set, metaclass=Singleton):
    is_iterable = ...
    _inf = ...
    _sup = ...
    is_empty = ...
    is_finite_set = ...
    def __iter__(self) -> Generator[Any | Rational | Integer, Any, NoReturn]: ...

class Naturals(Set, metaclass=Singleton):
    is_iterable = ...
    _inf = ...
    _sup = ...
    is_empty = ...
    is_finite_set = ...
    def __iter__(self) -> Generator[Any, Any, NoReturn]: ...
    def as_relational(self, x) -> And: ...

class Naturals0(Naturals):
    _inf = ...

class Integers(Set, metaclass=Singleton):
    is_iterable = ...
    is_empty = ...
    is_finite_set = ...
    def __iter__(self) -> Generator[Any, Any, NoReturn]: ...
    def as_relational(self, x) -> And: ...

class Reals(Interval, metaclass=Singleton):
    @property
    def start(self): ...
    @property
    def end(self): ...
    @property
    def left_open(self) -> Literal[True]: ...
    @property
    def right_open(self) -> Literal[True]: ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...

class ImageSet(Set):
    def __new__(cls, flambda, *sets) -> FiniteSet | Self: ...

    lamda = ...
    base_sets = ...
    @property
    def base_set(self) -> Any | FiniteSet | ProductSet: ...
    @property
    def base_pset(self) -> FiniteSet | ProductSet: ...
    def __iter__(self) -> Iterator[Any]: ...
    @property
    def is_iterable(self) -> bool: ...
    def doit(self, **hints) -> Any | FiniteSet | Self: ...

class Range(Set):
    def __new__(cls, *args): ...

    start = ...
    stop = ...
    step = ...
    @property
    def reversed(self) -> Self: ...
    def __iter__(self) -> Iterator[Any]: ...
    @property
    def is_iterable(self) -> bool: ...
    def __len__(self) -> int: ...
    @property
    def size(self): ...
    @property
    def is_finite_set(self) -> Literal[True]: ...
    @property
    def is_empty(self) -> None: ...
    def __bool__(self) -> bool: ...
    def __getitem__(self, i): ...
    def as_relational(self, x) -> And: ...

def normalize_theta_set(theta) -> FiniteSet | Union | Interval: ...

class ComplexRegion(Set):
    is_ComplexRegion = ...
    def __new__(cls, sets, polar=...) -> FiniteSet | CartesianComplexRegion | PolarComplexRegion: ...
    @property
    def sets(self) -> Basic: ...
    @property
    def psets(self) -> tuple[Basic] | tuple[Basic, ...]: ...
    @property
    def a_interval(self) -> FiniteSet | Union: ...
    @property
    def b_interval(self) -> FiniteSet | Union: ...
    @classmethod
    def from_real(cls, sets) -> FiniteSet | CartesianComplexRegion: ...

class CartesianComplexRegion(ComplexRegion):
    polar = ...
    variables = ...
    def __new__(cls, sets) -> FiniteSet | Self: ...
    @property
    def expr(self): ...

class PolarComplexRegion(ComplexRegion):
    polar = ...
    variables = ...
    def __new__(cls, sets) -> Self: ...
    @property
    def expr(self): ...

class Complexes(CartesianComplexRegion, metaclass=Singleton):
    is_empty = ...
    is_finite_set = ...
    @property
    def sets(self) -> FiniteSet | ProductSet: ...
    def __new__(cls) -> Self: ...
