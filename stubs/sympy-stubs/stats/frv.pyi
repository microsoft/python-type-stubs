from typing import Any, Dict, Generator, Literal, Self
from sympy import Basic, Equality, FiniteSet, Ne, Piecewise, Sum
from sympy.core.cache import cacheit
from sympy.core.function import Lambda
from sympy.core.logic import Or
from sympy.core.relational import Relational
from sympy.series.order import Order
from sympy.stats.crv import ProductContinuousDomain
from sympy.stats.drv import ProductDiscreteDomain
from sympy.stats.rv import ConditionalDomain, Density, Distribution, IndependentProductPSpace, NamedArgsMixin, PSpace, ProductDomain, RandomDomain, SinglePSpace

class FiniteDensity(dict):
    def __call__(self, item) -> Literal[0]:
        ...
    
    @property
    def dict(self) -> dict[Any, Any]:
        ...
    


class FiniteDomain(RandomDomain):
    is_Finite = ...
    @property
    def symbols(self) -> FiniteSet:
        ...
    
    @property
    def elements(self) -> Basic:
        ...
    
    @property
    def dict(self) -> FiniteSet:
        ...
    
    def __contains__(self, other) -> bool:
        ...
    
    def __iter__(self):
        ...
    
    def as_boolean(self) -> Or:
        ...
    


class SingleFiniteDomain(FiniteDomain):
    def __new__(cls, symbol, set) -> Self:
        ...
    
    @property
    def symbol(self) -> Basic:
        ...
    
    @property
    def symbols(self) -> FiniteSet:
        ...
    
    @property
    def set(self) -> Basic:
        ...
    
    @property
    def elements(self) -> FiniteSet:
        ...
    
    def __iter__(self) -> Generator[frozenset[tuple[Basic, Any]], None, None]:
        ...
    
    def __contains__(self, other) -> bool:
        ...
    


class ProductFiniteDomain(ProductDomain, FiniteDomain):
    def __iter__(self) -> Generator[frozenset[Any], None, None]:
        ...
    
    @property
    def elements(self) -> FiniteSet:
        ...
    


class ConditionalFiniteDomain(ConditionalDomain, ProductFiniteDomain):
    def __new__(cls, domain, condition) -> Self:
        ...
    
    def __contains__(self, other) -> Basic | Literal[False]:
        ...
    
    def __iter__(self) -> Generator[Any, None, None]:
        ...
    
    @property
    def set(self) -> FiniteSet:
        ...
    
    def as_boolean(self) -> Or:
        ...
    


class SingleFiniteDistribution(Distribution, NamedArgsMixin):
    def __new__(cls, *args) -> Self:
        ...
    
    @staticmethod
    def check(*args) -> None:
        ...
    
    @property
    @cacheit
    def dict(self) -> Density | dict[Any, Any]:
        ...
    
    def pmf(self, *args):
        ...
    
    @property
    def set(self):
        ...
    
    values = ...
    items = ...
    is_symbolic = ...
    __iter__ = ...
    __getitem__ = ...
    def __call__(self, *args):
        ...
    
    def __contains__(self, other) -> bool:
        ...
    


class FinitePSpace(PSpace):
    is_Finite = ...
    def __new__(cls, domain, density) -> Self:
        ...
    
    def prob_of(self, elem):
        ...
    
    def where(self, condition) -> ConditionalFiniteDomain:
        ...
    
    def compute_density(self, expr) -> FiniteDensity:
        ...
    
    @cacheit
    def compute_cdf(self, expr) -> dict[Any, Any]:
        ...
    
    @cacheit
    def sorted_cdf(self, expr, python_float=...) -> list[tuple[Any, float]] | list[tuple[Any, Any]]:
        ...
    
    @cacheit
    def compute_characteristic_function(self, expr) -> Lambda:
        ...
    
    @cacheit
    def compute_moment_generating_function(self, expr) -> Lambda:
        ...
    
    def compute_expectation(self, expr, rvs=..., **kwargs):
        ...
    
    def compute_quantile(self, expr) -> Lambda:
        ...
    
    def probability(self, condition):
        ...
    
    def conditional_space(self, condition) -> FinitePSpace:
        ...
    
    def sample(self, size=..., library=..., seed=...) -> dict[Any, Any]:
        ...
    


class SingleFinitePSpace(SinglePSpace, FinitePSpace):
    @property
    def domain(self) -> SingleFiniteDomain:
        ...
    
    @property
    def distribution(self) -> Basic:
        ...
    
    def pmf(self, expr):
        ...
    
    @cacheit
    def compute_characteristic_function(self, expr) -> Lambda:
        ...
    
    @cacheit
    def compute_moment_generating_function(self, expr) -> Lambda:
        ...
    
    def compute_quantile(self, expr) -> Lambda:
        ...
    
    def compute_density(self, expr) -> Lambda | FiniteDensity:
        ...
    
    def compute_cdf(self, expr) -> Lambda | dict[Any, Any]:
        ...
    
    def compute_expectation(self, expr, rvs=..., **kwargs) -> tuple[Any, ...] | Sum | Order | Any | Piecewise | Basic | Equality | Relational | Ne | None:
        ...
    
    def probability(self, condition):
        ...
    
    def conditional_space(self, condition) -> FinitePSpace:
        ...
    


class ProductFinitePSpace(IndependentProductPSpace, FinitePSpace):
    @property
    def domain(self) -> ProductDiscreteDomain | ProductContinuousDomain | ProductFiniteDomain:
        ...
    
    @property
    @cacheit
    def density(self) -> Dict:
        ...
    
    def probability(self, condition):
        ...
    
    def compute_density(self, expr) -> FiniteDensity:
        ...
    


