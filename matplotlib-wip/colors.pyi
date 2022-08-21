from .scale import AsinhScale, FuncScale, LogScale, SymmetricalLogScale
import numpy as np
from typing import Callable, Literal
from matplotlib._typing import *

import functools
from collections.abc import Mapping

class _ColorMapping(dict):
    def __init__(self, mapping) -> None: ...
    def __setitem__(self, key, value): ...
    def __delitem__(self, key): ...

def get_named_colors_mapping():
    """Return the global mapping of names to named colors."""
    ...

class ColorSequenceRegistry(Mapping):
    r"""
    Container for sequences of colors that are known to Matplotlib by name.

    The universal registry instance is `matplotlib.color_sequences`. There
    should be no need for users to instantiate `.ColorSequenceRegistry`
    themselves.

    Read access uses a dict-like interface mapping names to lists of colors::

        import matplotlib as mpl
        cmap = mpl.color_sequences['tab10']

    The returned lists are copies, so that their modification does not change
    the global definition of the color sequence.

    Additional color sequences can be added via
    `.ColorSequenceRegistry.register`::

        mpl.color_sequences.register('rgb', ['r', 'g', 'b'])
    """

    def __init__(self) -> None: ...
    def __getitem__(self, item): ...
    def __iter__(self): ...
    def __len__(self): ...
    def __str__(self) -> str: ...
    def register(self, name: str, color_list: list[Color]):
        """
        Register a new color sequence.

        The color sequence registry stores a copy of the given *color_list*, so
        that future changes to the original list do not affect the registered
        color sequence. Think of this as the registry taking a snapshot
        of *color_list* at registration.

        Parameters
        ----------
        name : str
            The name for the color sequence.

        color_list : list of colors
            An iterable returning valid Matplotlib colors when iterating over.
            Note however that the returned color sequence will always be a
            list regardless of the input type.

        """
        ...
    def unregister(self, name):
        """
        Remove a sequence from the registry.

        You cannot remove built-in color sequences.

        If the name is not registered, returns with no error.
        """
        ...

def is_color_like(c):
    """Return whether *c* can be interpreted as an RGB(A) color."""
    ...

def same_color(c1, c2):
    """
    Return whether the colors *c1* and *c2* are the same.

    *c1*, *c2* can be single colors or lists/arrays of colors.
    """
    ...

def to_rgba(c: np.ma.masked_array, alpha: float = ...) -> tuple:
    """
    Convert *c* to an RGBA color.

    Parameters
    ----------
    c : Matplotlib color or ``np.ma.masked``

    alpha : float, optional
        If *alpha* is given, force the alpha value of the returned RGBA tuple
        to *alpha*.

        If None, the alpha value from *c* is used. If *c* does not have an
        alpha channel, then alpha defaults to 1.

        *alpha* is ignored for the color value ``"none"`` (case-insensitive),
        which always maps to ``(0, 0, 0, 0)``.

    Returns
    -------
    tuple
        Tuple of floats ``(r, g, b, a)``, where each channel (red, green, blue,
        alpha) can assume values between 0 and 1.
    """
    ...

def to_rgba_array(c: ArrayLike, alpha: float = ...) -> list:
    """
    Convert *c* to a (n, 4) array of RGBA colors.

    Parameters
    ----------
    c : Matplotlib color or array of colors
        If *c* is a masked array, an np.ndarray is returned with a (0, 0, 0, 0)
        row for each masked value or row in *c*.

    alpha : float or sequence of floats, optional
        If *alpha* is given, force the alpha value of the returned RGBA tuple
        to *alpha*.

        If None, the alpha value from *c* is used. If *c* does not have an
        alpha channel, then alpha defaults to 1.

        *alpha* is ignored for the color value ``"none"`` (case-insensitive),
        which always maps to ``(0, 0, 0, 0)``.

        If *alpha* is a sequence and *c* is a single color, *c* will be
        repeated to match the length of *alpha*.

    Returns
    -------
    array
        (n, 4) array of RGBA colors,  where each channel (red, green, blue,
        alpha) can assume values between 0 and 1.
    """
    ...

def to_rgb(c):
    """Convert *c* to an RGB color, silently dropping the alpha channel."""
    ...

def to_hex(c: np.ma.masked_array, keep_alpha: bool = ...) -> str:
    """
    Convert *c* to a hex color.

    Parameters
    ----------
    c : :doc:`color </tutorials/colors/colors>` or `numpy.ma.masked`

    keep_alpha : bool, default: False
      If False, use the ``#rrggbb`` format, otherwise use ``#rrggbbaa``.

    Returns
    -------
    str
      ``#rrggbb`` or ``#rrggbbaa`` hex color string
    """
    ...

cnames = ...
hexColorPattern = ...
rgb2hex = ...
hex2color = ...

class ColorConverter:
    """
    A class only kept for backwards compatibility.

    Its functionality is entirely provided by module-level functions.
    """

    colors = ...
    cache = ...
    to_rgb = ...
    to_rgba = ...
    to_rgba_array = ...

colorConverter = ...

class Colormap:
    """
    Baseclass for all scalar to RGBA mappings.

    Typically, Colormap instances are used to convert data values (floats)
    from the interval ``[0, 1]`` to the RGBA color that the respective
    Colormap represents. For scaling of data into the ``[0, 1]`` interval see
    `Normalize`. Subclasses of `ScalarMappable`
    make heavy use of this ``data -> normalize -> map-to-color`` processing
    chain.
    """

    def __init__(self, name, N=...) -> None:
        """
        Parameters
        ----------
        name : str
            The name of the colormap.
        N : int
            The number of rgb quantization levels.
        """
        ...
    def __call__(
        self,
        X: float | int | np.ndarray | Scalar,
        alpha: float | ArrayLike | None = ...,
        bytes: bool = ...,
    ) -> tuple:
        """
        Parameters
        ----------
        X : float or int, np.ndarray or scalar
            The data value(s) to convert to RGBA.
            For floats, X should be in the interval ``[0.0, 1.0]`` to
            return the RGBA values ``X*100`` percent along the Colormap line.
            For integers, X should be in the interval ``[0, Colormap.N)`` to
            return RGBA values *indexed* from the Colormap with index ``X``.
        alpha : float or array-like or None
            Alpha must be a scalar between 0 and 1, a sequence of such
            floats with shape matching X, or None.
        bytes : bool
            If False (default), the returned RGBA values will be floats in the
            interval ``[0, 1]`` otherwise they will be uint8s in the interval
            ``[0, 255]``.

        Returns
        -------
        Tuple of RGBA values if X is scalar, otherwise an array of
        RGBA values with a shape of ``X.shape + (4, )``.
        """
        ...
    def __copy__(self): ...
    def __eq__(self, other) -> bool: ...
    def get_bad(self):
        """Get the color for masked values."""
        ...
    def set_bad(self, color=..., alpha=...):
        """Set the color for masked values."""
        ...
    def get_under(self):
        """Get the color for low out-of-range values."""
        ...
    def set_under(self, color=..., alpha=...):
        """Set the color for low out-of-range values."""
        ...
    def get_over(self):
        """Get the color for high out-of-range values."""
        ...
    def set_over(self, color=..., alpha=...):
        """Set the color for high out-of-range values."""
        ...
    def set_extremes(self, *, bad=..., under=..., over=...):
        """
        Set the colors for masked (*bad*) values and, when ``norm.clip =
        False``, low (*under*) and high (*over*) out-of-range values.
        """
        ...
    def with_extremes(self, *, bad=..., under=..., over=...):
        """
        Return a copy of the colormap, for which the colors for masked (*bad*)
        values and, when ``norm.clip = False``, low (*under*) and high (*over*)
        out-of-range values, have been set accordingly.
        """
        ...
    def is_gray(self):
        """Return whether the colormap is grayscale."""
        ...
    def reversed(self, name: str = ...):
        """
        Return a reversed instance of the Colormap.

        .. note:: This function is not implemented for base class.

        Parameters
        ----------
        name : str, optional
            The name for the reversed colormap. If it's None the
            name will be the name of the parent colormap + "_r".

        See Also
        --------
        LinearSegmentedColormap.reversed
        ListedColormap.reversed
        """
        ...
    def copy(self):
        """Return a copy of the colormap."""
        ...

class LinearSegmentedColormap(Colormap):
    """
    Colormap objects based on lookup tables using linear segments.

    The lookup table is generated using linear interpolation for each
    primary color, with the 0-1 domain divided into any number of
    segments.
    """

    def __init__(self, name, segmentdata, N=..., gamma=...) -> None:
        """
        Create colormap from linear mapping segments

        segmentdata argument is a dictionary with a red, green and blue
        entries. Each entry should be a list of *x*, *y0*, *y1* tuples,
        forming rows in a table. Entries for alpha are optional.

        Example: suppose you want red to increase from 0 to 1 over
        the bottom half, green to do the same over the middle half,
        and blue over the top half.  Then you would use::

            cdict = {'red':   [(0.0,  0.0, 0.0),
                               (0.5,  1.0, 1.0),
                               (1.0,  1.0, 1.0)],

                     'green': [(0.0,  0.0, 0.0),
                               (0.25, 0.0, 0.0),
                               (0.75, 1.0, 1.0),
                               (1.0,  1.0, 1.0)],

                     'blue':  [(0.0,  0.0, 0.0),
                               (0.5,  0.0, 0.0),
                               (1.0,  1.0, 1.0)]}

        Each row in the table for a given color is a sequence of
        *x*, *y0*, *y1* tuples.  In each sequence, *x* must increase
        monotonically from 0 to 1.  For any input value *z* falling
        between *x[i]* and *x[i+1]*, the output value of a given color
        will be linearly interpolated between *y1[i]* and *y0[i+1]*::

            row i:   x  y0  y1
                           /
                          /
            row i+1: x  y0  y1

        Hence y0 in the first row and y1 in the last row are never used.

        See Also
        --------
        LinearSegmentedColormap.from_list
            Static method; factory function for generating a smoothly-varying
            LinearSegmentedColormap.
        """
        ...
    def set_gamma(self, gamma):
        """Set a new gamma value and regenerate colormap."""
        ...
    @staticmethod
    def from_list(name: str, colors, N: int = ..., gamma: float = ...):
        """
        Create a `LinearSegmentedColormap` from a list of colors.

        Parameters
        ----------
        name : str
            The name of the colormap.
        colors : array-like of colors or array-like of (value, color)
            If only colors are given, they are equidistantly mapped from the
            range :math:`[0, 1]`; i.e. 0 maps to ``colors[0]`` and 1 maps to
            ``colors[-1]``.
            If (value, color) pairs are given, the mapping is from *value*
            to *color*. This can be used to divide the range unevenly.
        N : int
            The number of rgb quantization levels.
        gamma : float
        """
        ...
    def reversed(self, name: str = ...) -> LinearSegmentedColormap:
        """
        Return a reversed instance of the Colormap.

        Parameters
        ----------
        name : str, optional
            The name for the reversed colormap. If it's None the
            name will be the name of the parent colormap + "_r".

        Returns
        -------
        LinearSegmentedColormap
            The reversed colormap.
        """
        ...

class ListedColormap(Colormap):
    """
    Colormap object generated from a list of colors.

    This may be most useful when indexing directly into a colormap,
    but it can also be used to generate special colormaps for ordinary
    mapping.

    Parameters
    ----------
    colors : list, array
        List of Matplotlib color specifications, or an equivalent Nx3 or Nx4
        floating point array (*N* rgb or rgba values).
    name : str, optional
        String to identify the colormap.
    N : int, optional
        Number of entries in the map. The default is *None*, in which case
        there is one colormap entry for each element in the list of colors.
        If ::

            N < len(colors)

        the list will be truncated at *N*. If ::

            N > len(colors)

        the list will be extended by repetition.
    """

    def __init__(self, colors: list, array, name: str = ..., N: int = ...) -> None: ...
    def reversed(self, name: str = ...) -> ListedColormap:
        """
        Return a reversed instance of the Colormap.

        Parameters
        ----------
        name : str, optional
            The name for the reversed colormap. If it's None the
            name will be the name of the parent colormap + "_r".

        Returns
        -------
        ListedColormap
            A reversed instance of the colormap.
        """
        ...

class Normalize:
    """
    A class which, when called, linearly normalizes data into the
    ``[0.0, 1.0]`` interval.
    """

    def __init__(self, vmin=..., vmax=..., clip=...) -> None:
        """
        Parameters
        ----------
        vmin, vmax : float or None
            If *vmin* and/or *vmax* is not given, they are initialized from the
            minimum and maximum value, respectively, of the first input
            processed; i.e., ``__call__(A)`` calls ``autoscale_None(A)``.

        clip : bool, default: False
            If ``True`` values falling outside the range ``[vmin, vmax]``,
            are mapped to 0 or 1, whichever is closer, and masked values are
            set to 1.  If ``False`` masked values remain masked.

            Clipping silently defeats the purpose of setting the over, under,
            and masked colors in a colormap, so it is likely to lead to
            surprises; therefore the default is ``clip=False``.

        Notes
        -----
        Returns 0 if ``vmin == vmax``.
        """
        ...
    @property
    def vmin(self): ...
    @vmin.setter
    def vmin(self, value): ...
    @property
    def vmax(self): ...
    @vmax.setter
    def vmax(self, value): ...
    @property
    def clip(self): ...
    @clip.setter
    def clip(self, value): ...
    @staticmethod
    def process_value(value):
        """
        Homogenize the input *value* for easy and efficient normalization.

        *value* can be a scalar or sequence.

        Returns
        -------
        result : masked array
            Masked array with the same shape as *value*.
        is_scalar : bool
            Whether *value* is a scalar.

        Notes
        -----
        Float dtypes are preserved; integer types with two bytes or smaller are
        converted to np.float32, and larger types are converted to np.float64.
        Preserving float32 when possible, and using in-place operations,
        greatly improves speed for large arrays.
        """
        ...
    def __call__(self, value, clip: bool = ...):
        """
        Normalize *value* data in the ``[vmin, vmax]`` interval into the
        ``[0.0, 1.0]`` interval and return it.

        Parameters
        ----------
        value
            Data to normalize.
        clip : bool
            If ``None``, defaults to ``self.clip`` (which defaults to
            ``False``).

        Notes
        -----
        If not already initialized, ``self.vmin`` and ``self.vmax`` are
        initialized using ``self.autoscale_None(value)``.
        """
        ...
    def inverse(self, value): ...
    def autoscale(self, A):
        """Set *vmin*, *vmax* to min, max of *A*."""
        ...
    def autoscale_None(self, A):
        """If vmin or vmax are not set, use the min/max of *A* to set them."""
        ...
    def scaled(self):
        """Return whether vmin and vmax are set."""
        ...

class TwoSlopeNorm(Normalize):
    def __init__(self, vcenter, vmin=..., vmax=...) -> None:
        """
        Normalize data with a set center.

        Useful when mapping data with an unequal rates of change around a
        conceptual center, e.g., data that range from -2 to 4, with 0 as
        the midpoint.

        Parameters
        ----------
        vcenter : float
            The data value that defines ``0.5`` in the normalization.
        vmin : float, optional
            The data value that defines ``0.0`` in the normalization.
            Defaults to the min value of the dataset.
        vmax : float, optional
            The data value that defines ``1.0`` in the normalization.
            Defaults to the max value of the dataset.

        Examples
        --------
        This maps data value -4000 to 0., 0 to 0.5, and +10000 to 1.0; data
        between is linearly interpolated::

            >>> import matplotlib.colors as mcolors
            >>> offset = mcolors.TwoSlopeNorm(vmin=-4000.,
                                              vcenter=0., vmax=10000)
            >>> data = [-4000., -2000., 0., 2500., 5000., 7500., 10000.]
            >>> offset(data)
            array([0., 0.25, 0.5, 0.625, 0.75, 0.875, 1.0])
        """
        ...
    @property
    def vcenter(self): ...
    @vcenter.setter
    def vcenter(self, value): ...
    def autoscale_None(self, A):
        """
        Get vmin and vmax, and then clip at vcenter
        """
        ...
    def __call__(self, value, clip=...):
        """
        Map value to the interval [0, 1]. The clip argument is unused.
        """
        ...
    def inverse(self, value): ...

class CenteredNorm(Normalize):
    def __init__(self, vcenter=..., halfrange=..., clip=...) -> None:
        """
        Normalize symmetrical data around a center (0 by default).

        Unlike `TwoSlopeNorm`, `CenteredNorm` applies an equal rate of change
        around the center.

        Useful when mapping symmetrical data around a conceptual center
        e.g., data that range from -2 to 4, with 0 as the midpoint, and
        with equal rates of change around that midpoint.

        Parameters
        ----------
        vcenter : float, default: 0
            The data value that defines ``0.5`` in the normalization.
        halfrange : float, optional
            The range of data values that defines a range of ``0.5`` in the
            normalization, so that *vcenter* - *halfrange* is ``0.0`` and
            *vcenter* + *halfrange* is ``1.0`` in the normalization.
            Defaults to the largest absolute difference to *vcenter* for
            the values in the dataset.

        Examples
        --------
        This maps data values -2 to 0.25, 0 to 0.5, and 4 to 1.0
        (assuming equal rates of change above and below 0.0):

            >>> import matplotlib.colors as mcolors
            >>> norm = mcolors.CenteredNorm(halfrange=4.0)
            >>> data = [-2., 0., 4.]
            >>> norm(data)
            array([0.25, 0.5 , 1.  ])
        """
        ...
    def autoscale(self, A):
        """
        Set *halfrange* to ``max(abs(A-vcenter))``, then set *vmin* and *vmax*.
        """
        ...
    def autoscale_None(self, A):
        """Set *vmin* and *vmax*."""
        ...
    @property
    def vcenter(self): ...
    @vcenter.setter
    def vcenter(self, vcenter): ...
    @property
    def halfrange(self): ...
    @halfrange.setter
    def halfrange(self, halfrange): ...
    def __call__(self, value, clip: bool = ...): ...

def make_norm_from_scale(scale_cls, base_norm_cls=..., *, init=...):
    """
    Decorator for building a `.Normalize` subclass from a `~.scale.ScaleBase`
    subclass.

    After ::

        @make_norm_from_scale(scale_cls)
        class norm_cls(Normalize):
            ...

    *norm_cls* is filled with methods so that normalization computations are
    forwarded to *scale_cls* (i.e., *scale_cls* is the scale that would be used
    for the colorbar of a mappable normalized with *norm_cls*).

    If *init* is not passed, then the constructor signature of *norm_cls*
    will be ``norm_cls(vmin=None, vmax=None, clip=False)``; these three
    parameters will be forwarded to the base class (``Normalize.__init__``),
    and a *scale_cls* object will be initialized with no arguments (other than
    a dummy axis).

    If the *scale_cls* constructor takes additional parameters, then *init*
    should be passed to `make_norm_from_scale`.  It is a callable which is
    *only* used for its signature.  First, this signature will become the
    signature of *norm_cls*.  Second, the *norm_cls* constructor will bind the
    parameters passed to it using this signature, extract the bound *vmin*,
    *vmax*, and *clip* values, pass those to ``Normalize.__init__``, and
    forward the remaining bound values (including any defaults defined by the
    signature) to the *scale_cls* constructor.
    """
    ...

@make_norm_from_scale(
    FuncScale, init=lambda functions, vmin=None, vmax=None, clip=False: None
)
class FuncNorm(Normalize):
    """
    Arbitrary normalization using functions for the forward and inverse.

    Parameters
    ----------
    functions : (callable, callable)
        two-tuple of the forward and inverse functions for the normalization.
        The forward function must be monotonic.

        Both functions must have the signature ::

           def forward(values: array-like) -> array-like

    vmin, vmax : float or None
        If *vmin* and/or *vmax* is not given, they are initialized from the
        minimum and maximum value, respectively, of the first input
        processed; i.e., ``__call__(A)`` calls ``autoscale_None(A)``.

    clip : bool, default: False
        If ``True`` values falling outside the range ``[vmin, vmax]``,
        are mapped to 0 or 1, whichever is closer, and masked values are
        set to 1.  If ``False`` masked values remain masked.

        Clipping silently defeats the purpose of setting the over, under,
        and masked colors in a colormap, so it is likely to lead to
        surprises; therefore the default is ``clip=False``.
    """

    ...

@make_norm_from_scale(functools.partial(LogScale, nonpositive="mask"))
class LogNorm(Normalize):
    """Normalize a given value to the 0-1 range on a log scale."""

    ...

@make_norm_from_scale(
    SymmetricalLogScale,
    init=lambda linthresh, linscale=1, vmin=None, vmax=None, clip=False, *, base=10: None,
)
class SymLogNorm(Normalize):
    """
    The symmetrical logarithmic scale is logarithmic in both the
    positive and negative directions from the origin.

    Since the values close to zero tend toward infinity, there is a
    need to have a range around zero that is linear.  The parameter
    *linthresh* allows the user to specify the size of this range
    (-*linthresh*, *linthresh*).

    Parameters
    ----------
    linthresh : float
        The range within which the plot is linear (to avoid having the plot
        go to infinity around zero).
    linscale : float, default: 1
        This allows the linear range (-*linthresh* to *linthresh*) to be
        stretched relative to the logarithmic range. Its value is the
        number of decades to use for each half of the linear range. For
        example, when *linscale* == 1.0 (the default), the space used for
        the positive and negative halves of the linear range will be equal
        to one decade in the logarithmic range.
    base : float, default: 10
    """

    @property
    def linthresh(self): ...
    @linthresh.setter
    def linthresh(self, value): ...

@make_norm_from_scale(
    AsinhScale, init=lambda linear_width=1, vmin=None, vmax=None, clip=False: None
)
class AsinhNorm(Normalize):
    """
    The inverse hyperbolic sine scale is approximately linear near
    the origin, but becomes logarithmic for larger positive
    or negative values. Unlike the `SymLogNorm`, the transition between
    these linear and logarithmic regions is smooth, which may reduce
    the risk of visual artifacts.

    .. note::

       This API is provisional and may be revised in the future
       based on early user feedback.

    Parameters
    ----------
    linear_width : float, default: 1
        The effective width of the linear region, beyond which
        the transformation becomes asymptotically logarithmic
    """

    @property
    def linear_width(self): ...
    @linear_width.setter
    def linear_width(self, value): ...

class PowerNorm(Normalize):
    """
    Linearly map a given value to the 0-1 range and then apply
    a power-law normalization over that range.
    """

    def __init__(self, gamma, vmin=..., vmax=..., clip=...) -> None: ...
    def __call__(self, value, clip: bool = ...): ...
    def inverse(self, value): ...

class BoundaryNorm(Normalize):
    """
    Generate a colormap index based on discrete intervals.

    Unlike `Normalize` or `LogNorm`, `BoundaryNorm` maps values to integers
    instead of to the interval 0-1.
    """

    def __init__(self, boundaries, ncolors, clip=..., *, extend=...) -> None:
        """
        Parameters
        ----------
        boundaries : array-like
            Monotonically increasing sequence of at least 2 bin edges:  data
            falling in the n-th bin will be mapped to the n-th color.

        ncolors : int
            Number of colors in the colormap to be used.

        clip : bool, optional
            If clip is ``True``, out of range values are mapped to 0 if they
            are below ``boundaries[0]`` or mapped to ``ncolors - 1`` if they
            are above ``boundaries[-1]``.

            If clip is ``False``, out of range values are mapped to -1 if
            they are below ``boundaries[0]`` or mapped to *ncolors* if they are
            above ``boundaries[-1]``. These are then converted to valid indices
            by `Colormap.__call__`.

        extend : {'neither', 'both', 'min', 'max'}, default: 'neither'
            Extend the number of bins to include one or both of the
            regions beyond the boundaries.  For example, if ``extend``
            is 'min', then the color to which the region between the first
            pair of boundaries is mapped will be distinct from the first
            color in the colormap, and by default a
            `~matplotlib.colorbar.Colorbar` will be drawn with
            the triangle extension on the left or lower end.

        Notes
        -----
        If there are fewer bins (including extensions) than colors, then the
        color index is chosen by linearly interpolating the ``[0, nbins - 1]``
        range onto the ``[0, ncolors - 1]`` range, effectively skipping some
        colors in the middle of the colormap.
        """
        ...
    def __call__(self, value, clip=...):
        """
        This method behaves similarly to `.Normalize.__call__`, except that it
        returns integers or arrays of int16.
        """
        ...
    def inverse(self, value):
        """
        Raises
        ------
        ValueError
            BoundaryNorm is not invertible, so calling this method will always
            raise an error
        """
        ...

class NoNorm(Normalize):
    """
    Dummy replacement for `Normalize`, for the case where we want to use
    indices directly in a `~ScalarMappable`.
    """

    def __call__(self, value, clip: bool = ...): ...
    def inverse(self, value): ...

def rgb_to_hsv(arr):
    """
    Convert float rgb values (in the range [0, 1]), in a numpy array to hsv
    values.

    Parameters
    ----------
    arr : (..., 3) array-like
       All values must be in the range [0, 1]

    Returns
    -------
    (..., 3) np.ndarray
       Colors converted to hsv values in range [0, 1]
    """
    ...

def hsv_to_rgb(hsv):
    """
    Convert hsv values to rgb.

    Parameters
    ----------
    hsv : (..., 3) array-like
       All values assumed to be in range [0, 1]

    Returns
    -------
    (..., 3) np.ndarray
       Colors converted to RGB values in range [0, 1]
    """
    ...

class LightSource:
    """
    Create a light source coming from the specified azimuth and elevation.
    Angles are in degrees, with the azimuth measured
    clockwise from north and elevation up from the zero plane of the surface.

    `shade` is used to produce "shaded" rgb values for a data array.
    `shade_rgb` can be used to combine an rgb image with an elevation map.
    `hillshade` produces an illumination map of a surface.
    """

    def __init__(
        self,
        azdeg=...,
        altdeg=...,
        hsv_min_val=...,
        hsv_max_val=...,
        hsv_min_sat=...,
        hsv_max_sat=...,
    ) -> None:
        """
        Specify the azimuth (measured clockwise from south) and altitude
        (measured up from the plane of the surface) of the light source
        in degrees.

        Parameters
        ----------
        azdeg : float, default: 315 degrees (from the northwest)
            The azimuth (0-360, degrees clockwise from North) of the light
            source.
        altdeg : float, default: 45 degrees
            The altitude (0-90, degrees up from horizontal) of the light
            source.

        Notes
        -----
        For backwards compatibility, the parameters *hsv_min_val*,
        *hsv_max_val*, *hsv_min_sat*, and *hsv_max_sat* may be supplied at
        initialization as well.  However, these parameters will only be used if
        "blend_mode='hsv'" is passed into `shade` or `shade_rgb`.
        See the documentation for `blend_hsv` for more details.
        """
        ...
    @property
    def direction(self):
        """The unit vector direction towards the light source."""
        ...
    def hillshade(
        self,
        elevation,
        vert_exag: float = ...,
        dx: float = ...,
        dy: float = ...,
        fraction: float = ...,
    ) -> np.ndarray:
        """
        Calculate the illumination intensity for a surface using the defined
        azimuth and elevation for the light source.

        This computes the normal vectors for the surface, and then passes them
        on to `shade_normals`

        Parameters
        ----------
        elevation : 2D array-like
            The height values used to generate an illumination map
        vert_exag : number, optional
            The amount to exaggerate the elevation values by when calculating
            illumination. This can be used either to correct for differences in
            units between the x-y coordinate system and the elevation
            coordinate system (e.g. decimal degrees vs. meters) or to
            exaggerate or de-emphasize topographic effects.
        dx : number, optional
            The x-spacing (columns) of the input *elevation* grid.
        dy : number, optional
            The y-spacing (rows) of the input *elevation* grid.
        fraction : number, optional
            Increases or decreases the contrast of the hillshade.  Values
            greater than one will cause intermediate values to move closer to
            full illumination or shadow (and clipping any values that move
            beyond 0 or 1). Note that this is not visually or mathematically
            the same as vertical exaggeration.

        Returns
        -------
        np.ndarray
            A 2D array of illumination values between 0-1, where 0 is
            completely in shadow and 1 is completely illuminated.
        """
        ...
    def shade_normals(self, normals, fraction: float = ...) -> np.ndarray:
        """
        Calculate the illumination intensity for the normal vectors of a
        surface using the defined azimuth and elevation for the light source.

        Imagine an artificial sun placed at infinity in some azimuth and
        elevation position illuminating our surface. The parts of the surface
        that slope toward the sun should brighten while those sides facing away
        should become darker.

        Parameters
        ----------
        fraction : number, optional
            Increases or decreases the contrast of the hillshade.  Values
            greater than one will cause intermediate values to move closer to
            full illumination or shadow (and clipping any values that move
            beyond 0 or 1). Note that this is not visually or mathematically
            the same as vertical exaggeration.

        Returns
        -------
        np.ndarray
            A 2D array of illumination values between 0-1, where 0 is
            completely in shadow and 1 is completely illuminated.
        """
        ...
    def shade(
        self,
        data,
        cmap: Colormap,
        norm=...,
        blend_mode: Literal["hsv", "overlay", "soft"] | Callable = ...,
        vmin: float | None = ...,
        vmax: float | None = ...,
        vert_exag: float = ...,
        dx: float = ...,
        dy: float = ...,
        fraction: float = ...,
        **kwargs
    ) -> np.ndarray:
        """
        Combine colormapped data values with an illumination intensity map
        (a.k.a.  "hillshade") of the values.

        Parameters
        ----------
        data : 2D array-like
            The height values used to generate a shaded map.
        cmap : `~Colormap`
            The colormap used to color the *data* array. Note that this must be
            a `~Colormap` instance.  For example, rather than
            passing in ``cmap='gist_earth'``, use
            ``cmap=plt.get_cmap('gist_earth')`` instead.
        norm : `~Normalize` instance, optional
            The normalization used to scale values before colormapping. If
            None, the input will be linearly scaled between its min and max.
        blend_mode : {'hsv', 'overlay', 'soft'} or callable, optional
            The type of blending used to combine the colormapped data
            values with the illumination intensity.  Default is
            "overlay".  Note that for most topographic surfaces,
            "overlay" or "soft" appear more visually realistic. If a
            user-defined function is supplied, it is expected to
            combine an MxNx3 RGB array of floats (ranging 0 to 1) with
            an MxNx1 hillshade array (also 0 to 1).  (Call signature
            ``func(rgb, illum, **kwargs)``) Additional kwargs supplied
            to this function will be passed on to the *blend_mode*
            function.
        vmin : float or None, optional
            The minimum value used in colormapping *data*. If *None* the
            minimum value in *data* is used. If *norm* is specified, then this
            argument will be ignored.
        vmax : float or None, optional
            The maximum value used in colormapping *data*. If *None* the
            maximum value in *data* is used. If *norm* is specified, then this
            argument will be ignored.
        vert_exag : number, optional
            The amount to exaggerate the elevation values by when calculating
            illumination. This can be used either to correct for differences in
            units between the x-y coordinate system and the elevation
            coordinate system (e.g. decimal degrees vs. meters) or to
            exaggerate or de-emphasize topography.
        dx : number, optional
            The x-spacing (columns) of the input *elevation* grid.
        dy : number, optional
            The y-spacing (rows) of the input *elevation* grid.
        fraction : number, optional
            Increases or decreases the contrast of the hillshade.  Values
            greater than one will cause intermediate values to move closer to
            full illumination or shadow (and clipping any values that move
            beyond 0 or 1). Note that this is not visually or mathematically
            the same as vertical exaggeration.
        Additional kwargs are passed on to the *blend_mode* function.

        Returns
        -------
        np.ndarray
            An MxNx4 array of floats ranging between 0-1.
        """
        ...
    def shade_rgb(
        self,
        rgb: ArrayLike,
        elevation: ArrayLike,
        fraction: float = ...,
        blend_mode: Literal["hsv", "overlay", "soft"] | Callable = ...,
        vert_exag: float = ...,
        dx: float = ...,
        dy: float = ...,
        **kwargs
    ) -> np.ndarray:
        """
        Use this light source to adjust the colors of the *rgb* input array to
        give the impression of a shaded relief map with the given *elevation*.

        Parameters
        ----------
        rgb : array-like
            An (M, N, 3) RGB array, assumed to be in the range of 0 to 1.
        elevation : array-like
            An (M, N) array of the height values used to generate a shaded map.
        fraction : number
            Increases or decreases the contrast of the hillshade.  Values
            greater than one will cause intermediate values to move closer to
            full illumination or shadow (and clipping any values that move
            beyond 0 or 1). Note that this is not visually or mathematically
            the same as vertical exaggeration.
        blend_mode : {'hsv', 'overlay', 'soft'} or callable, optional
            The type of blending used to combine the colormapped data values
            with the illumination intensity.  For backwards compatibility, this
            defaults to "hsv". Note that for most topographic surfaces,
            "overlay" or "soft" appear more visually realistic. If a
            user-defined function is supplied, it is expected to combine an
            MxNx3 RGB array of floats (ranging 0 to 1) with an MxNx1 hillshade
            array (also 0 to 1).  (Call signature
            ``func(rgb, illum, **kwargs)``)
            Additional kwargs supplied to this function will be passed on to
            the *blend_mode* function.
        vert_exag : number, optional
            The amount to exaggerate the elevation values by when calculating
            illumination. This can be used either to correct for differences in
            units between the x-y coordinate system and the elevation
            coordinate system (e.g. decimal degrees vs. meters) or to
            exaggerate or de-emphasize topography.
        dx : number, optional
            The x-spacing (columns) of the input *elevation* grid.
        dy : number, optional
            The y-spacing (rows) of the input *elevation* grid.
        Additional kwargs are passed on to the *blend_mode* function.

        Returns
        -------
        np.ndarray
            An (m, n, 3) array of floats ranging between 0-1.
        """
        ...
    def blend_hsv(
        self,
        rgb: np.ndarray,
        intensity: np.ndarray,
        hsv_max_sat: float = ...,
        hsv_max_val: float = ...,
        hsv_min_val: float = ...,
        hsv_min_sat: float = ...,
    ) -> np.ndarray:
        """
        Take the input data array, convert to HSV values in the given colormap,
        then adjust those color values to give the impression of a shaded
        relief map with a specified light source.  RGBA values are returned,
        which can then be used to plot the shaded image with imshow.

        The color of the resulting image will be darkened by moving the (s, v)
        values (in hsv colorspace) toward (hsv_min_sat, hsv_min_val) in the
        shaded regions, or lightened by sliding (s, v) toward (hsv_max_sat,
        hsv_max_val) in regions that are illuminated.  The default extremes are
        chose so that completely shaded points are nearly black (s = 1, v = 0)
        and completely illuminated points are nearly white (s = 0, v = 1).

        Parameters
        ----------
        rgb : np.ndarray
            An MxNx3 RGB array of floats ranging from 0 to 1 (color image).
        intensity : np.ndarray
            An MxNx1 array of floats ranging from 0 to 1 (grayscale image).
        hsv_max_sat : number, default: 1
            The maximum saturation value that the *intensity* map can shift the
            output image to.
        hsv_min_sat : number, optional
            The minimum saturation value that the *intensity* map can shift the
            output image to. Defaults to 0.
        hsv_max_val : number, optional
            The maximum value ("v" in "hsv") that the *intensity* map can shift
            the output image to. Defaults to 1.
        hsv_min_val : number, optional
            The minimum value ("v" in "hsv") that the *intensity* map can shift
            the output image to. Defaults to 0.

        Returns
        -------
        np.ndarray
            An MxNx3 RGB array representing the combined images.
        """
        ...
    def blend_soft_light(self, rgb: np.ndarray, intensity: np.ndarray) -> np.ndarray:
        """
        Combine an rgb image with an intensity map using "soft light" blending,
        using the "pegtop" formula.

        Parameters
        ----------
        rgb : np.ndarray
            An MxNx3 RGB array of floats ranging from 0 to 1 (color image).
        intensity : np.ndarray
            An MxNx1 array of floats ranging from 0 to 1 (grayscale image).

        Returns
        -------
        np.ndarray
            An MxNx3 RGB array representing the combined images.
        """
        ...
    def blend_overlay(self, rgb: np.ndarray, intensity: np.ndarray) -> np.ndarray:
        """
        Combine an rgb image with an intensity map using "overlay" blending.

        Parameters
        ----------
        rgb : np.ndarray
            An MxNx3 RGB array of floats ranging from 0 to 1 (color image).
        intensity : np.ndarray
            An MxNx1 array of floats ranging from 0 to 1 (grayscale image).

        Returns
        -------
        np.ndarray
            An MxNx3 RGB array representing the combined images.
        """
        ...

def from_levels_and_colors(
    levels, colors, extend: Literal["neither", "min", "max", "both"] = ...
):
    """
    A helper routine to generate a cmap and a norm instance which
    behave similar to contourf's levels and colors arguments.

    Parameters
    ----------
    levels : sequence of numbers
        The quantization levels used to construct the `BoundaryNorm`.
        Value ``v`` is quantized to level ``i`` if ``lev[i] <= v < lev[i+1]``.
    colors : sequence of colors
        The fill color to use for each level. If *extend* is "neither" there
        must be ``n_level - 1`` colors. For an *extend* of "min" or "max" add
        one extra color, and for an *extend* of "both" add two colors.
    extend : {'neither', 'min', 'max', 'both'}, optional
        The behaviour when a value falls out of range of the given levels.
        See `~.Axes.contourf` for details.

    Returns
    -------
    cmap : `~Normalize`
    norm : `~Colormap`
    """
    ...
