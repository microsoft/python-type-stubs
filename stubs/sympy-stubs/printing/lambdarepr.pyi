from typing import Any

from sympy.printing.pycode import MpmathPrinter, PythonCodePrinter

__all__ = ['PythonCodePrinter', 'MpmathPrinter', 'NumPyPrinter', 'LambdaPrinter', 'NumPyPrinter', 'IntervalPrinter', 'lambdarepr']
class LambdaPrinter(PythonCodePrinter):
    printmethod = ...


class NumExprPrinter(LambdaPrinter):
    printmethod = ...
    _numexpr_functions = ...
    module = ...
    def blacklisted(self, expr):
        ...
    
    _print_ImmutableDenseMatrix = ...
    _print_Dict = ...
    def doprint(self, expr) -> str | tuple[set[tuple[Any, str]], set[Any], str]:
        ...
    


class IntervalPrinter(MpmathPrinter, LambdaPrinter):
    ...


def lambdarepr(expr, **settings) -> str | tuple[set[tuple[Any, str]], set[Any], str]:
    ...

