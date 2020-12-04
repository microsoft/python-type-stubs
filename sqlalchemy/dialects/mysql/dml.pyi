from ...sql.dml import Insert as StandardInsert
from ...sql.elements import ClauseElement
from typing import Any

class Insert(StandardInsert):
    @property
    def inserted(self): ...
    def inserted_alias(self): ...
    def on_duplicate_key_update(self, *args: Any, **kw: Any): ...

insert: Any

class OnDuplicateClause(ClauseElement):
    __visit_name__: str = ...
    inserted_alias: Any = ...
    update: Any = ...
    def __init__(self, inserted_alias: Any, update: Any) -> None: ...
