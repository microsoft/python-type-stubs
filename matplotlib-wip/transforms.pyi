import numpy as np
from typing import Literal, Sequence
from matplotlib._typing import *
from matplotlib.path import Path
from matplotlib.patches import Patch
from matplotlib.figure import Figure

DEBUG = ...

class TransformNode:
    """
    The base class for anything that participates in the transform tree
    and needs to invalidate its parents or be invalidated.  This includes
    classes that are not really transforms, such as bounding boxes, since some
    transforms depend on bounding boxes to compute their values.
    """

    INVALID_NON_AFFINE = ...
    INVALID_AFFINE = ...
    INVALID = ...
    is_affine = ...
    is_bbox = ...
    pass_through = ...
    def __init__(self, shorthand_name: str = ...) -> None:
        """
        Parameters
        ----------
        shorthand_name : str
            A string representing the "name" of the transform. The name carries
            no significance other than to improve the readability of
            ``str(transform)`` when DEBUG=True.
        """
        ...
    if DEBUG:
        def __str__(self) -> str: ...

    def __getstate__(self): ...
    def __setstate__(self, data_dict): ...
    def __copy__(self): ...
    def invalidate(self):
        """
        Invalidate this `TransformNode` and triggers an invalidation of its
        ancestors.  Should be called any time the transform changes.
        """
        ...
    def set_children(self, *children):
        """
        Set the children of the transform, to let the invalidation
        system know which transforms can invalidate this transform.
        Should be called from the constructor of any transforms that
        depend on other transforms.
        """
        ...
    def frozen(self):
        """
        Return a frozen copy of this transform node.  The frozen copy will not
        be updated when its children change.  Useful for storing a previously
        known state of a transform where ``copy.deepcopy()`` might normally be
        used.
        """
        ...

class BboxBase(TransformNode):
    """
    The base class of all bounding boxes.

    This class is immutable; `Bbox` is a mutable subclass.

    The canonical representation is as two points, with no
    restrictions on their ordering.  Convenience properties are
    provided to get the left, bottom, right and top edges and width
    and height, but these are not stored explicitly.
    """

    is_bbox = ...
    is_affine = ...
    if DEBUG: ...
    def frozen(self): ...
    def __array__(self, *args, **kwargs): ...
    @property
    def x0(self) -> float:
        """
        The first of the pair of *x* coordinates that define the bounding box.

        This is not guaranteed to be less than :attr:`x1` (for that, use
        :attr:`xmin`).
        """
        ...
    @property
    def y0(self) -> float:
        """
        The first of the pair of *y* coordinates that define the bounding box.

        This is not guaranteed to be less than :attr:`y1` (for that, use
        :attr:`ymin`).
        """
        ...
    @property
    def x1(self) -> float:
        """
        The second of the pair of *x* coordinates that define the bounding box.

        This is not guaranteed to be greater than :attr:`x0` (for that, use
        :attr:`xmax`).
        """
        ...
    @property
    def y1(self) -> float:
        """
        The second of the pair of *y* coordinates that define the bounding box.

        This is not guaranteed to be greater than :attr:`y0` (for that, use
        :attr:`ymax`).
        """
        ...
    @property
    def p0(self) -> tuple[float, float]:
        """
        The first pair of (*x*, *y*) coordinates that define the bounding box.

        This is not guaranteed to be the bottom-left corner (for that, use
        :attr:`min`).
        """
        ...
    @property
    def p1(self) -> tuple[float, float]:
        """
        The second pair of (*x*, *y*) coordinates that define the bounding box.

        This is not guaranteed to be the top-right corner (for that, use
        :attr:`max`).
        """
        ...
    @property
    def xmin(self) -> float:
        """The left edge of the bounding box."""
        ...
    @property
    def ymin(self) -> float:
        """The bottom edge of the bounding box."""
        ...
    @property
    def xmax(self) -> float:
        """The right edge of the bounding box."""
        ...
    @property
    def ymax(self) -> float:
        """The top edge of the bounding box."""
        ...
    @property
    def min(self) -> tuple[float, float]:
        """The bottom-left corner of the bounding box."""
        ...
    @property
    def max(self) -> tuple[float, float]:
        """The top-right corner of the bounding box."""
        ...
    @property
    def intervalx(self) -> tuple[float, float]:
        """
        The pair of *x* coordinates that define the bounding box.

        This is not guaranteed to be sorted from left to right.
        """
        ...
    @property
    def intervaly(self) -> tuple[float, float]:
        """
        The pair of *y* coordinates that define the bounding box.

        This is not guaranteed to be sorted from bottom to top.
        """
        ...
    @property
    def width(self) -> float:
        """The (signed) width of the bounding box."""
        ...
    @property
    def height(self) -> float:
        """The (signed) height of the bounding box."""
        ...
    @property
    def size(self) -> tuple[float, float]:
        """The (signed) width and height of the bounding box."""
        ...
    @property
    def bounds(self) -> tuple[float, float, float, float]:
        """Return (:attr:`x0`, :attr:`y0`, :attr:`width`, :attr:`height`)."""
        ...
    @property
    def extents(self) -> tuple[float, float, float, float]:
        """Return (:attr:`x0`, :attr:`y0`, :attr:`x1`, :attr:`y1`)."""
        ...
    def get_points(self): ...
    def containsx(self, x) -> bool:
        """
        Return whether *x* is in the closed (:attr:`x0`, :attr:`x1`) interval.
        """
        ...
    def containsy(self, y) -> bool:
        """
        Return whether *y* is in the closed (:attr:`y0`, :attr:`y1`) interval.
        """
        ...
    def contains(self, x, y) -> bool:
        """
        Return whether ``(x, y)`` is in the bounding box or on its edge.
        """
        ...
    def overlaps(self, other: BboxBase) -> bool:
        """
        Return whether this bounding box overlaps with the other bounding box.

        Parameters
        ----------
        other : `.BboxBase`
        """
        ...
    def fully_containsx(self, x: float) -> bool:
        """
        Return whether *x* is in the open (:attr:`x0`, :attr:`x1`) interval.
        """
        ...
    def fully_containsy(self, y: float) -> bool:
        """
        Return whether *y* is in the open (:attr:`y0`, :attr:`y1`) interval.
        """
        ...
    def fully_contains(self, x: float, y: float) -> bool:
        """
        Return whether ``x, y`` is in the bounding box, but not on its edge.
        """
        ...
    def fully_overlaps(self, other: BboxBase) -> bool:
        """
        Return whether this bounding box overlaps with the other bounding box,
        not including the edges.

        Parameters
        ----------
        other : `.BboxBase`
        """
        ...
    def transformed(self, transform: Transform):
        """
        Construct a `Bbox` by statically transforming this one by *transform*.
        """
        ...
    coefs = ...
    def anchored(
        self,
        c: Sequence[float] | Literal["C", "SW", "S", "SE", "E", "NE", "N", "NW", "W"],
        container: Bbox = ...,
    ):
        """
        Return a copy of the `Bbox` anchored to *c* within *container*.

        Parameters
        ----------
        c : (float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', ...}
            Either an (*x*, *y*) pair of relative coordinates (0 is left or
            bottom, 1 is right or top), 'C' (center), or a cardinal direction
            ('SW', southwest, is bottom left, etc.).
        container : `Bbox`, optional
            The box within which the `Bbox` is positioned; it defaults
            to the initial `Bbox`.

        See Also
        --------
        .Axes.set_anchor
        """
        ...
    def shrunk(self, mx: float, my: float) -> Bbox:
        """
        Return a copy of the `Bbox`, shrunk by the factor *mx*
        in the *x* direction and the factor *my* in the *y* direction.
        The lower left corner of the box remains unchanged.  Normally
        *mx* and *my* will be less than 1, but this is not enforced.
        """
        ...
    def shrunk_to_aspect(
        self, box_aspect: float, container=..., fig_aspect: float = ...
    ) -> Bbox:
        """
        Return a copy of the `Bbox`, shrunk so that it is as
        large as it can be while having the desired aspect ratio,
        *box_aspect*.  If the box coordinates are relative (i.e.
        fractions of a larger box such as a figure) then the
        physical aspect ratio of that figure is specified with
        *fig_aspect*, so that *box_aspect* can also be given as a
        ratio of the absolute dimensions, not the relative dimensions.
        """
        ...
    def splitx(self, *args) -> list[Bbox]:
        """
        Return a list of new `Bbox` objects formed by splitting the original
        one with vertical lines at fractional positions given by *args*.
        """
        ...
    def splity(self, *args) -> list[Bbox]:
        """
        Return a list of new `Bbox` objects formed by splitting the original
        one with horizontal lines at fractional positions given by *args*.
        """
        ...
    def count_contains(self, vertices) -> int:
        """
        Count the number of vertices contained in the `Bbox`.
        Any vertices with a non-finite x or y value are ignored.

        Parameters
        ----------
        vertices : Nx2 Numpy array.
        """
        ...
    def count_overlaps(self, bboxes: Sequence[Bbox]) -> int:
        """
        Count the number of bounding boxes that overlap this one.

        Parameters
        ----------
        bboxes : sequence of `.BboxBase`
        """
        ...
    def expanded(self, sw: float, sh: float) -> Bbox:
        """
        Construct a `Bbox` by expanding this one around its center by the
        factors *sw* and *sh*.
        """
        ...
    def padded(self, p: float) -> Bbox:
        """Construct a `Bbox` by padding this one on all four sides by *p*."""
        ...
    def translated(self, tx: float, ty: float) -> Bbox:
        """Construct a `Bbox` by translating this one by *tx* and *ty*."""
        ...
    def corners(
        self,
    ) -> tuple[
        tuple[float, float],
        tuple[float, float],
        tuple[float, float],
        tuple[float, float],
    ]:
        """
        Return the corners of this rectangle as an array of points.

        Specifically, this returns the array
        ``[[x0, y0], [x0, y1], [x1, y0], [x1, y1]]``.
        """
        ...
    def rotated(self, radians: float) -> Bbox:
        """
        Return the axes-aligned bounding box that bounds the result of rotating
        this `Bbox` by an angle of *radians*.
        """
        ...
    @staticmethod
    def union(bboxes: Sequence[Bbox]) -> Bbox:
        """Return a `Bbox` that contains all of the given *bboxes*."""
        ...
    @staticmethod
    def intersection(bbox1: Bbox, bbox2: Bbox) -> None | Bbox:
        """
        Return the intersection of *bbox1* and *bbox2* if they intersect, or
        None if they don't.
        """
        ...

class Bbox(BboxBase):
    """
    A mutable bounding box.

    Examples
    --------
    **Create from known bounds**

    The default constructor takes the boundary "points" ``[[xmin, ymin],
    [xmax, ymax]]``.

        >>> Bbox([[1, 1], [3, 7]])
        Bbox([[1.0, 1.0], [3.0, 7.0]])

    Alternatively, a Bbox can be created from the flattened points array, the
    so-called "extents" ``(xmin, ymin, xmax, ymax)``

        >>> Bbox.from_extents(1, 1, 3, 7)
        Bbox([[1.0, 1.0], [3.0, 7.0]])

    or from the "bounds" ``(xmin, ymin, width, height)``.

        >>> Bbox.from_bounds(1, 1, 2, 6)
        Bbox([[1.0, 1.0], [3.0, 7.0]])

    **Create from collections of points**

    The "empty" object for accumulating Bboxs is the null bbox, which is a
    stand-in for the empty set.

        >>> Bbox.null()
        Bbox([[inf, inf], [-inf, -inf]])

    Adding points to the null bbox will give you the bbox of those points.

        >>> box = Bbox.null()
        >>> box.update_from_data_xy([[1, 1]])
        >>> box
        Bbox([[1.0, 1.0], [1.0, 1.0]])
        >>> box.update_from_data_xy([[2, 3], [3, 2]], ignore=False)
        >>> box
        Bbox([[1.0, 1.0], [3.0, 3.0]])

    Setting ``ignore=True`` is equivalent to starting over from a null bbox.

        >>> box.update_from_data_xy([[1, 1]], ignore=True)
        >>> box
        Bbox([[1.0, 1.0], [1.0, 1.0]])

    .. warning::

        It is recommended to always specify ``ignore`` explicitly.  If not, the
        default value of ``ignore`` can be changed at any time by code with
        access to your Bbox, for example using the method `~.Bbox.ignore`.

    **Properties of the ``null`` bbox**

    .. note::

        The current behavior of `Bbox.null()` may be surprising as it does
        not have all of the properties of the "empty set", and as such does
        not behave like a "zero" object in the mathematical sense. We may
        change that in the future (with a deprecation period).

    The null bbox is the identity for intersections

        >>> Bbox.intersection(Bbox([[1, 1], [3, 7]]), Bbox.null())
        Bbox([[1.0, 1.0], [3.0, 7.0]])

    except with itself, where it returns the full space.

        >>> Bbox.intersection(Bbox.null(), Bbox.null())
        Bbox([[-inf, -inf], [inf, inf]])

    A union containing null will always return the full space (not the other
    set!)

        >>> Bbox.union([Bbox([[0, 0], [0, 0]]), Bbox.null()])
        Bbox([[-inf, -inf], [inf, inf]])
    """

    def __init__(self, points: np.ndarray, **kwargs) -> None:
        """
        Parameters
        ----------
        points : np.ndarray
            A 2x2 numpy array of the form ``[[x0, y0], [x1, y1]]``.
        """
        ...
    def invalidate(self): ...
    def frozen(self): ...
    @staticmethod
    def unit() -> Bbox:
        """Create a new unit `Bbox` from (0, 0) to (1, 1)."""
        ...
    @staticmethod
    def null() -> Bbox:
        """Create a new null `Bbox` from (inf, inf) to (-inf, -inf)."""
        ...
    @staticmethod
    def from_bounds(x0: float, y0: float, width: float, height: float) -> Bbox:
        """
        Create a new `Bbox` from *x0*, *y0*, *width* and *height*.

        *width* and *height* may be negative.
        """
        ...
    @staticmethod
    def from_extents(*args, minpos: float | None = ...):
        """
        Create a new Bbox from *left*, *bottom*, *right* and *top*.

        The *y*-axis increases upwards.

        Parameters
        ----------
        left, bottom, right, top : float
            The four extents of the bounding box.

        minpos : float or None
           If this is supplied, the Bbox will have a minimum positive value
           set. This is useful when dealing with logarithmic scales and other
           scales where negative bounds result in floating point errors.
        """
        ...
    def __format__(self, fmt: str): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def ignore(self, value: bool):
        """
        Set whether the existing bounds of the box should be ignored
        by subsequent calls to :meth:`update_from_data_xy`.

        value : bool
           - When ``True``, subsequent calls to :meth:`update_from_data_xy`
             will ignore the existing bounds of the `Bbox`.

           - When ``False``, subsequent calls to :meth:`update_from_data_xy`
             will include the existing bounds of the `Bbox`.
        """
        ...
    def update_from_path(
        self,
        path: Path,
        ignore: bool | None = ...,
        updatex: bool = True,
        updatey: bool = True,
    ):
        """
        Update the bounds of the `Bbox` to contain the vertices of the
        provided path. After updating, the bounds will have positive *width*
        and *height*; *x0* and *y0* will be the minimal values.

        Parameters
        ----------
        path : `~Path`

        ignore : bool, optional
           - when ``True``, ignore the existing bounds of the `Bbox`.
           - when ``False``, include the existing bounds of the `Bbox`.
           - when ``None``, use the last value passed to :meth:`ignore`.

        updatex, updatey : bool, default: True
            When ``True``, update the x/y values.
        """
        ...
    def update_from_data_x(self, x: np.ndarray, ignore: bool | None = ...):
        """
        Update the x-bounds of the `Bbox` based on the passed in data. After
        updating, the bounds will have positive *width*, and *x0* will be the
        minimal value.

        Parameters
        ----------
        x : np.ndarray
            Array of x-values.

        ignore : bool, optional
           - When ``True``, ignore the existing bounds of the `Bbox`.
           - When ``False``, include the existing bounds of the `Bbox`.
           - When ``None``, use the last value passed to :meth:`ignore`.
        """
        ...
    def update_from_data_y(self, y: np.ndarray, ignore: bool | None = ...):
        """
        Update the y-bounds of the `Bbox` based on the passed in data. After
        updating, the bounds will have positive *height*, and *y0* will be the
        minimal value.

        Parameters
        ----------
        y : np.ndarray
            Array of y-values.

        ignore : bool, optional
           - When ``True``, ignore the existing bounds of the `Bbox`.
           - When ``False``, include the existing bounds of the `Bbox`.
           - When ``None``, use the last value passed to :meth:`ignore`.
        """
        ...
    def update_from_data_xy(
        self,
        xy: np.ndarray,
        ignore: bool | None = ...,
        updatex: bool = True,
        updatey: bool = True,
    ):
        """
        Update the bounds of the `Bbox` based on the passed in data. After
        updating, the bounds will have positive *width* and *height*;
        *x0* and *y0* will be the minimal values.

        Parameters
        ----------
        xy : np.ndarray
            A numpy array of 2D points.

        ignore : bool, optional
           - When ``True``, ignore the existing bounds of the `Bbox`.
           - When ``False``, include the existing bounds of the `Bbox`.
           - When ``None``, use the last value passed to :meth:`ignore`.

        updatex, updatey : bool, default: True
            When ``True``, update the x/y values.
        """
        ...
    @BboxBase.x0.setter
    def x0(self, val: float): ...
    @BboxBase.y0.setter
    def y0(self, val: float): ...
    @BboxBase.x1.setter
    def x1(self, val: float): ...
    @BboxBase.y1.setter
    def y1(self, val: float): ...
    @BboxBase.p0.setter
    def p0(self, val: float): ...
    @BboxBase.p1.setter
    def p1(self, val: float): ...
    @BboxBase.intervalx.setter
    def intervalx(self, interval): ...
    @BboxBase.intervaly.setter
    def intervaly(self, interval): ...
    @BboxBase.bounds.setter
    def bounds(self, bounds): ...
    @property
    def minpos(self) -> float:
        """
        The minimum positive value in both directions within the Bbox.

        This is useful when dealing with logarithmic scales and other scales
        where negative bounds result in floating point errors, and will be used
        as the minimum extent instead of *p0*.
        """
        ...
    @property
    def minposx(self) -> float:
        """
        The minimum positive value in the *x*-direction within the Bbox.

        This is useful when dealing with logarithmic scales and other scales
        where negative bounds result in floating point errors, and will be used
        as the minimum *x*-extent instead of *x0*.
        """
        ...
    @property
    def minposy(self) -> float:
        """
        The minimum positive value in the *y*-direction within the Bbox.

        This is useful when dealing with logarithmic scales and other scales
        where negative bounds result in floating point errors, and will be used
        as the minimum *y*-extent instead of *y0*.
        """
        ...
    def get_points(self) -> tuple[tuple[float, float], tuple[float, float]]:
        """
        Get the points of the bounding box directly as a numpy array
        of the form: ``[[x0, y0], [x1, y1]]``.
        """
        ...
    def set_points(self, points) -> tuple[tuple[float, float], tuple[float, float]]:
        """
        Set the points of the bounding box directly from a numpy array
        of the form: ``[[x0, y0], [x1, y1]]``.  No error checking is
        performed, as this method is mainly for internal use.
        """
        ...
    def set(self, other: Bbox):
        """
        Set this bounding box from the "frozen" bounds of another `Bbox`.
        """
        ...
    def mutated(self) -> bool:
        """Return whether the bbox has changed since init."""
        ...
    def mutatedx(self) -> bool:
        """Return whether the x-limits have changed since init."""
        ...
    def mutatedy(self) -> bool:
        """Return whether the y-limits have changed since init."""
        ...

class TransformedBbox(BboxBase):
    """
    A `Bbox` that is automatically transformed by a given
    transform.  When either the child bounding box or transform
    changes, the bounds of this bbox will update accordingly.
    """

    def __init__(self, bbox: Bbox, transform: Transform, **kwargs) -> None:
        """
        Parameters
        ----------
        bbox : `Bbox`
        transform : `Transform`
        """
        ...
    def get_points(self): ...

class LockableBbox(BboxBase):
    """
    A `Bbox` where some elements may be locked at certain values.

    When the child bounding box changes, the bounds of this bbox will update
    accordingly with the exception of the locked elements.
    """

    def __init__(
        self,
        bbox: Bbox,
        x0: float | None = ...,
        y0: float | None = ...,
        x1: float | None = ...,
        y1: float | None = ...,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        bbox : `Bbox`
            The child bounding box to wrap.

        x0 : float or None
            The locked value for x0, or None to leave unlocked.

        y0 : float or None
            The locked value for y0, or None to leave unlocked.

        x1 : float or None
            The locked value for x1, or None to leave unlocked.

        y1 : float or None
            The locked value for y1, or None to leave unlocked.

        """
        ...
    def get_points(self): ...
    @property
    def locked_x0(self) -> float | None:
        """
        float or None: The value used for the locked x0.
        """
        ...
    @locked_x0.setter
    def locked_x0(self, x0: float | None): ...
    @property
    def locked_y0(self) -> float | None:
        """
        float or None: The value used for the locked y0.
        """
        ...
    @locked_y0.setter
    def locked_y0(self, y0: float | None): ...
    @property
    def locked_x1(self) -> float | None:
        """
        float or None: The value used for the locked x1.
        """
        ...
    @locked_x1.setter
    def locked_x1(self, x1: float | None): ...
    @property
    def locked_y1(self) -> float | None:
        """
        float or None: The value used for the locked y1.
        """
        ...
    @locked_y1.setter
    def locked_y1(self, y1: float | None): ...

class Transform(TransformNode):
    """
    The base class of all `TransformNode` instances that
    actually perform a transformation.

    All non-affine transformations should be subclasses of this class.
    New affine transformations should be subclasses of `Affine2D`.

    Subclasses of this class should override the following members (at
    minimum):

    - :attr:`input_dims`
    - :attr:`output_dims`
    - :meth:`transform`
    - :meth:`inverted` (if an inverse exists)

    The following attributes may be overridden if the default is unsuitable:

    - :attr:`is_separable` (defaults to True for 1D -> 1D transforms, False
      otherwise)
    - :attr:`has_inverse` (defaults to True if :meth:`inverted` is overridden,
      False otherwise)

    If the transform needs to do something non-standard with
    `Path` objects, such as adding curves
    where there were once line segments, it should override:

    - :meth:`transform_path`
    """

    input_dims = ...
    output_dims = ...
    is_separable = ...
    has_inverse = ...
    def __init_subclass__(cls): ...
    def __add__(self, other: Transform) -> Transform:
        """
        Compose two transforms together so that *self* is followed by *other*.

        ``A + B`` returns a transform ``C`` so that
        ``C.transform(x) == B.transform(A.transform(x))``.
        """
        ...
    @property
    def depth(self) -> int:
        """
        Return the number of transforms which have been chained
        together to form this Transform instance.

        .. note::

            For the special case of a Composite transform, the maximum depth
            of the two is returned.

        """
        ...
    def contains_branch(self, other: Transform):
        """
        Return whether the given transform is a sub-tree of this transform.

        This routine uses transform equality to identify sub-trees, therefore
        in many situations it is object id which will be used.

        For the case where the given transform represents the whole
        of this transform, returns True.
        """
        ...
    def contains_branch_seperately(self, other_transform: Transform):
        """
        Return whether the given branch is a sub-tree of this transform on
        each separate dimension.

        A common use for this method is to identify if a transform is a blended
        transform containing an Axes' data transform. e.g.::

            x_isdata, y_isdata = trans.contains_branch_seperately(ax.transData)

        """
        ...
    def __sub__(self, other: Transform) -> Transform:
        """
        Compose *self* with the inverse of *other*, cancelling identical terms
        if any::

            # In general:
            A - B == A + B.inverted()
            # (but see note regarding frozen transforms below).

            # If A "ends with" B (i.e. A == A' + B for some A') we can cancel
            # out B:
            (A' + B) - B == A'

            # Likewise, if B "starts with" A (B = A + B'), we can cancel out A:
            A - (A + B') == B'.inverted() == B'^-1

        Cancellation (rather than naively returning ``A + B.inverted()``) is
        important for multiple reasons:

        - It avoids floating-point inaccuracies when computing the inverse of
          B: ``B - B`` is guaranteed to cancel out exactly (resulting in the
          identity transform), whereas ``B + B.inverted()`` may differ by a
          small epsilon.
        - ``B.inverted()`` always returns a frozen transform: if one computes
          ``A + B + B.inverted()`` and later mutates ``B``, then
          ``B.inverted()`` won't be updated and the last two terms won't cancel
          out anymore; on the other hand, ``A + B - B`` will always be equal to
          ``A`` even if ``B`` is mutated.
        """
        ...
    def __array__(self, *args, **kwargs):
        """Array interface to get at this Transform's affine matrix."""
        ...
    def transform(self, values: ArrayLike) -> np.ndarray:
        """
        Apply this transformation on the given array of *values*.

        Parameters
        ----------
        values : array
            The input values as NumPy array of length :attr:`input_dims` or
            shape (N x :attr:`input_dims`).

        Returns
        -------
        array
            The output values as NumPy array of length :attr:`output_dims` or
            shape (N x :attr:`output_dims`), depending on the input.
        """
        ...
    def transform_affine(self, values: ArrayLike) -> np.ndarray:
        """
        Apply only the affine part of this transformation on the
        given array of values.

        ``transform(values)`` is always equivalent to
        ``transform_affine(transform_non_affine(values))``.

        In non-affine transformations, this is generally a no-op.  In
        affine transformations, this is equivalent to
        ``transform(values)``.

        Parameters
        ----------
        values : array
            The input values as NumPy array of length :attr:`input_dims` or
            shape (N x :attr:`input_dims`).

        Returns
        -------
        array
            The output values as NumPy array of length :attr:`output_dims` or
            shape (N x :attr:`output_dims`), depending on the input.
        """
        ...
    def transform_non_affine(self, values: ArrayLike) -> np.ndarray:
        """
        Apply only the non-affine part of this transformation.

        ``transform(values)`` is always equivalent to
        ``transform_affine(transform_non_affine(values))``.

        In non-affine transformations, this is generally equivalent to
        ``transform(values)``.  In affine transformations, this is
        always a no-op.

        Parameters
        ----------
        values : array
            The input values as NumPy array of length :attr:`input_dims` or
            shape (N x :attr:`input_dims`).

        Returns
        -------
        array
            The output values as NumPy array of length :attr:`output_dims` or
            shape (N x :attr:`output_dims`), depending on the input.
        """
        ...
    def transform_bbox(self, bbox: Bbox):
        """
        Transform the given bounding box.

        For smarter transforms including caching (a common requirement in
        Matplotlib), see `TransformedBbox`.
        """
        ...
    def get_affine(self):
        """Get the affine part of this transform."""
        ...
    def get_matrix(self):
        """Get the matrix for the affine part of this transform."""
        ...
    def transform_point(self, point):
        """
        Return a transformed point.

        This function is only kept for backcompatibility; the more general
        `.transform` method is capable of transforming both a list of points
        and a single point.

        The point is given as a sequence of length :attr:`input_dims`.
        The transformed point is returned as a sequence of length
        :attr:`output_dims`.
        """
        ...
    def transform_path(self, path: Path) -> Path:
        """
        Apply the transform to `.Path` *path*, returning a new `.Path`.

        In some cases, this transform may insert curves into the path
        that began as line segments.
        """
        ...
    def transform_path_affine(self, path: Path) -> Path:
        """
        Apply the affine part of this transform to `.Path` *path*, returning a
        new `.Path`.

        ``transform_path(path)`` is equivalent to
        ``transform_path_affine(transform_path_non_affine(values))``.
        """
        ...
    def transform_path_non_affine(self, path: Path) -> Path:
        """
        Apply the non-affine part of this transform to `.Path` *path*,
        returning a new `.Path`.

        ``transform_path(path)`` is equivalent to
        ``transform_path_affine(transform_path_non_affine(values))``.
        """
        ...
    def transform_angles(
        self,
        angles: ArrayLike,
        pts: ArrayLike,
        radians: bool = ...,
        pushoff: float = ...,
    ) -> np.ndarray:
        """
        Transform a set of angles anchored at specific locations.

        Parameters
        ----------
        angles : (N,) array-like
            The angles to transform.
        pts : (N, 2) array-like
            The points where the angles are anchored.
        radians : bool, default: False
            Whether *angles* are radians or degrees.
        pushoff : float
            For each point in *pts* and angle in *angles*, the transformed
            angle is computed by transforming a segment of length *pushoff*
            starting at that point and making that angle relative to the
            horizontal axis, and measuring the angle between the horizontal
            axis and the transformed segment.

        Returns
        -------
        (N,) array
        """
        ...
    def inverted(self) -> Transform:
        """
        Return the corresponding inverse transformation.

        It holds ``x == self.inverted().transform(self.transform(x))``.

        The return value of this method should be treated as
        temporary.  An update to *self* does not cause a corresponding
        update to its inverted copy.
        """
        ...

class TransformWrapper(Transform):
    """
    A helper class that holds a single child transform and acts
    equivalently to it.

    This is useful if a node of the transform tree must be replaced at
    run time with a transform of a different type.  This class allows
    that replacement to correctly trigger invalidation.

    `TransformWrapper` instances must have the same input and output dimensions
    during their entire lifetime, so the child transform may only be replaced
    with another child transform of the same dimensions.
    """

    pass_through = ...
    def __init__(self, child: Transform) -> None:
        """
        *child*: A `Transform` instance.  This child may later
        be replaced with :meth:`set`.
        """
        ...
    def __eq__(self, other: Transform) -> bool: ...
    def frozen(self): ...
    def set(self, child: Transform):
        """
        Replace the current child of this transform with another one.

        The new child must have the same number of input and output
        dimensions as the current child.
        """
        ...
    is_affine = ...
    is_separable = ...
    has_inverse = ...

class AffineBase(Transform):
    """
    The base class of all affine transformations of any number of dimensions.
    """

    is_affine = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __array__(self, *args, **kwargs): ...
    def __eq__(self, other) -> bool: ...
    def transform(self, values: ArrayLike) -> np.ndarray: ...
    def transform_affine(self, values: ArrayLike) -> np.ndarray: ...
    def transform_non_affine(self, points: ArrayLike) -> np.ndarray: ...
    def transform_path(self, path: Path) -> Path: ...
    def transform_path_affine(self, path: Path) -> Path: ...
    def transform_path_non_affine(self, path: Path) -> Path: ...
    def get_affine(self): ...

class Affine2DBase(AffineBase):
    """
    The base class of all 2D affine transformations.

    2D affine transformations are performed using a 3x3 numpy array::

        a c e
        b d f
        0 0 1

    This class provides the read-only interface.  For a mutable 2D
    affine transformation, use `Affine2D`.

    Subclasses of this class will generally only need to override a
    constructor and :meth:`get_matrix` that generates a custom 3x3 matrix.
    """

    input_dims = ...
    output_dims = ...
    def frozen(self): ...
    @property
    def is_separable(self) -> bool: ...
    def to_values(self) -> tuple[float, float, float, float, float, float]:
        """
        Return the values of the matrix as an ``(a, b, c, d, e, f)`` tuple.
        """
        ...
    def transform_affine(self, points: ArrayLike) -> np.ndarray: ...
    def inverted(self) -> Transform: ...

class Affine2D(Affine2DBase):
    """
    A mutable 2D affine transformation.
    """

    def __init__(self, matrix: ArrayLike = ..., **kwargs) -> None:
        """
        Initialize an Affine transform from a 3x3 numpy float array::

          a c e
          b d f
          0 0 1

        If *matrix* is None, initialize with the identity transform.
        """
        ...
    def __str__(self) -> str: ...
    @staticmethod
    def from_values(a: float, b: float, c: float, d: float, e: float, f: float):
        """
        Create a new Affine2D instance from the given values::

          a c e
          b d f
          0 0 1

        .
        """
        ...
    def get_matrix(self) -> np.ndarray:
        """
        Get the underlying transformation matrix as a 3x3 numpy array::

          a c e
          b d f
          0 0 1

        .
        """
        ...
    def set_matrix(self, mtx: np.ndarray):
        """
        Set the underlying transformation matrix from a 3x3 numpy array::

          a c e
          b d f
          0 0 1

        .
        """
        ...
    def set(self, other: Transform):
        """
        Set this transformation from the frozen copy of another
        `Affine2DBase` object.
        """
        ...
    @staticmethod
    def identity() -> Affine2D:
        """
        Return a new `Affine2D` object that is the identity transform.

        Unless this transform will be mutated later on, consider using
        the faster `IdentityTransform` class instead.
        """
        ...
    def clear(self) -> None:
        """
        Reset the underlying matrix to the identity transform.
        """
        ...
    def rotate(self, theta: float) -> Affine2D:
        """
        Add a rotation (in radians) to this transform in place.

        Returns *self*, so this method can easily be chained with more
        calls to :meth:`rotate`, :meth:`rotate_deg`, :meth:`translate`
        and :meth:`scale`.
        """
        ...
    def rotate_deg(self, degrees: float) -> Affine2D:
        """
        Add a rotation (in degrees) to this transform in place.

        Returns *self*, so this method can easily be chained with more
        calls to :meth:`rotate`, :meth:`rotate_deg`, :meth:`translate`
        and :meth:`scale`.
        """
        ...
    def rotate_around(self, x: float, y: float, theta: float) -> Affine2D:
        """
        Add a rotation (in radians) around the point (x, y) in place.

        Returns *self*, so this method can easily be chained with more
        calls to :meth:`rotate`, :meth:`rotate_deg`, :meth:`translate`
        and :meth:`scale`.
        """
        ...
    def rotate_deg_around(self, x: float, y: float, degrees: float) -> Affine2D:
        """
        Add a rotation (in degrees) around the point (x, y) in place.

        Returns *self*, so this method can easily be chained with more
        calls to :meth:`rotate`, :meth:`rotate_deg`, :meth:`translate`
        and :meth:`scale`.
        """
        ...
    def translate(self, tx: float, ty: float) -> Affine2D:
        """
        Add a translation in place.

        Returns *self*, so this method can easily be chained with more
        calls to :meth:`rotate`, :meth:`rotate_deg`, :meth:`translate`
        and :meth:`scale`.
        """
        ...
    def scale(self, sx: float, sy: float = ...) -> Affine2D:
        """
        Add a scale in place.

        If *sy* is None, the same scale is applied in both the *x*- and
        *y*-directions.

        Returns *self*, so this method can easily be chained with more
        calls to :meth:`rotate`, :meth:`rotate_deg`, :meth:`translate`
        and :meth:`scale`.
        """
        ...
    def skew(self, xShear: float, yShear: float) -> Affine2D:
        """
        Add a skew in place.

        *xShear* and *yShear* are the shear angles along the *x*- and
        *y*-axes, respectively, in radians.

        Returns *self*, so this method can easily be chained with more
        calls to :meth:`rotate`, :meth:`rotate_deg`, :meth:`translate`
        and :meth:`scale`.
        """
        ...
    def skew_deg(self, xShear: float, yShear: float) -> Affine2D:
        """
        Add a skew in place.

        *xShear* and *yShear* are the shear angles along the *x*- and
        *y*-axes, respectively, in degrees.

        Returns *self*, so this method can easily be chained with more
        calls to :meth:`rotate`, :meth:`rotate_deg`, :meth:`translate`
        and :meth:`scale`.
        """
        ...

class IdentityTransform(Affine2DBase):
    """
    A special class that does one thing, the identity transform, in a
    fast way.
    """

    _mtx = np.identity(3)
    def frozen(self): ...
    def get_matrix(self): ...
    def transform(self, points: ArrayLike) -> np.ndarray: ...
    def transform_affine(self, points: ArrayLike) -> np.ndarray: ...
    def transform_non_affine(self, points: ArrayLike) -> np.ndarray: ...
    def transform_path(self, path: Path) -> Path: ...
    def transform_path_affine(self, path: Path) -> Path: ...
    def transform_path_non_affine(self, path: Path) -> Path: ...
    def get_affine(self): ...
    def inverted(self) -> Transform: ...

class _BlendedMixin:
    """Common methods for `BlendedGenericTransform` and `BlendedAffine2D`."""

    def __eq__(self, other) -> bool: ...
    def contains_branch_seperately(self, transform: Transform) -> bool: ...

class BlendedGenericTransform(_BlendedMixin, Transform):
    """
    A "blended" transform uses one transform for the *x*-direction, and
    another transform for the *y*-direction.

    This "generic" version can handle any given child transform in the
    *x*- and *y*-directions.
    """

    input_dims = ...
    output_dims = ...
    is_separable = ...
    pass_through = ...
    def __init__(
        self, x_transform: Transform, y_transform: Transform, **kwargs
    ) -> None:
        """
        Create a new "blended" transform using *x_transform* to transform the
        *x*-axis and *y_transform* to transform the *y*-axis.

        You will generally not call this constructor directly but use the
        `blended_transform_factory` function instead, which can determine
        automatically which kind of blended transform to create.
        """
        ...
    @property
    def depth(self): ...
    def contains_branch(self, other: Transform) -> bool: ...

    is_affine = ...
    has_inverse = ...
    def frozen(self): ...
    def transform_non_affine(self, points: ArrayLike) -> np.ndarray: ...
    def inverted(self) -> Transform: ...
    def get_affine(self): ...

class BlendedAffine2D(_BlendedMixin, Affine2DBase):
    """
    A "blended" transform uses one transform for the *x*-direction, and
    another transform for the *y*-direction.

    This version is an optimization for the case where both child
    transforms are of type `Affine2DBase`.
    """

    is_separable = ...
    def __init__(
        self, x_transform: Transform, y_transform: Transform, **kwargs
    ) -> None:
        """
        Create a new "blended" transform using *x_transform* to transform the
        *x*-axis and *y_transform* to transform the *y*-axis.

        Both *x_transform* and *y_transform* must be 2D affine transforms.

        You will generally not call this constructor directly but use the
        `blended_transform_factory` function instead, which can determine
        automatically which kind of blended transform to create.
        """
        ...
    def get_matrix(self): ...

def blended_transform_factory(
    x_transform: Transform, y_transform: Transform
) -> Transform:
    """
    Create a new "blended" transform using *x_transform* to transform
    the *x*-axis and *y_transform* to transform the *y*-axis.

    A faster version of the blended transform is returned for the case
    where both child transforms are affine.
    """
    ...

class CompositeGenericTransform(Transform):
    """
    A composite transform formed by applying transform *a* then
    transform *b*.

    This "generic" version can handle any two arbitrary
    transformations.
    """

    pass_through = ...
    def __init__(self, a: Transform, b: Transform, **kwargs) -> None:
        """
        Create a new composite transform that is the result of
        applying transform *a* then transform *b*.

        You will generally not call this constructor directly but write ``a +
        b`` instead, which will automatically choose the best kind of composite
        transform instance to create.
        """
        ...
    def frozen(self): ...
    def __eq__(self, other) -> bool: ...

    depth = ...
    is_affine = ...
    is_separable = ...
    has_inverse = ...

    def transform_affine(self, points: ArrayLike) -> np.ndarray: ...
    def transform_non_affine(self, points: ArrayLike) -> np.ndarray: ...
    def transform_path_non_affine(self, path: Path) -> Path: ...
    def get_affine(self): ...
    def inverted(self) -> Transform: ...

class CompositeAffine2D(Affine2DBase):
    """
    A composite transform formed by applying transform *a* then transform *b*.

    This version is an optimization that handles the case where both *a*
    and *b* are 2D affines.
    """

    def __init__(self, a: Transform, b: Transform, **kwargs) -> None:
        """
        Create a new composite transform that is the result of
        applying `Affine2DBase` *a* then `Affine2DBase` *b*.

        You will generally not call this constructor directly but write ``a +
        b`` instead, which will automatically choose the best kind of composite
        transform instance to create.
        """
        ...
    @property
    def depth(self): ...
    def get_matrix(self): ...

def composite_transform_factory(a: Transform, b: Transform) -> Transform:
    """
    Create a new composite transform that is the result of applying
    transform a then transform b.

    Shortcut versions of the blended transform are provided for the
    case where both child transforms are affine, or one or the other
    is the identity transform.

    Composite transforms may also be created using the '+' operator,
    e.g.::

      c = a + b
    """
    ...

class BboxTransform(Affine2DBase):
    """
    `BboxTransform` linearly transforms points from one `Bbox` to another.
    """

    is_separable = ...
    def __init__(self, boxin, boxout, **kwargs) -> None:
        """
        Create a new `BboxTransform` that linearly transforms
        points from *boxin* to *boxout*.
        """
        ...
    def get_matrix(self): ...

class BboxTransformTo(Affine2DBase):
    """
    `BboxTransformTo` is a transformation that linearly transforms points from
    the unit bounding box to a given `Bbox`.
    """

    is_separable = ...
    def __init__(self, boxout, **kwargs) -> None:
        """
        Create a new `BboxTransformTo` that linearly transforms
        points from the unit bounding box to *boxout*.
        """
        ...
    def get_matrix(self): ...

class BboxTransformToMaxOnly(BboxTransformTo):
    """
    `BboxTransformTo` is a transformation that linearly transforms points from
    the unit bounding box to a given `Bbox` with a fixed upper left of (0, 0).
    """

    def get_matrix(self): ...

class BboxTransformFrom(Affine2DBase):
    """
    `BboxTransformFrom` linearly transforms points from a given `Bbox` to the
    unit bounding box.
    """

    is_separable = ...
    def __init__(self, boxin, **kwargs) -> None: ...
    def get_matrix(self): ...

class ScaledTranslation(Affine2DBase):
    """
    A transformation that translates by *xt* and *yt*, after *xt* and *yt*
    have been transformed by *scale_trans*.
    """

    def __init__(self, xt: float, yt: float, scale_trans, **kwargs) -> None: ...
    def get_matrix(self): ...

class AffineDeltaTransform(Affine2DBase):
    r"""
    A transform wrapper for transforming displacements between pairs of points.

    This class is intended to be used to transform displacements ("position
    deltas") between pairs of points (e.g., as the ``offset_transform``
    of `.Collection`\s): given a transform ``t`` such that ``t =
    AffineDeltaTransform(t) + offset``, ``AffineDeltaTransform``
    satisfies ``AffineDeltaTransform(a - b) == AffineDeltaTransform(a) -
    AffineDeltaTransform(b)``.

    This is implemented by forcing the offset components of the transform
    matrix to zero.

    This class is experimental as of 3.3, and the API may change.
    """
    def __init__(self, transform: Transform, **kwargs) -> None: ...
    def get_matrix(self): ...

class TransformedPath(TransformNode):
    """
    A `TransformedPath` caches a non-affine transformed copy of the
    `~.path.Path`.  This cached copy is automatically updated when the
    non-affine part of the transform changes.

    .. note::

        Paths are considered immutable by this class. Any update to the
        path's vertices/codes will not trigger a transform recomputation.

    """

    def __init__(self, path, transform: Transform) -> None:
        """
        Parameters
        ----------
        path : `~.path.Path`
        transform : `Transform`
        """
        ...
    def get_transformed_points_and_affine(self) -> Path:
        """
        Return a copy of the child path, with the non-affine part of
        the transform already applied, along with the affine part of
        the path necessary to complete the transformation.  Unlike
        :meth:`get_transformed_path_and_affine`, no interpolation will
        be performed.
        """
        ...
    def get_transformed_path_and_affine(self) -> Path:
        """
        Return a copy of the child path, with the non-affine part of
        the transform already applied, along with the affine part of
        the path necessary to complete the transformation.
        """
        ...
    def get_fully_transformed_path(self) -> Path:
        """
        Return a fully-transformed copy of the child path.
        """
        ...
    def get_affine(self): ...

class TransformedPatchPath(TransformedPath):
    """
    A `TransformedPatchPath` caches a non-affine transformed copy of the
    `~.patches.Patch`. This cached copy is automatically updated when the
    non-affine part of the transform or the patch changes.
    """

    def __init__(self, patch: Patch) -> None:
        """
        Parameters
        ----------
        patch : `~.patches.Patch`
        """
        ...

def nonsingular(
    vmin: float,
    vmax: float,
    expander: float = ...,
    tiny: float = ...,
    increasing: bool = ...,
):
    """
    Modify the endpoints of a range as needed to avoid singularities.

    Parameters
    ----------
    vmin, vmax : float
        The initial endpoints.
    expander : float, default: 0.001
        Fractional amount by which *vmin* and *vmax* are expanded if
        the original interval is too small, based on *tiny*.
    tiny : float, default: 1e-15
        Threshold for the ratio of the interval to the maximum absolute
        value of its endpoints.  If the interval is smaller than
        this, it will be expanded.  This value should be around
        1e-15 or larger; otherwise the interval will be approaching
        the double precision resolution limit.
    increasing : bool, default: True
        If True, swap *vmin*, *vmax* if *vmin* > *vmax*.

    Returns
    -------
    vmin, vmax : float
        Endpoints, expanded and/or swapped if necessary.
        If either input is inf or NaN, or if both inputs are 0 or very
        close to zero, it returns -*expander*, *expander*.
    """
    ...

def interval_contains(interval: Sequence[float], val: float) -> bool:
    """
    Check, inclusively, whether an interval includes a given value.

    Parameters
    ----------
    interval : (float, float)
        The endpoints of the interval.
    val : float
        Value to check is within interval.

    Returns
    -------
    bool
        Whether *val* is within the *interval*.
    """
    ...

def interval_contains_open(interval: Sequence[float], val: float) -> bool:
    """
    Check, excluding endpoints, whether an interval includes a given value.

    Parameters
    ----------
    interval : (float, float)
        The endpoints of the interval.
    val : float
        Value to check is within interval.

    Returns
    -------
    bool
        Whether *val* is within the *interval*.
    """
    ...

def offset_copy(
    trans: Transform,
    fig: Figure | None = None,
    x: float = 0,
    y: float = 0,
    units: Literal["inches", "points", "dots"] = "inches",
) -> Transform:
    """
    Return a new transform with an added offset.

    Parameters
    ----------
    trans : `Transform` subclass
        Any transform, to which offset will be applied.
    fig : `~Figure`, default: None
        Current figure. It can be None if *units* are 'dots'.
    x, y : float, default: 0.0
        The offset to apply.
    units : {'inches', 'points', 'dots'}, default: 'inches'
        Units of the offset.

    Returns
    -------
    `Transform` subclass
        Transform with applied offset.
    """
    ...
