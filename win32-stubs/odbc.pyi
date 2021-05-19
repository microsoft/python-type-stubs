# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: odbc, version: unspecified
# Module: odbc, version: unspecified

'A Python wrapper around the ODBC API.'

import typing
import builtins as _mod_builtins
import dbi as _mod_dbi

odbcError = _mod_builtins.type
DATE: str
NUMBER: str
RAW: str
def SQLDataSources() -> typing.Any:
    ...

SQL_FETCH_ABSOLUTE: int
SQL_FETCH_FIRST: int
SQL_FETCH_FIRST_SYSTEM: int
SQL_FETCH_FIRST_USER: int
SQL_FETCH_LAST: int
SQL_FETCH_NEXT: int
SQL_FETCH_PRIOR: int
SQL_FETCH_RELATIVE: int
STRING: str
TYPES: tuple
__doc__: str
__file__: str
__name__: str
__package__: str
dataError = _mod_dbi.dataError
error: odbcError
integrityError = _mod_dbi.integrityError
internalError = _mod_dbi.internalError
noError = _mod_dbi.noError
def odbc() -> typing.Any:
    ...

opError = _mod_dbi.opError
progError = _mod_dbi.progError
def __getattr__(name) -> typing.Any:
    ...

