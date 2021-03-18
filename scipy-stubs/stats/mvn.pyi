# Python: 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
# Library: scipy, version: 1.6.1
# Module: scipy.stats.mvn, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def dkblck() -> typing.Any:
    "'i'-scalar\n"
    ...

def mvndst() -> typing.Any:
    "error,value,inform = mvndst(lower,upper,infin,correl,[maxpts,abseps,releps])\n\nWrapper for ``mvndst``.\n\nParameters\n----------\nlower : input rank-1 array('d') with bounds (n)\nupper : input rank-1 array('d') with bounds (n)\ninfin : input rank-1 array('i') with bounds (n)\ncorrel : input rank-1 array('d') with bounds (n*(n-1)/2)\n\nOther Parameters\n----------------\nmaxpts : input int, optional\n    Default: 2000\nabseps : input float, optional\n    Default: 1e-06\nreleps : input float, optional\n    Default: 1e-06\n\nReturns\n-------\nerror : float\nvalue : float\ninform : int\n"
    ...

def mvnun() -> typing.Any:
    "value,inform = mvnun(lower,upper,means,covar,[maxpts,abseps,releps])\n\nWrapper for ``mvnun``.\n\nParameters\n----------\nlower : input rank-1 array('d') with bounds (d)\nupper : input rank-1 array('d') with bounds (d)\nmeans : input rank-2 array('d') with bounds (d,n)\ncovar : input rank-2 array('d') with bounds (d,d)\n\nOther Parameters\n----------------\nmaxpts : input int, optional\n    Default: d*1000\nabseps : input float, optional\n    Default: 1e-06\nreleps : input float, optional\n    Default: 1e-06\n\nReturns\n-------\nvalue : float\ninform : int\n"
    ...

def mvnun_weighted() -> typing.Any:
    "value,inform = mvnun_weighted(lower,upper,means,weights,covar,[maxpts,abseps,releps])\n\nWrapper for ``mvnun_weighted``.\n\nParameters\n----------\nlower : input rank-1 array('d') with bounds (d)\nupper : input rank-1 array('d') with bounds (d)\nmeans : input rank-2 array('d') with bounds (d,n)\nweights : input rank-1 array('d') with bounds (n)\ncovar : input rank-2 array('d') with bounds (d,d)\n\nOther Parameters\n----------------\nmaxpts : input int, optional\n    Default: d*1000\nabseps : input float, optional\n    Default: 1e-06\nreleps : input float, optional\n    Default: 1e-06\n\nReturns\n-------\nvalue : float\ninform : int\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

