from ... import Column as Column, MetaData as MetaData, Table as Table, cast as cast, util as util
from ...ext.compiler import compiles as compiles
from ...sql import expression as expression
from ...types import Boolean as Boolean, Integer as Integer, String as String, TypeDecorator as TypeDecorator, Unicode as Unicode
from typing import Any

ischema: Any

class CoerceUnicode(TypeDecorator):
    impl: Any = ...
    def process_bind_param(self, value: Any, dialect: Any): ...
    def bind_expression(self, bindvalue: Any): ...

class _cast_on_2005(expression.ColumnElement):
    bindvalue: Any = ...
    def __init__(self, bindvalue: Any) -> None: ...

schemata: Any
tables: Any
columns: Any
constraints: Any
column_constraints: Any
key_constraints: Any
ref_constraints: Any
views: Any
computed_columns: Any
