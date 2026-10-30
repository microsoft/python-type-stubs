from typing import Any, Literal
from typing_extensions import Self

from sympy.core.expr import Expr

class Prefix(Expr):
    _op_priority = ...
    is_commutative = ...
    def __new__(cls, name, abbrev, exponent, base=..., latex_repr=...) -> Self: ...
    @property
    def name(self): ...
    @property
    def abbrev(self): ...
    @property
    def scale_factor(self): ...
    @property
    def base(self): ...
    def __mul__(self, other) -> Prefix | Literal[1]: ...
    def __truediv__(self, other) -> Prefix | Literal[1]: ...
    def __rtruediv__(self, other) -> Prefix: ...

def prefix_unit(unit, prefixes) -> list[Any]: ...

yotta: Prefix
zetta: Prefix
exa: Prefix
peta: Prefix
tera: Prefix
giga: Prefix
mega: Prefix
kilo: Prefix
hecto: Prefix
deca: Prefix
deci: Prefix
centi: Prefix
milli: Prefix
micro: Prefix
nano: Prefix
pico: Prefix
femto: Prefix
atto: Prefix
zepto: Prefix
yocto: Prefix
PREFIXES: dict[str, Prefix]
kibi: Prefix
mebi: Prefix
gibi: Prefix
tebi: Prefix
pebi: Prefix
exbi: Prefix
BIN_PREFIXES: dict[str, Prefix]
