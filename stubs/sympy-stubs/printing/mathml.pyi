from typing import Any, Text

from sympy.codegen.ast import Element
from sympy.printing.printer import Printer, print_function

class MathMLPrinterBase(Printer):
    _default_settings: dict[str, Any] = ...
    def __init__(self, settings=...) -> None:
        class RawText(Text):
            ...
        
        
    
    def doprint(self, expr):
        ...
    
    def apply_patch(self) -> None:
        ...
    
    def restore_patch(self) -> None:
        ...
    


class MathMLContentPrinter(MathMLPrinterBase):
    printmethod = ...
    def mathml_tag(self, e) -> str:
        ...
    
    _print_MatrixSymbol = ...
    _print_RandomSymbol = ...
    _print_Implies = ...
    _print_Not = ...
    _print_Xor = ...


class MathMLPresentationPrinter(MathMLPrinterBase):
    printmethod = ...
    def mathml_tag(self, e) -> str:
        ...
    
    def parenthesize(self, item, level, strict=...) -> Element | str:
        ...
    
    _print_RandomSymbol = ...
    _print_Determinant = ...
    _print_frozenset = ...
    _print_BooleanTrue = ...
    _print_BooleanFalse = ...
    _print_Max = ...
    _print_bell = ...


@print_function(MathMLPrinterBase)
def mathml(expr, printer=..., **settings):
    ...

def print_mathml(expr, printer=..., **settings) -> None:
    ...

MathMLPrinter = MathMLContentPrinter
