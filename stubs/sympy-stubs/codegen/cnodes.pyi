from typing_extensions import Self

from sympy.codegen.ast import Attribute as _Attribute, FunctionCall, Node, String, Token, Type as _Type
from sympy.core.basic import Basic

void: _Type
restrict: _Attribute
volatile: _Attribute
static: _Attribute

def alignof(arg) -> FunctionCall: ...
def sizeof(arg) -> FunctionCall: ...

class CommaOperator(Basic):
    def __new__(cls, *args) -> Self: ...

class Label(Node):
    _fields = ...
    defaults = ...
    _construct_name = String

class goto(Token):
    _fields = ...
    _construct_label = Label

class PreDecrement(Basic):
    nargs = ...

class PostDecrement(Basic):
    nargs = ...

class PreIncrement(Basic):
    nargs = ...

class PostIncrement(Basic):
    nargs = ...

class struct(Node):
    _fields = ...
    defaults = ...
    _construct_name = String

class union(struct):
    __slots__ = ...
