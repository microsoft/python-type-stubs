from typing import Sequence
from ._layoutgrid import LayoutGrid
from .figure import Figure, FigureBase
from .gridspec import GridSpecBase

class LayoutEngine:
    """
    Base class for Matplotlib layout engines.

    A layout engine can be passed to a figure at instantiation or at any time
    with `~.figure.Figure.set_layout_engine`.  Once attached to a figure, the
    layout engine ``execute`` function is called at draw time by
    `~.figure.Figure.draw`, providing a special draw-time hook.

    .. note::

       However, note that layout engines affect the creation of colorbars, so
       `~.figure.Figure.set_layout_engine` should be called before any
       colorbars are created.

    Currently, there are two properties of `LayoutEngine` classes that are
    consulted while manipulating the figure:

    - ``engine.colorbar_gridspec`` tells `.Figure.colorbar` whether to make the
       axes using the gridspec method (see `.colorbar.make_axes_gridspec`) or
       not (see `.colorbar.make_axes`);
    - ``engine.adjust_compatible`` stops `.Figure.subplots_adjust` from being
        run if it is not compatible with the layout engine.

    To implement a custom `LayoutEngine`:

    1. override ``_adjust_compatible`` and ``_colorbar_gridspec``
    2. override `LayoutEngine.set` to update *self._params*
    3. override `LayoutEngine.execute` with your implementation

    """

    def __init__(self, **kwargs) -> None: ...
    def set(self, **kwargs): ...
    @property
    def colorbar_gridspec(self) -> bool:
        """
        Return a boolean if the layout engine creates colorbars using a
        gridspec.
        """
        ...
    @property
    def adjust_compatible(self) -> bool:
        """
        Return a boolean if the layout engine is compatible with
        `~.Figure.subplots_adjust`.
        """
        ...
    def get(self):
        """
        Return copy of the parameters for the layout engine.
        """
        ...
    def execute(self, fig: Figure):
        """
        Execute the layout on the figure given by *fig*.
        """
        ...

class TightLayoutEngine(LayoutEngine):
    """
    Implements the ``tight_layout`` geometry management.  See
    :doc:`/tutorials/intermediate/tight_layout_guide` for details.
    """

    def __init__(
        self,
        *,
        pad: float = 1.08,
        h_pad: float = ...,
        w_pad: float = ...,
        rect: Sequence[float] = ...,
        **kwargs
    ) -> None:
        """
        Initialize tight_layout engine.

        Parameters
        ----------
        pad : float, 1.08
            Padding between the figure edge and the edges of subplots, as a
            fraction of the font size.
        h_pad, w_pad : float
            Padding (height/width) between edges of adjacent subplots.
            Defaults to *pad*.
        rect : tuple of 4 floats, optional
            (left, bottom, right, top) rectangle in normalized figure
            coordinates that the subplots (including labels)
            will fit into. Defaults to using the entire figure.
        """
        ...
    def execute(self, fig: Figure) -> None:
        """
        Execute tight_layout.

        This decides the subplot parameters given the padding that
        will allow the axes labels to not be covered by other labels
        and axes.

        Parameters
        ----------
        fig : `.Figure` to perform layout on.

        See also: `.figure.Figure.tight_layout` and `.pyplot.tight_layout`.
        """
        ...
    def set(
        self,
        *,
        pad: float = 1.08,
        w_pad: float = ...,
        h_pad: float = ...,
        rect: Sequence[float] = ...
    ) -> None: ...

class ConstrainedLayoutEngine(LayoutEngine):
    """
    Implements the ``constrained_layout`` geometry management.  See
    :doc:`/tutorials/intermediate/constrainedlayout_guide` for details.
    """

    def __init__(
        self,
        *,
        h_pad: float = ...,
        w_pad: float = ...,
        hspace: float = ...,
        wspace: float = ...,
        rect: Sequence[float] = ...,
        compress: bool = ...,
        **kwargs
    ) -> None:
        """
        Initialize ``constrained_layout`` settings.

        Parameters
        ----------
        h_pad, w_pad : float
            Padding around the axes elements in figure-normalized units.
            Default to :rc:`figure.constrained_layout.h_pad` and
            :rc:`figure.constrained_layout.w_pad`.
        hspace, wspace : float
            Fraction of the figure to dedicate to space between the
            axes.  These are evenly spread between the gaps between the axes.
            A value of 0.2 for a three-column layout would have a space
            of 0.1 of the figure width between each column.
            If h/wspace < h/w_pad, then the pads are used instead.
            Default to :rc:`figure.constrained_layout.hspace` and
            :rc:`figure.constrained_layout.wspace`.
        rect : tuple of 4 floats
            Rectangle in figure coordinates to perform constrained layout in
            (left, bottom, width, height), each from 0-1.
        compress : bool
            Whether to shift Axes so that white space in between them is
            removed. This is useful for simple grids of fixed-aspect Axes (e.g.
            a grid of images).  See :ref:`compressed_layout`.
        """
        ...
    def execute(
        self, fig: Figure
    ) -> dict[str | FigureBase | GridSpecBase, bool | LayoutGrid]:
        """
        Perform constrained_layout and move and resize axes accordingly.

        Parameters
        ----------
        fig : `.Figure` to perform layout on.
        """
        ...
    def set(
        self,
        *,
        h_pad: float = ...,
        w_pad: float = ...,
        hspace: float = ...,
        wspace: float = ...,
        rect: tuple = ...
    ) -> None:
        """
        Set the pads for constrained_layout.

        Parameters
        ----------
        h_pad, w_pad : float
            Padding around the axes elements in figure-normalized units.
            Default to :rc:`figure.constrained_layout.h_pad` and
            :rc:`figure.constrained_layout.w_pad`.
        hspace, wspace : float
            Fraction of the figure to dedicate to space between the
            axes.  These are evenly spread between the gaps between the axes.
            A value of 0.2 for a three-column layout would have a space
            of 0.1 of the figure width between each column.
            If h/wspace < h/w_pad, then the pads are used instead.
            Default to :rc:`figure.constrained_layout.hspace` and
            :rc:`figure.constrained_layout.wspace`.
        rect : tuple of 4 floats
            Rectangle in figure coordinates to perform constrained layout in
            (left, bottom, width, height), each from 0-1.
        """
        ...
