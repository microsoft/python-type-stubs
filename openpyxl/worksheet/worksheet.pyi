# Core Library modules
import datetime
from decimal import Decimal
from typing import Any, Iterator, Optional, Tuple, Union

# Third party modules
from openpyxl.cell.cell import Cell, MergedCell
from openpyxl.cell.read_only import ReadOnlyCell
from openpyxl.chart.bar_chart import BarChart
from openpyxl.descriptors import String
from openpyxl.drawing.image import Image
from openpyxl.workbook.child import _WorkbookChild
from openpyxl.workbook.workbook import Workbook
from openpyxl.worksheet.cell_range import CellRange
from openpyxl.worksheet.dimensions import ColumnDimension, RowDimension
from openpyxl.worksheet.merge import MergedCellRange
from openpyxl.worksheet.table import Table, TableList
from openpyxl.worksheet.tests.test_dimensions import DummyWorkbook
from openpyxl.worksheet.tests.test_worksheet import DummyWorkbook
from openpyxl.worksheet.views import SheetView

def _gutter(idx: int, offset: int, max_val: int) -> range: ...

class Worksheet(_WorkbookChild):
    def __delitem__(self, key: str) -> None: ...
    def __getitem__(self, key: Union[str, slice, int]) -> Any: ...
    def __init__(
        self,
        parent: Union[DummyWorkbook, DummyWorkbook, Workbook],
        title: Optional[Union[str, int]] = ...,
    ) -> None:
        _WorkbookChild.__init__(self, parent, title)
        self._setup()
    def _setup(self):
        self.row_dimensions = DimensionHolder(
            worksheet=self, default_factory=self._add_row
        )
        self.column_dimensions = DimensionHolder(
            worksheet=self, default_factory=self._add_column
        )
        self.row_breaks = RowBreak()
        self.col_breaks = ColBreak()
        self._cells = {}
        self._charts = []
        self._images = []
        self._rels = RelationshipList()
        self._drawing = None
        self._comments = []
        self.merged_cells = MultiCellRange()
        self._tables = TableList()
        self._pivots = []
        self.data_validations = DataValidationList()
        self._hyperlinks = []
        self.sheet_state = "visible"
        self.page_setup = PrintPageSetup(worksheet=self)
        self.print_options = PrintOptions()
        self._print_rows = None
        self._print_cols = None
        self._print_area = None
        self.page_margins = PageMargins()
        self.views = SheetViewList()
        self.protection = SheetProtection()

        self._current_row = 0
        self.auto_filter = AutoFilter()
        self.paper_size = None
        self.formula_attributes = {}
        self.orientation = None
        self.conditional_formatting = ConditionalFormattingList()
        self.legacy_drawing = None
        self.sheet_properties = WorksheetProperties()
        self.sheet_format = SheetFormatProperties()
        self.scenarios = ScenarioList()
    def __iter__(self) -> Iterator[Any]: ...
    def __setitem__(self, key: str, value: Union[str, int]) -> None: ...
    def _add_cell(self, cell: Cell) -> None: ...
    def _add_column(self) -> ColumnDimension: ...
    def _add_row(self) -> RowDimension: ...
    def _cells_by_col(
        self,
        min_col: int,
        min_row: int,
        max_col: int,
        max_row: int,
        values_only: bool = ...,
    ) -> Iterator[Tuple[Cell, ...]]: ...
    def _cells_by_row(
        self,
        min_col: int,
        min_row: int,
        max_col: int,
        max_row: int,
        values_only: bool = ...,
    ) -> Iterator[Any]: ...
    def _clean_merge_range(self, mcr: MergedCellRange) -> None: ...
    def _get_cell(self, row: int, column: int) -> Union[MergedCell, Cell]: ...
    def _invalid_row(self, iterable: str): ...
    def _move_cell(
        self,
        row: int,
        column: int,
        row_offset: int,
        col_offset: int,
        translate: bool = ...,
    ) -> None: ...
    def _move_cells(
        self,
        min_row: Optional[int] = ...,
        min_col: Optional[int] = ...,
        offset: int = ...,
        row_or_col: str = ...,
    ) -> None: ...
    @property
    def active_cell(self) -> str: ...
    def add_chart(self, chart: BarChart, anchor: Optional[str] = ...) -> None: ...
    def add_image(self, img: Image, anchor: Optional[str] = ...) -> None: ...
    def add_table(self, table: Table) -> None: ...
    def append(self, iterable: Any) -> None: ...
    def calculate_dimension(self) -> str: ...
    def cell(
        self,
        row: int,
        column: int,
        value: Optional[
            Union[
                int,
                float,
                Decimal,
                str,
                bytes,
                datetime.datetime,
                datetime.date,
                datetime.time,
                datetime.timedelta,
            ]
        ] = ...,
    ) -> Union[MergedCell, ReadOnlyCell, Cell]: ...
    @property
    def columns(self) -> Iterator[Any]: ...
    def delete_cols(self, idx: int, amount: int = ...) -> None: ...
    def delete_rows(self, idx: int, amount: int = ...) -> None: ...
    def insert_cols(self, idx: int, amount: int = ...) -> None: ...
    def insert_rows(self, idx: int, amount: int = ...) -> None: ...
    def iter_cols(
        self,
        min_col: Optional[int] = ...,
        max_col: Optional[int] = ...,
        min_row: None = ...,
        max_row: None = ...,
        values_only: bool = ...,
    ) -> Iterator[Any]: ...
    def iter_rows(
        self,
        min_row: Optional[int] = ...,
        max_row: Optional[int] = ...,
        min_col: Optional[int] = ...,
        max_col: Optional[int] = ...,
        values_only: bool = ...,
    ) -> Iterator[Any]: ...
    @property
    def max_column(self) -> int: ...
    @property
    def max_row(self) -> int: ...
    def merge_cells(
        self,
        range_string: Optional[str] = ...,
        start_row: Optional[int] = ...,
        start_column: Optional[int] = ...,
        end_row: Optional[int] = ...,
        end_column: Optional[int] = ...,
    ) -> None: ...
    @property
    def min_column(self) -> int: ...
    @property
    def min_row(self) -> int: ...
    def move_range(
        self,
        cell_range: Union[CellRange, str],
        rows: int = ...,
        cols: int = ...,
        translate: bool = ...,
    ) -> None: ...
    @property
    def print_titles(self) -> Optional[str]: ...
    @property
    def rows(self) -> Iterator[Any]: ...
    @property
    def selected_cell(self) -> str: ...
    @property
    def sheet_view(self) -> SheetView: ...
    @property
    def show_gridlines(self) -> None: ...
    @property
    def tables(self) -> TableList: ...
    def unmerge_cells(
        self,
        range_string: Optional[str] = ...,
        start_row: Optional[int] = ...,
        start_column: Optional[int] = ...,
        end_row: Optional[int] = ...,
        end_column: Optional[int] = ...,
    ) -> None: ...
    @property
    def values(
        self,
    ) -> Iterator[
        Union[
            Tuple[str, None, None, None, None, None, None],
            Tuple[None, None, None, None, None, None, None],
            Tuple[None, None, None, None, None, None, str],
        ]
    ]: ...
    @property
    def freeze_panes(self) -> Optional[String]:
        if self.sheet_view.pane is not None:
            return self.sheet_view.pane.topLeftCell
        return None
    @freeze_panes.setter
    def freeze_panes(self, topLeftCell=None) -> None: ...
