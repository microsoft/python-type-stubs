from ... import exc as exc, log as log, sql as sql, util as util
from ...engine import default as default, reflection as reflection
from ...sql import compiler as compiler, elements as elements
from ...types import BINARY as BINARY, BLOB as BLOB, BOOLEAN as BOOLEAN, DATE as DATE, VARBINARY as VARBINARY
from ...util import topological as topological
from .enumerated import ENUM as ENUM, SET as SET
from .json import JSON as JSON, JSONIndexType as JSONIndexType, JSONPathType as JSONPathType
from .types import BIGINT as BIGINT, BIT as BIT, CHAR as CHAR, DATETIME as DATETIME, DECIMAL as DECIMAL, DOUBLE as DOUBLE, FLOAT as FLOAT, INTEGER as INTEGER, LONGBLOB as LONGBLOB, LONGTEXT as LONGTEXT, MEDIUMBLOB as MEDIUMBLOB, MEDIUMINT as MEDIUMINT, MEDIUMTEXT as MEDIUMTEXT, NCHAR as NCHAR, NUMERIC as NUMERIC, NVARCHAR as NVARCHAR, REAL as REAL, SMALLINT as SMALLINT, TEXT as TEXT, TIME as TIME, TIMESTAMP as TIMESTAMP, TINYBLOB as TINYBLOB, TINYINT as TINYINT, TINYTEXT as TINYTEXT, VARCHAR as VARCHAR, YEAR as YEAR
from sqlalchemy import literal_column as literal_column
from sqlalchemy.sql import visitors as visitors
from typing import Any, Optional

RESERVED_WORDS: Any
AUTOCOMMIT_RE: Any
SET_RE: Any
MSTime = TIME
MSSet = SET
MSEnum = ENUM
MSLongBlob = LONGBLOB
MSMediumBlob = MEDIUMBLOB
MSTinyBlob = TINYBLOB
MSBlob = BLOB
MSBinary = BINARY
MSVarBinary = VARBINARY
MSNChar = NCHAR
MSNVarChar = NVARCHAR
MSChar = CHAR
MSString = VARCHAR
MSLongText = LONGTEXT
MSMediumText = MEDIUMTEXT
MSTinyText = TINYTEXT
MSText = TEXT
MSYear = YEAR
MSTimeStamp = TIMESTAMP
MSBit = BIT
MSSmallInteger = SMALLINT
MSTinyInteger = TINYINT
MSMediumInteger = MEDIUMINT
MSBigInteger = BIGINT
MSNumeric = NUMERIC
MSDecimal = DECIMAL
MSDouble = DOUBLE
MSReal = REAL
MSFloat = FLOAT
MSInteger = INTEGER
colspecs: Any
ischema_names: Any

class MySQLExecutionContext(default.DefaultExecutionContext):
    def should_autocommit_text(self, statement: Any): ...
    def create_server_side_cursor(self): ...

class MySQLCompiler(compiler.SQLCompiler):
    render_table_with_column_in_update_from: bool = ...
    extract_map: Any = ...
    def visit_random_func(self, fn: Any, **kw: Any): ...
    def visit_sysdate_func(self, fn: Any, **kw: Any): ...
    def visit_json_getitem_op_binary(self, binary: Any, operator: Any, **kw: Any): ...
    def visit_json_path_getitem_op_binary(self, binary: Any, operator: Any, **kw: Any): ...
    def visit_on_duplicate_key_update(self, on_duplicate: Any, **kw: Any): ...
    def visit_concat_op_binary(self, binary: Any, operator: Any, **kw: Any): ...
    def visit_match_op_binary(self, binary: Any, operator: Any, **kw: Any): ...
    def get_from_hint_text(self, table: Any, text: Any): ...
    def visit_typeclause(self, typeclause: Any, type_: Optional[Any] = ..., **kw: Any): ...
    def visit_cast(self, cast: Any, **kw: Any): ...
    def render_literal_value(self, value: Any, type_: Any): ...
    def visit_true(self, element: Any, **kw: Any): ...
    def visit_false(self, element: Any, **kw: Any): ...
    def get_select_precolumns(self, select: Any, **kw: Any): ...
    def visit_join(self, join: Any, asfrom: bool = ..., **kwargs: Any): ...
    def for_update_clause(self, select: Any, **kw: Any): ...
    def limit_clause(self, select: Any, **kw: Any): ...
    def update_limit_clause(self, update_stmt: Any): ...
    def update_tables_clause(self, update_stmt: Any, from_table: Any, extra_froms: Any, **kw: Any): ...
    def update_from_clause(self, update_stmt: Any, from_table: Any, extra_froms: Any, from_hints: Any, **kw: Any) -> None: ...
    def delete_table_clause(self, delete_stmt: Any, from_table: Any, extra_froms: Any): ...
    def delete_extra_from_clause(self, delete_stmt: Any, from_table: Any, extra_froms: Any, from_hints: Any, **kw: Any): ...
    def visit_empty_set_expr(self, element_types: Any): ...
    def visit_is_distinct_from_binary(self, binary: Any, operator: Any, **kw: Any): ...
    def visit_isnot_distinct_from_binary(self, binary: Any, operator: Any, **kw: Any): ...

class MySQLDDLCompiler(compiler.DDLCompiler):
    def get_column_specification(self, column: Any, **kw: Any): ...
    def post_create_table(self, table: Any): ...
    def visit_create_index(self, create: Any, **kw: Any): ...
    def visit_primary_key_constraint(self, constraint: Any): ...
    def visit_drop_index(self, drop: Any): ...
    def visit_drop_constraint(self, drop: Any): ...
    def define_constraint_match(self, constraint: Any): ...
    def visit_set_table_comment(self, create: Any): ...
    def visit_drop_table_comment(self, create: Any): ...
    def visit_set_column_comment(self, create: Any): ...

class MySQLTypeCompiler(compiler.GenericTypeCompiler):
    def visit_NUMERIC(self, type_: Any, **kw: Any): ...
    def visit_DECIMAL(self, type_: Any, **kw: Any): ...
    def visit_DOUBLE(self, type_: Any, **kw: Any): ...
    def visit_REAL(self, type_: Any, **kw: Any): ...
    def visit_FLOAT(self, type_: Any, **kw: Any): ...
    def visit_INTEGER(self, type_: Any, **kw: Any): ...
    def visit_BIGINT(self, type_: Any, **kw: Any): ...
    def visit_MEDIUMINT(self, type_: Any, **kw: Any): ...
    def visit_TINYINT(self, type_: Any, **kw: Any): ...
    def visit_SMALLINT(self, type_: Any, **kw: Any): ...
    def visit_BIT(self, type_: Any, **kw: Any): ...
    def visit_DATETIME(self, type_: Any, **kw: Any): ...
    def visit_DATE(self, type_: Any, **kw: Any): ...
    def visit_TIME(self, type_: Any, **kw: Any): ...
    def visit_TIMESTAMP(self, type_: Any, **kw: Any): ...
    def visit_YEAR(self, type_: Any, **kw: Any): ...
    def visit_TEXT(self, type_: Any, **kw: Any): ...
    def visit_TINYTEXT(self, type_: Any, **kw: Any): ...
    def visit_MEDIUMTEXT(self, type_: Any, **kw: Any): ...
    def visit_LONGTEXT(self, type_: Any, **kw: Any): ...
    def visit_VARCHAR(self, type_: Any, **kw: Any): ...
    def visit_CHAR(self, type_: Any, **kw: Any): ...
    def visit_NVARCHAR(self, type_: Any, **kw: Any): ...
    def visit_NCHAR(self, type_: Any, **kw: Any): ...
    def visit_VARBINARY(self, type_: Any, **kw: Any): ...
    def visit_JSON(self, type_: Any, **kw: Any): ...
    def visit_large_binary(self, type_: Any, **kw: Any): ...
    def visit_enum(self, type_: Any, **kw: Any): ...
    def visit_BLOB(self, type_: Any, **kw: Any): ...
    def visit_TINYBLOB(self, type_: Any, **kw: Any): ...
    def visit_MEDIUMBLOB(self, type_: Any, **kw: Any): ...
    def visit_LONGBLOB(self, type_: Any, **kw: Any): ...
    def visit_ENUM(self, type_: Any, **kw: Any): ...
    def visit_SET(self, type_: Any, **kw: Any): ...
    def visit_BOOLEAN(self, type_: Any, **kw: Any): ...

class MySQLIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words: Any = ...
    def __init__(self, dialect: Any, server_ansiquotes: bool = ..., **kw: Any) -> None: ...

class MySQLDialect(default.DefaultDialect):
    name: str = ...
    supports_alter: bool = ...
    supports_native_boolean: bool = ...
    max_identifier_length: int = ...
    max_index_name_length: int = ...
    supports_native_enum: bool = ...
    supports_for_update_of: bool = ...
    supports_sane_rowcount: bool = ...
    supports_sane_multi_rowcount: bool = ...
    supports_multivalues_insert: bool = ...
    supports_comments: bool = ...
    inline_comments: bool = ...
    default_paramstyle: str = ...
    colspecs: Any = ...
    cte_follows_insert: bool = ...
    statement_compiler: Any = ...
    ddl_compiler: Any = ...
    type_compiler: Any = ...
    ischema_names: Any = ...
    preparer: Any = ...
    construct_arguments: Any = ...
    isolation_level: Any = ...
    def __init__(self, isolation_level: Optional[Any] = ..., json_serializer: Optional[Any] = ..., json_deserializer: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def on_connect(self): ...
    def set_isolation_level(self, connection: Any, level: Any) -> None: ...
    def get_isolation_level(self, connection: Any): ...
    def do_commit(self, dbapi_connection: Any) -> None: ...
    def do_rollback(self, dbapi_connection: Any) -> None: ...
    def do_begin_twophase(self, connection: Any, xid: Any) -> None: ...
    def do_prepare_twophase(self, connection: Any, xid: Any) -> None: ...
    def do_rollback_twophase(self, connection: Any, xid: Any, is_prepared: bool = ..., recover: bool = ...) -> None: ...
    def do_commit_twophase(self, connection: Any, xid: Any, is_prepared: bool = ..., recover: bool = ...) -> None: ...
    def do_recover_twophase(self, connection: Any): ...
    def is_disconnect(self, e: Any, connection: Any, cursor: Any): ...
    def has_table(self, connection: Any, table_name: Any, schema: Optional[Any] = ...): ...
    identifier_preparer: Any = ...
    def initialize(self, connection: Any) -> None: ...
    def get_schema_names(self, connection: Any, **kw: Any): ...
    def get_table_names(self, connection: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_view_names(self, connection: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_table_options(self, connection: Any, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_columns(self, connection: Any, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_pk_constraint(self, connection: Any, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_foreign_keys(self, connection: Any, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_check_constraints(self, connection: Any, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_table_comment(self, connection: Any, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_indexes(self, connection: Any, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_unique_constraints(self, connection: Any, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_view_definition(self, connection: Any, view_name: Any, schema: Optional[Any] = ..., **kw: Any): ...

class _DecodingRowProxy:
    rowproxy: Any = ...
    charset: Any = ...
    def __init__(self, rowproxy: Any, charset: Any) -> None: ...
    def __getitem__(self, index: Any): ...
    def __getattr__(self, attr: Any): ...
