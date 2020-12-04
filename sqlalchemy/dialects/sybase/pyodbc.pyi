from sqlalchemy import processors as processors, types as sqltypes
from sqlalchemy.connectors.pyodbc import PyODBCConnector as PyODBCConnector
from sqlalchemy.dialects.sybase.base import SybaseDialect as SybaseDialect, SybaseExecutionContext as SybaseExecutionContext
from typing import Any

class _SybNumeric_pyodbc(sqltypes.Numeric):
    def bind_processor(self, dialect: Any): ...

class SybaseExecutionContext_pyodbc(SybaseExecutionContext):
    def set_ddl_autocommit(self, connection: Any, value: Any) -> None: ...

class SybaseDialect_pyodbc(PyODBCConnector, SybaseDialect):
    execution_ctx_cls: Any = ...
    colspecs: Any = ...
dialect = SybaseDialect_pyodbc
