from ast import Attribute
from typing import Self

from sympy.codegen.ast import FunctionCall, Node, String, Token, Variable
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.function import Function
from sympy.core.numbers import Float

pure = ...
elemental = ...
intent_in = ...
intent_out = ...
intent_inout = ...
allocatable = ...

class Program(Token):
    _fields = ...
    _construct_name = String
    _construct_body = ...

class use_rename(Token):
    _fields = ...
    _construct_local = String
    _construct_original = String

class use(Token):
    _fields = ...
    defaults = ...
    _construct_namespace = ...
    _construct_rename = ...
    _construct_only = ...

class Module(Token):
    _fields = ...
    defaults = ...
    _construct_name = String
    _construct_definitions = ...

class Subroutine(Node):
    __slots__ = ...
    _fields = ...
    _construct_name = String
    _construct_parameters = ...

class SubroutineCall(Token):
    _fields = ...
    _construct_name = ...
    _construct_subroutine_args = ...

class Do(Token):
    _fields = ...
    defaults = ...
    _construct_body = ...
    _construct_counter = ...
    _construct_first = ...
    _construct_last = ...
    _construct_step = ...
    _construct_concurrent = ...

class ArrayConstructor(Token):
    _fields = ...
    _construct_elements = ...

class ImpliedDoLoop(Token):
    _fields = ...
    defaults = ...
    _construct_expr = ...
    _construct_counter = ...
    _construct_first = ...
    _construct_last = ...
    _construct_step = ...

class Extent(Basic):
    def __new__(cls, *args) -> Self: ...

assumed_extent = ...

def dimension(*args) -> Attribute: ...

assumed_size = ...

def array(symbol, dim, intent=..., *, attrs=..., value=..., type=...) -> Variable: ...
def allocated(array) -> FunctionCall: ...
def lbound(array, dim=..., kind=...) -> FunctionCall: ...
def ubound(array, dim=..., kind=...) -> FunctionCall: ...
def shape(source, kind=...) -> FunctionCall: ...
def size(array, dim=..., kind=...) -> FunctionCall: ...
def reshape(source, shape, pad=..., order=...) -> FunctionCall: ...
def bind_C(name=...) -> Attribute: ...

class GoTo(Token):
    _fields = ...
    defaults = ...
    _construct_labels = ...
    _construct_expr = ...

class FortranReturn(Token):
    _fields = ...
    defaults = ...
    _construct_return_value = ...

class FFunction(Function):
    _required_standard = ...

class F95Function(FFunction):
    _required_standard = ...

class isign(FFunction):
    nargs = ...

class dsign(FFunction):
    nargs = ...

class cmplx(FFunction):
    nargs = ...

class kind(FFunction):
    nargs = ...

class merge(F95Function):
    nargs = ...

class _literal(Float):
    _token: str = ...
    _decimals: int = ...

class literal_sp(_literal):
    _token = ...
    _decimals = ...

class literal_dp(_literal):
    _token = ...
    _decimals = ...

class sum_(Token, Expr):
    _fields = ...
    defaults = ...
    _construct_array = ...
    _construct_dim = ...

class product_(Token, Expr):
    _fields = ...
    defaults = ...
    _construct_array = ...
    _construct_dim = ...
