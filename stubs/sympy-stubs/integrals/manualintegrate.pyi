from typing import Any, Callable, NamedTuple, Sequence, Type
from abc import ABC, abstractmethod
from dataclasses import dataclass
from sympy.core.cache import cacheit
from sympy.core.expr import Expr
from sympy.core.function import Derivative, UndefinedFunction
from sympy.core.relational import Boolean
from sympy.core.symbol import Symbol, Wild
from sympy.functions.elementary.exponential import exp
from sympy.functions.elementary.piecewise import Piecewise
from sympy.tensor.array.array_derivatives import ArrayDerivative

@dataclass
class Rule(ABC):
    integrand: Expr
    variable: Symbol
    @abstractmethod
    def eval(self) -> Expr:
        ...
    
    @abstractmethod
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class AtomicRule(Rule, ABC):
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class ConstantRule(AtomicRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class ConstantTimesRule(Rule):
    constant: Expr
    other: Expr
    substep: Rule
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class PowerRule(AtomicRule):
    base: Expr
    exp: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class NestedPowRule(AtomicRule):
    base: Expr
    exp: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class AddRule(Rule):
    substeps: list[Rule]
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class URule(Rule):
    u_var: Symbol
    u_func: Expr
    substep: Rule
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class PartsRule(Rule):
    u: Symbol
    dv: Expr
    v_step: Rule
    second_step: Rule | None
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class CyclicPartsRule(Rule):
    parts_rules: list[PartsRule]
    coefficient: Expr
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class TrigRule(AtomicRule, ABC):
    ...


@dataclass
class SinRule(TrigRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class CosRule(TrigRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class SecTanRule(TrigRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class CscCotRule(TrigRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class Sec2Rule(TrigRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class Csc2Rule(TrigRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class HyperbolicRule(AtomicRule, ABC):
    ...


@dataclass
class SinhRule(HyperbolicRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class CoshRule(HyperbolicRule):
    def eval(self) -> type[UndefinedFunction]:
        ...
    


@dataclass
class ExpRule(AtomicRule):
    base: Expr
    exp: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class ReciprocalRule(AtomicRule):
    base: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class ArcsinRule(AtomicRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class ArcsinhRule(AtomicRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class ReciprocalSqrtQuadraticRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class SqrtQuadraticDenomRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    coeffs: list[Expr]
    def eval(self) -> Expr:
        ...
    


@dataclass
class SqrtQuadraticRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class AlternativeRule(Rule):
    alternatives: list[Rule]
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class DontKnowRule(Rule):
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class DerivativeRule(AtomicRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class RewriteRule(Rule):
    rewritten: Expr
    substep: Rule
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class CompleteSquareRule(RewriteRule):
    ...


@dataclass
class PiecewiseRule(Rule):
    subfunctions: Sequence[tuple[Rule, bool | Boolean]]
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class HeavisideRule(Rule):
    harg: Expr
    ibnd: Expr
    substep: Rule
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class DiracDeltaRule(AtomicRule):
    n: Expr
    a: Expr
    b: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class TrigSubstitutionRule(Rule):
    theta: Expr
    func: Expr
    rewritten: Expr
    substep: Rule
    restriction: bool | Boolean
    def eval(self) -> Expr:
        ...
    
    def contains_dont_know(self) -> bool:
        ...
    


@dataclass
class ArctanRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class OrthogonalPolyRule(AtomicRule, ABC):
    n: Expr
    ...


@dataclass
class JacobiRule(OrthogonalPolyRule):
    a: Expr
    b: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class GegenbauerRule(OrthogonalPolyRule):
    a: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class ChebyshevTRule(OrthogonalPolyRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class ChebyshevURule(OrthogonalPolyRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class LegendreRule(OrthogonalPolyRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class HermiteRule(OrthogonalPolyRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class LaguerreRule(OrthogonalPolyRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class AssocLaguerreRule(OrthogonalPolyRule):
    a: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class IRule(AtomicRule, ABC):
    a: Expr
    b: Expr
    ...


@dataclass
class CiRule(IRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class ChiRule(IRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class EiRule(IRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class SiRule(IRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class ShiRule(IRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class LiRule(IRule):
    def eval(self) -> Expr:
        ...
    


@dataclass
class ErfRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class FresnelCRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class FresnelSRule(AtomicRule):
    a: Expr
    b: Expr
    c: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class PolylogRule(AtomicRule):
    a: Expr
    b: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class UpperGammaRule(AtomicRule):
    a: Expr
    e: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class EllipticFRule(AtomicRule):
    a: Expr
    d: Expr
    def eval(self) -> Expr:
        ...
    


@dataclass
class EllipticERule(AtomicRule):
    a: Expr
    d: Expr
    def eval(self) -> Expr:
        ...
    


class IntegralInfo(NamedTuple):
    integrand: Expr
    symbol: Symbol
    ...


def manual_diff(f, symbol) -> int | ArrayDerivative | Derivative:
    ...

def manual_subs(expr, *args):
    ...

inverse_trig_functions = ...
def find_substitutions(integrand, symbol, u_var) -> list[Any]:
    ...

def rewriter(condition, rewrite) -> Callable[..., RewriteRule | None]:
    ...

def proxy_rewriter(condition, rewrite) -> Callable[..., RewriteRule | None]:
    ...

def multiplexer(conditions) -> Callable[..., Any | None]:
    ...

def alternatives(*rules) -> Callable[..., Any | AlternativeRule | None]:
    ...

def constant_rule(integral) -> ConstantRule:
    ...

def power_rule(integral) -> ReciprocalRule | PowerRule | ExpRule | ConstantRule | PiecewiseRule | None:
    ...

def exp_rule(integral) -> ExpRule | None:
    ...

def orthogonal_poly_rule(integral) -> None:
    ...

_special_function_patterns: list[tuple[Type, Expr, Callable | None, tuple]] = ...
_wilds = ...
_symbol = ...
def special_function_rule(integral) -> None:
    ...

def nested_pow_rule(integral: IntegralInfo) -> Rule | None:
    class NoMatch(Exception):
        ...
    
    

def inverse_trig_rule(integral: IntegralInfo, degenerate=...) -> NestedPowRule | Rule | None:
    ...

def add_rule(integral) -> AddRule | None:
    ...

def mul_rule(integral: IntegralInfo) -> ConstantTimesRule | None:
    ...

def parts_rule(integral) -> ConstantTimesRule | CyclicPartsRule | PartsRule | None:
    ...

def trig_rule(integral) -> SinRule | CosRule | Sec2Rule | Csc2Rule | RewriteRule | None:
    ...

def trig_product_rule(integral: IntegralInfo) -> SecTanRule | CscCotRule | None:
    ...

def quadratic_denom_rule(integral) -> ArctanRule | RewriteRule | PiecewiseRule | URule | ConstantTimesRule | None:
    ...

def sqrt_linear_rule(integral: IntegralInfo) -> PiecewiseRule | URule | None:
    ...

def sqrt_quadratic_rule(integral: IntegralInfo, degenerate=...) -> Rule | None:
    ...

def hyperbolic_rule(integral: tuple[Expr, Symbol]) -> SinhRule | CoshRule | RewriteRule | None:
    ...

@cacheit
def make_wilds(symbol) -> tuple[Wild, Wild, Wild, Wild]:
    ...

@cacheit
def sincos_pattern(symbol) -> tuple[Any, Wild, Wild, Wild, Wild]:
    ...

@cacheit
def tansec_pattern(symbol) -> tuple[Any, Wild, Wild, Wild, Wild]:
    ...

@cacheit
def cotcsc_pattern(symbol) -> tuple[Any, Wild, Wild, Wild, Wild]:
    ...

@cacheit
def heaviside_pattern(symbol) -> tuple[Any, Wild, Wild, Wild]:
    ...

def uncurry(func) -> Callable[..., Any]:
    ...

def trig_rewriter(rewrite) -> Callable[..., RewriteRule | None]:
    ...

sincos_botheven_condition = ...
sincos_botheven = ...
sincos_sinodd_condition = ...
sincos_sinodd = ...
sincos_cosodd_condition = ...
sincos_cosodd = ...
tansec_seceven_condition = ...
tansec_seceven = ...
tansec_tanodd_condition = ...
tansec_tanodd = ...
tan_tansquared_condition = ...
tan_tansquared = ...
cotcsc_csceven_condition = ...
cotcsc_csceven = ...
cotcsc_cotodd_condition = ...
cotcsc_cotodd = ...
def trig_sincos_rule(integral) -> None:
    ...

def trig_tansec_rule(integral) -> None:
    ...

def trig_cotcsc_rule(integral) -> None:
    ...

def trig_sindouble_rule(integral) -> DontKnowRule | tuple[Any, Any] | Rule | None:
    ...

def trig_powers_products_rule(integral) -> DontKnowRule | Rule | tuple[Any, Any]:
    ...

def trig_substitution_rule(integral) -> TrigSubstitutionRule | None:
    ...

def heaviside_rule(integral) -> HeavisideRule | None:
    ...

def dirac_delta_rule(integral: IntegralInfo) -> Rule | None:
    ...

def substitution_rule(integral) -> AlternativeRule | None:
    ...

partial_fractions_rule = ...
cancel_rule = ...
distribute_expand_rule = ...
trig_expand_rule = ...
def derivative_rule(integral) -> DerivativeRule | DontKnowRule | ConstantRule:
    ...

def rewrites_rule(integral) -> RewriteRule | None:
    ...

def fallback_rule(integral) -> DontKnowRule:
    ...

_integral_cache: dict[Expr, Expr | None] = ...
_parts_u_cache: dict[Expr, int] = ...
_cache_dummy = ...
def integral_steps(integrand, symbol, **options) -> DontKnowRule | tuple[Any, Any] | Rule:
    ...

def manualintegrate(f, var) -> Piecewise | Expr:
    ...

