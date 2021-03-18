# Python: 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
# Library: scipy, version: 1.6.1
# Module: scipy.integrate.lsoda, version: $Revision: $
import typing
import builtins as _mod_builtins

__doc__: str
__file__: str
__name__: str
__package__: str
__version__: bytes
def lsoda() -> typing.Any:
    "y,t,istate = lsoda(f,y,t,tout,rtol,atol,itask,istate,rwork,iwork,jac,jt,[f_extra_args,overwrite_y,jac_extra_args])\n\nWrapper for ``lsoda``.\n\nParameters\n----------\nf : call-back function\ny : input rank-1 array('d') with bounds (neq)\nt : input float\ntout : input float\nrtol : input rank-1 array('d') with bounds (*)\natol : input rank-1 array('d') with bounds (*)\nitask : input int\nistate : input int\nrwork : input rank-1 array('d') with bounds (lrw)\niwork : input rank-1 array('i') with bounds (liw)\njac : call-back function\njt : input int\n\nOther Parameters\n----------------\nf_extra_args : input tuple, optional\n    Default: ()\noverwrite_y : input int, optional\n    Default: 0\njac_extra_args : input tuple, optional\n    Default: ()\n\nReturns\n-------\ny : rank-1 array('d') with bounds (neq)\nt : float\nistate : int\n\nNotes\n-----\nCall-back functions::\n\n  def f(t,y): return ydot\n  Required arguments:\n    t : input float\n    y : input rank-1 array('d') with bounds (n)\n  Return objects:\n    ydot : rank-1 array('d') with bounds (n)\n  def jac(t,y): return jac\n  Required arguments:\n    t : input float\n    y : input rank-1 array('d') with bounds (n)\n  Return objects:\n    jac : rank-2 array('d') with bounds (nrowpd,n)\n"
    ...

def types() -> typing.Any:
    "'i'-scalar\n"
    ...

def __getattr__(name) -> typing.Any:
    ...

