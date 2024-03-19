from typing import Any, Generator, Iterator, NoReturn, Self
from sympy.core.basic import Basic
from sympy.core.cache import cacheit
from sympy.core.decorators import call_highest_priority
from sympy.core.relational import Eq, Ne, Relational
from sympy.core.singleton import Singleton
from sympy.series.order import Order
from sympy.sets.sets import Complement, FiniteSet, Intersection, Interval, Union

class SeqBase(Basic):
    is_commutative = ...
    _op_priority = ...
    @property
    def gen(self):
        ...
    
    @property
    def interval(self):
        ...
    
    @property
    def start(self):
        ...
    
    @property
    def stop(self):
        ...
    
    @property
    def length(self):
        ...
    
    @property
    def variables(self) -> tuple[()]:
        ...
    
    @property
    def free_symbols(self) -> set[Basic]:
        ...
    
    @cacheit
    def coeff(self, pt):
        ...
    
    def coeff_mul(self, other) -> Order:
        ...
    
    def __add__(self, other) -> SeqAdd:
        ...
    
    @call_highest_priority('__add__')
    def __radd__(self, other):
        ...
    
    def __sub__(self, other) -> SeqAdd:
        ...
    
    @call_highest_priority('__sub__')
    def __rsub__(self, other):
        ...
    
    def __neg__(self) -> Order:
        ...
    
    def __mul__(self, other) -> SeqMul:
        ...
    
    @call_highest_priority('__mul__')
    def __rmul__(self, other):
        ...
    
    def __iter__(self) -> Generator[Any, Any, None]:
        ...
    
    def __getitem__(self, index) -> list[Any] | None:
        ...
    
    def find_linear_recurrence(self, n, d=..., gfvar=...) -> list[Any] | tuple[list[Any], None] | tuple[Any | list[Any], Any]:
        ...
    


class EmptySequence(SeqBase, metaclass=Singleton):
    @property
    def interval(self):
        ...
    
    @property
    def length(self):
        ...
    
    def coeff_mul(self, coeff) -> Self:
        ...
    
    def __iter__(self) -> Iterator[Any]:
        ...
    


class SeqExpr(SeqBase):
    @property
    def gen(self) -> Basic:
        ...
    
    @property
    def interval(self) -> FiniteSet | Interval:
        ...
    
    @property
    def start(self):
        ...
    
    @property
    def stop(self):
        ...
    
    @property
    def length(self):
        ...
    
    @property
    def variables(self) -> tuple[Any]:
        ...
    


class SeqPer(SeqExpr):
    def __new__(cls, periodical, limits=...) -> Self:
        ...
    
    @property
    def period(self) -> int:
        ...
    
    @property
    def periodical(self) -> Basic:
        ...
    
    def coeff_mul(self, coeff) -> SeqPer:
        ...
    


class SeqFormula(SeqExpr):
    def __new__(cls, formula, limits=...) -> Self:
        ...
    
    @property
    def formula(self) -> Basic:
        ...
    
    def coeff_mul(self, coeff) -> SeqFormula:
        ...
    
    def expand(self, *args, **kwargs) -> SeqFormula:
        ...
    


class RecursiveSeq(SeqBase):
    def __new__(cls, recurrence, yn, n, initial=..., start=...) -> Self:
        ...
    
    @property
    def recurrence(self) -> Eq | Relational | Ne:
        ...
    
    @property
    def yn(self) -> Basic:
        ...
    
    @property
    def y(self) -> type[Basic]:
        ...
    
    @property
    def n(self) -> Basic:
        ...
    
    @property
    def initial(self) -> Basic:
        ...
    
    @property
    def start(self) -> Basic:
        ...
    
    @property
    def stop(self):
        ...
    
    @property
    def interval(self) -> tuple[Basic, Any]:
        ...
    
    def __iter__(self) -> Generator[Any, Any, NoReturn]:
        ...
    


def sequence(seq, limits=...) -> SeqPer | SeqFormula:
    ...

class SeqExprOp(SeqBase):
    @property
    def gen(self) -> tuple[Any, ...]:
        ...
    
    @property
    def interval(self) -> FiniteSet | Intersection | Union | Complement:
        ...
    
    @property
    def start(self):
        ...
    
    @property
    def stop(self):
        ...
    
    @property
    def variables(self) -> tuple[Any, ...]:
        ...
    
    @property
    def length(self):
        ...
    


class SeqAdd(SeqExprOp):
    def __new__(cls, *args, **kwargs) -> SeqAdd | Self:
        ...
    
    @staticmethod
    def reduce(args) -> SeqAdd:
        ...
    


class SeqMul(SeqExprOp):
    def __new__(cls, *args, **kwargs) -> SeqMul | Self:
        ...
    
    @staticmethod
    def reduce(args) -> SeqMul:
        ...
    


