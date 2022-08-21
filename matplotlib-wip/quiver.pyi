from .collections import PolyCollection
from typing import Literal
from ._typing import *
from .backend_bases import Event, MouseEvent, RendererBase
from .figure import Figure
from .axes import Axes
from .artist import Artist, allow_rasterization

class QuiverKey(Artist):
    """Labelled arrow for use as a quiver plot scale key."""

    halign = ...
    valign = ...
    pivot = ...
    def __init__(
        self,
        Q: Quiver,
        X: float,
        Y: float,
        U: float,
        label: str,
        *,
        angle: float = 0,
        coordinates: Literal["axes", "figure", "data", "inches"] = "axes",
        color: Color = ...,
        labelsep: float = 0.1,
        labelpos: Literal["N", "S", "E", "W"] = ...,
        labelcolor: Color = ...,
        fontproperties: dict = ...,
        **kwargs
    ) -> None:
        """
        Add a key to a quiver plot.

        The positioning of the key depends on *X*, *Y*, *coordinates*, and
        *labelpos*.  If *labelpos* is 'N' or 'S', *X*, *Y* give the position of
        the middle of the key arrow.  If *labelpos* is 'E', *X*, *Y* positions
        the head, and if *labelpos* is 'W', *X*, *Y* positions the tail; in
        either of these two cases, *X*, *Y* is somewhere in the middle of the
        arrow+label key object.

        Parameters
        ----------
        Q : `Quiver`
            A `.Quiver` object as returned by a call to `~.Axes.quiver()`.
        X, Y : float
            The location of the key.
        U : float
            The length of the key.
        label : str
            The key label (e.g., length and units of the key).
        angle : float, default: 0
            The angle of the key arrow, in degrees anti-clockwise from the
            x-axis.
        coordinates : {'axes', 'figure', 'data', 'inches'}, default: 'axes'
            Coordinate system and units for *X*, *Y*: 'axes' and 'figure' are
            normalized coordinate systems with (0, 0) in the lower left and
            (1, 1) in the upper right; 'data' are the axes data coordinates
            (used for the locations of the vectors in the quiver plot itself);
            'inches' is position in the figure in inches, with (0, 0) at the
            lower left corner.
        color : color
            Overrides face and edge colors from *Q*.
        labelpos : {'N', 'S', 'E', 'W'}
            Position the label above, below, to the right, to the left of the
            arrow, respectively.
        labelsep : float, default: 0.1
            Distance in inches between the arrow and the label.
        labelcolor : color, default: :rc:`text.color`
            Label color.
        fontproperties : dict, optional
            A dictionary with keyword arguments accepted by the
            `~FontProperties` initializer:
            *family*, *style*, *variant*, *size*, *weight*.
        **kwargs
            Any additional keyword arguments are used to override vector
            properties taken from *Q*.
        """
        ...
    @property
    def labelsep(self): ...
    @allow_rasterization
    def draw(self, renderer: RendererBase): ...
    def set_figure(self, fig: Figure): ...
    def contains(self, mouseevent: MouseEvent) -> bool: ...

class Quiver(PolyCollection):
    """
    Specialized PolyCollection for arrows.

    The only API method is set_UVC(), which can be used
    to change the size, orientation, and color of the
    arrows; their locations are fixed when the class is
    instantiated.  Possibly this method will be useful
    in animations.

    Much of the work in this class is done in the draw()
    method so that as much information as possible is available
    about the plot.  In subsequent draw() calls, recalculation
    is limited to things that might have changed, so there
    should be no performance penalty from putting the calculations
    in the draw() method.
    """

    def __init__(
        self,
        a: Axes,
        *args,
        scale: float = ...,
        headwidth: float = ...,
        headlength: float = ...,
        headaxislength: float = ...,
        minshaft: float = ...,
        minlength: float = ...,
        units=...,
        scale_units=...,
        angles=...,
        width: float = ...,
        color: Color = ...,
        pivot=...,
        **kwargs
    ) -> None:
        """
        The constructor takes one required argument, an Axes
        instance, followed by the args and kwargs described
        by the following pyplot interface documentation:
        %s
        """
        ...
    def get_datalim(self, transData): ...
    @allow_rasterization
    def draw(self, renderer: RendererBase): ...
    def set_UVC(self, U, V, C=...): ...

    quiver_doc = ...

class Barbs(PolyCollection):
    """
    Specialized PolyCollection for barbs.

    The only API method is :meth:`set_UVC`, which can be used to
    change the size, orientation, and color of the arrows.  Locations
    are changed using the :meth:`set_offsets` collection method.
    Possibly this method will be useful in animations.

    There is one internal function :meth:`_find_tails` which finds
    exactly what should be put on the barb given the vector magnitude.
    From there :meth:`_make_barbs` is used to find the vertices of the
    polygon to represent the barb based on this information.
    """

    def __init__(
        self,
        ax: Axes,
        *args,
        pivot=...,
        length: float = ...,
        barbcolor: Color = ...,
        flagcolor: Color = ...,
        sizes=...,
        fill_empty=...,
        barb_increments=...,
        rounding=...,
        flip_barb=...,
        **kwargs
    ) -> None:
        """
        The constructor takes one required argument, an Axes
        instance, followed by the args and kwargs described
        by the following pyplot interface documentation:
        %(barbs_doc)s
        """
        ...
    def set_UVC(self, U, V, C=...): ...
    def set_offsets(self, xy):
        """
        Set the offsets for the barb polygons.  This saves the offsets passed
        in and masks them as appropriate for the existing U/V data.

        Parameters
        ----------
        xy : sequence of pairs of floats
        """
        ...
    barbs_doc = ...
