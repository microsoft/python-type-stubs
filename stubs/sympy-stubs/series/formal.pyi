from typing import Any, Generator, Self
from sympy.core.basic import Basic
from sympy.core.function import Function, UndefinedFunction
from sympy.core.numbers import Float, Integer, Rational
from sympy.core.relational import Equality, Ne, Relational
from sympy.functions.elementary.piecewise import Piecewise
from sympy.series.order import Order
from sympy.series.sequences import SeqFormula, SeqPer
from sympy.series.series_class import SeriesBase
from sympy.sets.sets import FiniteSet, Interval

def rational_algorithm(f, x, k, order=..., full=...) -> tuple[Any, Any, int] | None:
    ...

def rational_independent(terms, x) -> list[Any]:
    ...

def simpleDE(f, x, g, order=...) -> Generator[tuple[Any, int], Any, None]:
    ...

def exp_re(DE, r, k):
    ...

def hyper_re(DE, r, k):
    ...

def rsolve_hypergeometric(f, x, P, Q, k, m) -> tuple[Any | Piecewise, Any, Any | type[UndefinedFunction] | Rational | Integer | Float | Order] | None:
    ...

def solve_de(f, x, DE, order, g, k) -> tuple[Any | Piecewise, Any, Any | type[UndefinedFunction] | Rational | Integer | Float | Order] | tuple[Any, Any, Any] | None:
    ...

def hyper_algorithm(f, x, k, order=...) -> tuple[Any | Piecewise, Any, Any | type[UndefinedFunction] | Rational | Integer | Float | Order] | tuple[Any, Any, Any] | None:
    ...

def compute_fps(f, x, x0=..., dir=..., hyper=..., order=..., rational=..., full=...) -> tuple[Any, Any, Any] | tuple[Any | SeqPer | SeqFormula, Any | SeqPer | SeqFormula, Any] | tuple[Any | SeqPer | SeqFormula, Any | None, Any] | None:
    ...

class Coeff(Function):
    @classmethod
    def eval(cls, p, x, n) -> None:
        ...
    


class FormalPowerSeries(SeriesBase):
    def __new__(cls, *args) -> Self:
        ...
    
    def __init__(self, *args) -> None:
        ...
    
    @property
    def function(self) -> Basic:
        ...
    
    @property
    def x(self) -> Basic:
        ...
    
    @property
    def x0(self) -> Basic:
        ...
    
    @property
    def dir(self) -> Basic:
        ...
    
    @property
    def ak(self):
        ...
    
    @property
    def xk(self):
        ...
    
    @property
    def ind(self):
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
    def infinite(self):
        ...
    
    def polynomial(self, n=...) -> Order:
        ...
    
    def truncate(self, n=...) -> Generator[Any, Any, None]:
        ...
    
    def zero_coeff(self):
        ...
    
    def integrate(self, x=..., **kwargs) -> Equality | Relational | Ne | Self:
        ...
    
    def product(self, other, x=..., n=...) -> Generator[Any, Any, None] | FormalPowerSeriesProduct:
        ...
    
    def coeff_bell(self, n) -> SeqPer | SeqFormula:
        ...
    
    def compose(self, other, x=..., n=...) -> Generator[Any, Any, None] | FormalPowerSeriesCompose:
        ...
    
    def inverse(self, x=..., n=...) -> Generator[Any, Any, None] | FormalPowerSeriesInverse:
        ...
    
    def __add__(self, other) -> Self | Order:
        ...
    
    def __radd__(self, other) -> Self | Order:
        ...
    
    def __neg__(self) -> Self:
        ...
    
    def __sub__(self, other) -> Self | Order:
        ...
    
    def __rsub__(self, other) -> FormalPowerSeries | Order:
        ...
    
    def __mul__(self, other) -> Order | Self:
        ...
    
    def __rmul__(self, other) -> Order | Self:
        ...
    


class FiniteFormalPowerSeries(FormalPowerSeries):
    def __init__(self, *args) -> None:
        ...
    
    @property
    def ffps(self) -> Basic:
        ...
    
    @property
    def gfps(self) -> Basic:
        ...
    
    @property
    def f(self):
        ...
    
    @property
    def g(self):
        ...
    
    @property
    def infinite(self):
        ...
    
    def polynomial(self, n):
        ...
    
    def truncate(self, n=...):
        ...
    
    def integrate(self, x):
        ...
    


class FormalPowerSeriesProduct(FiniteFormalPowerSeries):
    def __init__(self, *args) -> None:
        ...
    
    @property
    def function(self):
        ...
    


class FormalPowerSeriesCompose(FiniteFormalPowerSeries):
    @property
    def function(self):
        ...
    


class FormalPowerSeriesInverse(FiniteFormalPowerSeries):
    def __init__(self, *args) -> None:
        ...
    
    @property
    def function(self):
        ...
    
    @property
    def g(self):
        ...
    
    @property
    def gfps(self):
        ...
    


def fps(f, x=..., x0=..., dir=..., hyper=..., order=..., rational=..., full=...) -> FormalPowerSeries:
    ...

