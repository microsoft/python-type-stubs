# Python: 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
# Library: scipy, version: 1.6.1
# Module: scipy.stats.statlib, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def gscale() -> typing.Any:
    "astart,a1,ifault = gscale(test,other)\n\nWrapper for ``gscale``.\n\nParameters\n----------\ntest : input int\nother : input int\n\nReturns\n-------\nastart : float\na1 : rank-1 array('f') with bounds (l1)\nifault : int\n"
    ...

def prho() -> typing.Any:
    'ifault = prho(n,is)\n\nWrapper for ``prho``.\n\nParameters\n----------\nn : input int\nis : input int\n\nReturns\n-------\nprho : float\nifault : int\n'
    ...

def swilk() -> typing.Any:
    "a,w,pw,ifault = swilk(x,a,[init,n1])\n\nWrapper for ``swilk``.\n\nParameters\n----------\nx : input rank-1 array('f') with bounds (n)\na : input rank-1 array('f') with bounds (n2)\n\nOther Parameters\n----------------\ninit : input int, optional\n    Default: 0\nn1 : input int, optional\n    Default: n\n\nReturns\n-------\na : rank-1 array('f') with bounds (n2)\nw : float\npw : float\nifault : int\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

