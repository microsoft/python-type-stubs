from sympy import Symbol
from sympy.core.evalf import evalf
from sympy.core.power import Pow
from sympy.simplify.powsimp import powsimp
from sympy.simplify.simplify import simplify

x = Symbol("x")  # type: ignore[no-untyped-call]
power = Pow(x, 2)
result = simplify(powsimp(x))  # type: ignore[no-untyped-call]
evalf(result, 53, {})
