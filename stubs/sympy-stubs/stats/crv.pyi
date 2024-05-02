from typing import Any, Literal, Self

from sympy import Basic, Equality, FiniteSet, Integral, Ne
from sympy.core.cache import cacheit
from sympy.core.function import Lambda
from sympy.core.logic import And
from sympy.core.relational import Relational
from sympy.sets.sets import Union
from sympy.stats.rv import (
    ConditionalDomain,
    Distribution,
    NamedArgsMixin,
    ProductDomain,
    PSpace,
    RandomDomain,
    RandomSymbol,
    SingleDomain,
    SinglePSpace,
)

class ContinuousDomain(RandomDomain):
    is_Continuous = ...
    def as_boolean(self):
        ...
    


class SingleContinuousDomain(ContinuousDomain, SingleDomain):
    def compute_expectation(self, expr, variables=..., **kwargs) -> Equality | Relational | Ne | Integral:
        ...
    
    def as_boolean(self):
        ...
    


class ProductContinuousDomain(ProductDomain, ContinuousDomain):
    def compute_expectation(self, expr, variables=..., **kwargs):
        ...
    
    def as_boolean(self) -> And:
        ...
    


class ConditionalContinuousDomain(ContinuousDomain, ConditionalDomain):
    def compute_expectation(self, expr, variables=..., **kwargs) -> Equality | Relational | Ne | Integral:
        ...
    
    def as_boolean(self) -> And:
        ...
    
    @property
    def set(self):
        ...
    


class ContinuousDistribution(Distribution):
    def __call__(self, *args):
        ...
    


class SingleContinuousDistribution(ContinuousDistribution, NamedArgsMixin):
    set = ...
    def __new__(cls, *args) -> Self:
        ...
    
    @staticmethod
    def check(*args) -> None:
        ...
    
    @cacheit
    def compute_cdf(self, **kwargs) -> Lambda:
        ...
    
    def cdf(self, x, **kwargs) -> Basic:
        ...
    
    @cacheit
    def compute_characteristic_function(self, **kwargs) -> Lambda:
        ...
    
    def characteristic_function(self, t, **kwargs) -> Basic:
        ...
    
    @cacheit
    def compute_moment_generating_function(self, **kwargs) -> Lambda:
        ...
    
    def moment_generating_function(self, t, **kwargs) -> Basic:
        ...
    
    def expectation(self, expr, var, evaluate=..., **kwargs) -> Equality | Relational | Ne | Any | Integral | Literal[0]:
        ...
    
    @cacheit
    def compute_quantile(self, **kwargs) -> Lambda:
        ...
    
    def quantile(self, x, **kwargs) -> Basic:
        ...
    


class ContinuousPSpace(PSpace):
    is_Continuous = ...
    is_real = ...
    @property
    def pdf(self):
        ...
    
    def compute_expectation(self, expr, rvs=..., evaluate=..., **kwargs):
        ...
    
    def compute_density(self, expr, **kwargs) -> Lambda:
        ...
    
    @cacheit
    def compute_cdf(self, expr, **kwargs) -> Lambda:
        ...
    
    @cacheit
    def compute_characteristic_function(self, expr, **kwargs) -> Lambda:
        ...
    
    @cacheit
    def compute_moment_generating_function(self, expr, **kwargs) -> Lambda:
        ...
    
    @cacheit
    def compute_quantile(self, expr, **kwargs) -> Lambda:
        ...
    
    def probability(self, condition, **kwargs):
        ...
    
    def where(self, condition) -> SingleContinuousDomain:
        ...
    
    def conditional_space(self, condition, normalize=..., **kwargs) -> ContinuousPSpace:
        ...
    


class SingleContinuousPSpace(ContinuousPSpace, SinglePSpace):
    @property
    def set(self):
        ...
    
    @property
    def domain(self) -> SingleContinuousDomain:
        ...
    
    def sample(self, size=..., library=..., seed=...) -> dict[RandomSymbol, Any]:
        ...
    
    def compute_expectation(self, expr, rvs=..., evaluate=..., **kwargs) -> Equality | Relational | Ne | Integral:
        ...
    
    def compute_cdf(self, expr, **kwargs) -> Lambda:
        ...
    
    def compute_characteristic_function(self, expr, **kwargs) -> Lambda:
        ...
    
    def compute_moment_generating_function(self, expr, **kwargs) -> Lambda:
        ...
    
    def compute_density(self, expr, **kwargs) -> Basic | Lambda:
        ...
    
    def compute_quantile(self, expr, **kwargs) -> Lambda:
        ...
    


def reduce_rational_inequalities_wrap(condition, var) -> FiniteSet | Union | None:
    ...

