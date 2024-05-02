from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict as tDict,
    List,
    Optional,
    Self,
    Tuple as tTuple,
    Type,
    Union as tUnion,
    overload,
)

from mpmath import mpc, mpf
from sympy.concrete.products import Product
from sympy.concrete.summations import Sum
from sympy.core.add import Add
from sympy.core.expr import Expr
from sympy.core.mul import Mul
from sympy.core.numbers import AlgebraicNumber, Float, Integer, Number, Rational
from sympy.core.power import Pow
from sympy.core.symbol import Symbol
from sympy.functions.elementary.complexes import Abs, im, re
from sympy.functions.elementary.exponential import exp, log
from sympy.functions.elementary.integers import ceiling, floor
from sympy.functions.elementary.trigonometric import atan
from sympy.integrals.integrals import Integral

if TYPE_CHECKING:
    ...
LG10 = ...
rnd = ...
def bitcount(n):
    ...

INF = ...
MINUS_INF = ...
DEFAULT_MAXPREC = ...
class PrecisionExhausted(ArithmeticError):
    ...


MPF_TUP = tTuple[int, int, int, int]
TMP_RES = Any
OPT_DICT = tDict[str, Any]
def fastlog(x: Optional[MPF_TUP]) -> tUnion[int, Any]:
    ...

def pure_complex(v: Expr, or_real=...) -> tuple[Number, Number] | None:
    ...

SCALED_ZERO_TUP = tTuple[List[int], int, int, int]
@overload
def scaled_zero(mag: SCALED_ZERO_TUP, sign=...) -> MPF_TUP:
    ...

@overload
def scaled_zero(mag: int, sign=...) -> tTuple[SCALED_ZERO_TUP, int]:
    ...

def scaled_zero(mag: tUnion[SCALED_ZERO_TUP, int], sign=...) -> tUnion[MPF_TUP, tTuple[SCALED_ZERO_TUP, int]]:
    ...

def iszero(mpf: tUnion[MPF_TUP, SCALED_ZERO_TUP, None], scaled=...) -> Optional[bool]:
    ...

def complex_accuracy(result: TMP_RES) -> tUnion[int, Any]:
    ...

def get_abs(expr: Expr, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def get_complex_part(expr: Expr, no: int, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def evalf_abs(expr: Abs, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def evalf_re(expr: re, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def evalf_im(expr: im, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def finalize_complex(re: MPF_TUP, im: MPF_TUP, prec: int) -> TMP_RES:
    ...

def chop_parts(value: TMP_RES, prec: int) -> TMP_RES:
    ...

def check_target(expr: Expr, result: TMP_RES, prec: int) -> None:
    ...

def get_integer_part(expr: Expr, no: int, options: OPT_DICT, return_ints=...) -> tUnion[TMP_RES, tTuple[int, int]]:
    ...

def evalf_ceiling(expr: ceiling, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def evalf_floor(expr: floor, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def evalf_float(expr: Float, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def evalf_rational(expr: Rational, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def evalf_integer(expr: Integer, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def add_terms(terms: list, prec: int, target_prec: int) -> tTuple[tUnion[MPF_TUP, SCALED_ZERO_TUP, None], Optional[int]]:
    ...

def evalf_add(v: Add, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def evalf_mul(v: Mul, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def evalf_pow(v: Pow, prec: int, options) -> TMP_RES:
    ...

def evalf_exp(expr: exp, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def evalf_trig(v: Expr, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def evalf_log(expr: log, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def evalf_atan(v: atan, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def evalf_subs(prec: int, subs: dict) -> dict:
    ...

def evalf_piecewise(expr: Expr, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def evalf_alg_num(a: AlgebraicNumber, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def as_mpmath(x: Any, prec: int, options: OPT_DICT) -> tUnion[mpc, mpf]:
    ...

def do_integral(expr: Integral, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def evalf_integral(expr: Integral, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def check_convergence(numer: Expr, denom: Expr, n: Symbol) -> tTuple[int, Any, Any]:
    ...

def hypsum(expr: Expr, n: Symbol, start: int, prec: int) -> mpf:
    ...

def evalf_prod(expr: Product, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def evalf_sum(expr: Sum, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def evalf_symbol(x: Expr, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

evalf_table: tDict[Type[Expr], Callable[[Expr, int, OPT_DICT], TMP_RES]] = ...
def evalf(x: Expr, prec: int, options: OPT_DICT) -> TMP_RES:
    ...

def quad_to_mpmath(q, ctx=...):
    ...

class EvalfMixin:
    __slots__: tTuple[str, ...] = ...
    def evalf(self, n=..., subs=..., maxn=..., chop=..., strict=..., quad=..., verbose=...) -> Self | EvalfMixin | TMP_RES | Float:
        ...
    
    n = ...


def N(x, n=..., **options):
    ...

