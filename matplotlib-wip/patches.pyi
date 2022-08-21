import numpy as np
from typing import Literal, Sequence
from ._typing import *
from .transforms import Bbox, Transform
from .path import Path
from ._enums import CapStyle, JoinStyle
from .backend_bases import MouseEvent, RendererBase
from .artist import Artist, allow_rasterization

class Patch(Artist):
    """
    A patch is a 2D artist with a face color and an edge color.

    If any of *edgecolor*, *facecolor*, *linewidth*, or *antialiased*
    are *None*, they default to their rc params setting.
    """

    zorder: float = ...

    def __init__(
        self,
        edgecolor: Color = ...,
        facecolor: Color = ...,
        color: Color = ...,
        linewidth: float = ...,
        linestyle=...,
        antialiased: bool = ...,
        hatch=...,
        fill=...,
        capstyle: CapStyle = ...,
        joinstyle: JoinStyle = ...,
        **kwargs
    ) -> None:
        """
        The following kwarg properties are supported

        %(Patch:kwdoc)s
        """
        ...
    def get_verts(self):
        """
        Return a copy of the vertices used in this patch.

        If the patch contains Bezier curves, the curves will be interpolated by
        line segments.  To access the curves as curves, use `get_path`.
        """
        ...
    def contains(self, mouseevent: MouseEvent, radius: float = ...):
        """
        Test whether the mouse event occurred in the patch.

        Returns
        -------
        (bool, empty dict)
        """
        ...
    def contains_point(self, point: Sequence[float], radius: float = ...) -> bool:
        """
        Return whether the given point is inside the patch.

        Parameters
        ----------
        point : (float, float)
            The point (x, y) to check, in target coordinates of
            ``self.get_transform()``. These are display coordinates for patches
            that are added to a figure or axes.
        radius : float, optional
            Add an additional margin on the patch in target coordinates of
            ``self.get_transform()``. See `.Path.contains_point` for further
            details.

        Returns
        -------
        bool

        Notes
        -----
        The proper use of this method depends on the transform of the patch.
        Isolated patches do not have a transform. In this case, the patch
        creation coordinates and the point coordinates match. The following
        example checks that the center of a circle is within the circle

        >>> center = 0, 0
        >>> c = Circle(center, radius=1)
        >>> c.contains_point(center)
        True

        The convention of checking against the transformed patch stems from
        the fact that this method is predominantly used to check if display
        coordinates (e.g. from mouse events) are within the patch. If you want
        to do the above check with data coordinates, you have to properly
        transform them first:

        >>> center = 0, 0
        >>> c = Circle(center, radius=1)
        >>> plt.gca().add_patch(c)
        >>> transformed_center = c.get_transform().transform(center)
        >>> c.contains_point(transformed_center)
        True

        """
        ...
    def contains_points(self, points: ArrayLike, radius: float = ...) -> list[bool]:
        """
        Return whether the given points are inside the patch.

        Parameters
        ----------
        points : (N, 2) array
            The points to check, in target coordinates of
            ``self.get_transform()``. These are display coordinates for patches
            that are added to a figure or axes. Columns contain x and y values.
        radius : float, optional
            Add an additional margin on the patch in target coordinates of
            ``self.get_transform()``. See `.Path.contains_point` for further
            details.

        Returns
        -------
        length-N bool array

        Notes
        -----
        The proper use of this method depends on the transform of the patch.
        See the notes on `.Patch.contains_point`.
        """
        ...
    def update_from(self, other: Patch): ...
    def get_extents(self) -> Bbox:
        """
        Return the `Patch`'s axis-aligned extents as a `~.transforms.Bbox`.
        """
        ...
    def get_transform(self) -> Transform:
        """Return the `~.transforms.Transform` applied to the `Patch`."""
        ...
    def get_data_transform(self) -> Transform:
        """
        Return the `~.transforms.Transform` mapping data coordinates to
        physical coordinates.
        """
        ...
    def get_patch_transform(self) -> Transform:
        """
        Return the `~.transforms.Transform` instance mapping patch coordinates
        to data coordinates.

        For example, one may define a patch of a circle which represents a
        radius of 5 by providing coordinates for a unit circle, and a
        transform which scales the coordinates (the patch coordinate) by 5.
        """
        ...
    def get_antialiased(self) -> bool:
        """Return whether antialiasing is used for drawing."""
        ...
    def get_edgecolor(self) -> Color:
        """Return the edge color."""
        ...
    def get_facecolor(self) -> Color:
        """Return the face color."""
        ...
    def get_linewidth(self) -> float:
        """Return the line width in points."""
        ...
    def get_linestyle(self):
        """Return the linestyle."""
        ...
    def set_antialiased(self, aa: bool | None):
        """
        Set whether to use antialiased rendering.

        Parameters
        ----------
        aa : bool or None
        """
        ...
    def set_edgecolor(self, color: Color | None):
        """
        Set the patch edge color.

        Parameters
        ----------
        color : color or None
        """
        ...
    def set_facecolor(self, color: Color | None):
        """
        Set the patch face color.

        Parameters
        ----------
        color : color or None
        """
        ...
    def set_color(self, c: Color):
        """
        Set both the edgecolor and the facecolor.

        Parameters
        ----------
        c : color

        See Also
        --------
        Patch.set_facecolor, Patch.set_edgecolor
            For setting the edge or face color individually.
        """
        ...
    def set_alpha(self, alpha: Scalar | None): ...
    def set_linewidth(self, w: float | None):
        """
        Set the patch linewidth in points.

        Parameters
        ----------
        w : float or None
        """
        ...
    def set_linestyle(
        self,
        ls: Literal[
            "-",
            "solid",
            "--",
            "dashed",
            "-.",
            "dashdot",
            ":",
            "dotted",
            "None",
            "none",
            " ",
            "",
        ],
    ):
        """
        Set the patch linestyle.

        ==========================================  =================
        linestyle                                   description
        ==========================================  =================
        ``'-'`` or ``'solid'``                      solid line
        ``'--'`` or  ``'dashed'``                   dashed line
        ``'-.'`` or  ``'dashdot'``                  dash-dotted line
        ``':'`` or ``'dotted'``                     dotted line
        ``'none'``, ``'None'``, ``' '``, or ``''``  draw nothing
        ==========================================  =================

        Alternatively a dash tuple of the following form can be provided::

            (offset, onoffseq)

        where ``onoffseq`` is an even length tuple of on and off ink in points.

        Parameters
        ----------
        ls : {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
            The line style.
        """
        ...
    def set_fill(self, b: bool):
        """
        Set whether to fill the patch.

        Parameters
        ----------
        b : bool
        """
        ...
    def get_fill(self) -> bool:
        """Return whether the patch is filled."""
        ...
    fill = ...

    def set_capstyle(self, s: CapStyle | Literal["butt", "projecting", "round"]):
        """
        Set the `.CapStyle`.

        The default capstyle is 'round' for `.FancyArrowPatch` and 'butt' for
        all other patches.

        Parameters
        ----------
        s : `.CapStyle` or %(CapStyle)s
        """
        ...
    def get_capstyle(self) -> CapStyle:
        """Return the capstyle."""
        ...
    def set_joinstyle(self, s: JoinStyle | Literal["miter", "round", "bevel"]):
        """
        Set the `.JoinStyle`.

        The default joinstyle is 'round' for `.FancyArrowPatch` and 'miter' for
        all other patches.

        Parameters
        ----------
        s : `.JoinStyle` or %(JoinStyle)s
        """
        ...
    def get_joinstyle(self) -> JoinStyle | str:
        """Return the joinstyle."""
        ...
    def set_hatch(
        self, hatch: Literal["/", "\\", "|", "-", "+", "x", "o", "O", ".", "*"]
    ):
        r"""
        Set the hatching pattern.

        *hatch* can be one of::

          /   - diagonal hatching
          \   - back diagonal
          |   - vertical
          -   - horizontal
          +   - crossed
          x   - crossed diagonal
          o   - small circle
          O   - large circle
          .   - dots
          *   - stars

        Letters can be combined, in which case all the specified
        hatchings are done.  If same letter repeats, it increases the
        density of hatching of that pattern.

        Hatching is supported in the PostScript, PDF, SVG and Agg
        backends only.

        Parameters
        ----------
        hatch : {'/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
        """
        ...
    def get_hatch(self) -> str:
        """Return the hatching pattern."""
        ...
    @allow_rasterization
    def draw(self, renderer: RendererBase): ...
    def get_path(self) -> Path:
        """Return the path of this patch."""
        ...
    def get_window_extent(self, renderer: RendererBase = ...): ...

class Shadow(Patch):
    def __str__(self) -> str: ...
    def __init__(self, patch: Patch, ox: float, oy: float, **kwargs) -> None:
        """
        Create a shadow of the given *patch*.

        By default, the shadow will have the same face color as the *patch*,
        but darkened.

        Parameters
        ----------
        patch : `.Patch`
            The patch to create the shadow for.
        ox, oy : float
            The shift of the shadow in data coordinates, scaled by a factor
            of dpi/72.
        **kwargs
            Properties of the shadow patch. Supported keys are:

            %(Patch:kwdoc)s
        """
        ...
    def get_path(self) -> Path: ...
    def get_patch_transform(self) -> Transform: ...
    def draw(self, renderer: RendererBase): ...

class Rectangle(Patch):
    """
    A rectangle defined via an anchor point *xy* and its *width* and *height*.

    The rectangle extends from ``xy[0]`` to ``xy[0] + width`` in x-direction
    and from ``xy[1]`` to ``xy[1] + height`` in y-direction. ::

      :                +------------------+
      :                |                  |
      :              height               |
      :                |                  |
      :               (xy)---- width -----+

    One may picture *xy* as the bottom left corner, but which corner *xy* is
    actually depends on the direction of the axis and the sign of *width*
    and *height*; e.g. *xy* would be the bottom right corner if the x-axis
    was inverted or if *width* was negative.
    """

    def __str__(self) -> str: ...
    def __init__(
        self,
        xy: Sequence[float],
        width: float,
        height: float,
        angle: float = 0,
        *,
        rotation_point: Literal["xy", "center"] | Sequence[float] = "xy",
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        xy : (float, float)
            The anchor point.
        width : float
            Rectangle width.
        height : float
            Rectangle height.
        angle : float, default: 0
            Rotation in degrees anti-clockwise about the rotation point.
        rotation_point : {'xy', 'center', (number, number)}, default: 'xy'
            If ``'xy'``, rotate around the anchor point. If ``'center'`` rotate
            around the center. If 2-tuple of number, rotate around this
            coordinate.

        Other Parameters
        ----------------
        **kwargs : `.Patch` properties
            %(Patch:kwdoc)s
        """
        ...
    def get_path(self) -> Path:
        """Return the vertices of the rectangle."""
        ...
    def get_patch_transform(self): ...
    @property
    def rotation_point(self):
        """The rotation point of the patch."""
        ...
    @rotation_point.setter
    def rotation_point(self, value): ...
    def get_x(self) -> float:
        """Return the left coordinate of the rectangle."""
        ...
    def get_y(self) -> float:
        """Return the bottom coordinate of the rectangle."""
        ...
    def get_xy(self) -> tuple[float, float]:
        """Return the left and bottom coords of the rectangle as a tuple."""
        ...
    def get_corners(self) -> list[tuple[float, float]]:
        """
        Return the corners of the rectangle, moving anti-clockwise from
        (x0, y0).
        """
        ...
    def get_center(self) -> tuple[float, float]:
        """Return the centre of the rectangle."""
        ...
    def get_width(self) -> float:
        """Return the width of the rectangle."""
        ...
    def get_height(self) -> float:
        """Return the height of the rectangle."""
        ...
    def get_angle(self) -> float:
        """Get the rotation angle in degrees."""
        ...
    def set_x(self, x: float):
        """Set the left coordinate of the rectangle."""
        ...
    def set_y(self, y: float):
        """Set the bottom coordinate of the rectangle."""
        ...
    def set_angle(self, angle: float):
        """
        Set the rotation angle in degrees.

        The rotation is performed anti-clockwise around *xy*.
        """
        ...
    def set_xy(self, xy: Sequence[float]):
        """
        Set the left and bottom coordinates of the rectangle.

        Parameters
        ----------
        xy : (float, float)
        """
        ...
    def set_width(self, w: float):
        """Set the width of the rectangle."""
        ...
    def set_height(self, h: float):
        """Set the height of the rectangle."""
        ...
    def set_bounds(self, *args):
        """
        Set the bounds of the rectangle as *left*, *bottom*, *width*, *height*.

        The values may be passed as separate parameters or as a tuple::

            set_bounds(left, bottom, width, height)
            set_bounds((left, bottom, width, height))

        .. ACCEPTS: (left, bottom, width, height)
        """
        ...
    def get_bbox(self) -> Bbox:
        """Return the `.Bbox`."""
        ...
    xy: tuple[float, float] = ...

class RegularPolygon(Patch):
    """A regular polygon patch."""

    def __str__(self) -> str: ...
    def __init__(
        self,
        xy: Sequence[float],
        numVertices: int,
        radius: float = ...,
        orientation: float = ...,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        xy : (float, float)
            The center position.

        numVertices : int
            The number of vertices.

        radius : float
            The distance from the center to each of the vertices.

        orientation : float
            The polygon rotation angle (in radians).

        **kwargs
            `Patch` properties:

            %(Patch:kwdoc)s
        """
        ...
    def get_path(self) -> Path: ...
    def get_patch_transform(self) -> Transform: ...

class PathPatch(Patch):
    """A general polycurve path patch."""

    def __str__(self) -> str: ...
    def __init__(self, path: Path, **kwargs) -> None:
        """
        *path* is a `~.path.Path` object.

        Valid keyword arguments are:

        %(Patch:kwdoc)s
        """
        ...
    def get_path(self) -> Path: ...
    def set_path(self, path: Path): ...

class StepPatch(PathPatch):
    """
    A path patch describing a stepwise constant function.

    By default the path is not closed and starts and stops at
    baseline value.
    """

    def __init__(
        self,
        values: ArrayLike,
        edges: ArrayLike,
        *,
        orientation: Literal["vertical", "horizontal"] = "vertical",
        baseline: float | ArrayLike | None = 0,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        values : array-like
            The step heights.

        edges : array-like
            The edge positions, with ``len(edges) == len(vals) + 1``,
            between which the curve takes on vals values.

        orientation : {'vertical', 'horizontal'}, default: 'vertical'
            The direction of the steps. Vertical means that *values* are
            along the y-axis, and edges are along the x-axis.

        baseline : float, array-like or None, default: 0
            The bottom value of the bounding edges or when
            ``fill=True``, position of lower edge. If *fill* is
            True or an array is passed to *baseline*, a closed
            path is drawn.

        Other valid keyword arguments are:

        %(Patch:kwdoc)s
        """
        ...
    def get_data(self):
        """Get `.StepPatch` values, edges and baseline as namedtuple."""
        ...
    def set_data(
        self,
        values: ArrayLike | None = ...,
        edges: ArrayLike = ...,
        baseline: float | ArrayLike | None = ...,
    ):
        """
        Set `.StepPatch` values, edges and baseline.

        Parameters
        ----------
        values : 1D array-like or None
            Will not update values, if passing None
        edges : 1D array-like, optional
        baseline : float, 1D array-like or None
        """
        ...

class Polygon(Patch):
    """A general polygon patch."""

    def __str__(self) -> str: ...
    def __init__(self, xy: Sequence[float], closed: bool = ..., **kwargs) -> None:
        """
        *xy* is a numpy array with shape Nx2.

        If *closed* is *True*, the polygon will be closed so the
        starting and ending points are the same.

        Valid keyword arguments are:

        %(Patch:kwdoc)s
        """
        ...
    def get_path(self) -> Path:
        """Get the `.Path` of the polygon."""
        ...
    def get_closed(self) -> bool:
        """Return whether the polygon is closed."""
        ...
    def set_closed(self, closed: bool):
        """
        Set whether the polygon is closed.

        Parameters
        ----------
        closed : bool
           True if the polygon is closed
        """
        ...
    def get_xy(self) -> np.ndarray:
        """
        Get the vertices of the path.

        Returns
        -------
        (N, 2) numpy array
            The coordinates of the vertices.
        """
        ...
    def set_xy(self, xy: ArrayLike):
        """
        Set the vertices of the polygon.

        Parameters
        ----------
        xy : (N, 2) array-like
            The coordinates of the vertices.

        Notes
        -----
        Unlike `~.path.Path`, we do not ignore the last input vertex. If the
        polygon is meant to be closed, and the last point of the polygon is not
        equal to the first, we assume that the user has not explicitly passed a
        ``CLOSEPOLY`` vertex, and add it ourselves.
        """
        ...
    xy = ...

class Wedge(Patch):
    """Wedge shaped patch."""

    def __str__(self) -> str: ...
    def __init__(
        self,
        center: Sequence[float],
        r: float,
        theta1: float,
        theta2: float,
        width: float = ...,
        **kwargs
    ) -> None:
        """
        A wedge centered at *x*, *y* center with radius *r* that
        sweeps *theta1* to *theta2* (in degrees).  If *width* is given,
        then a partial wedge is drawn from inner radius *r* - *width*
        to outer radius *r*.

        Valid keyword arguments are:

        %(Patch:kwdoc)s
        """
        ...
    def set_center(self, center: Sequence[float]): ...
    def set_radius(self, radius: float): ...
    def set_theta1(self, theta1: float): ...
    def set_theta2(self, theta2: float): ...
    def set_width(self, widt: float): ...
    def get_path(self) -> Path: ...

class Arrow(Patch):
    """An arrow patch."""

    def __str__(self) -> str: ...
    def __init__(
        self, x: float, y: float, dx: float, dy: float, width: float = ..., **kwargs
    ) -> None:
        """
        Draws an arrow from (*x*, *y*) to (*x* + *dx*, *y* + *dy*).
        The width of the arrow is scaled by *width*.

        Parameters
        ----------
        x : float
            x coordinate of the arrow tail.
        y : float
            y coordinate of the arrow tail.
        dx : float
            Arrow length in the x direction.
        dy : float
            Arrow length in the y direction.
        width : float, default: 1
            Scale factor for the width of the arrow. With a default value of 1,
            the tail width is 0.2 and head width is 0.6.
        **kwargs
            Keyword arguments control the `Patch` properties:

            %(Patch:kwdoc)s

        See Also
        --------
        FancyArrow
            Patch that allows independent control of the head and tail
            properties.
        """
        ...
    def get_path(self) -> Path: ...
    def get_patch_transform(self) -> Transform: ...

class FancyArrow(Polygon):
    """
    Like Arrow, but lets you set head width and head height independently.
    """

    def __str__(self) -> str: ...
    def __init__(
        self,
        x: float,
        y: float,
        dx: float,
        dy: float,
        width: float = 0.001,
        length_includes_head: bool = False,
        head_width: float = ...,
        head_length: float | None = ...,
        shape: Literal["full", "left", "right"] = "full",
        overhang: float = 0,
        head_starts_at_zero: bool = False,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        x, y : float
            The x and y coordinates of the arrow base.

        dx, dy : float
            The length of the arrow along x and y direction.

        width : float, default: 0.001
            Width of full arrow tail.

        length_includes_head : bool, default: False
            True if head is to be counted in calculating the length.

        head_width : float or None, default: 3*width
            Total width of the full arrow head.

        head_length : float or None, default: 1.5*head_width
            Length of arrow head.

        shape : {'full', 'left', 'right'}, default: 'full'
            Draw the left-half, right-half, or full arrow.

        overhang : float, default: 0
            Fraction that the arrow is swept back (0 overhang means
            triangular shape). Can be negative or greater than one.

        head_starts_at_zero : bool, default: False
            If True, the head starts being drawn at coordinate 0
            instead of ending at coordinate 0.

        **kwargs
            `.Patch` properties:

            %(Patch:kwdoc)s
        """
        ...
    def set_data(
        self,
        *,
        x: float | None = None,
        y: float | None = None,
        dx: float | None = None,
        dy: float | None = None,
        width: float | None = None,
        head_width: float | None = None,
        head_length: float | None = None
    ):
        """
        Set `.FancyArrow` x, y, dx, dy, width, head_with, and head_length.
        Values left as None will not be updated.

        Parameters
        ----------
        x, y : float or None, default: None
            The x and y coordinates of the arrow base.

        dx, dy : float or None, default: None
            The length of the arrow along x and y direction.

        width : float or None, default: None
            Width of full arrow tail.

        head_width : float or None, default: None
            Total width of the full arrow head.

        head_length : float or None, default: None
            Length of arrow head.
        """
        ...

class CirclePolygon(RegularPolygon):
    """A polygon-approximation of a circle patch."""

    def __str__(self) -> str: ...
    def __init__(
        self, xy: Sequence[float], radius: float = ..., resolution=..., **kwargs
    ) -> None:
        """
        Create a circle at *xy* = (*x*, *y*) with given *radius*.

        This circle is approximated by a regular polygon with *resolution*
        sides.  For a smoother circle drawn with splines, see `Circle`.

        Valid keyword arguments are:

        %(Patch:kwdoc)s
        """
        ...

class Ellipse(Patch):
    """A scale-free ellipse."""

    def __str__(self) -> str: ...
    def __init__(
        self,
        xy: Sequence[float],
        width: float,
        height: float,
        angle: float = 0,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        xy : (float, float)
            xy coordinates of ellipse centre.
        width : float
            Total length (diameter) of horizontal axis.
        height : float
            Total length (diameter) of vertical axis.
        angle : float, default: 0
            Rotation in degrees anti-clockwise.

        Notes
        -----
        Valid keyword arguments are:

        %(Patch:kwdoc)s
        """
        ...
    def get_path(self) -> Path:
        """Return the path of the ellipse."""
        ...
    def get_patch_transform(self) -> Transform: ...
    def set_center(self, xy: Sequence[float]):
        """
        Set the center of the ellipse.

        Parameters
        ----------
        xy : (float, float)
        """
        ...
    def get_center(self) -> tuple[float, float]:
        """Return the center of the ellipse."""
        ...
    center = ...
    def set_width(self, width: float):
        """
        Set the width of the ellipse.

        Parameters
        ----------
        width : float
        """
        ...
    def get_width(self) -> float:
        """
        Return the width of the ellipse.
        """
        ...
    width = ...
    def set_height(self, height: float):
        """
        Set the height of the ellipse.

        Parameters
        ----------
        height : float
        """
        ...
    def get_height(self) -> float:
        """Return the height of the ellipse."""
        ...
    height = ...
    def set_angle(self, angle: float):
        """
        Set the angle of the ellipse.

        Parameters
        ----------
        angle : float
        """
        ...
    def get_angle(self) -> float:
        """Return the angle of the ellipse."""
        ...
    angle = ...
    def get_corners(self):
        """
        Return the corners of the ellipse bounding box.

        The bounding box orientation is moving anti-clockwise from the
        lower left corner defined before rotation.
        """
        ...

class Annulus(Patch):
    """
    An elliptical annulus.
    """

    def __init__(
        self,
        xy: Sequence[float],
        r: float | Sequence[float],
        width: float,
        angle: float = 0,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        xy : (float, float)
            xy coordinates of annulus centre.
        r : float or (float, float)
            The radius, or semi-axes:

            - If float: radius of the outer circle.
            - If two floats: semi-major and -minor axes of outer ellipse.
        width : float
            Width (thickness) of the annular ring. The width is measured inward
            from the outer ellipse so that for the inner ellipse the semi-axes
            are given by ``r - width``. *width* must be less than or equal to
            the semi-minor axis.
        angle : float, default: 0
            Rotation angle in degrees (anti-clockwise from the positive
            x-axis). Ignored for circular annuli (i.e., if *r* is a scalar).
        **kwargs
            Keyword arguments control the `Patch` properties:

            %(Patch:kwdoc)s
        """
        ...
    def __str__(self) -> str: ...
    def set_center(self, xy: Sequence[float]):
        """
        Set the center of the annulus.

        Parameters
        ----------
        xy : (float, float)
        """
        ...
    def get_center(self) -> tuple[float, float]:
        """Return the center of the annulus."""
        ...
    center = ...
    def set_width(self, width: float):
        """
        Set the width (thickness) of the annulus ring.

        The width is measured inwards from the outer ellipse.

        Parameters
        ----------
        width : float
        """
        ...
    def get_width(self) -> float:
        """Return the width (thickness) of the annulus ring."""
        ...
    width = ...
    def set_angle(self, angle: float):
        """
        Set the tilt angle of the annulus.

        Parameters
        ----------
        angle : float
        """
        ...
    def get_angle(self) -> float:
        """Return the angle of the annulus."""
        ...
    angle = ...
    def set_semimajor(self, a: float):
        """
        Set the semi-major axis *a* of the annulus.

        Parameters
        ----------
        a : float
        """
        ...
    def set_semiminor(self, b: float):
        """
        Set the semi-minor axis *b* of the annulus.

        Parameters
        ----------
        b : float
        """
        ...
    def set_radii(self, r: float):
        """
        Set the semi-major (*a*) and semi-minor radii (*b*) of the annulus.

        Parameters
        ----------
        r : float or (float, float)
            The radius, or semi-axes:

            - If float: radius of the outer circle.
            - If two floats: semi-major and -minor axes of outer ellipse.
        """
        ...
    def get_radii(self) -> float:
        """Return the semi-major and semi-minor radii of the annulus."""
        ...
    radii = ...
    def get_path(self) -> Path: ...

class Circle(Ellipse):
    """
    A circle patch.
    """

    def __str__(self) -> str: ...
    def __init__(self, xy: Sequence[float], radius: float = ..., **kwargs) -> None:
        """
        Create a true circle at center *xy* = (*x*, *y*) with given *radius*.

        Unlike `CirclePolygon` which is a polygonal approximation, this uses
        Bezier splines and is much closer to a scale-free circle.

        Valid keyword arguments are:

        %(Patch:kwdoc)s
        """
        ...
    def set_radius(self, radius: float):
        """
        Set the radius of the circle.

        Parameters
        ----------
        radius : float
        """
        ...
    def get_radius(self) -> float:
        """Return the radius of the circle."""
        ...
    radius: float = ...

class Arc(Ellipse):
    """
    An elliptical arc, i.e. a segment of an ellipse.

    Due to internal optimizations, there are certain restrictions on using Arc:

    - The arc cannot be filled.

    - The arc must be used in an `~.axes.Axes` instance. It can not be added
      directly to a `.Figure` because it is optimized to only render the
      segments that are inside the axes bounding box with high resolution.
    """

    def __str__(self) -> str: ...
    def __init__(
        self,
        xy: Sequence[float],
        width: float,
        height: float,
        angle: float = 0,
        theta1: float = 0,
        theta2: float = 360,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        xy : (float, float)
            The center of the ellipse.

        width : float
            The length of the horizontal axis.

        height : float
            The length of the vertical axis.

        angle : float
            Rotation of the ellipse in degrees (counterclockwise).

        theta1, theta2 : float, default: 0, 360
            Starting and ending angles of the arc in degrees. These values
            are relative to *angle*, e.g. if *angle* = 45 and *theta1* = 90
            the absolute starting angle is 135.
            Default *theta1* = 0, *theta2* = 360, i.e. a complete ellipse.
            The arc is drawn in the counterclockwise direction.
            Angles greater than or equal to 360, or smaller than 0, are
            represented by an equivalent angle in the range [0, 360), by
            taking the input value mod 360.

        Other Parameters
        ----------------
        **kwargs : `.Patch` properties
            Most `.Patch` properties are supported as keyword arguments,
            with the exception of *fill* and *facecolor* because filling is
            not supported.

        %(Patch:kwdoc)s
        """
        ...
    @allow_rasterization
    def draw(self, renderer: RendererBase):
        """
        Draw the arc to the given *renderer*.

        Notes
        -----
        Ellipses are normally drawn using an approximation that uses
        eight cubic Bezier splines.  The error of this approximation
        is 1.89818e-6, according to this unverified source:

          Lancaster, Don.  *Approximating a Circle or an Ellipse Using
          Four Bezier Cubic Splines.*

          https://www.tinaja.com/glib/ellipse4.pdf

        There is a use case where very large ellipses must be drawn
        with very high accuracy, and it is too expensive to render the
        entire ellipse with enough segments (either splines or line
        segments).  Therefore, in the case where either radius of the
        ellipse is large enough that the error of the spline
        approximation will be visible (greater than one pixel offset
        from the ideal), a different technique is used.

        In that case, only the visible parts of the ellipse are drawn,
        with each visible arc using a fixed number of spline segments
        (8).  The algorithm proceeds as follows:

        1. The points where the ellipse intersects the axes bounding
           box are located.  (This is done be performing an inverse
           transformation on the axes bbox such that it is relative
           to the unit circle -- this makes the intersection
           calculation much easier than doing rotated ellipse
           intersection directly).

           This uses the "line intersecting a circle" algorithm from:

               Vince, John.  *Geometry for Computer Graphics: Formulae,
               Examples & Proofs.*  London: Springer-Verlag, 2005.

        2. The angles of each of the intersection points are calculated.

        3. Proceeding counterclockwise starting in the positive
           x-direction, each of the visible arc-segments between the
           pairs of vertices are drawn using the Bezier arc
           approximation technique implemented in `.Path.arc`.
        """
        ...

def bbox_artist(artist, renderer: RendererBase, props: dict = ..., fill=...):
    """
    A debug function to draw a rectangle around the bounding
    box returned by an artist's `.Artist.get_window_extent`
    to test whether the artist is returning the correct bbox.

    *props* is a dict of rectangle props with the additional property
    'pad' that sets the padding around the bbox in points.
    """
    ...

def draw_bbox(bbox, renderer: RendererBase, color: Color = ..., trans: Transform = ...):
    """
    A debug function to draw a rectangle around the bounding
    box returned by an artist's `.Artist.get_window_extent`
    to test whether the artist is returning the correct bbox.
    """
    ...

class _Style:
    """
    A base class for the Styles. It is meant to be a container class,
    where actual styles are declared as subclass of it, and it
    provides some helper functions.
    """

    def __new__(cls, stylename: str, **kwargs):
        """Return the instance of the subclass with the given style name."""
        ...
    @classmethod
    def get_styles(cls):
        """Return a dictionary of available styles."""
        ...
    @classmethod
    def pprint_styles(cls):
        """Return the available styles as pretty-printed string."""
        ...
    @classmethod
    def register(cls, name: str, style: _Style):
        """Register a new style."""
        ...

class BoxStyle(_Style):
    """
    `BoxStyle` is a container class which defines several
    boxstyle classes, which are used for `FancyBboxPatch`.

    A style object can be created as::

           BoxStyle.Round(pad=0.2)

    or::

           BoxStyle("Round", pad=0.2)

    or::

           BoxStyle("Round, pad=0.2")

    The following boxstyle classes are defined.

    %(AvailableBoxstyles)s

    An instance of a boxstyle class is a callable object, with the signature ::

       __call__(self, x0, y0, width, height, mutation_size) -> Path

    *x0*, *y0*, *width* and *height* specify the location and size of the box
    to be drawn; *mutation_size* scales the outline properties such as padding.
    """

    class Square:
        """A square box."""

        def __init__(self, pad: float = 0.3) -> None:
            """
            Parameters
            ----------
            pad : float, default: 0.3
                The amount of padding around the original box.
            """
            ...
        def __call__(
            self, x0: float, y0: float, width: float, height: float, mutation_size
        ): ...

    class Circle:
        """A circular box."""

        def __init__(self, pad: float = 0.3) -> None:
            """
            Parameters
            ----------
            pad : float, default: 0.3
                The amount of padding around the original box.
            """
            ...
        def __call__(
            self, x0: float, y0: float, width: float, height: float, mutation_size
        ): ...

    class LArrow:
        """A box in the shape of a left-pointing arrow."""

        def __init__(self, pad: float = 0.3) -> None:
            """
            Parameters
            ----------
            pad : float, default: 0.3
                The amount of padding around the original box.
            """
            ...
        def __call__(self, x0, y0, width, height, mutation_size): ...

    class RArrow(LArrow):
        """A box in the shape of a right-pointing arrow."""

        def __call__(
            self, x0: float, y0: float, width: float, height: float, mutation_size
        ): ...

    class DArrow:
        """A box in the shape of a two-way arrow."""

        def __init__(self, pad: float = 0.3) -> None:
            """
            Parameters
            ----------
            pad : float, default: 0.3
                The amount of padding around the original box.
            """
            ...
        def __call__(
            self, x0: float, y0: float, width: float, height: float, mutation_size
        ): ...

    class Round:
        """A box with round corners."""

        def __init__(self, pad=0.3, rounding_size: float = ...) -> None:
            """
            Parameters
            ----------
            pad : float, default: 0.3
                The amount of padding around the original box.
            rounding_size : float, default: *pad*
                Radius of the corners.
            """
            ...
        def __call__(
            self, x0: float, y0: float, width: float, height: float, mutation_size
        ): ...

    class Round4:
        """A box with rounded edges."""

        def __init__(self, pad: float = 0.3, rounding_size: float = ...) -> None:
            """
            Parameters
            ----------
            pad : float, default: 0.3
                The amount of padding around the original box.
            rounding_size : float, default: *pad*/2
                Rounding of edges.
            """
            ...
        def __call__(
            self, x0: float, y0: float, width: float, height: float, mutation_size
        ): ...

    class Sawtooth:
        """A box with a sawtooth outline."""

        def __init__(self, pad: float = 0.3, tooth_size: float = ...) -> None:
            """
            Parameters
            ----------
            pad : float, default: 0.3
                The amount of padding around the original box.
            tooth_size : float, default: *pad*/2
                Size of the sawtooth.
            """
            ...
        def __call__(
            self, x0: float, y0: float, width: float, height: float, mutation_size
        ): ...

    class Roundtooth(Sawtooth):
        """A box with a rounded sawtooth outline."""

        def __call__(
            self, x0: float, y0: float, width: float, height: float, mutation_size
        ): ...

class ConnectionStyle(_Style):
    """
    `ConnectionStyle` is a container class which defines
    several connectionstyle classes, which is used to create a path
    between two points.  These are mainly used with `FancyArrowPatch`.

    A connectionstyle object can be either created as::

           ConnectionStyle.Arc3(rad=0.2)

    or::

           ConnectionStyle("Arc3", rad=0.2)

    or::

           ConnectionStyle("Arc3, rad=0.2")

    The following classes are defined

    %(AvailableConnectorstyles)s

    An instance of any connection style class is an callable object,
    whose call signature is::

        __call__(self, posA, posB,
                 patchA=None, patchB=None,
                 shrinkA=2., shrinkB=2.)

    and it returns a `.Path` instance. *posA* and *posB* are
    tuples of (x, y) coordinates of the two points to be
    connected. *patchA* (or *patchB*) is given, the returned path is
    clipped so that it start (or end) from the boundary of the
    patch. The path is further shrunk by *shrinkA* (or *shrinkB*)
    which is given in points.
    """

    class _Base:
        """
        A base class for connectionstyle classes. The subclass needs
        to implement a *connect* method whose call signature is::

          connect(posA, posB)

        where posA and posB are tuples of x, y coordinates to be
        connected.  The method needs to return a path connecting two
        points. This base class defines a __call__ method, and a few
        helper methods.
        """

        class SimpleEvent:
            def __init__(self, xy: Sequence[float]) -> None: ...

        def __call__(
            self, posA, posB, shrinkA=..., shrinkB=..., patchA=..., patchB=...
        ):
            """
            Call the *connect* method to create a path between *posA* and
            *posB*; then clip and shrink the path.
            """
            ...

    class Arc3(_Base):
        """
        Creates a simple quadratic Bezier curve between two
        points. The curve is created so that the middle control point
        (C1) is located at the same distance from the start (C0) and
        end points(C2) and the distance of the C1 to the line
        connecting C0-C2 is *rad* times the distance of C0-C2.
        """

        def __init__(self, rad=...) -> None:
            """
            *rad*
              curvature of the curve.
            """
            ...
        def connect(self, posA, posB): ...

    class Angle3(_Base):
        """
        Creates a simple quadratic Bezier curve between two
        points. The middle control points is placed at the
        intersecting point of two lines which cross the start and
        end point, and have a slope of angleA and angleB, respectively.
        """

        def __init__(self, angleA: float = ..., angleB: float = ...) -> None:
            """
            *angleA*
              starting angle of the path

            *angleB*
              ending angle of the path
            """
            ...
        def connect(self, posA, posB): ...

    class Angle(_Base):
        """
        Creates a piecewise continuous quadratic Bezier path between
        two points. The path has a one passing-through point placed at
        the intersecting point of two lines which cross the start
        and end point, and have a slope of angleA and angleB, respectively.
        The connecting edges are rounded with *rad*.
        """

        def __init__(
            self, angleA: float = ..., angleB: float = ..., rad: float = ...
        ) -> None:
            """
            *angleA*
              starting angle of the path

            *angleB*
              ending angle of the path

            *rad*
              rounding radius of the edge
            """
            ...
        def connect(self, posA, posB): ...

    class Arc(_Base):
        """
        Creates a piecewise continuous quadratic Bezier path between
        two points. The path can have two passing-through points, a
        point placed at the distance of armA and angle of angleA from
        point A, another point with respect to point B. The edges are
        rounded with *rad*.
        """

        def __init__(
            self,
            angleA: float = ...,
            angleB: float = ...,
            armA: float = ...,
            armB: float = ...,
            rad: float = ...,
        ) -> None:
            """
            *angleA* :
              starting angle of the path

            *angleB* :
              ending angle of the path

            *armA* :
              length of the starting arm

            *armB* :
              length of the ending arm

            *rad* :
              rounding radius of the edges
            """
            ...
        def connect(self, posA, posB): ...

    class Bar(_Base):
        """
        A line with *angle* between A and B with *armA* and
        *armB*. One of the arms is extended so that they are connected in
        a right angle. The length of armA is determined by (*armA*
        + *fraction* x AB distance). Same for armB.
        """

        def __init__(
            self,
            armA: float = ...,
            armB: float = ...,
            fraction: float = ...,
            angle: float = ...,
        ) -> None:
            """
            Parameters
            ----------
            armA : float
                minimum length of armA

            armB : float
                minimum length of armB

            fraction : float
                a fraction of the distance between two points that
                will be added to armA and armB.

            angle : float or None
                angle of the connecting line (if None, parallel
                to A and B)
            """
            ...
        def connect(self, posA, posB): ...

class ArrowStyle(_Style):
    """
    `ArrowStyle` is a container class which defines several
    arrowstyle classes, which is used to create an arrow path along a
    given path.  These are mainly used with `FancyArrowPatch`.

    A arrowstyle object can be either created as::

           ArrowStyle.Fancy(head_length=.4, head_width=.4, tail_width=.4)

    or::

           ArrowStyle("Fancy", head_length=.4, head_width=.4, tail_width=.4)

    or::

           ArrowStyle("Fancy, head_length=.4, head_width=.4, tail_width=.4")

    The following classes are defined

    %(AvailableArrowstyles)s

    An instance of any arrow style class is a callable object,
    whose call signature is::

        __call__(self, path, mutation_size, linewidth, aspect_ratio=1.)

    and it returns a tuple of a `.Path` instance and a boolean
    value. *path* is a `.Path` instance along which the arrow
    will be drawn. *mutation_size* and *aspect_ratio* have the same
    meaning as in `BoxStyle`. *linewidth* is a line width to be
    stroked. This is meant to be used to correct the location of the
    head so that it does not overshoot the destination point, but not all
    classes support it.
    """

    class _Base:
        """
        Arrow Transmuter Base class

        ArrowTransmuterBase and its derivatives are used to make a fancy
        arrow around a given path. The __call__ method returns a path
        (which will be used to create a PathPatch instance) and a boolean
        value indicating the path is open therefore is not fillable.  This
        class is not an artist and actual drawing of the fancy arrow is
        done by the FancyArrowPatch class.
        """

        @staticmethod
        def ensure_quadratic_bezier(path: Path):
            """
            Some ArrowStyle classes only works with a simple quadratic
            Bezier curve (created with `.ConnectionStyle.Arc3` or
            `.ConnectionStyle.Angle3`). This static method checks if the
            provided path is a simple quadratic Bezier curve and returns its
            control points if true.
            """
            ...
        def transmute(self, path: Path, mutation_size, linewidth: float):
            """
            The transmute method is the very core of the ArrowStyle class and
            must be overridden in the subclasses. It receives the path object
            along which the arrow will be drawn, and the mutation_size, with
            which the arrow head etc. will be scaled. The linewidth may be
            used to adjust the path so that it does not pass beyond the given
            points. It returns a tuple of a Path instance and a boolean. The
            boolean value indicate whether the path can be filled or not. The
            return value can also be a list of paths and list of booleans of a
            same length.
            """
            ...
        def __call__(
            self, path: Path, mutation_size, linewidth: float, aspect_ratio: float = ...
        ):
            """
            The __call__ method is a thin wrapper around the transmute method
            and takes care of the aspect ratio.
            """
            ...

    class _Curve(_Base):
        """
        A simple arrow which will work with any path instance. The
        returned path is the concatenation of the original path, and at
        most two paths representing the arrow head or bracket at the begin
        point and at the end point. The arrow heads can be either open
        or closed.
        """

        beginarrow = ...
        arrow = ...
        fillbegin = ...
        def __init__(
            self,
            head_length: float = ...,
            head_width: float = ...,
            widthA: float = ...,
            widthB: float = ...,
            lengthA: float = ...,
            lengthB: float = ...,
            angleA: float = ...,
            angleB: float = ...,
            scaleA: float = ...,
            scaleB: float = ...,
        ) -> None:
            """
            Parameters
            ----------
            head_length : float, default: 0.4
                Length of the arrow head, relative to *mutation_scale*.
            head_width : float, default: 0.2
                Width of the arrow head, relative to *mutation_scale*.
            widthA : float, default: 1.0
                Width of the bracket at the beginning of the arrow
            widthB : float, default: 1.0
                Width of the bracket at the end of the arrow
            lengthA : float, default: 0.2
                Length of the bracket at the beginning of the arrow
            lengthB : float, default: 0.2
                Length of the bracket at the end of the arrow
            angleA : float, default 0
                Orientation of the bracket at the beginning, as a
                counterclockwise angle. 0 degrees means perpendicular
                to the line.
            angleB : float, default 0
                Orientation of the bracket at the beginning, as a
                counterclockwise angle. 0 degrees means perpendicular
                to the line.
            scaleA : float, default *mutation_size*
                The mutation_size for the beginning bracket
            scaleB : float, default *mutation_size*
                The mutation_size for the end bracket
            """
            ...
        def transmute(self, path, mutation_size, linewidth): ...

    class Curve(_Curve):
        """A simple curve without any arrow head."""

        def __init__(self) -> None: ...

    class CurveA(_Curve):
        """An arrow with a head at its begin point."""

        arrow = ...

    class CurveB(_Curve):
        """An arrow with a head at its end point."""

        arrow = ...

    class CurveAB(_Curve):
        """An arrow with heads both at the begin and the end point."""

        arrow = ...

    class CurveFilledA(_Curve):
        """An arrow with filled triangle head at the begin."""

        arrow = ...

    class CurveFilledB(_Curve):
        """An arrow with filled triangle head at the end."""

        arrow = ...

    class CurveFilledAB(_Curve):
        """An arrow with filled triangle heads at both ends."""

        arrow = ...

    class BracketA(_Curve):
        """An arrow with an outward square bracket at its start."""

        arrow = ...
        def __init__(
            self, widthA: float = ..., lengthA: float = ..., angleA: float = ...
        ) -> None:
            """
            Parameters
            ----------
            widthA : float, default: 1.0
                Width of the bracket.
            lengthA : float, default: 0.2
                Length of the bracket.
            angleA : float, default: 0 degrees
                Orientation of the bracket, as a counterclockwise angle.
                0 degrees means perpendicular to the line.
            """
            ...

    class BracketB(_Curve):
        """An arrow with an outward square bracket at its end."""

        arrow = ...
        def __init__(
            self, widthB: float = ..., lengthB: float = ..., angleB: float = ...
        ) -> None:
            """
            Parameters
            ----------
            widthB : float, default: 1.0
                Width of the bracket.
            lengthB : float, default: 0.2
                Length of the bracket.
            angleB : float, default: 0 degrees
                Orientation of the bracket, as a counterclockwise angle.
                0 degrees means perpendicular to the line.
            """
            ...

    class BracketAB(_Curve):
        """An arrow with outward square brackets at both ends."""

        arrow = ...
        def __init__(
            self,
            widthA: float = ...,
            lengthA: float = ...,
            angleA: float = ...,
            widthB: float = ...,
            lengthB: float = ...,
            angleB: float = ...,
        ) -> None:
            """
            Parameters
            ----------
            widthA, widthB : float, default: 1.0
                Width of the bracket.
            lengthA, lengthB : float, default: 0.2
                Length of the bracket.
            angleA, angleB : float, default: 0 degrees
                Orientation of the bracket, as a counterclockwise angle.
                0 degrees means perpendicular to the line.
            """
            ...

    class BarAB(_Curve):
        """An arrow with vertical bars ``|`` at both ends."""

        arrow = ...
        def __init__(
            self,
            widthA: float = ...,
            angleA: float = ...,
            widthB: float = ...,
            angleB: float = ...,
        ) -> None:
            """
            Parameters
            ----------
            widthA, widthB : float, default: 1.0
                Width of the bracket.
            angleA, angleB : float, default: 0 degrees
                Orientation of the bracket, as a counterclockwise angle.
                0 degrees means perpendicular to the line.
            """
            ...

    class BracketCurve(_Curve):
        """
        An arrow with an outward square bracket at its start and a head at
        the end.
        """

        arrow = ...
        def __init__(
            self, widthA: float = ..., lengthA: float = ..., angleA: float = ...
        ) -> None:
            """
            Parameters
            ----------
            widthA : float, default: 1.0
                Width of the bracket.
            lengthA : float, default: 0.2
                Length of the bracket.
            angleA : float, default: 0 degrees
                Orientation of the bracket, as a counterclockwise angle.
                0 degrees means perpendicular to the line.
            """
            ...

    class CurveBracket(_Curve):
        """
        An arrow with an outward square bracket at its end and a head at
        the start.
        """

        arrow = ...
        def __init__(
            self, widthB: float = ..., lengthB: float = ..., angleB: float = ...
        ) -> None:
            """
            Parameters
            ----------
            widthB : float, default: 1.0
                Width of the bracket.
            lengthB : float, default: 0.2
                Length of the bracket.
            angleB : float, default: 0 degrees
                Orientation of the bracket, as a counterclockwise angle.
                0 degrees means perpendicular to the line.
            """
            ...

    class Simple(_Base):
        """A simple arrow. Only works with a quadratic Bezier curve."""

        def __init__(
            self,
            head_length: float = ...,
            head_width: float = ...,
            tail_width: float = ...,
        ) -> None:
            """
            Parameters
            ----------
            head_length : float, default: 0.5
                Length of the arrow head.

            head_width : float, default: 0.5
                Width of the arrow head.

            tail_width : float, default: 0.2
                Width of the arrow tail.
            """
            ...
        def transmute(self, path: Path, mutation_size, linewidth: float): ...

    class Fancy(_Base):
        """A fancy arrow. Only works with a quadratic Bezier curve."""

        def __init__(
            self,
            head_length: float = ...,
            head_width: float = ...,
            tail_width: float = ...,
        ) -> None:
            """
            Parameters
            ----------
            head_length : float, default: 0.4
                Length of the arrow head.

            head_width : float, default: 0.4
                Width of the arrow head.

            tail_width : float, default: 0.4
                Width of the arrow tail.
            """
            ...
        def transmute(self, path: Path, mutation_size, linewidth: float): ...

    class Wedge(_Base):
        """
        Wedge(?) shape. Only works with a quadratic Bezier curve.  The
        begin point has a width of the tail_width and the end point has a
        width of 0. At the middle, the width is shrink_factor*tail_width.
        """

        def __init__(self, tail_width: float = ..., shrink_factor: float = ...) -> None:
            """
            Parameters
            ----------
            tail_width : float, default: 0.3
                Width of the tail.

            shrink_factor : float, default: 0.5
                Fraction of the arrow width at the middle point.
            """
            ...
        def transmute(self, path: Path, mutation_size, linewidth: float): ...

class FancyBboxPatch(Patch):
    """
    A fancy box around a rectangle with lower left at *xy* = (*x*, *y*)
    with specified width and height.

    `.FancyBboxPatch` is similar to `.Rectangle`, but it draws a fancy box
    around the rectangle. The transformation of the rectangle box to the
    fancy box is delegated to the style classes defined in `.BoxStyle`.
    """

    def __str__(self) -> str: ...
    def __init__(
        self,
        xy: Sequence[float],
        width: float,
        height: float,
        boxstyle: str | BoxStyle = ...,
        bbox_transmuter=...,
        mutation_scale: float = ...,
        mutation_aspect: float = ...,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        xy : float, float
          The lower left corner of the box.

        width : float
            The width of the box.

        height : float
            The height of the box.

        boxstyle : str or `BoxStyle`
            The style of the fancy box. This can either be a `.BoxStyle`
            instance or a string of the style name and optionally comma
            separated attributes (e.g. "Round, pad=0.2"). This string is
            passed to `.BoxStyle` to construct a `.BoxStyle` object. See
            there for a full documentation.

            The following box styles are available:

            %(AvailableBoxstyles)s

        mutation_scale : float, default: 1
            Scaling factor applied to the attributes of the box style
            (e.g. pad or rounding_size).

        mutation_aspect : float, default: 1
            The height of the rectangle will be squeezed by this value before
            the mutation and the mutated box will be stretched by the inverse
            of it. For example, this allows different horizontal and vertical
            padding.

        Other Parameters
        ----------------
        **kwargs : `.Patch` properties

        %(Patch:kwdoc)s
        """
        ...
    def set_boxstyle(self, boxstyle: str | BoxStyle = ..., **kwargs):
        """
        Set the box style.

        Most box styles can be further configured using attributes.
        Attributes from the previous box style are not reused.

        Without argument (or with ``boxstyle=None``), the available box styles
        are returned as a human-readable string.

        Parameters
        ----------
        boxstyle : str or `BoxStyle`
            The style of the fancy box. This can either be a `.BoxStyle`
            instance or a string of the style name and optionally comma
            separated attributes (e.g. "Round, pad=0.2"). This string is
            passed to `.BoxStyle` to construct a `.BoxStyle` object. See
            there for a full documentation.

            The following box styles are available:

            %(AvailableBoxstyles)s

            .. ACCEPTS: %(ListBoxstyles)s

        **kwargs
            Additional attributes for the box style. See the table above for
            supported parameters.

        Examples
        --------
        ::

            set_boxstyle("round,pad=0.2")
            set_boxstyle("round", pad=0.2)

        """
        ...
    def set_mutation_scale(self, scale: float):
        """
        Set the mutation scale.

        Parameters
        ----------
        scale : float
        """
        ...
    def get_mutation_scale(self):
        """Return the mutation scale."""
        ...
    def set_mutation_aspect(self, aspect: float):
        """
        Set the aspect ratio of the bbox mutation.

        Parameters
        ----------
        aspect : float
        """
        ...
    def get_mutation_aspect(self) -> float:
        """Return the aspect ratio of the bbox mutation."""
        ...
    def get_boxstyle(self) -> str | BoxStyle:
        """Return the boxstyle object."""
        ...
    def get_path(self) -> Path:
        """Return the mutated path of the rectangle."""
        ...
    def get_x(self) -> float:
        """Return the left coord of the rectangle."""
        ...
    def get_y(self) -> float:
        """Return the bottom coord of the rectangle."""
        ...
    def get_width(self) -> float:
        """Return the width of the rectangle."""
        ...
    def get_height(self) -> float:
        """Return the height of the rectangle."""
        ...
    def set_x(self, x: float):
        """
        Set the left coord of the rectangle.

        Parameters
        ----------
        x : float
        """
        ...
    def set_y(self, y: float):
        """
        Set the bottom coord of the rectangle.

        Parameters
        ----------
        y : float
        """
        ...
    def set_width(self, w: float):
        """
        Set the rectangle width.

        Parameters
        ----------
        w : float
        """
        ...
    def set_height(self, h: float):
        """
        Set the rectangle height.

        Parameters
        ----------
        h : float
        """
        ...
    def set_bounds(self, *args):
        """
        Set the bounds of the rectangle.

        Call signatures::

            set_bounds(left, bottom, width, height)
            set_bounds((left, bottom, width, height))

        Parameters
        ----------
        left, bottom : float
            The coordinates of the bottom left corner of the rectangle.
        width, height : float
            The width/height of the rectangle.
        """
        ...
    def get_bbox(self) -> Bbox:
        """Return the `.Bbox`."""
        ...

class FancyArrowPatch(Patch):
    """
    A fancy arrow patch. It draws an arrow using the `ArrowStyle`.

    The head and tail positions are fixed at the specified start and end points
    of the arrow, but the size and shape (in display coordinates) of the arrow
    does not change when the axis is moved or zoomed.
    """

    def __str__(self) -> str: ...
    def __init__(
        self,
        posA: Sequence[float] = ...,
        posB: Sequence[float] = ...,
        path: Path = ...,
        arrowstyle: str | ArrowStyle = ...,
        connectionstyle: str | ConnectionStyle = ...,
        patchA: Patch = ...,
        patchB: Patch = ...,
        shrinkA: float = ...,
        shrinkB: float = ...,
        mutation_scale: float = ...,
        mutation_aspect: float = ...,
        **kwargs
    ) -> None:
        """
        There are two ways for defining an arrow:

        - If *posA* and *posB* are given, a path connecting two points is
          created according to *connectionstyle*. The path will be
          clipped with *patchA* and *patchB* and further shrunken by
          *shrinkA* and *shrinkB*. An arrow is drawn along this
          resulting path using the *arrowstyle* parameter.

        - Alternatively if *path* is provided, an arrow is drawn along this
          path and *patchA*, *patchB*, *shrinkA*, and *shrinkB* are ignored.

        Parameters
        ----------
        posA, posB : (float, float), default: None
            (x, y) coordinates of arrow tail and arrow head respectively.

        path : `~Path`, default: None
            If provided, an arrow is drawn along this path and *patchA*,
            *patchB*, *shrinkA*, and *shrinkB* are ignored.

        arrowstyle : str or `.ArrowStyle`, default: 'simple'
            The `.ArrowStyle` with which the fancy arrow is drawn.  If a
            string, it should be one of the available arrowstyle names, with
            optional comma-separated attributes.  The optional attributes are
            meant to be scaled with the *mutation_scale*.  The following arrow
            styles are available:

            %(AvailableArrowstyles)s

        connectionstyle : str or `.ConnectionStyle` or None, optional, \
default: 'arc3'
            The `.ConnectionStyle` with which *posA* and *posB* are connected.
            If a string, it should be one of the available connectionstyle
            names, with optional comma-separated attributes.  The following
            connection styles are available:

            %(AvailableConnectorstyles)s

        patchA, patchB : `.Patch`, default: None
            Head and tail patches, respectively.

        shrinkA, shrinkB : float, default: 2
            Shrinking factor of the tail and head of the arrow respectively.

        mutation_scale : float, default: 1
            Value with which attributes of *arrowstyle* (e.g., *head_length*)
            will be scaled.

        mutation_aspect : None or float, default: None
            The height of the rectangle will be squeezed by this value before
            the mutation and the mutated box will be stretched by the inverse
            of it.

        Other Parameters
        ----------------
        **kwargs : `.Patch` properties, optional
            Here is a list of available `.Patch` properties:

        %(Patch:kwdoc)s

            In contrast to other patches, the default ``capstyle`` and
            ``joinstyle`` for `FancyArrowPatch` are set to ``"round"``.
        """
        ...
    def set_positions(
        self, posA: None | Sequence[float], posB: None | Sequence[Sequence]
    ):
        """
        Set the begin and end positions of the connecting path.

        Parameters
        ----------
        posA, posB : None, tuple
            (x, y) coordinates of arrow tail and arrow head respectively. If
            `None` use current value.
        """
        ...
    def set_patchA(self, patchA: Patch):
        """
        Set the tail patch.

        Parameters
        ----------
        patchA : `.patches.Patch`
        """
        ...
    def set_patchB(self, patchB: Patch):
        """
        Set the head patch.

        Parameters
        ----------
        patchB : `.patches.Patch`
        """
        ...
    def set_connectionstyle(
        self, connectionstyle: str | ConnectionStyle | None, **kwargs
    ):
        """
        Set the connection style. Old attributes are forgotten.

        Parameters
        ----------
        connectionstyle : str or `.ConnectionStyle` or None, optional
            Can be a string with connectionstyle name with
            optional comma-separated attributes, e.g.::

                set_connectionstyle("arc,angleA=0,armA=30,rad=10")

            Alternatively, the attributes can be provided as keywords, e.g.::

                set_connectionstyle("arc", angleA=0,armA=30,rad=10)

            Without any arguments (or with ``connectionstyle=None``), return
            available styles as a list of strings.
        """
        ...
    def get_connectionstyle(self) -> ConnectionStyle:
        """Return the `ConnectionStyle` used."""
        ...
    def set_arrowstyle(self, arrowstyle: None | ArrowStyle | str = ..., **kwargs):
        """
        Set the arrow style. Old attributes are forgotten. Without arguments
        (or with ``arrowstyle=None``) returns available box styles as a list of
        strings.

        Parameters
        ----------
        arrowstyle : None or ArrowStyle or str, default: None
            Can be a string with arrowstyle name with optional comma-separated
            attributes, e.g.::

                set_arrowstyle("Fancy,head_length=0.2")

            Alternatively attributes can be provided as keywords, e.g.::

                set_arrowstyle("fancy", head_length=0.2)

        """
        ...
    def get_arrowstyle(self) -> ArrowStyle:
        """Return the arrowstyle object."""
        ...
    def set_mutation_scale(self, scale: float):
        """
        Set the mutation scale.

        Parameters
        ----------
        scale : float
        """
        ...
    def get_mutation_scale(self) -> float:
        """
        Return the mutation scale.

        Returns
        -------
        scalar
        """
        ...
    def set_mutation_aspect(self, aspect: float):
        """
        Set the aspect ratio of the bbox mutation.

        Parameters
        ----------
        aspect : float
        """
        ...
    def get_mutation_aspect(self) -> float:
        """Return the aspect ratio of the bbox mutation."""
        ...
    def get_path(self) -> Path:
        """Return the path of the arrow in the data coordinates."""
        ...
    get_path_in_displaycoord = ...
    def draw(self, renderer: RendererBase): ...

class ConnectionPatch(FancyArrowPatch):
    """A patch that connects two points (possibly in different axes)."""

    def __str__(self) -> str: ...
    def __init__(
        self,
        xyA: Sequence[float],
        xyB: Sequence[float],
        coordsA,
        coordsB=...,
        axesA=...,
        axesB=...,
        arrowstyle: str | ArrowStyle = ...,
        connectionstyle: str | ConnectionStyle = ...,
        patchA: Patch = ...,
        patchB: Patch = ...,
        shrinkA: float = ...,
        shrinkB: float = ...,
        mutation_scale: float = ...,
        mutation_aspect: float = ...,
        clip_on: bool = ...,
        **kwargs
    ) -> None:
        """
        Connect point *xyA* in *coordsA* with point *xyB* in *coordsB*.

        Valid keys are

        ===============  ======================================================
        Key              Description
        ===============  ======================================================
        arrowstyle       the arrow style
        connectionstyle  the connection style
        relpos           default is (0.5, 0.5)
        patchA           default is bounding box of the text
        patchB           default is None
        shrinkA          default is 2 points
        shrinkB          default is 2 points
        mutation_scale   default is text size (in points)
        mutation_aspect  default is 1.
        ?                any key for `matplotlib.patches.PathPatch`
        ===============  ======================================================

        *coordsA* and *coordsB* are strings that indicate the
        coordinates of *xyA* and *xyB*.

        ==================== ==================================================
        Property             Description
        ==================== ==================================================
        'figure points'      points from the lower left corner of the figure
        'figure pixels'      pixels from the lower left corner of the figure
        'figure fraction'    0, 0 is lower left of figure and 1, 1 is upper
                             right
        'subfigure points'   points from the lower left corner of the subfigure
        'subfigure pixels'   pixels from the lower left corner of the subfigure
        'subfigure fraction' fraction of the subfigure, 0, 0 is lower left.
        'axes points'        points from lower left corner of axes
        'axes pixels'        pixels from lower left corner of axes
        'axes fraction'      0, 0 is lower left of axes and 1, 1 is upper right
        'data'               use the coordinate system of the object being
                             annotated (default)
        'offset points'      offset (in points) from the *xy* value
        'polar'              you can specify *theta*, *r* for the annotation,
                             even in cartesian plots.  Note that if you are
                             using a polar axes, you do not need to specify
                             polar for the coordinate system since that is the
                             native "data" coordinate system.
        ==================== ==================================================

        Alternatively they can be set to any valid
        `~Transform`.

        Note that 'subfigure pixels' and 'figure pixels' are the same
        for the parent figure, so users who want code that is usable in
        a subfigure can use 'subfigure pixels'.

        .. note::

           Using `ConnectionPatch` across two `~.axes.Axes` instances
           is not directly compatible with :doc:`constrained layout
           </tutorials/intermediate/constrainedlayout_guide>`. Add the artist
           directly to the `.Figure` instead of adding it to a specific Axes,
           or exclude it from the layout using ``con.set_in_layout(False)``.

           .. code-block:: default

              fig, ax = plt.subplots(1, 2, constrained_layout=True)
              con = ConnectionPatch(..., axesA=ax[0], axesB=ax[1])
              fig.add_artist(con)

        """
        ...
    def set_annotation_clip(self, b: bool | None):
        """
        Set the annotation's clipping behavior.

        Parameters
        ----------
        b : bool or None
            - True: The annotation will be clipped when ``self.xy`` is
              outside the axes.
            - False: The annotation will always be drawn.
            - None: The annotation will be clipped when ``self.xy`` is
              outside the axes and ``self.xycoords == "data"``.
        """
        ...
    def get_annotation_clip(self) -> bool:
        """
        Return the clipping behavior.

        See `.set_annotation_clip` for the meaning of the return value.
        """
        ...
    def draw(self, renderer): ...
