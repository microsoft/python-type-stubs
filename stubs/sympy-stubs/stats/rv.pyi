from functools import singledispatch
from typing import Any, Generator, Literal, Self
from sympy import Equality, FiniteSet, Integral, Ne, Piecewise, ProductSet, Sum
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.function import Lambda
from sympy.core.logic import And
from sympy.core.relational import Relational
from sympy.matrices.expressions.matexpr import MatrixSymbol
from sympy.series.order import Order
from sympy.stats.compound_rv import CompoundPSpace
from sympy.stats.crv import ContinuousPSpace, ProductContinuousDomain
from sympy.stats.drv import DiscretePSpace, ProductDiscreteDomain
from sympy.stats.frv import ConditionalFiniteDomain, FiniteDensity, FinitePSpace, ProductFiniteDomain, ProductFinitePSpace
from sympy.stats.frv_types import BernoulliDistribution
from sympy.stats.joint_rv import JointRandomSymbol
from sympy.stats.stochastic_process import StochasticPSpace
from sympy.stats.symbolic_multivariate_probability import ExpectationMatrix
from sympy.stats.symbolic_probability import Expectation, Probability
from sympy.utilities.decorator import doctest_depends_on

x = ...
@singledispatch
def is_random(x) -> bool:
    ...

@is_random.register(Basic)
def _(x) -> bool:
    ...

class RandomDomain(Basic):
    is_ProductDomain = ...
    is_Finite = ...
    is_Continuous = ...
    is_Discrete = ...
    def __new__(cls, symbols, *args) -> Self:
        ...
    
    @property
    def symbols(self) -> Basic:
        ...
    
    @property
    def set(self) -> Basic:
        ...
    
    def __contains__(self, other):
        ...
    
    def compute_expectation(self, expr):
        ...
    


class SingleDomain(RandomDomain):
    def __new__(cls, symbol, set) -> Self:
        ...
    
    @property
    def symbol(self) -> Basic:
        ...
    
    @property
    def symbols(self) -> FiniteSet:
        ...
    
    def __contains__(self, other) -> bool:
        ...
    


class MatrixDomain(RandomDomain):
    def __new__(cls, symbol, set) -> Self:
        ...
    
    @property
    def symbol(self) -> Basic:
        ...
    
    @property
    def symbols(self) -> FiniteSet:
        ...
    


class ConditionalDomain(RandomDomain):
    def __new__(cls, fulldomain, condition) -> Self:
        ...
    
    @property
    def symbols(self):
        ...
    
    @property
    def fulldomain(self) -> Basic:
        ...
    
    @property
    def condition(self) -> Basic:
        ...
    
    @property
    def set(self):
        ...
    
    def as_boolean(self) -> And:
        ...
    


class PSpace(Basic):
    is_Finite: bool = ...
    is_Continuous: bool = ...
    is_Discrete: bool = ...
    is_real: bool = ...
    @property
    def domain(self) -> Basic:
        ...
    
    @property
    def density(self) -> Basic:
        ...
    
    @property
    def values(self) -> frozenset[RandomSymbol]:
        ...
    
    @property
    def symbols(self):
        ...
    
    def where(self, condition):
        ...
    
    def compute_density(self, expr):
        ...
    
    def sample(self, size=..., library=..., seed=...):
        ...
    
    def probability(self, condition):
        ...
    
    def compute_expectation(self, expr):
        ...
    


class SinglePSpace(PSpace):
    def __new__(cls, s, distribution) -> Self:
        ...
    
    @property
    def value(self) -> RandomSymbol:
        ...
    
    @property
    def symbol(self) -> Basic:
        ...
    
    @property
    def distribution(self) -> Basic:
        ...
    
    @property
    def pdf(self):
        ...
    


class RandomSymbol(Expr):
    def __new__(cls, symbol, pspace=...) -> RandomSymbol | Self:
        ...
    
    is_finite = ...
    is_symbol = ...
    is_Atom = ...
    _diff_wrt = ...
    pspace = ...
    symbol = ...
    name = ...
    @property
    def is_commutative(self) -> Any:
        ...
    
    @property
    def free_symbols(self) -> set[Self]:
        ...
    


class RandomIndexedSymbol(RandomSymbol):
    def __new__(cls, idx_obj, pspace=...) -> Self:
        ...
    
    symbol = ...
    name = ...
    @property
    def key(self) -> Basic | None:
        ...
    
    @property
    def free_symbols(self) -> set[Basic] | set[Self]:
        ...
    
    @property
    def pspace(self) -> Basic:
        ...
    


class RandomMatrixSymbol(RandomSymbol, MatrixSymbol):
    def __new__(cls, symbol, n, m, pspace=...) -> Self:
        ...
    
    symbol = ...
    pspace = ...


class ProductPSpace(PSpace):
    ...


class IndependentProductPSpace(ProductPSpace):
    def __new__(cls, *spaces) -> ProductFinitePSpace | Self:
        ...
    
    @property
    def pdf(self) -> Order | Basic:
        ...
    
    @property
    def rs_space_dict(self) -> dict[Any, Any]:
        ...
    
    @property
    def symbols(self) -> FiniteSet:
        ...
    
    @property
    def spaces(self) -> FiniteSet:
        ...
    
    @property
    def values(self) -> frozenset[Any]:
        ...
    
    def compute_expectation(self, expr, rvs=..., evaluate=..., **kwargs):
        ...
    
    @property
    def domain(self) -> ProductDiscreteDomain | ProductContinuousDomain | ProductFiniteDomain | ProductDomain:
        ...
    
    @property
    def density(self):
        ...
    
    def sample(self, size=..., library=..., seed=...) -> dict[Any, Any]:
        ...
    
    def probability(self, condition, **kwargs) -> Order | Lambda | Probability | Equality | Relational | Ne | int:
        ...
    
    def compute_density(self, expr, **kwargs) -> Lambda:
        ...
    
    def compute_cdf(self, expr, **kwargs):
        ...
    
    def conditional_space(self, condition, normalize=..., **kwargs) -> FinitePSpace | ContinuousPSpace | DiscretePSpace:
        ...
    


class ProductDomain(RandomDomain):
    is_ProductDomain = ...
    def __new__(cls, *domains) -> ProductDiscreteDomain | ProductContinuousDomain | ProductFiniteDomain | Self:
        ...
    
    @property
    def sym_domain_dict(self) -> dict[Any, Basic]:
        ...
    
    @property
    def symbols(self) -> FiniteSet:
        ...
    
    @property
    def domains(self) -> tuple[Basic, ...]:
        ...
    
    @property
    def set(self) -> FiniteSet | ProductSet:
        ...
    
    def __contains__(self, other) -> bool:
        ...
    
    def as_boolean(self) -> And:
        ...
    


def random_symbols(expr) -> list[Any]:
    ...

def pspace(expr) -> Any | CompoundPSpace | StochasticPSpace | ProductFinitePSpace | IndependentProductPSpace:
    ...

def sumsets(sets) -> frozenset[Any]:
    ...

def rs_swap(a, b) -> dict[Any, Any]:
    ...

def given(expr, condition=..., **kwargs) -> Relational | Basic | bool:
    ...

def expectation(expr, condition=..., numsamples=..., evaluate=..., **kwargs) -> Basic | Expectation | tuple[Any, ...] | Sum | Order | Any | Piecewise | Equality | Relational | Ne | Integral | ExpectationMatrix | None:
    ...

def probability(condition, given_condition=..., numsamples=..., evaluate=..., **kwargs) -> Any | BernoulliDistribution | Probability | Equality | Lambda | Order | Relational | Ne | int:
    ...

class Density(Basic):
    expr = ...
    def __new__(cls, expr, condition=...) -> Self:
        ...
    
    @property
    def condition(self) -> Basic | None:
        ...
    
    def doit(self, evaluate=..., **kwargs) -> Density | dict[Any, Any] | Lambda | Basic | Any | FiniteDensity | None:
        ...
    


def density(expr, condition=..., evaluate=..., numsamples=..., **kwargs) -> dict[Any, Any] | Density | Lambda | Basic | Any | FiniteDensity | None:
    ...

def cdf(expr, condition=..., evaluate=..., **kwargs) -> Lambda | Any | dict[Any, Any]:
    ...

def characteristic_function(expr, condition=..., evaluate=..., **kwargs) -> Lambda | Any:
    ...

def moment_generating_function(expr, condition=..., evaluate=..., **kwargs) -> Lambda | Any:
    ...

def where(condition, given_condition=..., **kwargs) -> ConditionalFiniteDomain | Any:
    ...

@doctest_depends_on(modules=('scipy', ))
def sample(expr, condition=..., size=..., library=..., numsamples=..., seed=..., **kwargs) -> list[Any | JointRandomSymbol | Basic] | JointRandomSymbol | Basic:
    ...

def quantile(expr, evaluate=..., **kwargs) -> Lambda | Any:
    ...

def sample_iter(expr, condition=..., size=..., library=..., numsamples=..., seed=..., **kwargs) -> Generator[Any, Any, None] | Generator[Any | JointRandomSymbol | Basic, Any, None]:
    ...

def sample_iter_lambdify(expr, condition=..., size=..., numsamples=..., seed=..., **kwargs) -> Generator[Any, Any, None] | Generator[Any | JointRandomSymbol | Basic, Any, None]:
    ...

def sample_iter_subs(expr, condition=..., size=..., numsamples=..., seed=..., **kwargs) -> Generator[Any, Any, None] | Generator[Any | JointRandomSymbol | Basic, Any, None]:
    ...

def sampling_P(condition, given_condition=..., library=..., numsamples=..., evalf=..., seed=..., **kwargs):
    ...

def sampling_E(expr, given_condition=..., library=..., numsamples=..., evalf=..., seed=..., **kwargs):
    ...

def sampling_density(expr, given_condition=..., library=..., numsamples=..., seed=..., **kwargs) -> dict[Any, Any]:
    ...

def dependent(a, b) -> Any | bool:
    ...

def independent(a, b) -> bool:
    ...

def pspace_independent(a, b) -> bool | None:
    ...

def rv_subs(expr, symbols=...):
    ...

class NamedArgsMixin:
    _argnames: tuple[str, ...] = ...
    def __getattr__(self, attr):
        ...
    


class Distribution(Basic):
    def sample(self, size=..., library=..., seed=...):
        ...
    


def sample_stochastic_process(process):
    ...

