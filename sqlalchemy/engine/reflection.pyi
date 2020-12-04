from .. import exc as exc, inspection as inspection, sql as sql, util as util
from ..sql import operators as operators
from ..sql.type_api import TypeEngine as TypeEngine
from ..util import deprecated as deprecated, topological as topological
from .base import Connectable as Connectable
from typing import Any, Optional

def cache(fn: Any, self: Any, con: Any, *args: Any, **kw: Any): ...

class Inspector:
    bind: Any = ...
    engine: Any = ...
    dialect: Any = ...
    info_cache: Any = ...
    def __init__(self, bind: Any) -> None: ...
    @classmethod
    def from_engine(cls, bind: Any): ...
    @property
    def default_schema_name(self): ...
    def get_schema_names(self): ...
    def get_table_names(self, schema: Optional[Any] = ..., order_by: Optional[Any] = ...): ...
    def get_sorted_table_and_fkc_names(self, schema: Optional[Any] = ...): ...
    def get_temp_table_names(self): ...
    def get_temp_view_names(self): ...
    def get_table_options(self, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_view_names(self, schema: Optional[Any] = ...): ...
    def get_view_definition(self, view_name: Any, schema: Optional[Any] = ...): ...
    def get_columns(self, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_primary_keys(self, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_pk_constraint(self, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_foreign_keys(self, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_indexes(self, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_unique_constraints(self, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_table_comment(self, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_check_constraints(self, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def reflecttable(self, table: Any, include_columns: Any, exclude_columns: Any = ..., resolve_fks: bool = ..., _extend_on: Optional[Any] = ...) -> None: ...