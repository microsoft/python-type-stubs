from pathlib import Path
from sympy.utilities.decorator import doctest_depends_on

__doctest_requires__ = ...
def add_mathml_headers(s):
    ...

@doctest_depends_on(modules=('lxml', ))
def apply_xsl(mml, xsl) -> str:
    ...

@doctest_depends_on(modules=('lxml', ))
def c2p(mml, simple=...) -> str:
    ...

