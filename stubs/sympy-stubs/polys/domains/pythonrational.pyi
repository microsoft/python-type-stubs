from sympy.core.numbers import Integer, Rational
from sympy.external.pythonmpq import PythonMPQ

PythonRational = PythonMPQ

def sympify_pythonrational(arg) -> Rational | Integer: ...
