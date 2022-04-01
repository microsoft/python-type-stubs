from typing import (
    Any,
    List,
    Optional,
    Union,
)
from openpyxl.worksheet.header_footer import HeaderFooter

def avoid_duplicate_name(names: List[str], value: str) -> str: ...

class _WorkbookChild:

    __title = ""
    _id = None
    _path = "{0}"
    _parent = None
    _default_title = "Sheet"
    def __init__(
        self, parent: Optional[Any] = ..., title: Optional[Union[bytes, str, int]] = ...
    ) -> None:
        self._parent = parent
        self.title = title or self._default_title
        self.HeaderFooter = HeaderFooter()
    def __repr__(self) -> str: ...
    @property
    def encoding(self) -> str: ...
    @property
    def parent(self) -> Any: ...
    @property
    def path(self) -> str: ...
