from functools import _Wrapped
from types import NotImplementedType
from typing import Any, Callable, Iterator, Literal, Self, Tuple
from sympy.combinatorics.galois import S1TransitiveSubgroups, S2TransitiveSubgroups, S3TransitiveSubgroups
from sympy.combinatorics.perm_groups import PermutationGroup
from sympy.core.add import Add
from sympy.core.basic import Basic
from sympy.core.decorators import _sympifyit
from sympy.core.expr import Expr
from sympy.core.function import Derivative
from sympy.core.mul import Mul
from sympy.core.numbers import Integer
from sympy.core.relational import Equality, Ne, Relational
from sympy.series.order import Order
from sympy.utilities import public

def _polifyit(func) -> _Wrapped[..., Any, ..., Any]:
    ...

@public
class Poly(Basic):
    __slots__ = ...
    is_commutative = ...
    is_Poly = ...
    _op_priority = ...
    def __new__(cls, rep, *gens, **args) -> Self:
        ...
    
    @classmethod
    def new(cls, rep, *gens) -> Self:
        ...
    
    @property
    def expr(self) -> Order:
        ...
    
    @property
    def args(self) -> tuple[Any | Order, ...]:
        ...
    
    @classmethod
    def from_dict(cls, rep, *gens, **args) -> Self:
        ...
    
    @classmethod
    def from_list(cls, rep, *gens, **args) -> Self:
        ...
    
    @classmethod
    def from_poly(cls, rep, *gens, **args) -> Self:
        ...
    
    @classmethod
    def from_expr(cls, rep, *gens, **args) -> Self:
        ...
    
    def __hash__(self) -> int:
        ...
    
    @property
    def free_symbols(self) -> set[Any]:
        ...
    
    @property
    def free_symbols_in_domain(self) -> set[Any]:
        ...
    
    @property
    def gen(self):
        ...
    
    @property
    def domain(self):
        ...
    
    @property
    def zero(self) -> Self:
        ...
    
    @property
    def one(self) -> Self:
        ...
    
    @property
    def unit(self) -> Self:
        ...
    
    def unify(f, g) -> tuple[Any | Self, Any | Self]:
        ...
    
    def per(f, rep, gens=..., remove=...) -> Self:
        ...
    
    def set_domain(f, domain) -> Self:
        ...
    
    def get_domain(f):
        ...
    
    def set_modulus(f, modulus) -> Self:
        ...
    
    def get_modulus(f) -> Integer:
        ...
    
    def exclude(f) -> Self:
        ...
    
    def replace(f, x, y=..., **_ignore) -> Self:
        ...
    
    def match(f, *args, **kwargs):
        ...
    
    def reorder(f, *gens, **args) -> Self:
        ...
    
    def ltrim(f, gen) -> Self:
        ...
    
    def has_only_gens(f, *gens) -> bool:
        ...
    
    def to_ring(f) -> Self:
        ...
    
    def to_field(f) -> Self:
        ...
    
    def to_exact(f) -> Self:
        ...
    
    def retract(f, field=...) -> Self:
        ...
    
    def slice(f, x, m, n=...) -> Self:
        ...
    
    def coeffs(f, order=...) -> list[Any]:
        ...
    
    def monoms(f, order=...):
        ...
    
    def terms(f, order=...) -> list[tuple[Any, Any]]:
        ...
    
    def all_coeffs(f) -> list[Any]:
        ...
    
    def all_monoms(f):
        ...
    
    def all_terms(f) -> list[tuple[Any, Any]]:
        ...
    
    def termwise(f, func, *gens, **args) -> Self:
        ...
    
    def length(f) -> int:
        ...
    
    def as_dict(f, native=..., zero=...):
        ...
    
    def as_list(f, native=...):
        ...
    
    def as_expr(f, *gens) -> Order:
        ...
    
    def as_poly(self, *gens, **args) -> Any | None:
        ...
    
    def lift(f) -> Self:
        ...
    
    def deflate(f) -> tuple[Any, Any | Self]:
        ...
    
    def inject(f, front=...) -> Self:
        ...
    
    def eject(f, *gens) -> Self:
        ...
    
    def terms_gcd(f) -> tuple[Any, Any | Self]:
        ...
    
    def add_ground(f, coeff) -> Self:
        ...
    
    def sub_ground(f, coeff) -> Self:
        ...
    
    def mul_ground(f, coeff) -> Self:
        ...
    
    def quo_ground(f, coeff) -> Self:
        ...
    
    def exquo_ground(f, coeff) -> Self:
        ...
    
    def abs(f) -> Self:
        ...
    
    def neg(f) -> Self:
        ...
    
    def add(f, g) -> Self:
        ...
    
    def sub(f, g) -> Self:
        ...
    
    def mul(f, g) -> Self:
        ...
    
    def sqr(f) -> Self:
        ...
    
    def pow(f, n) -> Self:
        ...
    
    def pdiv(f, g) -> tuple[Any | Self, Any | Self]:
        ...
    
    def prem(f, g) -> Self:
        ...
    
    def pquo(f, g) -> Self:
        ...
    
    def pexquo(f, g) -> Self:
        ...
    
    def div(f, g, auto=...) -> tuple[Any | Self, Any | Self]:
        ...
    
    def rem(f, g, auto=...) -> Self:
        ...
    
    def quo(f, g, auto=...) -> Self:
        ...
    
    def exquo(f, g, auto=...) -> Self:
        ...
    
    def degree(f, gen=...):
        ...
    
    def degree_list(f):
        ...
    
    def total_degree(f):
        ...
    
    def homogenize(f, s) -> Self:
        ...
    
    def homogeneous_order(f):
        ...
    
    def LC(f, order=...):
        ...
    
    def TC(f):
        ...
    
    def EC(f, order=...):
        ...
    
    def coeff_monomial(f, monom):
        ...
    
    def nth(f, *N):
        ...
    
    def coeff(f, x, n=..., right=...):
        ...
    
    def LM(f, order=...) -> Any:
        ...
    
    def EM(f, order=...) -> Any:
        ...
    
    def LT(f, order=...) -> tuple[Any, Any]:
        ...
    
    def ET(f, order=...) -> tuple[Any, Any]:
        ...
    
    def max_norm(f):
        ...
    
    def l1_norm(f):
        ...
    
    def clear_denoms(self, convert=...) -> tuple[Any, Self] | tuple[Any, Any | Self]:
        ...
    
    def rat_clear_denoms(self, g) -> tuple[Any | Self, Any | Self]:
        ...
    
    def integrate(self, *specs, **args) -> Self:
        ...
    
    def diff(f, *specs, **kwargs) -> Derivative | Self:
        ...
    
    _eval_derivative = ...
    def eval(self, x, a=..., auto=...) -> Self:
        ...
    
    def __call__(f, *values) -> Self:
        ...
    
    def half_gcdex(f, g, auto=...) -> tuple[Any | Self, Any | Self]:
        ...
    
    def gcdex(f, g, auto=...) -> tuple[Any | Self, Any | Self, Any | Self]:
        ...
    
    def invert(f, g, auto=...) -> Self:
        ...
    
    def revert(f, n) -> Self:
        ...
    
    def subresultants(f, g) -> list[Any | Self]:
        ...
    
    def resultant(f, g, includePRS=...) -> tuple[Any | Self, list[Any | Self]] | Self:
        ...
    
    def discriminant(f) -> Self:
        ...
    
    def dispersionset(f, g=...) -> set[int] | set[Any]:
        ...
    
    def dispersion(f, g=...) -> int:
        ...
    
    def cofactors(f, g) -> tuple[Any | Self, Any | Self, Any | Self]:
        ...
    
    def gcd(f, g) -> Self:
        ...
    
    def lcm(f, g) -> Self:
        ...
    
    def trunc(f, p) -> Self:
        ...
    
    def monic(self, auto=...) -> Self:
        ...
    
    def content(f):
        ...
    
    def primitive(f) -> tuple[Any, Any | Self]:
        ...
    
    def compose(f, g) -> Self:
        ...
    
    def decompose(f) -> list[Any | Self]:
        ...
    
    def shift(f, a) -> Self:
        ...
    
    def transform(f, p, q) -> Self:
        ...
    
    def sturm(self, auto=...) -> list[Any | Self]:
        ...
    
    def gff_list(f) -> list[tuple[Any | Self, Any]]:
        ...
    
    def norm(f) -> Self:
        ...
    
    def sqf_norm(f) -> tuple[Any, Any | Self, Any | Self]:
        ...
    
    def sqf_part(f) -> Self:
        ...
    
    def sqf_list(f, all=...) -> tuple[Any, list[tuple[Any | Self, Any]]]:
        ...
    
    def sqf_list_include(f, all=...) -> list[tuple[Any | Self, Any]]:
        ...
    
    def factor_list(f) -> tuple[Any, list[tuple[Self, Literal[1]]]] | tuple[Any, list[tuple[Any | Self, Any]]]:
        ...
    
    def factor_list_include(f) -> list[tuple[Self, Literal[1]]] | list[tuple[Any | Self, Any]]:
        ...
    
    def intervals(f, all=..., eps=..., inf=..., sup=..., fast=..., sqf=...) -> list[tuple[Any, Any]] | tuple[list[tuple[Any, Any]], list[tuple[Any, Any]]] | list[tuple[tuple[Any, Any], Any]] | tuple[list[tuple[tuple[Any, Any], Any]], list[tuple[tuple[Any, Any], Any]]]:
        ...
    
    def refine_root(f, s, t, eps=..., steps=..., fast=..., check_sqf=...) -> tuple[Any, Any]:
        ...
    
    def count_roots(f, inf=..., sup=...) -> Integer:
        ...
    
    def root(f, index, radicals=...) -> Any:
        ...
    
    def real_roots(f, multiple=..., radicals=...) -> list[list[Any]] | list[tuple[Any, int]]:
        ...
    
    def all_roots(f, multiple=..., radicals=...) -> list[list[Any]] | list[tuple[Any, int]]:
        ...
    
    def nroots(f, n=..., maxsteps=..., cleanup=...) -> list[Any]:
        ...
    
    def ground_roots(f) -> dict[Any, Any]:
        ...
    
    def nth_power_roots_poly(f, n) -> Self:
        ...
    
    def same_root(f, a, b):
        ...
    
    def cancel(f, g, include=...) -> tuple[Any, Any | Self, Any | Self] | tuple[Any | Self, ...]:
        ...
    
    def make_monic_over_integers_by_scaling_roots(f) -> tuple[Self, Any] | tuple[Any | Self, Any]:
        ...
    
    def galois_group(f, by_name=..., max_tries=..., randomize=...) -> tuple[PermutationGroup | Literal[S1TransitiveSubgroups.S1, S2TransitiveSubgroups.S2, S3TransitiveSubgroups.A3, S3TransitiveSubgroups.S3] | None, bool]:
        ...
    
    @property
    def is_zero(f):
        ...
    
    @property
    def is_one(f):
        ...
    
    @property
    def is_sqf(f):
        ...
    
    @property
    def is_monic(f):
        ...
    
    @property
    def is_primitive(f):
        ...
    
    @property
    def is_ground(f):
        ...
    
    @property
    def is_linear(f):
        ...
    
    @property
    def is_quadratic(f):
        ...
    
    @property
    def is_monomial(f):
        ...
    
    @property
    def is_homogeneous(f):
        ...
    
    @property
    def is_irreducible(f):
        ...
    
    @property
    def is_univariate(f) -> bool:
        ...
    
    @property
    def is_multivariate(f) -> bool:
        ...
    
    @property
    def is_cyclotomic(f):
        ...
    
    def __abs__(f) -> Self:
        ...
    
    def __neg__(f) -> Self:
        ...
    
    @_polifyit
    def __add__(f, g) -> Self:
        ...
    
    @_polifyit
    def __radd__(f, g):
        ...
    
    @_polifyit
    def __sub__(f, g) -> Self:
        ...
    
    @_polifyit
    def __rsub__(f, g):
        ...
    
    @_polifyit
    def __mul__(f, g) -> Self:
        ...
    
    @_polifyit
    def __rmul__(f, g):
        ...
    
    @_sympifyit('n', NotImplemented)
    def __pow__(f, n) -> Self | NotImplementedType:
        ...
    
    @_polifyit
    def __divmod__(f, g) -> tuple[Any | Self, Any | Self]:
        ...
    
    @_polifyit
    def __rdivmod__(f, g):
        ...
    
    @_polifyit
    def __mod__(f, g) -> Self:
        ...
    
    @_polifyit
    def __rmod__(f, g):
        ...
    
    @_polifyit
    def __floordiv__(f, g) -> Self:
        ...
    
    @_polifyit
    def __rfloordiv__(f, g):
        ...
    
    @_sympifyit('g', NotImplemented)
    def __truediv__(f, g):
        ...
    
    @_sympifyit('g', NotImplemented)
    def __rtruediv__(f, g):
        ...
    
    @_sympifyit('other', NotImplemented)
    def __eq__(self, other) -> bool:
        ...
    
    @_sympifyit('g', NotImplemented)
    def __ne__(f, g) -> bool:
        ...
    
    def __bool__(f) -> bool:
        ...
    
    def eq(f, g, strict=...) -> Literal[False]:
        ...
    
    def ne(f, g, strict=...) -> bool:
        ...
    


@public
class PurePoly(Poly):
    def __hash__(self) -> int:
        ...
    
    @property
    def free_symbols(self):
        ...
    
    @_sympifyit('other', NotImplemented)
    def __eq__(self, other) -> bool:
        ...
    


@public
def poly_from_expr(expr, *gens, **args) -> tuple[Any, Any]:
    ...

@public
def parallel_poly_from_expr(exprs, *gens, **args) -> tuple[list[Any], Any]:
    ...

@public
def degree(f, gen=...) -> Integer:
    ...

@public
def total_degree(f, *gens) -> Integer:
    ...

@public
def degree_list(f, *gens, **args) -> tuple[Any | Integer, ...]:
    ...

@public
def LC(f, *gens, **args) -> Any:
    ...

@public
def LM(f, *gens, **args) -> Any:
    ...

@public
def LT(f, *gens, **args) -> Any:
    ...

@public
def pdiv(f, g, *gens, **args) -> tuple[Any, Any]:
    ...

@public
def prem(f, g, *gens, **args) -> Any:
    ...

@public
def pquo(f, g, *gens, **args) -> Any:
    ...

@public
def pexquo(f, g, *gens, **args) -> Any:
    ...

@public
def div(f, g, *gens, **args) -> tuple[Any, Any]:
    ...

@public
def rem(f, g, *gens, **args) -> Any:
    ...

@public
def quo(f, g, *gens, **args) -> Any:
    ...

@public
def exquo(f, g, *gens, **args) -> Any:
    ...

@public
def half_gcdex(f, g, *gens, **args) -> tuple[Any, Any]:
    ...

@public
def gcdex(f, g, *gens, **args) -> tuple[Any, Any, Any]:
    ...

@public
def invert(f, g, *gens, **args) -> Any:
    ...

@public
def subresultants(f, g, *gens, **args) -> list[Any] | Any:
    ...

@public
def resultant(f, g, *gens, includePRS=..., **args) -> tuple[Any, list[Any]] | Any | tuple[Any, Any]:
    ...

@public
def discriminant(f, *gens, **args) -> Any:
    ...

@public
def cofactors(f, g, *gens, **args) -> tuple[Any, Any, Any]:
    ...

@public
def gcd_list(seq, *gens, **args) -> Any:
    ...

@public
def gcd(f, g=..., *gens, **args) -> Any:
    ...

@public
def lcm_list(seq, *gens, **args) -> Expr | Any:
    ...

@public
def lcm(f, g=..., *gens, **args) -> Any:
    ...

@public
def terms_gcd(f, *gens, **args) -> Equality | Relational | Ne | Any | Add | Order | Mul:
    ...

@public
def trunc(f, p, *gens, **args) -> Any:
    ...

@public
def monic(f, *gens, **args) -> Any:
    ...

@public
def content(f, *gens, **args) -> Any:
    ...

@public
def primitive(f, *gens, **args) -> tuple[Any, Any]:
    ...

@public
def compose(f, g, *gens, **args) -> Any:
    ...

@public
def decompose(f, *gens, **args) -> list[Any] | Any:
    ...

@public
def sturm(f, *gens, **args) -> list[Any] | Any:
    ...

@public
def gff_list(f, *gens, **args) -> list[tuple[Any, Any]] | Any:
    ...

@public
def gff(f, *gens, **args):
    ...

@public
def sqf_norm(f, *gens, **args) -> tuple[Any | Integer, Any, Any]:
    ...

@public
def sqf_part(f, *gens, **args) -> Any:
    ...

def to_rational_coeffs(f) -> tuple[Any | None, Any, None, Any | None] | tuple[None, None, Any | None, Any] | None:
    ...

@public
def sqf_list(f, *gens, **args) -> tuple[Any, list[tuple[Any, Any]] | list[Any]] | tuple[Any, list[tuple[Any, Any]] | list[Any], list[tuple[Any, Any]] | list[Any]]:
    ...

@public
def sqf(f, *gens, **args) -> Add | Order | Mul:
    ...

@public
def factor_list(f, *gens, **args) -> tuple[Any, list[tuple[Any, Any]] | list[Any]] | tuple[Any, list[tuple[Any, Any]] | list[Any], list[tuple[Any, Any]] | list[Any]]:
    ...

@public
def factor(f, *gens, deep=..., **args) -> Add | Order | Mul | Expr | Any:
    ...

@public
def intervals(F, all=..., eps=..., inf=..., sup=..., strict=..., fast=..., sqf=...) -> list[Any] | Any:
    ...

@public
def refine_root(f, s, t, eps=..., steps=..., fast=..., check_sqf=...) -> Any:
    ...

@public
def count_roots(f, inf=..., sup=...) -> Any:
    ...

@public
def real_roots(f, multiple=...) -> Any:
    ...

@public
def nroots(f, n=..., maxsteps=..., cleanup=...) -> Any:
    ...

@public
def ground_roots(f, *gens, **args) -> Any:
    ...

@public
def nth_power_roots_poly(f, n, *gens, **args) -> Any:
    ...

@public
def cancel(f, *gens, _signsimp=..., **args):
    ...

@public
def reduced(f, G, *gens, **args) -> tuple[list[Any], Any]:
    ...

@public
def groebner(F, *gens, **args) -> Any:
    ...

@public
def is_zero_dimensional(F, *gens, **args) -> Any:
    ...

@public
class GroebnerBasis(Basic):
    def __new__(cls, F, *gens, **args) -> Self:
        ...
    
    @property
    def args(self) -> tuple[Tuple, Tuple]:
        ...
    
    @property
    def exprs(self) -> list[Any]:
        ...
    
    @property
    def polys(self) -> list[Any]:
        ...
    
    @property
    def gens(self):
        ...
    
    @property
    def domain(self):
        ...
    
    @property
    def order(self):
        ...
    
    def __len__(self) -> int:
        ...
    
    def __iter__(self) -> Iterator[Any]:
        ...
    
    def __getitem__(self, item):
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    @property
    def is_zero_dimensional(self) -> bool:
        ...
    
    def fglm(self, order) -> Self:
        ...
    
    def reduce(self, expr, auto=...) -> tuple[list[Any], Any]:
        ...
    
    def contains(self, poly):
        ...
    


@public
def poly(expr, *gens, **args) -> Any:
    ...

def named_poly(n, f, K, name, x, polys):
    ...

