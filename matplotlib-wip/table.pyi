from typing import Literal, Sequence
from ._typing import *
from .text import Text
from .path import Path
from .backend_bases import MouseEvent, RendererBase
from .font_manager import FontProperties
from .figure import Figure
from .transforms import Bbox, Transform
from .axes import Axes
from .artist import Artist, allow_rasterization
from .patches import Rectangle

class Cell(Rectangle):
    """
    A cell is a `.Rectangle` with some associated `.Text`.

    As a user, you'll most likely not creates cells yourself. Instead, you
    should use either the `~matplotlib.table.table` factory function or
    `.Table.add_cell`.
    """

    PAD = ...

    def __init__(
        self,
        xy: Sequence[float],
        width: float,
        height: float,
        edgecolor: Color = ...,
        facecolor: Color = ...,
        fill: bool = ...,
        text: str = ...,
        loc: Literal["left", "center", "right"] = "right",
        fontproperties: FontProperties = ...,
        *,
        visible_edges: str = "closed"
    ) -> None:
        """
        Parameters
        ----------
        xy : 2-tuple
            The position of the bottom left corner of the cell.
        width : float
            The cell width.
        height : float
            The cell height.
        edgecolor : color
            The color of the cell border.
        facecolor : color
            The cell facecolor.
        fill : bool
            Whether the cell background is filled.
        text : str
            The cell text.
        loc : {'left', 'center', 'right'}, default: 'right'
            The alignment of the text within the cell.
        fontproperties : dict
            A dict defining the font properties of the text. Supported keys and
            values are the keyword arguments accepted by `.FontProperties`.
        visible_edges : str, default: 'closed'
            The cell edges to be drawn with a line: a substring of 'BRTL'
            (bottom, right, top, left), or one of 'open' (no edges drawn),
            'closed' (all edges drawn), 'horizontal' (bottom and top),
            'vertical' (right and left).
        """
        ...
    def set_transform(self, trans: Transform): ...
    def set_figure(self, fig: Figure) -> None: ...
    def get_text(self) -> Text:
        """Return the cell `.Text` instance."""
        ...
    def set_fontsize(self, size: float) -> None:
        """Set the text fontsize."""
        ...
    def get_fontsize(self) -> float:
        """Return the cell fontsize."""
        ...
    def auto_set_font_size(self, renderer: RendererBase) -> float:
        """Shrink font size until the text fits into the cell width."""
        ...
    @allow_rasterization
    def draw(self, renderer):
        RendererBase: ...
    def get_text_bounds(self, renderer: RendererBase):
        """
        Return the text bounds as *(x, y, width, height)* in table coordinates.
        """
        ...
    def get_required_width(self, renderer: RendererBase):
        """Return the minimal required width for the cell."""
        ...
    def set_text_props(self, **kwargs) -> None:
        """
        Update the text properties.

        Valid keyword arguments are:

        %(Text:kwdoc)s
        """
        ...
    @property
    def visible_edges(self) -> str:
        """
        The cell edges to be drawn with a line.

        Reading this property returns a substring of 'BRTL' (bottom, right,
        top, left').

        When setting this property, you can use a substring of 'BRTL' or one
        of {'open', 'closed', 'horizontal', 'vertical'}.
        """
        ...
    @visible_edges.setter
    def visible_edges(self, value: str): ...
    def get_path(self) -> Path:
        """Return a `.Path` for the `.visible_edges`."""
        ...

CustomCell = Cell

class Table(Artist):
    """
    A table of cells.

    The table consists of a grid of cells, which are indexed by (row, column).

    For a simple table, you'll have a full grid of cells with indices from
    (0, 0) to (num_rows-1, num_cols-1), in which the cell (0, 0) is positioned
    at the top left. However, you can also add cells with negative indices.
    You don't have to add a cell to every grid position, so you can create
    tables that have holes.

    *Note*: You'll usually not create an empty table from scratch. Instead use
    `~matplotlib.table.table` to create a table from data.
    """

    codes = ...
    FONTSIZE = ...
    AXESPAD = ...
    def __init__(self, ax: Axes, loc: str = ..., bbox: Bbox = ..., **kwargs) -> None:
        """
        Parameters
        ----------
        ax : `Axes`
            The `~.axes.Axes` to plot the table into.
        loc : str
            The position of the cell with respect to *ax*. This must be one of
            the `~.Table.codes`.
        bbox : `.Bbox` or None
            A bounding box to draw the table into. If this is not *None*, this
            overrides *loc*.

        Other Parameters
        ----------------
        **kwargs
            `.Artist` properties.
        """
        ...
    def add_cell(self, row: int, col: int, *args, **kwargs) -> Cell:
        """
        Create a cell and add it to the table.

        Parameters
        ----------
        row : int
            Row index.
        col : int
            Column index.
        *args, **kwargs
            All other parameters are passed on to `Cell`.

        Returns
        -------
        `.Cell`
            The created cell.

        """
        ...
    def __setitem__(self, position: Sequence[int], cell: Cell) -> None:
        """
        Set a custom cell in a given position.
        """
        ...
    def __getitem__(self, position) -> Cell:
        """Retrieve a custom cell from a given position."""
        ...
    @property
    def edges(self):
        """
        The default value of `~.Cell.visible_edges` for newly added
        cells using `.add_cell`.

        Notes
        -----
        This setting does currently only affect newly created cells using
        `.add_cell`.

        To change existing cells, you have to set their edges explicitly::

            for c in tab.get_celld().values():
                c.visible_edges = 'horizontal'

        """
        ...
    @edges.setter
    def edges(self, value): ...
    @allow_rasterization
    def draw(self, renderer: RendererBase): ...
    def contains(self, mouseevent: MouseEvent): ...
    def get_children(self) -> list[Artist]:
        """Return the Artists contained by the table."""
        ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def auto_set_column_width(self, col: int) -> None:
        """
        Automatically set the widths of given columns to optimal sizes.

        Parameters
        ----------
        col : int or sequence of ints
            The indices of the columns to auto-scale.
        """
        ...
    def auto_set_font_size(self, value: float = ...):
        """Automatically set font size."""
        ...
    def scale(self, xscale: float, yscale: float):
        """Scale column widths by *xscale* and row heights by *yscale*."""
        ...
    def set_fontsize(self, size: float):
        """
        Set the font size, in points, of the cell text.

        Parameters
        ----------
        size : float

        Notes
        -----
        As long as auto font size has not been disabled, the value will be
        clipped such that the text fits horizontally into the cell.

        You can disable this behavior using `.auto_set_font_size`.

        >>> the_table.auto_set_font_size(False)
        >>> the_table.set_fontsize(20)

        However, there is no automatic scaling of the row height so that the
        text may exceed the cell boundary.
        """
        ...
    def get_celld(self) -> dict[Sequence[int], Cell]:
        r"""
        Return a dict of cells in the table mapping *(row, column)* to
        `.Cell`\s.

        Notes
        -----
        You can also directly index into the Table object to access individual
        cells::

            cell = table[row, col]

        """
        ...

def table(
    ax,
    cellText: ArrayLike = ...,
    cellColours: ArrayLike = ...,
    cellLoc: Literal["left", "center", "right"] = "right",
    colWidths: Sequence[float] = ...,
    rowLabels: Sequence[str] = ...,
    rowColours: Sequence[Color] = ...,
    rowLoc: Literal["left", "center", "right"] = "left",
    colLabels: Sequence[str] = ...,
    colColours: Sequence[Color] = ...,
    colLoc: Literal["left", "center", "right"] = "left",
    loc: str = ...,
    bbox: Bbox = ...,
    edges: str | Literal["open", "closed", "horizontal", "vertical"] = ...,
    **kwargs
) -> Table:
    """
    Add a table to an `~.axes.Axes`.

    At least one of *cellText* or *cellColours* must be specified. These
    parameters must be 2D lists, in which the outer lists define the rows and
    the inner list define the column values per row. Each row must have the
    same number of elements.

    The table can optionally have row and column headers, which are configured
    using *rowLabels*, *rowColours*, *rowLoc* and *colLabels*, *colColours*,
    *colLoc* respectively.

    For finer grained control over tables, use the `.Table` class and add it to
    the axes with `.Axes.add_table`.

    Parameters
    ----------
    cellText : 2D list of str, optional
        The texts to place into the table cells.

        *Note*: Line breaks in the strings are currently not accounted for and
        will result in the text exceeding the cell boundaries.

    cellColours : 2D list of colors, optional
        The background colors of the cells.

    cellLoc : {'left', 'center', 'right'}, default: 'right'
        The alignment of the text within the cells.

    colWidths : list of float, optional
        The column widths in units of the axes. If not given, all columns will
        have a width of *1 / ncols*.

    rowLabels : list of str, optional
        The text of the row header cells.

    rowColours : list of colors, optional
        The colors of the row header cells.

    rowLoc : {'left', 'center', 'right'}, default: 'left'
        The text alignment of the row header cells.

    colLabels : list of str, optional
        The text of the column header cells.

    colColours : list of colors, optional
        The colors of the column header cells.

    colLoc : {'left', 'center', 'right'}, default: 'left'
        The text alignment of the column header cells.

    loc : str, optional
        The position of the cell with respect to *ax*. This must be one of
        the `~.Table.codes`.

    bbox : `.Bbox`, optional
        A bounding box to draw the table into. If this is not *None*, this
        overrides *loc*.

    edges : substring of 'BRTL' or {'open', 'closed', 'horizontal', 'vertical'}
        The cell edges to be drawn with a line. See also
        `~.Cell.visible_edges`.

    Returns
    -------
    `~matplotlib.table.Table`
        The created table.

    Other Parameters
    ----------------
    **kwargs
        `.Table` properties.

    %(Table:kwdoc)s
    """
    ...
