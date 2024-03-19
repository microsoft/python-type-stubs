from typing import Any
from sympy import Basic, FiniteSet, Intersection, Piecewise
from sympy.core.cache import cacheit
from sympy.core.function import Lambda
from sympy.core.numbers import Integer, Rational
from sympy.sets.sets import Complement, Union
from sympy.stats.frv import SingleFiniteDistribution
from sympy.stats.rv import Density, RandomSymbol

__all__ = ['FiniteRV', 'DiscreteUniform', 'Die', 'Bernoulli', 'Coin', 'Binomial', 'BetaBinomial', 'Hypergeometric', 'Rademacher', 'IdealSoliton', 'RobustSoliton']
def rv(name, cls, *args, **kwargs) -> RandomSymbol:
    ...

class FiniteDistributionHandmade(SingleFiniteDistribution):
    @property
    def dict(self) -> Basic:
        ...
    
    def pmf(self, x) -> Lambda:
        ...
    
    @property
    def set(self) -> set[Any]:
        ...
    
    @staticmethod
    def check(density) -> None:
        ...
    


def FiniteRV(name, density, **kwargs) -> RandomSymbol:
    ...

class DiscreteUniformDistribution(SingleFiniteDistribution):
    @staticmethod
    def check(*args) -> None:
        ...
    
    @property
    def p(self) -> Rational | Integer:
        ...
    
    @property
    @cacheit
    def dict(self) -> dict[Basic, Rational | Any | Integer]:
        ...
    
    @property
    def set(self) -> set[Basic]:
        ...
    
    def pmf(self, x) -> Rational | Integer:
        ...
    


def DiscreteUniform(name, items) -> RandomSymbol:
    ...

class DieDistribution(SingleFiniteDistribution):
    _argnames = ...
    @staticmethod
    def check(sides) -> None:
        ...
    
    @property
    def is_symbolic(self) -> bool:
        ...
    
    @property
    def high(self):
        ...
    
    @property
    def low(self):
        ...
    
    @property
    def set(self) -> FiniteSet | Intersection | Union | Complement | set[Any | Integer]:
        ...
    
    def pmf(self, x) -> Piecewise:
        ...
    


def Die(name, sides=...) -> RandomSymbol:
    ...

class BernoulliDistribution(SingleFiniteDistribution):
    _argnames = ...
    @staticmethod
    def check(p, succ, fail) -> None:
        ...
    
    @property
    def set(self) -> set[Any]:
        ...
    
    def pmf(self, x) -> Piecewise:
        ...
    


def Bernoulli(name, p, succ=..., fail=...) -> RandomSymbol:
    ...

def Coin(name, p=...) -> RandomSymbol:
    ...

class BinomialDistribution(SingleFiniteDistribution):
    _argnames = ...
    @staticmethod
    def check(n, p, succ, fail) -> None:
        ...
    
    @property
    def high(self):
        ...
    
    @property
    def low(self):
        ...
    
    @property
    def is_symbolic(self) -> bool:
        ...
    
    @property
    def set(self) -> FiniteSet | Intersection | Union | Complement | set[Any]:
        ...
    
    def pmf(self, x) -> Piecewise:
        ...
    
    @property
    @cacheit
    def dict(self) -> Density | dict[Any, Any | Piecewise]:
        ...
    


def Binomial(name, n, p, succ=..., fail=...) -> RandomSymbol:
    ...

class BetaBinomialDistribution(SingleFiniteDistribution):
    _argnames = ...
    @staticmethod
    def check(n, alpha, beta) -> None:
        ...
    
    @property
    def high(self):
        ...
    
    @property
    def low(self):
        ...
    
    @property
    def is_symbolic(self) -> bool:
        ...
    
    @property
    def set(self) -> FiniteSet | Intersection | Union | Complement | set[Any | Integer]:
        ...
    
    def pmf(self, k):
        ...
    


def BetaBinomial(name, n, alpha, beta) -> RandomSymbol:
    ...

class HypergeometricDistribution(SingleFiniteDistribution):
    _argnames = ...
    @staticmethod
    def check(n, N, m) -> None:
        ...
    
    @property
    def is_symbolic(self) -> bool:
        ...
    
    @property
    def high(self) -> Piecewise:
        ...
    
    @property
    def low(self) -> Piecewise:
        ...
    
    @property
    def set(self) -> FiniteSet | Intersection | Union | Complement | set[int]:
        ...
    
    def pmf(self, k):
        ...
    


def Hypergeometric(name, N, m, n) -> RandomSymbol:
    ...

class RademacherDistribution(SingleFiniteDistribution):
    @property
    def set(self) -> set[int]:
        ...
    
    @property
    def pmf(self) -> Lambda:
        ...
    


def Rademacher(name) -> RandomSymbol:
    ...

class IdealSolitonDistribution(SingleFiniteDistribution):
    _argnames = ...
    @staticmethod
    def check(k) -> None:
        ...
    
    @property
    def low(self):
        ...
    
    @property
    def high(self):
        ...
    
    @property
    def set(self) -> set[Any | Integer]:
        ...
    
    @property
    @cacheit
    def dict(self) -> Density | dict[int, Rational | Any | Integer]:
        ...
    
    def pmf(self, x) -> Piecewise:
        ...
    


def IdealSoliton(name, k) -> RandomSymbol:
    ...

class RobustSolitonDistribution(SingleFiniteDistribution):
    _argnames = ...
    @staticmethod
    def check(k, delta, c) -> None:
        ...
    
    @property
    def R(self):
        ...
    
    @property
    def Z(self):
        ...
    
    @property
    def low(self):
        ...
    
    @property
    def high(self):
        ...
    
    @property
    def set(self) -> set[Any | Integer]:
        ...
    
    @property
    def is_symbolic(self) -> bool:
        ...
    
    def pmf(self, x):
        ...
    


def RobustSoliton(name, k, delta, c) -> RandomSymbol:
    ...

