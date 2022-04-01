from io import BufferedReader
from typing import (
    List,
    Union,
)
from zipfile import ZipExtFile

def read_string_table(xml_source: Union[ZipExtFile, BufferedReader]) -> List[str]: ...
