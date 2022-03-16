from openpyxl.packaging.relationship import (
    Relationship,
    RelationshipList,
)
from openpyxl.packaging.workbook import ChildSheet
from openpyxl.pivot.cache import CacheDefinition
from typing import (
    Dict,
    Iterator,
    Tuple,
)
from zipfile import ZipFile

class WorkbookParser:
    def __init__(
        self, archive: ZipFile, workbook_part_name: str, keep_links: bool = ...
    ) -> None: ...
    def assign_names(self) -> None: ...
    def find_sheets(self) -> Iterator[Tuple[ChildSheet, Relationship]]: ...
    def parse(self) -> None: ...
    @property
    def pivot_caches(self) -> Dict[int, CacheDefinition]: ...
    @property
    def rels(self) -> RelationshipList: ...
