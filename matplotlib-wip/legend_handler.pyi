import datetime
import numpy as np
from typing import Any, Callable, Iterable, Literal, Sequence
from matplotlib._typing import *
from matplotlib.path import Path
from matplotlib.patches import Patch
from matplotlib.offsetbox import OffsetBox
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
from matplotlib.legend import Legend
from matplotlib.container import BarContainer
from matplotlib.axes import Axes
from matplotlib.artist import Artist

"""
This type stub file was generated by pyright.
"""
from matplotlib.container import BarContainer
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from typing import Callable, Optional

from collections.abc import Sequence
from . import _api

"""
This type stub file was generated by pyright.
"""

def update_from_first_child(tgt: Rectangle, src: BarContainer) -> None: ...

class HandlerBase:
    """
    A Base class for default legend handlers.

    The derived classes are meant to override *create_artists* method, which
    has a following signature.::

      def create_artists(self, legend, orig_handle,
                         xdescent, ydescent, width, height, fontsize,
                         trans):

    The overridden method needs to create artists of the given
    transform that fits in the given dimension (xdescent, ydescent,
    width, height) that are scaled by fontsize if necessary.

    """

    def __init__(
        self,
        xpad: float = ...,
        ypad: float = ...,
        update_func: Optional[Callable] = ...,
    ) -> None: ...
    def update_prop(self, legend_handle, orig_handle, legend): ...
    def adjust_drawing_area(
        self, legend, orig_handle, xdescent, ydescent, width, height, fontsize
    ): ...
    def legend_artist(
        self, legend: Legend, orig_handle: Artist, fontsize: int, handlebox: OffsetBox
    ):
        """
        Return the artist that this HandlerBase generates for the given
        original artist/handle.

        Parameters
        ----------
        legend : `~Legend`
            The legend for which these legend artists are being created.
        orig_handle : :class:`Artist` or similar
            The object for which these legend artists are being created.
        fontsize : int
            The fontsize in pixels. The artists being created should
            be scaled according to the given fontsize.
        handlebox : `OffsetBox`
            The box which has been created to hold this legend entry's
            artists. Artists created in the `legend_artist` method must
            be added to this handlebox inside this method.

        """
        ...
    def create_artists(
        self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans
    ): ...

class HandlerNpoints(HandlerBase):
    """
    A legend handler that shows *numpoints* points in the legend entry.
    """

    def __init__(
        self, marker_pad: float = ..., numpoints: None = ..., **kwargs
    ) -> None:
        """
        Parameters
        ----------
        marker_pad : float
            Padding between points in legend entry.
        numpoints : int
            Number of points to show in legend entry.
        **kwargs
            Keyword arguments forwarded to `.HandlerBase`.
        """
        ...
    def get_numpoints(self, legend): ...
    def get_xdata(self, legend, xdescent, ydescent, width, height, fontsize): ...

class HandlerNpointsYoffsets(HandlerNpoints):
    """
    A legend handler that shows *numpoints* in the legend, and allows them to
    be individually offset in the y-direction.
    """

    def __init__(self, numpoints: None = ..., yoffsets: None = ..., **kwargs) -> None:
        """
        Parameters
        ----------
        numpoints : int
            Number of points to show in legend entry.
        yoffsets : array of floats
            Length *numpoints* list of y offsets for each point in
            legend entry.
        **kwargs
            Keyword arguments forwarded to `.HandlerNpoints`.
        """
        ...
    def get_ydata(self, legend, xdescent, ydescent, width, height, fontsize): ...

class HandlerLine2DCompound(HandlerNpoints):
    """
    Original handler for `.Line2D` instances, that relies on combining
    a line-only with a marker-only artist.  May be deprecated in the future.
    """

    def create_artists(
        self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans
    ): ...

class _Line2DHandleList(Sequence):
    def __init__(self, legline: Line2D) -> None: ...
    def __len__(self): ...
    def __getitem__(self, index: int) -> Line2D: ...

class HandlerLine2D(HandlerNpoints):
    """
    Handler for `.Line2D` instances.

    See Also
    --------
    HandlerLine2DCompound : An earlier handler implementation, which used one
                            artist for the line and another for the marker(s).
    """

    def create_artists(
        self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans
    ): ...

class HandlerPatch(HandlerBase):
    """
    Handler for `.Patch` instances.
    """

    def __init__(self, patch_func: None = ..., **kwargs) -> None:
        """
        Parameters
        ----------
        patch_func : callable, optional
            The function that creates the legend key artist.
            *patch_func* should have the signature::

                def patch_func(legend=legend, orig_handle=orig_handle,
                               xdescent=xdescent, ydescent=ydescent,
                               width=width, height=height, fontsize=fontsize)

            Subsequently the created artist will have its ``update_prop``
            method called and the appropriate transform will be applied.

        **kwargs
            Keyword arguments forwarded to `.HandlerBase`.
        """
        ...
    def create_artists(
        self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans
    ): ...

class HandlerStepPatch(HandlerBase):
    """
    Handler for `~.matplotlib.patches.StepPatch` instances.
    """

    def create_artists(
        self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans
    ): ...

class HandlerLineCollection(HandlerLine2D):
    """
    Handler for `.LineCollection` instances.
    """

    def get_numpoints(self, legend): ...
    def create_artists(
        self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans
    ): ...

class HandlerRegularPolyCollection(HandlerNpointsYoffsets):
    r"""Handler for `.RegularPolyCollection`\s."""
    def __init__(self, yoffsets: None = ..., sizes: None = ..., **kwargs) -> None: ...
    def get_numpoints(self, legend): ...
    def get_sizes(
        self, legend, orig_handle, xdescent, ydescent, width, height, fontsize
    ): ...
    def update_prop(self, legend_handle, orig_handle, legend): ...
    def create_collection(self, orig_handle, sizes, offsets, offset_transform): ...
    def create_artists(
        self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans
    ): ...

class HandlerPathCollection(HandlerRegularPolyCollection):
    r"""Handler for `.PathCollection`\s, which are used by `~.Axes.scatter`."""

    def create_collection(self, orig_handle, sizes, offsets, offset_transform): ...

class HandlerCircleCollection(HandlerRegularPolyCollection):
    r"""Handler for `.CircleCollection`\s."""

    def create_collection(self, orig_handle, sizes, offsets, offset_transform): ...

class HandlerErrorbar(HandlerLine2D):
    """Handler for Errorbars."""

    def __init__(
        self,
        xerr_size: float = ...,
        yerr_size: None = ...,
        marker_pad: float = ...,
        numpoints: None = ...,
        **kwargs
    ) -> None: ...
    def get_err_size(self, legend, xdescent, ydescent, width, height, fontsize): ...
    def create_artists(
        self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans
    ): ...

class HandlerStem(HandlerNpointsYoffsets):
    """
    Handler for plots produced by `~.Axes.stem`.
    """

    def __init__(
        self,
        marker_pad: float = ...,
        numpoints: None = ...,
        bottom: None = ...,
        yoffsets: None = ...,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        marker_pad : float, default: 0.3
            Padding between points in legend entry.
        numpoints : int, optional
            Number of points to show in legend entry.
        bottom : float, optional

        yoffsets : array of floats, optional
            Length *numpoints* list of y offsets for each point in
            legend entry.
        **kwargs
            Keyword arguments forwarded to `.HandlerNpointsYoffsets`.
        """
        ...
    def get_ydata(self, legend, xdescent, ydescent, width, height, fontsize): ...
    def create_artists(
        self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans
    ): ...

class HandlerTuple(HandlerBase):
    """
    Handler for Tuple.
    """

    def __init__(
        self, ndivide: Optional[int] = ..., pad: Optional[float] = ..., **kwargs
    ) -> None:
        """
        Parameters
        ----------
        ndivide : int, default: 1
            The number of sections to divide the legend area into.  If None,
            use the length of the input tuple.
        pad : float, default: :rc:`legend.borderpad`
            Padding in units of fraction of font size.
        **kwargs
            Keyword arguments forwarded to `.HandlerBase`.
        """
        ...
    def create_artists(
        self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans
    ): ...

class HandlerPolyCollection(HandlerBase):
    """
    Handler for `.PolyCollection` used in `~.Axes.fill_between` and
    `~.Axes.stackplot`.
    """

    def create_artists(
        self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans
    ): ...
