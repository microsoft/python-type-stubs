from sympy.core.basic import Basic
from sympy.core.symbol import Dummy as _Dummy

def powsimp(expr, deep=..., combine=..., force=..., measure=...): ...
def powdenest(eq, force=..., polar=...) -> bool | Basic: ...

_y: _Dummy
