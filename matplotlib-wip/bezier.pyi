from ._typing import *
from typing import Callable

class NonIntersectingPathException(ValueError): ...

def get_intersection(cx1, cy1, cos_t1, sin_t1, cx2, cy2, cos_t2, sin_t2):
    """
    Return the intersection between the line through (*cx1*, *cy1*) at angle
    *t1* and the line through (*cx2*, *cy2*) at angle *t2*.
    """
    ...

def get_normal_points(cx, cy, cos_t, sin_t, length):
    """
    For a line passing through (*cx*, *cy*) and having an angle *t*, return
    locations of the two points located along its perpendicular line at the
    distance of *length*.
    """
    ...

def split_de_casteljau(beta, t):
    """
    Split a Bezier segment defined by its control points *beta* into two
    separate segments divided at *t* and return their control points.
    """
    ...

def find_bezier_t_intersecting_with_closedpath(
    bezier_point_at_t: Callable,
    inside_closedpath: Callable,
    t0: float = ...,
    t1: float = ...,
    tolerance: float = ...,
) -> tuple[float, float]:
    """
    Find the intersection of the Bezier curve with a closed path.

    The intersection point *t* is approximated by two parameters *t0*, *t1*
    such that *t0* <= *t* <= *t1*.

    Search starts from *t0* and *t1* and uses a simple bisecting algorithm
    therefore one of the end points must be inside the path while the other
    doesn't. The search stops when the distance of the points parametrized by
    *t0* and *t1* gets smaller than the given *tolerance*.

    Parameters
    ----------
    bezier_point_at_t : callable
        A function returning x, y coordinates of the Bezier at parameter *t*.
        It must have the signature::

            bezier_point_at_t(t: float) -> tuple[float, float]

    inside_closedpath : callable
        A function returning True if a given point (x, y) is inside the
        closed path. It must have the signature::

            inside_closedpath(point: tuple[float, float]) -> bool

    t0, t1 : float
        Start parameters for the search.

    tolerance : float
        Maximal allowed distance between the final points.

    Returns
    -------
    t0, t1 : float
        The Bezier path parameters.
    """
    ...

class BezierSegment:
    """
    A d-dimensional Bezier segment.

    Parameters
    ----------
    control_points : (N, d) array
        Location of the *N* control points.
    """

    def __init__(self, control_points) -> None: ...
    def __call__(self, t: ArrayLike) -> tuple:
        """
        Evaluate the Bezier curve at point(s) t in [0, 1].

        Parameters
        ----------
        t : (k,) array-like
            Points at which to evaluate the curve.

        Returns
        -------
        (k, d) array
            Value of the curve for each point in *t*.
        """
        ...
    def point_at_t(self, t) -> tuple[float]:
        """
        Evaluate the curve at a single point, returning a tuple of *d* floats.
        """
        ...
    @property
    def control_points(self):
        """The control points of the curve."""
        ...
    @property
    def dimension(self):
        """The dimension of the curve."""
        ...
    @property
    def degree(self) -> int:
        """Degree of the polynomial. One less the number of control points."""
        ...
    @property
    def polynomial_coefficients(self):
        r"""
        The polynomial coefficients of the Bezier curve.

        .. warning:: Follows opposite convention from `numpy.polyval`.

        Returns
        -------
        (n+1, d) array
            Coefficients after expanding in polynomial basis, where :math:`n`
            is the degree of the bezier curve and :math:`d` its dimension.
            These are the numbers (:math:`C_j`) such that the curve can be
            written :math:`\sum_{j=0}^n C_j t^j`.

        Notes
        -----
        The coefficients are calculated as

        .. math::

            {n \choose j} \sum_{i=0}^j (-1)^{i+j} {j \choose i} P_i

        where :math:`P_i` are the control points of the curve.
        """
        ...
    def axis_aligned_extrema(self) -> tuple:
        """
        Return the dimension and location of the curve's interior extrema.

        The extrema are the points along the curve where one of its partial
        derivatives is zero.

        Returns
        -------
        dims : array of int
            Index :math:`i` of the partial derivative which is zero at each
            interior extrema.
        dzeros : array of float
            Of same size as dims. The :math:`t` such that :math:`d/dx_i B(t) =
            0`
        """
        ...

def split_bezier_intersecting_with_closedpath(
    bezier, inside_closedpath: Callable, tolerance: float = ...
) -> list:
    """
    Split a Bezier curve into two at the intersection with a closed path.

    Parameters
    ----------
    bezier : (N, 2) array-like
        Control points of the Bezier segment. See `.BezierSegment`.
    inside_closedpath : callable
        A function returning True if a given point (x, y) is inside the
        closed path. See also `.find_bezier_t_intersecting_with_closedpath`.
    tolerance : float
        The tolerance for the intersection. See also
        `.find_bezier_t_intersecting_with_closedpath`.

    Returns
    -------
    left, right
        Lists of control points for the two Bezier segments.
    """
    ...

def split_path_inout(path, inside, tolerance=..., reorder_inout=...):
    """
    Divide a path into two segments at the point where ``inside(x, y)`` becomes
    False.
    """
    ...

def inside_circle(cx, cy, r) -> Callable:
    """
    Return a function that checks whether a point is in a circle with center
    (*cx*, *cy*) and radius *r*.

    The returned function has the signature::

        f(xy: tuple[float, float]) -> bool
    """
    ...

def get_cos_sin(x0, y0, x1, y1): ...
def check_if_parallel(
    dx1: float, dy1: float, dx2: float, dy2: float, tolerance: float = ...
) -> bool:
    """
    Check if two lines are parallel.

    Parameters
    ----------
    dx1, dy1, dx2, dy2 : float
        The gradients *dy*/*dx* of the two lines.
    tolerance : float
        The angular tolerance in radians up to which the lines are considered
        parallel.

    Returns
    -------
    is_parallel
        - 1 if two lines are parallel in same direction.
        - -1 if two lines are parallel in opposite direction.
        - False otherwise.
    """
    ...

def get_parallels(bezier2, width):
    """
    Given the quadratic Bezier control points *bezier2*, returns
    control points of quadratic Bezier lines roughly parallel to given
    one separated by *width*.
    """
    ...

def find_control_points(c1x, c1y, mmx, mmy, c2x, c2y):
    """
    Find control points of the Bezier curve passing through (*c1x*, *c1y*),
    (*mmx*, *mmy*), and (*c2x*, *c2y*), at parametric values 0, 0.5, and 1.
    """
    ...

def make_wedged_bezier2(bezier2, width, w1=..., wm=..., w2=...):
    """
    Being similar to get_parallels, returns control points of two quadratic
    Bezier lines having a width roughly parallel to given one separated by
    *width*.
    """
    ...
