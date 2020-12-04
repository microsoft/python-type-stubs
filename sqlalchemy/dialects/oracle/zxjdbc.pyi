from ... import sql as sql, types as sqltypes, util as util
from ...connectors.zxJDBC import ZxJDBCConnector as ZxJDBCConnector
from ...engine import result as _result
from ...sql import expression as expression
from .base import OracleCompiler as OracleCompiler, OracleDialect as OracleDialect, OracleExecutionContext as OracleExecutionContext
from typing import Any

SQLException: Any
zxJDBC: Any

class _ZxJDBCDate(sqltypes.Date):
    def result_processor(self, dialect: Any, coltype: Any): ...

class _ZxJDBCNumeric(sqltypes.Numeric):
    def result_processor(self, dialect: Any, coltype: Any): ...

class OracleCompiler_zxjdbc(OracleCompiler):
    returning_cols: Any = ...
    returning_parameters: Any = ...
    def returning_clause(self, stmt: Any, returning_cols: Any): ...

class OracleExecutionContext_zxjdbc(OracleExecutionContext):
    statement: Any = ...
    def pre_exec(self) -> None: ...
    def get_result_proxy(self): ...
    def create_cursor(self): ...

class ReturningResultProxy(_result.FullyBufferedResultProxy):
    def __init__(self, context: Any, returning_row: Any) -> None: ...

class ReturningParam:
    type: Any = ...
    def __init__(self, type_: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...

class OracleDialect_zxjdbc(ZxJDBCConnector, OracleDialect):
    jdbc_db_name: str = ...
    jdbc_driver_name: str = ...
    statement_compiler: Any = ...
    execution_ctx_cls: Any = ...
    colspecs: Any = ...
    DataHandler: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    implicit_returning: Any = ...
    def initialize(self, connection: Any) -> None: ...
dialect = OracleDialect_zxjdbc
