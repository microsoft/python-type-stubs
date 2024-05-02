from typing import Any

from sympy.core import Basic, Expr, Float
from sympy.printing.codeprinter import CodePrinter

known_functions = ...
class MCodePrinter(CodePrinter):
    printmethod = ...
    language = ...
    _default_settings: dict[str, Any] = ...
    _number_symbols: set[tuple[Expr, Float]] = ...
    _not_supported: set[Basic] = ...
    def __init__(self, settings=...) -> None:
        ...
    
    _print_tuple = ...
    _print_Tuple = ...
    _print_MinMaxBase = ...


def mathematica_code(expr, **settings) -> str | tuple[set[tuple[Any, str]], set[Any], str]:
    ...

