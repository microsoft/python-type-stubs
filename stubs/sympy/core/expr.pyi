from collections import defaultdict
from typing import TYPE_CHECKING, Any, Literal, Self
from sympy import Derivative, Equality, Integer, Mul, Order, Pow
from sympy.core.basic import Atom, Basic
from sympy.core.evalf import EvalfMixin
from sympy.core.decorators import call_highest_priority, sympify_method_args, sympify_return
from sympy.core.cache import cacheit
from sympy.core.function import UndefinedFunction
from sympy.core.numbers import Float, Number, Rational
from sympy.core.relational import Ne, Relational
from sympy.series.formal import FormalPowerSeries
from sympy.series.fourier import FiniteFourierSeries, FourierSeries
from sympy.tensor.array.array_derivatives import ArrayDerivative

if TYPE_CHECKING:
    ...
@sympify_method_args
class Expr(Basic, EvalfMixin):
    __slots__: tuple[str, ...] = ...
    is_scalar = ...
    @cacheit
    def sort_key(self, order=...) -> tuple[tuple[Literal[5], Literal[0], str] | Any, tuple[int, tuple[tuple[tuple[Literal[5], Literal[0], str], tuple[int, tuple[Any, ...]], Any, Any] | Any | tuple[tuple[Literal[10, 0], Literal[0], str | Any], tuple[int, tuple[Any, ...]] | tuple[Literal[1], tuple[str]], Any, Any], ...]], tuple[tuple[Literal[5], Literal[0], str], tuple[int, tuple[Any, ...]], Any, Any] | Any, Number]:
        ...
    
    _op_priority = ...
    def __pos__(self) -> Self:
        ...
    
    def __neg__(self) -> Mul:
        ...
    
    def __abs__(self) -> Expr:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    @call_highest_priority('__radd__')
    def __add__(self, other) -> Order:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    @call_highest_priority('__add__')
    def __radd__(self, other) -> Order:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    @call_highest_priority('__rsub__')
    def __sub__(self, other) -> Order:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    @call_highest_priority('__sub__')
    def __rsub__(self, other) -> Order:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    @call_highest_priority('__rmul__')
    def __mul__(self, other) -> Order:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    @call_highest_priority('__mul__')
    def __rmul__(self, other) -> Order:
        ...
    
    def __pow__(self, other, mod=...) -> Expr:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    @call_highest_priority('__pow__')
    def __rpow__(self, other) -> Pow:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    @call_highest_priority('__rtruediv__')
    def __truediv__(self, other) -> Pow | Order:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    @call_highest_priority('__truediv__')
    def __rtruediv__(self, other) -> Pow | Order:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    @call_highest_priority('__rmod__')
    def __mod__(self, other) -> type[UndefinedFunction]:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    @call_highest_priority('__mod__')
    def __rmod__(self, other) -> type[UndefinedFunction]:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    @call_highest_priority('__rfloordiv__')
    def __floordiv__(self, other) -> type[UndefinedFunction]:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    @call_highest_priority('__floordiv__')
    def __rfloordiv__(self, other) -> type[UndefinedFunction]:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    @call_highest_priority('__rdivmod__')
    def __divmod__(self, other) -> tuple[type[UndefinedFunction] | Any, type[UndefinedFunction] | Any]:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    @call_highest_priority('__divmod__')
    def __rdivmod__(self, other) -> tuple[type[UndefinedFunction] | Any, type[UndefinedFunction] | Any]:
        ...
    
    def __int__(self) -> int:
        ...
    
    def __float__(self) -> float:
        ...
    
    def __complex__(self) -> complex:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    def __ge__(self, other) -> bool:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    def __le__(self, other) -> bool:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    def __gt__(self, other) -> bool:
        ...
    
    @sympify_return([('other', 'Expr')], NotImplemented)
    def __lt__(self, other) -> bool:
        ...
    
    def __trunc__(self) -> Integer:
        ...
    
    def __format__(self, format_spec: str) -> str:
        ...
    
    @property
    def is_number(self) -> bool:
        ...
    
    def is_constant(self, *wrt, **flags):
        ...
    
    def equals(self, other, failing_expression=...):
        ...
    
    def conjugate(self) -> type[UndefinedFunction]:
        ...
    
    def dir(self, x, cdir):
        ...
    
    def transpose(self) -> type[UndefinedFunction]:
        ...
    
    def adjoint(self) -> type[UndefinedFunction]:
        ...
    
    def as_ordered_factors(self, order=...) -> list[Self]:
        ...
    
    def as_poly(self, *gens, **args) -> Any | None:
        ...
    
    def as_ordered_terms(self, order=..., data=...) -> list[Basic] | tuple[list[Any], list[Any]] | list[Any]:
        ...
    
    def as_terms(self) -> tuple[list[Any], list[Any]]:
        ...
    
    def removeO(self) -> Self:
        ...
    
    def getO(self) -> None:
        ...
    
    def getn(self) -> None:
        ...
    
    def count_ops(self, visual=...):
        ...
    
    def args_cnc(self, cset=..., warn=..., split_1=...) -> list[Any]:
        ...
    
    def coeff(self, x, n=..., right=..., _first=...):
        ...
    
    def as_expr(self, *gens) -> Self:
        ...
    
    def as_coefficient(self, expr) -> None:
        ...
    
    def as_independent(self, *deps, **hint) -> tuple[Expr, Expr]:
        ...
    
    def as_real_imag(self, deep=..., **hints) -> tuple[type[UndefinedFunction] | Any, type[UndefinedFunction] | Any] | None:
        ...
    
    def as_powers_dict(self) -> defaultdict[Any, int]:
        ...
    
    def as_coefficients_dict(self, *syms) -> defaultdict[Any, int]:
        ...
    
    def as_base_exp(self) -> tuple[Expr, Expr]:
        ...
    
    def as_coeff_mul(self, *deps, **kwargs) -> tuple[Expr, tuple[Expr, ...]]:
        ...
    
    def as_coeff_add(self, *deps) -> tuple[Expr, tuple[Expr, ...]]:
        ...
    
    def primitive(self) -> tuple[Any, Any] | tuple[Any | Mul | Number, Any | Mul | Expr]:
        ...
    
    def as_content_primitive(self, radical=..., clear=...) -> tuple[Any, Self]:
        ...
    
    def as_numer_denom(self) -> tuple[Self, Any]:
        ...
    
    def normal(self) -> Self | Mul:
        ...
    
    def extract_multiplicatively(self, c):
        ...
    
    def extract_additively(self, c) -> Self | Order | None:
        ...
    
    @property
    def expr_free_symbols(self) -> set[Any]:
        ...
    
    def could_extract_minus_sign(self) -> Literal[False]:
        ...
    
    def extract_branch_factor(self, allow_half=...) -> tuple[Any, Any]:
        ...
    
    def is_polynomial(self, *syms) -> Literal[True] | None:
        ...
    
    def is_rational_function(self, *syms) -> bool | None:
        ...
    
    def is_meromorphic(self, x, a) -> Literal[True] | None:
        ...
    
    def is_algebraic_expr(self, *syms) -> Literal[True] | None:
        ...
    
    def series(self, x=..., x0=..., n=..., dir=..., logx=..., cdir=...):
        ...
    
    def aseries(self, x=..., n=..., bound=..., hir=...) -> Self:
        ...
    
    def taylor_term(self, n, x, *previous_terms):
        ...
    
    def lseries(self, x=..., x0=..., dir=..., logx=..., cdir=...):
        ...
    
    def nseries(self, x=..., x0=..., n=..., dir=..., logx=..., cdir=...) -> Self:
        ...
    
    def limit(self, x, xlim, dir=...):
        ...
    
    def compute_leading_term(self, x, logx=...) -> Self | Order | Any:
        ...
    
    @cacheit
    def as_leading_term(self, *symbols, logx=..., cdir=...) -> Self:
        ...
    
    def as_coeff_exponent(self, x) -> tuple[Expr, Expr]:
        ...
    
    def leadterm(self, x, logx=..., cdir=...) -> tuple[Any | Expr | Basic, Expr | Any]:
        ...
    
    def as_coeff_Mul(self, rational: bool = ...) -> tuple[Number, Expr]:
        ...
    
    def as_coeff_Add(self, rational=...) -> tuple[Number, Expr]:
        ...
    
    def fps(self, x=..., x0=..., dir=..., hyper=..., order=..., rational=..., full=...) -> FormalPowerSeries:
        ...
    
    def fourier_series(self, limits=...) -> FiniteFourierSeries | FourierSeries:
        ...
    
    def diff(self, *symbols, **assumptions) -> ArrayDerivative | Derivative:
        ...
    
    @cacheit
    def expand(self, deep=..., modulus=..., power_base=..., power_exp=..., mul=..., log=..., multinomial=..., basic=..., **hints) -> Order | Any | Self:
        ...
    
    def integrate(self, *args, **kwargs) -> Equality | Relational | Ne:
        ...
    
    def nsimplify(self, constants=..., tolerance=..., full=...):
        ...
    
    def separate(self, deep=..., force=...):
        ...
    
    def collect(self, syms, func=..., evaluate=..., exact=..., distribute_order_term=...):
        ...
    
    def together(self, *args, **kwargs) -> Any:
        ...
    
    def apart(self, x=..., **args) -> Any:
        ...
    
    def ratsimp(self) -> Any:
        ...
    
    def trigsimp(self, **args) -> Any:
        ...
    
    def radsimp(self, **kwargs):
        ...
    
    def powsimp(self, *args, **kwargs):
        ...
    
    def combsimp(self) -> Any:
        ...
    
    def gammasimp(self) -> Self | Any:
        ...
    
    def factor(self, *gens, **args) -> Any:
        ...
    
    def cancel(self, *gens, **args) -> Any:
        ...
    
    def invert(self, g, *gens, **args) -> int | Any:
        ...
    
    def round(self, n=...) -> Self | Integer | Rational | Float:
        ...
    
    __round__ = ...


class AtomicExpr(Atom, Expr):
    is_number = ...
    is_Atom = ...
    __slots__ = ...
    @property
    def expr_free_symbols(self) -> set[Self]:
        ...
    


class UnevaluatedExpr(Expr):
    def __new__(cls, arg, **kwargs) -> Self:
        ...
    
    def doit(self, **hints) -> Basic:
        ...
    


def unchanged(func, *args):
    ...

class ExprBuilder:
    def __init__(self, op, args=..., validator=..., check=...) -> None:
        ...
    
    def validate(self) -> None:
        ...
    
    def build(self, check=...):
        ...
    
    def append_argument(self, arg, check=...) -> None:
        ...
    
    def __getitem__(self, item) -> Any:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def search_element(self, elem) -> tuple[int] | None:
        ...
    


