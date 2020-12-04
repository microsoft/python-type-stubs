from . import interfaces as interfaces, reflection as reflection, result as result
from .. import event as event, exc as exc, pool as pool, processors as processors, types as sqltypes, util as util
from ..sql import compiler as compiler, expression as expression, schema as schema
from ..sql.elements import quoted_name as quoted_name
from typing import Any, Optional

AUTOCOMMIT_REGEXP: Any
SERVER_SIDE_CURSOR_RE: Any

class DefaultDialect(interfaces.Dialect):
    statement_compiler: Any = ...
    ddl_compiler: Any = ...
    type_compiler: Any = ...
    preparer: Any = ...
    supports_alter: bool = ...
    supports_comments: bool = ...
    inline_comments: bool = ...
    default_sequence_base: int = ...
    execute_sequence_format: Any = ...
    supports_views: bool = ...
    supports_sequences: bool = ...
    sequences_optional: bool = ...
    preexecute_autoincrement_sequences: bool = ...
    postfetch_lastrowid: bool = ...
    implicit_returning: bool = ...
    supports_right_nested_joins: bool = ...
    cte_follows_insert: bool = ...
    supports_native_enum: bool = ...
    supports_native_boolean: bool = ...
    non_native_boolean_check_constraint: bool = ...
    supports_simple_order_by_label: bool = ...
    tuple_in_values: bool = ...
    engine_config_types: Any = ...
    supports_native_decimal: bool = ...
    supports_unicode_statements: bool = ...
    supports_unicode_binds: bool = ...
    returns_unicode_strings: bool = ...
    description_encoding: Any = ...
    name: str = ...
    max_identifier_length: int = ...
    max_index_name_length: Any = ...
    supports_sane_rowcount: bool = ...
    supports_sane_multi_rowcount: bool = ...
    colspecs: Any = ...
    default_paramstyle: str = ...
    supports_default_values: bool = ...
    supports_empty_insert: bool = ...
    supports_multivalues_insert: bool = ...
    supports_is_distinct_from: bool = ...
    supports_server_side_cursors: bool = ...
    supports_for_update_of: bool = ...
    server_version_info: Any = ...
    construct_arguments: Any = ...
    requires_name_normalize: bool = ...
    reflection_options: Any = ...
    dbapi_exception_translation_map: Any = ...
    convert_unicode: Any = ...
    encoding: Any = ...
    positional: bool = ...
    dbapi: Any = ...
    paramstyle: Any = ...
    identifier_preparer: Any = ...
    case_sensitive: Any = ...
    empty_in_strategy: Any = ...
    label_length: Any = ...
    def __init__(self, convert_unicode: bool = ..., encoding: str = ..., paramstyle: Optional[Any] = ..., dbapi: Optional[Any] = ..., implicit_returning: Optional[Any] = ..., supports_right_nested_joins: Optional[Any] = ..., case_sensitive: bool = ..., supports_native_boolean: Optional[Any] = ..., empty_in_strategy: str = ..., max_identifier_length: Optional[Any] = ..., label_length: Optional[Any] = ..., **kwargs: Any) -> None: ...
    @property
    def dialect_description(self): ...
    @property
    def supports_sane_rowcount_returning(self): ...
    @classmethod
    def get_pool_class(cls, url: Any): ...
    @classmethod
    def load_provisioning(cls) -> None: ...
    default_schema_name: Any = ...
    default_isolation_level: Any = ...
    def initialize(self, connection: Any) -> None: ...
    def on_connect(self) -> None: ...
    def type_descriptor(self, typeobj: Any): ...
    def reflecttable(self, connection: Any, table: Any, include_columns: Any, exclude_columns: Any, resolve_fks: Any, **opts: Any): ...
    def get_pk_constraint(self, conn: Any, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def validate_identifier(self, ident: Any) -> None: ...
    def connect(self, *cargs: Any, **cparams: Any): ...
    def create_connect_args(self, url: Any): ...
    def set_engine_execution_options(self, engine: Any, opts: Any) -> None: ...
    def set_connection_execution_options(self, connection: Any, opts: Any) -> None: ...
    def do_begin(self, dbapi_connection: Any) -> None: ...
    def do_rollback(self, dbapi_connection: Any) -> None: ...
    def do_commit(self, dbapi_connection: Any) -> None: ...
    def do_close(self, dbapi_connection: Any) -> None: ...
    def do_ping(self, dbapi_connection: Any): ...
    def create_xid(self): ...
    def do_savepoint(self, connection: Any, name: Any) -> None: ...
    def do_rollback_to_savepoint(self, connection: Any, name: Any) -> None: ...
    def do_release_savepoint(self, connection: Any, name: Any) -> None: ...
    def do_executemany(self, cursor: Any, statement: Any, parameters: Any, context: Optional[Any] = ...) -> None: ...
    def do_execute(self, cursor: Any, statement: Any, parameters: Any, context: Optional[Any] = ...) -> None: ...
    def do_execute_no_params(self, cursor: Any, statement: Any, context: Optional[Any] = ...) -> None: ...
    def is_disconnect(self, e: Any, connection: Any, cursor: Any): ...
    def reset_isolation_level(self, dbapi_conn: Any) -> None: ...
    def normalize_name(self, name: Any): ...
    def denormalize_name(self, name: Any): ...

class _RendersLiteral:
    def literal_processor(self, dialect: Any): ...

class _StrDateTime(_RendersLiteral, sqltypes.DateTime): ...
class _StrDate(_RendersLiteral, sqltypes.Date): ...
class _StrTime(_RendersLiteral, sqltypes.Time): ...

class StrCompileDialect(DefaultDialect):
    statement_compiler: Any = ...
    ddl_compiler: Any = ...
    type_compiler: Any = ...
    preparer: Any = ...
    supports_sequences: bool = ...
    sequences_optional: bool = ...
    preexecute_autoincrement_sequences: bool = ...
    implicit_returning: bool = ...
    supports_native_boolean: bool = ...
    supports_simple_order_by_label: bool = ...
    colspecs: Any = ...

class DefaultExecutionContext(interfaces.ExecutionContext):
    isinsert: bool = ...
    isupdate: bool = ...
    isdelete: bool = ...
    is_crud: bool = ...
    is_text: bool = ...
    isddl: bool = ...
    executemany: bool = ...
    compiled: Any = ...
    statement: Any = ...
    result_column_struct: Any = ...
    returned_defaults: Any = ...
    def engine(self): ...
    def postfetch_cols(self): ...
    def prefetch_cols(self): ...
    def returning_cols(self) -> None: ...
    def no_parameters(self): ...
    def should_autocommit(self): ...
    @property
    def connection(self): ...
    def should_autocommit_text(self, statement: Any): ...
    def create_cursor(self): ...
    def create_server_side_cursor(self) -> None: ...
    def pre_exec(self) -> None: ...
    def post_exec(self) -> None: ...
    def get_result_processor(self, type_: Any, colname: Any, coltype: Any): ...
    def get_lastrowid(self): ...
    def handle_dbapi_exception(self, e: Any) -> None: ...
    def get_result_proxy(self): ...
    @property
    def rowcount(self): ...
    def supports_sane_rowcount(self): ...
    def supports_sane_multi_rowcount(self): ...
    def lastrow_has_defaults(self): ...
    def set_input_sizes(self, translate: Optional[Any] = ..., include_types: Optional[Any] = ..., exclude_types: Optional[Any] = ...) -> None: ...
    current_parameters: Any = ...
    def get_current_parameters(self, isolate_multiinsert_groups: bool = ...): ...
    def get_insert_default(self, column: Any): ...
    def get_update_default(self, column: Any): ...
