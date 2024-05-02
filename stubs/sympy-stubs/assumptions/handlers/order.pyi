from typing import Literal
from sympy.core import Add, Basic, Expr, Mul, Pow
from sympy.core.numbers import ImaginaryUnit, NaN
from sympy.functions import Abs, acos, acot, asin, atan, exp, factorial, log
from sympy.matrices import Determinant, Trace
from sympy.matrices.expressions.matexpr import MatrixElement
from sympy.assumptions.predicates.order import ExtendedNegativePredicate, ExtendedNonNegativePredicate, ExtendedNonPositivePredicate, ExtendedNonZeroPredicate, ExtendedPositivePredicate, NegativePredicate, NonNegativePredicate, NonPositivePredicate, NonZeroPredicate, PositivePredicate, ZeroPredicate

@NegativePredicate.register(Basic)
def _(expr, assumptions) -> Literal[False] | None:
    ...

@NegativePredicate.register(Expr)
def _(expr, assumptions):
    ...

@NegativePredicate.register(Add)
def _(expr, assumptions) -> bool | None:
    ...

@NegativePredicate.register(Mul)
def _(expr, assumptions) -> bool | None:
    ...

@NegativePredicate.register(Pow)
def _(expr, assumptions) -> bool | None:
    ...

@NegativePredicate.register_many(Abs, ImaginaryUnit)
def _(expr, assumptions) -> Literal[False]:
    ...

@NegativePredicate.register(exp)
def _(expr, assumptions) -> Literal[False]:
    ...

@NonNegativePredicate.register(Basic)
def _(expr, assumptions) -> bool | None:
    ...

@NonNegativePredicate.register(Expr)
def _(expr, assumptions):
    ...

@NonZeroPredicate.register(Expr)
def _(expr, assumptions):
    ...

@NonZeroPredicate.register(Basic)
def _(expr, assumptions) -> bool | None:
    ...

@NonZeroPredicate.register(Add)
def _(expr, assumptions) -> Literal[True] | None:
    ...

@NonZeroPredicate.register(Mul)
def _(expr, assumptions) -> bool | None:
    ...

@NonZeroPredicate.register(Pow)
def _(expr, assumptions) -> bool | None:
    ...

@NonZeroPredicate.register(Abs)
def _(expr, assumptions) -> bool | None:
    ...

@NonZeroPredicate.register(NaN)
def _(expr, assumptions) -> None:
    ...

@ZeroPredicate.register(Expr)
def _(expr, assumptions):
    ...

@ZeroPredicate.register(Basic)
def _(expr, assumptions) -> bool | None:
    ...

@ZeroPredicate.register(Mul)
def _(expr, assumptions) -> bool | None:
    ...

@NonPositivePredicate.register(Expr)
def _(expr, assumptions):
    ...

@NonPositivePredicate.register(Basic)
def _(expr, assumptions) -> bool | None:
    ...

@PositivePredicate.register(Expr)
def _(expr, assumptions):
    ...

@PositivePredicate.register(Basic)
def _(expr, assumptions) -> Literal[False] | None:
    ...

@PositivePredicate.register(Mul)
def _(expr, assumptions) -> bool | None:
    ...

@PositivePredicate.register(Add)
def _(expr, assumptions) -> bool | None:
    ...

@PositivePredicate.register(Pow)
def _(expr, assumptions) -> bool | None:
    ...

@PositivePredicate.register(exp)
def _(expr, assumptions) -> bool | None:
    ...

@PositivePredicate.register(log)
def _(expr, assumptions) -> bool | None:
    ...

@PositivePredicate.register(factorial)
def _(expr, assumptions) -> Literal[True] | None:
    ...

@PositivePredicate.register(ImaginaryUnit)
def _(expr, assumptions) -> Literal[False]:
    ...

@PositivePredicate.register(Abs)
def _(expr, assumptions) -> bool | None:
    ...

@PositivePredicate.register(Trace)
def _(expr, assumptions) -> Literal[True] | None:
    ...

@PositivePredicate.register(Determinant)
def _(expr, assumptions) -> Literal[True] | None:
    ...

@PositivePredicate.register(MatrixElement)
def _(expr, assumptions) -> Literal[True] | None:
    ...

@PositivePredicate.register(atan)
def _(expr, assumptions) -> bool | None:
    ...

@PositivePredicate.register(asin)
def _(expr, assumptions) -> bool | None:
    ...

@PositivePredicate.register(acos)
def _(expr, assumptions) -> Literal[True] | None:
    ...

@PositivePredicate.register(acot)
def _(expr, assumptions) -> bool | None:
    ...

@PositivePredicate.register(NaN)
def _(expr, assumptions) -> None:
    ...

@ExtendedNegativePredicate.register(object)
def _(expr, assumptions) -> bool | None:
    ...

@ExtendedPositivePredicate.register(object)
def _(expr, assumptions) -> bool | None:
    ...

@ExtendedNonZeroPredicate.register(object)
def _(expr, assumptions) -> bool | None:
    ...

@ExtendedNonPositivePredicate.register(object)
def _(expr, assumptions) -> bool | None:
    ...

@ExtendedNonNegativePredicate.register(object)
def _(expr, assumptions) -> bool | None:
    ...

