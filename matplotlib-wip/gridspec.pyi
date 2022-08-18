import datetime
import numpy as np
from typing import Any, Callable, Iterable, Literal, Sequence
from matplotlib._typing import *
from matplotlib.gridspec import SubplotSpec
from matplotlib.figure import Figure

"""
This type stub file was generated by pyright.
"""
from matplotlib.figure import Figure, SubFigure, SubplotParams
from typing import Any, List, Optional, Tuple, Union

"""
This type stub file was generated by pyright.
"""

class GridSpecBase:
    """
    A base class of GridSpec that specifies the geometry of the grid
    that a subplot will be placed.
    """

    def __init__(
        self,
        nrows: int,
        ncols: int,
        height_ratios: Optional[
            Union[list[int], list[float], Tuple[int, int], list[Union[int, float]]]
        ] = ...,
        width_ratios: Optional[Union[list[float], Tuple[int, int], list[int]]] = ...,
    ) -> None:
        """
        Parameters
        ----------
        nrows, ncols : int
            The number of rows and columns of the grid.
        width_ratios : array-like of length *ncols*, optional
            Defines the relative widths of the columns. Each column gets a
            relative width of ``width_ratios[i] / sum(width_ratios)``.
            If not given, all columns will have the same width.
        height_ratios : array-like of length *nrows*, optional
            Defines the relative heights of the rows. Each row gets a
            relative height of ``height_ratios[i] / sum(height_ratios)``.
            If not given, all rows will have the same height.
        """
        ...
    def __repr__(self): ...

    nrows = ...
    ncols = ...
    def get_geometry(self) -> Tuple[int, int]:
        """
        Return a tuple containing the number of rows and columns in the grid.
        """
        ...
    def get_subplot_params(self, figure=...): ...
    def new_subplotspec(
        self, loc: Tuple[int, int], rowspan: int = ..., colspan: int = ...
    ) -> "SubplotSpec":
        """
        Create and return a `.SubplotSpec` instance.

        Parameters
        ----------
        loc : (int, int)
            The position of the subplot in the grid as
            ``(row_index, column_index)``.
        rowspan, colspan : int, default: 1
            The number of rows and columns the subplot should span in the grid.
        """
        ...
    def set_width_ratios(
        self, width_ratios: Optional[Union[list[float], Tuple[int, int], list[int]]]
    ) -> None:
        """
        Set the relative widths of the columns.

        *width_ratios* must be of length *ncols*. Each column gets a relative
        width of ``width_ratios[i] / sum(width_ratios)``.
        """
        ...
    def get_width_ratios(self) -> list[int]:
        """
        Return the width ratios.

        This is *None* if no width ratios have been set explicitly.
        """
        ...
    def set_height_ratios(
        self,
        height_ratios: Optional[
            Union[list[float], list[int], Tuple[int, int], list[Union[int, float]]]
        ],
    ) -> None:
        """
        Set the relative heights of the rows.

        *height_ratios* must be of length *nrows*. Each row gets a relative
        height of ``height_ratios[i] / sum(height_ratios)``.
        """
        ...
    def get_height_ratios(self) -> list[Union[int, float]]:
        """
        Return the height ratios.

        This is *None* if no height ratios have been set explicitly.
        """
        ...
    def get_grid_positions(self, fig: Figure, raw: bool = ...):
        """
        Return the positions of the grid cells in figure coordinates.

        Parameters
        ----------
        fig : `~Figure`
            The figure the grid should be applied to. The subplot parameters
            (margins and spacing between subplots) are taken from *fig*.
        raw : bool, default: False
            If *True*, the subplot parameters of the figure are not taken
            into account. The grid spans the range [0, 1] in both directions
            without margins and there is no space between grid cells. This is
            used for constrained_layout.

        Returns
        -------
        bottoms, tops, lefts, rights : array
            The bottom, top, left, right positions of the grid cells in
            figure coordinates.
        """
        ...
    def __getitem__(self, key: Any) -> "SubplotSpec":
        """Create and return a `.SubplotSpec` instance."""
        ...
    def subplots(self, *, sharex=..., sharey=..., squeeze=..., subplot_kw=...):
        """
        Add all subplots specified by this `GridSpec` to its parent figure.

        See `.Figure.subplots` for detailed documentation.
        """
        ...

class GridSpec(GridSpecBase):
    """
    A grid layout to place subplots within a figure.

    The location of the grid cells is determined in a similar way to
    `~.figure.SubplotParams` using *left*, *right*, *top*, *bottom*, *wspace*
    and *hspace*.

    Indexing a GridSpec instance returns a `.SubplotSpec`.
    """

    def __init__(
        self,
        nrows: int,
        ncols: int,
        figure: Optional[Union[Figure, SubFigure]] = ...,
        left: Optional[float] = ...,
        bottom: Optional[Union[int, float]] = ...,
        right: Optional[float] = ...,
        top: Optional[Union[int, float]] = ...,
        wspace: Optional[Union[int, float]] = ...,
        hspace: Optional[Union[int, float]] = ...,
        width_ratios: Optional[Union[list[int], Tuple[int, int]]] = ...,
        height_ratios: Optional[
            Union[list[int], Tuple[int, int], list[Union[int, float]]]
        ] = ...,
    ) -> None:
        """
        Parameters
        ----------
        nrows, ncols : int
            The number of rows and columns of the grid.

        figure : `.Figure`, optional
            Only used for constrained layout to create a proper layoutgrid.

        left, right, top, bottom : float, optional
            Extent of the subplots as a fraction of figure width or height.
            Left cannot be larger than right, and bottom cannot be larger than
            top. If not given, the values will be inferred from a figure or
            rcParams at draw time. See also `GridSpec.get_subplot_params`.

        wspace : float, optional
            The amount of width reserved for space between subplots,
            expressed as a fraction of the average axis width.
            If not given, the values will be inferred from a figure or
            rcParams when necessary. See also `GridSpec.get_subplot_params`.

        hspace : float, optional
            The amount of height reserved for space between subplots,
            expressed as a fraction of the average axis height.
            If not given, the values will be inferred from a figure or
            rcParams when necessary. See also `GridSpec.get_subplot_params`.

        width_ratios : array-like of length *ncols*, optional
            Defines the relative widths of the columns. Each column gets a
            relative width of ``width_ratios[i] / sum(width_ratios)``.
            If not given, all columns will have the same width.

        height_ratios : array-like of length *nrows*, optional
            Defines the relative heights of the rows. Each row gets a
            relative height of ``height_ratios[i] / sum(height_ratios)``.
            If not given, all rows will have the same height.

        """
        ...
    def update(self, **kwargs) -> None:
        """
        Update the subplot parameters of the grid.

        Parameters that are not explicitly given are not changed. Setting a
        parameter to *None* resets it to :rc:`figure.subplot.*`.

        Parameters
        ----------
        left, right, top, bottom : float or None, optional
            Extent of the subplots as a fraction of figure width or height.
        wspace, hspace : float, optional
            Spacing between the subplots as a fraction of the average subplot
            width / height.
        """
        ...
    def get_subplot_params(
        self, figure: Union[Figure, SubFigure] = ...
    ) -> SubplotParams:
        """
        Return the `.SubplotParams` for the GridSpec.

        In order of precedence the values are taken from

        - non-*None* attributes of the GridSpec
        - the provided *figure*
        - :rc:`figure.subplot.*`
        """
        ...
    def locally_modified_subplot_params(self) -> list[Any]:
        """
        Return a list of the names of the subplot parameters explicitly set
        in the GridSpec.

        This is a subset of the attributes of `.SubplotParams`.
        """
        ...
    def tight_layout(
        self,
        figure: Figure,
        renderer: None = ...,
        pad: float = ...,
        h_pad: None = ...,
        w_pad: None = ...,
        rect: list[Optional[float]] = ...,
    ) -> None:
        """
        Adjust subplot parameters to give specified padding.

        Parameters
        ----------
        pad : float
            Padding between the figure edge and the edges of subplots, as a
            fraction of the font-size.
        h_pad, w_pad : float, optional
            Padding (height/width) between edges of adjacent subplots.
            Defaults to *pad*.
        rect : tuple of 4 floats, default: (0, 0, 1, 1), i.e. the whole figure
            (left, bottom, right, top) rectangle in normalized figure
            coordinates that the whole subplots area (including labels) will
            fit into.
        """
        ...

class GridSpecFromSubplotSpec(GridSpecBase):
    """
    GridSpec whose subplot layout parameters are inherited from the
    location specified by a given SubplotSpec.
    """

    def __init__(
        self,
        nrows: int,
        ncols: int,
        subplot_spec: "SubplotSpec",
        wspace: Optional[Union[int, float]] = ...,
        hspace: Optional[Union[int, float]] = ...,
        height_ratios: Optional[list[float]] = ...,
        width_ratios: Optional[list[float]] = ...,
    ) -> None:
        """
        Parameters
        ----------
        nrows, ncols : int
            Number of rows and number of columns of the grid.
        subplot_spec : SubplotSpec
            Spec from which the layout parameters are inherited.
        wspace, hspace : float, optional
            See `GridSpec` for more details. If not specified default values
            (from the figure or rcParams) are used.
        height_ratios : array-like of length *nrows*, optional
            See `GridSpecBase` for details.
        width_ratios : array-like of length *ncols*, optional
            See `GridSpecBase` for details.
        """
        ...
    def get_subplot_params(self, figure: Figure = ...) -> SubplotParams:
        """Return a dictionary of subplot layout parameters."""
        ...
    def get_topmost_subplotspec(self) -> "SubplotSpec":
        """
        Return the topmost `.SubplotSpec` instance associated with the subplot.
        """
        ...

class SubplotSpec:
    """
    The location of a subplot in a `GridSpec`.

    .. note::

        Likely, you'll never instantiate a `SubplotSpec` yourself. Instead you
        will typically obtain one from a `GridSpec` using item-access.

    Parameters
    ----------
    gridspec : `~matplotlib.gridspec.GridSpec`
        The GridSpec, which the subplot is referencing.
    num1, num2 : int
        The subplot will occupy the num1-th cell of the given
        gridspec.  If num2 is provided, the subplot will span between
        num1-th cell and num2-th cell *inclusive*.

        The index starts from 0.
    """

    def __init__(
        self,
        gridspec: Union[GridSpec, GridSpecFromSubplotSpec],
        num1: int,
        num2: int = ...,
    ) -> None: ...
    def __repr__(self): ...
    @property
    def num2(self): ...
    @num2.setter
    def num2(self, value): ...
    def get_gridspec(self) -> Union[GridSpec, GridSpecFromSubplotSpec]: ...
    def get_geometry(self):
        """
        Return the subplot geometry as tuple ``(n_rows, n_cols, start, stop)``.

        The indices *start* and *stop* define the range of the subplot within
        the `GridSpec`. *stop* is inclusive (i.e. for a single cell
        ``start == stop``).
        """
        ...
    @property
    def rowspan(self) -> range:
        """The rows spanned by this subplot, as a `range` object."""
        ...
    @property
    def colspan(self) -> range:
        """The columns spanned by this subplot, as a `range` object."""
        ...
    def is_first_row(self) -> bool: ...
    def is_last_row(self) -> bool: ...
    def is_first_col(self) -> bool: ...
    def is_last_col(self) -> bool: ...
    def get_position(self, figure):
        """
        Update the subplot position from ``figure.subplotpars``.
        """
        ...
    def get_topmost_subplotspec(self) -> "SubplotSpec":
        """
        Return the topmost `SubplotSpec` instance associated with the subplot.
        """
        ...
    def __eq__(self, other: Optional[SubplotSpec]) -> bool:
        """
        Two SubplotSpecs are considered equal if they refer to the same
        position(s) in the same `GridSpec`.
        """
        ...
    def __hash__(self) -> int: ...
    def subgridspec(self, nrows: int, ncols: int, **kwargs) -> GridSpecFromSubplotSpec:
        """
        Create a GridSpec within this subplot.

        The created `.GridSpecFromSubplotSpec` will have this `SubplotSpec` as
        a parent.

        Parameters
        ----------
        nrows : int
            Number of rows in grid.

        ncols : int
            Number or columns in grid.

        Returns
        -------
        `.GridSpecFromSubplotSpec`

        Other Parameters
        ----------------
        **kwargs
            All other parameters are passed to `.GridSpecFromSubplotSpec`.

        See Also
        --------
        matplotlib.pyplot.subplots

        Examples
        --------
        Adding three subplots in the space occupied by a single subplot::

            fig = plt.figure()
            gs0 = fig.add_gridspec(3, 1)
            ax1 = fig.add_subplot(gs0[0])
            ax2 = fig.add_subplot(gs0[1])
            gssub = gs0[2].subgridspec(1, 3)
            for i in range(3):
                fig.add_subplot(gssub[0, i])
        """
        ...
