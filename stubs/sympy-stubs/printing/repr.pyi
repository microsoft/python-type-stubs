from typing import Any, LiteralString

from sympy.printing.printer import Printer, print_function

class ReprPrinter(Printer):
    printmethod = ...
    _default_settings: dict[str, Any] = ...
    def reprify(self, args, sep):
        ...
    
    def emptyPrinter(self, expr) -> str | LiteralString:
        ...
    


@print_function(ReprPrinter)
def srepr(expr, **settings) -> str:
    ...

