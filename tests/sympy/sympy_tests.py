from typing import Any
from typing_extensions import assert_type

import numpy as np
from sympy import (
    Add,
    And,
    Basic,
    Catalan,
    E,
    EmptySequence,
    EmptySet,
    Expr,
    I,
    Integers,
    Lambda,
    MatAdd,
    MatMul,
    Mul,
    Naturals0,
    Or,
    Pow,
    S,
    Symbol,
    false,
    nan,
    oo,
    pi,
    true,
    zoo,
)
from sympy.codegen.ast import Attribute, FloatType, SignedIntType, float64, int32, pointer_const
from sympy.codegen.fnodes import intent_in
from sympy.combinatorics import cube
from sympy.combinatorics.polyhedron import Polyhedron
from sympy.core import pi as core_pi
from sympy.core.containers import Tuple
from sympy.core.decorators import _sympifyit, call_highest_priority, sympify_method_args, sympify_return
from sympy.core.numbers import (
    Catalan as CatalanNumber,
    ComplexInfinity,
    Exp1,
    Float,
    ImaginaryUnit,
    Infinity,
    Integer,
    NaN,
    Pi,
    Rational,
)
from sympy.core.singleton import SingletonRegistry
from sympy.functions.elementary.complexes import Abs, im, re
from sympy.functions.elementary.exponential import log
from sympy.functions.elementary.integers import RoundFunction, ceiling, floor, frac
from sympy.functions.elementary.trigonometric import atan
from sympy.logic.boolalg import Boolean, BooleanFalse, BooleanTrue
from sympy.matrices.expressions.matexpr import MatrixExpr
from sympy.matrices.expressions.special import GenericIdentity, GenericZeroMatrix
from sympy.physics.units import kilo
from sympy.physics.units.prefixes import PREFIXES, Prefix
from sympy.physics.units.unitsystem import UnitSystem
from sympy.polys.domains.gaussiandomains import GaussianRational, GaussianRationalField
from sympy.polys.domains.pythonrational import PythonRational
from sympy.polys.monomials import MonomialOps
from sympy.polys.polyclasses import ANP, DMP
from sympy.series.sequences import EmptySequence as EmptySequenceType
from sympy.sets.fancysets import Integers as IntegersType, Naturals0 as Naturals0Type
from sympy.sets.sets import EmptySet as EmptySetType, FiniteSet, Interval
from sympy.stats.crv_types import BetaDistribution
from sympy.utilities.decorator import public

assert_type(S, SingletonRegistry)
assert_type(pi, Pi)
assert_type(core_pi, Pi)
assert_type(E, Exp1)
assert_type(I, ImaginaryUnit)
assert_type(oo, Infinity)
assert_type(zoo, ComplexInfinity)
assert_type(nan, NaN)
assert_type(Catalan, CatalanNumber)
assert_type(true, BooleanTrue)
assert_type(false, BooleanFalse)
assert_type(EmptySet, EmptySetType)
assert_type(EmptySequence, EmptySequenceType)
assert_type(Integers, IntegersType)
assert_type(Naturals0, Naturals0Type)
assert_type(And.identity, BooleanTrue)
assert_type(And.zero, BooleanFalse)
assert_type(Or.identity, BooleanFalse)
assert_type(Or.zero, BooleanTrue)
assert_type(And.nargs, FiniteSet | Naturals0Type)
assert_type(MatAdd.identity, GenericZeroMatrix)
assert_type(MatMul.identity, GenericIdentity)
assert_type(kilo, Prefix)
assert_type(PREFIXES["k"], Prefix)
assert_type(pointer_const, Attribute)
assert_type(intent_in, Attribute)
assert_type(float64, FloatType)
assert_type(int32, SignedIntType)
assert_type(cube, Polyhedron)
assert_type(BetaDistribution.set, Interval)
assert_type(GaussianRationalField.zero, GaussianRational)
assert_type(GaussianRationalField.one, GaussianRational)
assert_type(GaussianRationalField.imag_unit, GaussianRational)
assert_type(MonomialOps(2), MonomialOps)
assert_type(BooleanTrue(), BooleanTrue)
assert_type(BooleanFalse(), BooleanFalse)


def check_methods(
    basic: Basic,
    add: Add,
    mul: Mul,
    power: Pow,
    symbol: Symbol,
    polyhedron: Polyhedron,
    matrix: MatrixExpr,
    rational: Rational,
    elements: Tuple,
    units: UnitSystem,
) -> None:
    assert_type(basic.is_real, bool | None)
    assert_type(basic.is_commutative, bool | None)
    assert_type(add.args, tuple[Expr, ...])
    assert_type(mul.args, tuple[Expr, ...])
    assert_type(power.args, tuple[Expr, Expr])
    assert_type(symbol.binary_symbols, set[Symbol])
    assert_type(polyhedron.vertices, tuple[Any, ...] | Basic)
    assert_type(rational.__radd__(rational), Rational | Integer | Float)
    assert_type(elements.__rmul__(2), Tuple)
    assert_type(units.get_dimensional_expr(basic), Expr)
    assert_type(matrix.__array__(dtype=object, copy=True), np.ndarray[Any, np.dtype[np.object_]])
    basic.subs(arg1={symbol: pi})
    basic.subs(arg1=symbol, arg2=pi)
    PythonRational(1, 2)
    DMP([1, 0], object())
    ANP([1], [1, 0, 1], object())


def check_read_only(basic: Basic, add: Add, mul: Mul, power: Pow, rounded: RoundFunction) -> None:
    basic.is_real = True  # type: ignore[misc]
    basic.is_commutative = False  # type: ignore[misc]
    add.args = ()  # type: ignore[misc]
    mul.args = ()  # type: ignore[misc]
    power.args = (pi, pi)  # type: ignore[misc]
    rounded.args = (pi,)  # type: ignore[misc]


def check_expression_properties(
    absolute: Abs, real: re, imaginary: im, logarithm: log, arctangent: atan, function: Lambda, boolean: Boolean
) -> None:
    assert_type(absolute.args, tuple[Expr])
    assert_type(real.args, tuple[Expr])
    assert_type(imaginary.args, tuple[Expr])
    assert_type(logarithm.args, tuple[Expr])
    assert_type(arctangent.args, tuple[Expr])
    assert_type(function.bound_symbols, tuple[Any, ...])
    boolean.__rand__(true)
    boolean.__ror__(false)
    boolean.__rxor__(true)
    boolean.__rlshift__(false)
    boolean.__rrshift__(true)
    rounded: list[Expr] = [floor(pi), ceiling(pi), frac(pi)]
    assert_type(rounded, list[Expr])


@call_highest_priority("__radd__")
def priority_method(left: Rational, right: Rational) -> Rational:
    return left


@_sympifyit("right", NotImplemented)
def sympified_method(left: Rational, right: Rational) -> Rational:
    return left


@sympify_method_args
class Sympified:
    @sympify_return([("other", "Sympified")], NotImplemented)
    def method(self, other: "Sympified") -> int:
        return 1


assert_type(priority_method(Integer(1), Integer(2)), Rational)
assert_type(sympified_method(Integer(1), Integer(2)), Rational)
assert_type(Sympified().method(Sympified()), int)
assert_type(public(priority_method)(Integer(1), Integer(2)), Rational)
assert_type(public(Sympified)().method(Sympified()), int)
