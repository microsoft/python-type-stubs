from openpyxl.chart.line_chart import LineChart
from openpyxl.chart.scatter_chart import ScatterChart
from openpyxl.drawing.image import Image
from typing import (
    Any,
    List,
    Tuple,
    Union,
)
from zipfile import ZipFile

def find_images(
    archive: ZipFile, path: str
) -> Union[
    Tuple[List[ScatterChart], List[Any]],
    Tuple[List[Any], List[Any]],
    Tuple[List[Any], List[Image]],
    Tuple[List[LineChart], List[Any]],
]: ...
