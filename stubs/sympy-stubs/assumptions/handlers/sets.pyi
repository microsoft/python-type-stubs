from typing import Literal
from sympy.core import Add, Basic, Expr, Mul, Pow
from sympy.core.numbers import AlgebraicNumber, ComplexInfinity, Exp1, Float, GoldenRatio, ImaginaryUnit, Infinity, Integer, NaN, NegativeInfinity, Number, NumberSymbol, Pi, Rational, TribonacciConstant
from sympy.functions import Abs, acos, acot, asin, atan, cos, cot, exp, im, log, re, sin, tan
from sympy.matrices import Determinant, MatrixBase, Trace
from sympy.matrices.expressions.matexpr import MatrixElement
from sympy.assumptions.predicates.sets import AlgebraicPredicate, AntihermitianPredicate, ComplexPredicate, ExtendedRealPredicate, HermitianPredicate, ImaginaryPredicate, IntegerPredicate, IrrationalPredicate, RationalPredicate, RealPredicate

@IntegerPredicate.register_many(int, Integer)
def _(expr, assumptions) -> Literal[True]:
    ...

@IntegerPredicate.register_many(Exp1, GoldenRatio, ImaginaryUnit, Infinity, NegativeInfinity, Pi, Rational, TribonacciConstant)
def _(expr, assumptions) -> Literal[False]:
    ...

@IntegerPredicate.register(Expr)
def _(expr, assumptions):
    ...

@IntegerPredicate.register_many(Add, Pow)
def _(expr, assumptions) -> bool | None:
    ...

@IntegerPredicate.register(Mul)
def _(expr, assumptions) -> bool | None:
    ...

@IntegerPredicate.register(Abs)
def _(expr, assumptions) -> bool | None:
    ...

@IntegerPredicate.register_many(Determinant, MatrixElement, Trace)
def _(expr, assumptions) -> bool | None:
    ...

@RationalPredicate.register(Rational)
def _(expr, assumptions) -> Literal[True]:
    ...

@RationalPredicate.register(Float)
def _(expr, assumptions) -> None:
    ...

@RationalPredicate.register_many(Exp1, GoldenRatio, ImaginaryUnit, Infinity, NegativeInfinity, Pi, TribonacciConstant)
def _(expr, assumptions) -> Literal[False]:
    ...

@RationalPredicate.register(Expr)
def _(expr, assumptions):
    ...

@RationalPredicate.register_many(Add, Mul)
def _(expr, assumptions) -> bool | None:
    ...

@RationalPredicate.register(Pow)
def _(expr, assumptions) -> bool | None:
    ...

@RationalPredicate.register_many(asin, atan, cos, sin, tan)
def _(expr, assumptions) -> bool | None:
    ...

@RationalPredicate.register(exp)
def _(expr, assumptions) -> bool | None:
    ...

@RationalPredicate.register_many(acot, cot)
def _(expr, assumptions) -> Literal[False] | None:
    ...

@RationalPredicate.register_many(acos, log)
def _(expr, assumptions) -> bool | None:
    ...

@IrrationalPredicate.register(Expr)
def _(expr, assumptions):
    ...

@IrrationalPredicate.register(Basic)
def _(expr, assumptions) -> bool | None:
    ...

@RealPredicate.register_many(Abs, Exp1, Float, GoldenRatio, im, Pi, Rational, re, TribonacciConstant)
def _(expr, assumptions) -> Literal[True]:
    ...

@RealPredicate.register_many(ImaginaryUnit, Infinity, NegativeInfinity)
def _(expr, assumptions) -> Literal[False]:
    ...

@RealPredicate.register(Expr)
def _(expr, assumptions):
    ...

@RealPredicate.register(Add)
def _(expr, assumptions) -> bool | None:
    ...

@RealPredicate.register(Mul)
def _(expr, assumptions) -> bool | None:
    ...

@RealPredicate.register(Pow)
def _(expr, assumptions) -> bool | None:
    ...

@RealPredicate.register_many(cos, sin)
def _(expr, assumptions) -> Literal[True] | None:
    ...

@RealPredicate.register(exp)
def _(expr, assumptions) -> bool | None:
    ...

@RealPredicate.register(log)
def _(expr, assumptions) -> bool | None:
    ...

@RealPredicate.register_many(Determinant, MatrixElement, Trace)
def _(expr, assumptions) -> bool | None:
    ...

@ExtendedRealPredicate.register(object)
def _(expr, assumptions) -> bool | None:
    ...

@ExtendedRealPredicate.register_many(Infinity, NegativeInfinity)
def _(expr, assumptions) -> Literal[True]:
    ...

@ExtendedRealPredicate.register_many(Add, Mul, Pow)
def _(expr, assumptions) -> bool | None:
    ...

@HermitianPredicate.register(object)
def _(expr, assumptions) -> bool | None:
    ...

@HermitianPredicate.register(Add)
def _(expr, assumptions) -> bool | None:
    ...

@HermitianPredicate.register(Mul)
def _(expr, assumptions) -> bool | None:
    ...

@HermitianPredicate.register(Pow)
def _(expr, assumptions) -> Literal[True]:
    ...

@HermitianPredicate.register_many(cos, sin)
def _(expr, assumptions) -> Literal[True]:
    ...

@HermitianPredicate.register(exp)
def _(expr, assumptions) -> Literal[True]:
    ...

@HermitianPredicate.register(MatrixBase)
def _(mat, assumptions) -> bool:
    ...

@ComplexPredicate.register_many(Abs, cos, exp, im, ImaginaryUnit, log, Number, NumberSymbol, re, sin)
def _(expr, assumptions) -> Literal[True]:
    ...

@ComplexPredicate.register_many(Infinity, NegativeInfinity)
def _(expr, assumptions) -> Literal[False]:
    ...

@ComplexPredicate.register(Expr)
def _(expr, assumptions):
    ...

@ComplexPredicate.register_many(Add, Mul)
def _(expr, assumptions) -> bool | None:
    ...

@ComplexPredicate.register(Pow)
def _(expr, assumptions) -> bool | None:
    ...

@ComplexPredicate.register_many(Determinant, MatrixElement, Trace)
def _(expr, assumptions) -> bool | None:
    ...

@ComplexPredicate.register(NaN)
def _(expr, assumptions) -> None:
    ...

@ImaginaryPredicate.register(ImaginaryUnit)
def _(expr, assumptions) -> Literal[True]:
    ...

@ImaginaryPredicate.register(Expr)
def _(expr, assumptions):
    ...

@ImaginaryPredicate.register(Add)
def _(expr, assumptions) -> bool | None:
    ...

@ImaginaryPredicate.register(Mul)
def _(expr, assumptions) -> bool | None:
    ...

@ImaginaryPredicate.register(Pow)
def _(expr, assumptions) -> bool | None:
    ...

@ImaginaryPredicate.register(log)
def _(expr, assumptions) -> bool | None:
    ...

@ImaginaryPredicate.register(exp)
def _(expr, assumptions) -> bool | None:
    ...

@ImaginaryPredicate.register_many(Number, NumberSymbol)
def _(expr, assumptions) -> bool:
    ...

@ImaginaryPredicate.register(NaN)
def _(expr, assumptions) -> None:
    ...

@AntihermitianPredicate.register(object)
def _(expr, assumptions) -> bool | None:
    ...

@AntihermitianPredicate.register(Add)
def _(expr, assumptions) -> bool | None:
    ...

@AntihermitianPredicate.register(Mul)
def _(expr, assumptions) -> bool | None:
    ...

@AntihermitianPredicate.register(Pow)
def _(expr, assumptions) -> bool:
    ...

@AntihermitianPredicate.register(MatrixBase)
def _(mat, assumptions) -> bool:
    ...

@AlgebraicPredicate.register_many(AlgebraicNumber, Float, GoldenRatio, ImaginaryUnit, TribonacciConstant)
def _(expr, assumptions) -> Literal[True]:
    ...

@AlgebraicPredicate.register_many(ComplexInfinity, Exp1, Infinity, NegativeInfinity, Pi)
def _(expr, assumptions) -> Literal[False]:
    ...

@AlgebraicPredicate.register_many(Add, Mul)
def _(expr, assumptions) -> bool | None:
    ...

@AlgebraicPredicate.register(Pow)
def _(expr, assumptions) -> bool | None:
    ...

@AlgebraicPredicate.register(Rational)
def _(expr, assumptions):
    ...

@AlgebraicPredicate.register_many(asin, atan, cos, sin, tan)
def _(expr, assumptions) -> bool | None:
    ...

@AlgebraicPredicate.register(exp)
def _(expr, assumptions) -> bool | None:
    ...

@AlgebraicPredicate.register_many(acot, cot)
def _(expr, assumptions) -> Literal[False] | None:
    ...

@AlgebraicPredicate.register_many(acos, log)
def _(expr, assumptions) -> bool | None:
    ...

