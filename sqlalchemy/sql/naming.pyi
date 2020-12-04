from .. import event as event, events as events, exc as exc
from .elements import conv as conv
from .schema import CheckConstraint as CheckConstraint, Column as Column, Constraint as Constraint, ForeignKeyConstraint as ForeignKeyConstraint, Index as Index, PrimaryKeyConstraint as PrimaryKeyConstraint, Table as Table, UniqueConstraint as UniqueConstraint
from typing import Any

class ConventionDict:
    const: Any = ...
    table: Any = ...
    convention: Any = ...
    def __init__(self, const: Any, table: Any, convention: Any) -> None: ...
    def __getitem__(self, key: Any): ...
