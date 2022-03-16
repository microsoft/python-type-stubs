from io import (
    BufferedReader,
    BytesIO,
)
from openpyxl.packaging.manifest import (
    Manifest,
    Override,
)
from openpyxl.packaging.relationship import Relationship
from openpyxl.packaging.workbook import ChildSheet
from openpyxl.workbook.workbook import Workbook
from typing import Union
from zipfile import ZipFile

def _find_workbook_part(package: Manifest) -> Override: ...
def _validate_archive(filename: Union[str, BufferedReader, BytesIO]) -> ZipFile: ...
def load_workbook(
    filename: Union[str, BufferedReader, BytesIO],
    read_only: bool = ...,
    keep_vba: bool = ...,
    data_only: bool = ...,
    keep_links: bool = ...,
) -> Workbook: ...

class ExcelReader:
    def __init__(
        self,
        fn: Union[str, BufferedReader, BytesIO],
        read_only: bool = ...,
        keep_vba: bool = ...,
        data_only: bool = ...,
        keep_links: bool = ...,
    ) -> None: ...
    def read(self) -> None: ...
    def read_chartsheet(self, sheet: ChildSheet, rel: Relationship) -> None: ...
    def read_manifest(self) -> None: ...
    def read_properties(self) -> None: ...
    def read_strings(self) -> None: ...
    def read_theme(self) -> None: ...
    def read_workbook(self) -> None: ...
    def read_worksheets(self) -> None: ...
