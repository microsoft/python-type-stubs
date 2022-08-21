from .scale import SymmetricalLogTransform
from typing import Any, Callable, Literal, Sequence
from ._typing import *
from .axis import Axis
from functools import partial

__all__ = (
    "TickHelper",
    "Formatter",
    "FixedFormatter",
    "NullFormatter",
    "FuncFormatter",
    "FormatStrFormatter",
    "StrMethodFormatter",
    "ScalarFormatter",
    "LogFormatter",
    "LogFormatterExponent",
    "LogFormatterMathtext",
    "LogFormatterSciNotation",
    "LogitFormatter",
    "EngFormatter",
    "PercentFormatter",
    "Locator",
    "IndexLocator",
    "FixedLocator",
    "NullLocator",
    "LinearLocator",
    "LogLocator",
    "AutoLocator",
    "MultipleLocator",
    "MaxNLocator",
    "AutoMinorLocator",
    "SymmetricalLogLocator",
    "AsinhLocator",
    "LogitLocator",
)

class _DummyAxis:

    dataLim = ...
    viewLim = ...
    def __init__(self, minpos: int = ...) -> None: ...
    def get_view_interval(self): ...
    def set_view_interval(self, vmin: float, vmax: float): ...
    def get_minpos(self): ...
    def get_data_interval(self): ...
    def set_data_interval(self, vmin: float, vmax: float): ...
    def get_tick_space(self): ...

class TickHelper:
    axis = ...
    def set_axis(self, axis: Axis) -> None: ...
    def create_dummy_axis(self, **kwargs) -> None: ...
    def set_view_interval(self, vmin: float, vmax: float): ...
    def set_data_interval(self, vmin: float, vmax: float): ...
    def set_bounds(self, vmin: float, vmax: float): ...

class Formatter(TickHelper):
    """
    Create a string based on a tick value and location.
    """

    locs = ...
    def __call__(self, x, pos=...):
        """
        Return the format for tick value *x* at position pos.
        ``pos=None`` indicates an unspecified location.
        """
        ...
    def format_ticks(self, values: Sequence[float]) -> list[str]:
        """Return the tick labels for all the ticks at once."""
        ...
    def format_data(self, value) -> str:
        """
        Return the full string representation of the value with the
        position unspecified.
        """
        ...
    def format_data_short(self, value) -> str:
        """
        Return a short string version of the tick value.

        Defaults to the position-independent long value.
        """
        ...
    def get_offset(self) -> str: ...
    def set_locs(self, locs: ArrayLike) -> None:
        """
        Set the locations of the ticks.

        This method is called before computing the tick labels because some
        formatters need to know all tick locations to do so.
        """
        ...
    @staticmethod
    def fix_minus(s: str) -> str:
        """
        Some classes may want to replace a hyphen for minus with the proper
        Unicode symbol (U+2212) for typographical correctness.  This is a
        helper method to perform such a replacement when it is enabled via
        :rc:`axes.unicode_minus`.
        """
        ...

class NullFormatter(Formatter):
    """Always return the empty string."""

    def __call__(self, x: float, pos: int = ...): ...

class FixedFormatter(Formatter):
    """
    Return fixed strings for tick labels based only on position, not value.

    .. note::
        `.FixedFormatter` should only be used together with `.FixedLocator`.
        Otherwise, the labels may end up in unexpected positions.
    """

    def __init__(self, seq: Sequence[str]) -> None:
        """Set the sequence *seq* of strings that will be used for labels."""
        ...
    def __call__(self, x: float, pos: int = ...):
        """
        Return the label that matches the position, regardless of the value.

        For positions ``pos < len(seq)``, return ``seq[i]`` regardless of
        *x*. Otherwise return empty string. ``seq`` is the sequence of
        strings that this object was initialized with.
        """
        ...
    def get_offset(self) -> str: ...
    def set_offset_string(self, ofs: str): ...

class FuncFormatter(Formatter):
    """
    Use a user-defined function for formatting.

    The function should take in two inputs (a tick value ``x`` and a
    position ``pos``), and return a string containing the corresponding
    tick label.
    """

    def __init__(self, func: Callable | partial) -> None: ...
    def __call__(self, x: float, pos: int = ...):
        """
        Return the value of the user defined function.

        *x* and *pos* are passed through as-is.
        """
        ...
    def get_offset(self) -> str: ...
    def set_offset_string(self, ofs: str): ...

class FormatStrFormatter(Formatter):
    """
    Use an old-style ('%' operator) format string to format the tick.

    The format string should have a single variable format (%) in it.
    It will be applied to the value (not the position) of the tick.

    Negative numeric values will use a dash, not a Unicode minus; use mathtext
    to get a Unicode minus by wrapping the format specifier with $ (e.g.
    "$%g$").
    """

    def __init__(self, fmt: str) -> None: ...
    def __call__(self, x: float, pos: int = ...):
        """
        Return the formatted label string.

        Only the value *x* is formatted. The position is ignored.
        """
        ...

class StrMethodFormatter(Formatter):
    """
    Use a new-style format string (as used by `str.format`) to format the tick.

    The field used for the tick value must be labeled *x* and the field used
    for the tick position must be labeled *pos*.
    """

    def __init__(self, fmt: str) -> None: ...
    def __call__(self, x: float, pos: int = ...):
        """
        Return the formatted label string.

        *x* and *pos* are passed to `str.format` as keyword arguments
        with those exact names.
        """
        ...

class ScalarFormatter(Formatter):
    """
    Format tick values as a number.

    Parameters
    ----------
    useOffset : bool or float, default: :rc:`axes.formatter.useoffset`
        Whether to use offset notation. See `.set_useOffset`.
    useMathText : bool, default: :rc:`axes.formatter.use_mathtext`
        Whether to use fancy math formatting. See `.set_useMathText`.
    useLocale : bool, default: :rc:`axes.formatter.use_locale`.
        Whether to use locale settings for decimal sign and positive sign.
        See `.set_useLocale`.

    Notes
    -----
    In addition to the parameters above, the formatting of scientific vs.
    floating point representation can be configured via `.set_scientific`
    and `.set_powerlimits`).

    **Offset notation and scientific notation**

    Offset notation and scientific notation look quite similar at first sight.
    Both split some information from the formatted tick values and display it
    at the end of the axis.

    - The scientific notation splits up the order of magnitude, i.e. a
      multiplicative scaling factor, e.g. ``1e6``.

    - The offset notation separates an additive constant, e.g. ``+1e6``. The
      offset notation label is always prefixed with a ``+`` or ``-`` sign
      and is thus distinguishable from the order of magnitude label.

    The following plot with x limits ``1_000_000`` to ``1_000_010`` illustrates
    the different formatting. Note the labels at the right edge of the x axis.

    .. plot::

        lim = (1_000_000, 1_000_010)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, gridspec_kw={'hspace': 2})
        ax1.set(title='offset_notation', xlim=lim)
        ax2.set(title='scientific notation', xlim=lim)
        ax2.xaxis.get_major_formatter().set_useOffset(False)
        ax3.set(title='floating point notation', xlim=lim)
        ax3.xaxis.get_major_formatter().set_useOffset(False)
        ax3.xaxis.get_major_formatter().set_scientific(False)

    """

    def __init__(
        self,
        useOffset: bool | float = ...,
        useMathText: bool | None = ...,
        useLocale: bool | None = ...,
    ) -> None: ...
    def get_useOffset(self):
        """
        Return whether automatic mode for offset notation is active.

        This returns True if ``set_useOffset(True)``; it returns False if an
        explicit offset was set, e.g. ``set_useOffset(1000)``.

        See Also
        --------
        ScalarFormatter.set_useOffset
        """
        ...
    def set_useOffset(self, val: bool | float) -> None:
        """
        Set whether to use offset notation.

        When formatting a set numbers whose value is large compared to their
        range, the formatter can separate an additive constant. This can
        shorten the formatted numbers so that they are less likely to overlap
        when drawn on an axis.

        Parameters
        ----------
        val : bool or float
            - If False, do not use offset notation.
            - If True (=automatic mode), use offset notation if it can make
              the residual numbers significantly shorter. The exact behavior
              is controlled by :rc:`axes.formatter.offset_threshold`.
            - If a number, force an offset of the given value.

        Examples
        --------
        With active offset notation, the values

        ``100_000, 100_002, 100_004, 100_006, 100_008``

        will be formatted as ``0, 2, 4, 6, 8`` plus an offset ``+1e5``, which
        is written to the edge of the axis.
        """
        ...
    useOffset = ...
    def get_useLocale(self) -> bool | None:
        """
        Return whether locale settings are used for formatting.

        See Also
        --------
        ScalarFormatter.set_useLocale
        """
        ...
    def set_useLocale(self, val: bool | None):
        """
        Set whether to use locale settings for decimal sign and positive sign.

        Parameters
        ----------
        val : bool or None
            *None* resets to :rc:`axes.formatter.use_locale`.
        """
        ...
    useLocale = ...
    def get_useMathText(self) -> bool | None:
        """
        Return whether to use fancy math formatting.

        See Also
        --------
        ScalarFormatter.set_useMathText
        """
        ...
    def set_useMathText(self, val: bool | None) -> None:
        r"""
        Set whether to use fancy math formatting.

        If active, scientific notation is formatted as :math:`1.2 \times 10^3`.

        Parameters
        ----------
        val : bool or None
            *None* resets to :rc:`axes.formatter.use_mathtext`.
        """
        ...
    useMathText = ...
    def __call__(self, x: float, pos: int = ...) -> str:
        """
        Return the format for tick value *x* at position *pos*.
        """
        ...
    def set_scientific(self, bool) -> None:
        """
        Turn scientific notation on or off.

        See Also
        --------
        ScalarFormatter.set_powerlimits
        """
        ...
    def set_powerlimits(self, lims: Sequence[int]):
        r"""
        Set size thresholds for scientific notation.

        Parameters
        ----------
        lims : (int, int)
            A tuple *(min_exp, max_exp)* containing the powers of 10 that
            determine the switchover threshold. For a number representable as
            :math:`a \times 10^\mathrm{exp}` with :math:`1 <= |a| < 10`,
            scientific notation will be used if ``exp <= min_exp`` or
            ``exp >= max_exp``.

            The default limits are controlled by :rc:`axes.formatter.limits`.

            In particular numbers with *exp* equal to the thresholds are
            written in scientific notation.

            Typically, *min_exp* will be negative and *max_exp* will be
            positive.

            For example, ``formatter.set_powerlimits((-3, 4))`` will provide
            the following formatting:
            :math:`1 \times 10^{-3}, 9.9 \times 10^{-3}, 0.01,`
            :math:`9999, 1 \times 10^4`.

        See Also
        --------
        ScalarFormatter.set_scientific
        """
        ...
    def format_data_short(self, value) -> str: ...
    def format_data(self, value) -> str: ...
    def get_offset(self) -> str:
        """
        Return scientific notation, plus offset.
        """
        ...
    def set_locs(self, locs: Sequence[float]) -> None: ...

class LogFormatter(Formatter):
    """
    Base class for formatting ticks on a log or symlog scale.

    It may be instantiated directly, or subclassed.

    Parameters
    ----------
    base : float, default: 10.
        Base of the logarithm used in all calculations.

    labelOnlyBase : bool, default: False
        If True, label ticks only at integer powers of base.
        This is normally True for major ticks and False for
        minor ticks.

    minor_thresholds : (subset, all), default: (1, 0.4)
        If labelOnlyBase is False, these two numbers control
        the labeling of ticks that are not at integer powers of
        base; normally these are the minor ticks. The controlling
        parameter is the log of the axis data range.  In the typical
        case where base is 10 it is the number of decades spanned
        by the axis, so we can call it 'numdec'. If ``numdec <= all``,
        all minor ticks will be labeled.  If ``all < numdec <= subset``,
        then only a subset of minor ticks will be labeled, so as to
        avoid crowding. If ``numdec > subset`` then no minor ticks will
        be labeled.

    linthresh : None or float, default: None
        If a symmetric log scale is in use, its ``linthresh``
        parameter must be supplied here.

    Notes
    -----
    The `set_locs` method must be called to enable the subsetting
    logic controlled by the ``minor_thresholds`` parameter.

    In some cases such as the colorbar, there is no distinction between
    major and minor ticks; the tick locations might be set manually,
    or by a locator that puts ticks at integer powers of base and
    at intermediate locations.  For this situation, disable the
    minor_thresholds logic by using ``minor_thresholds=(np.inf, np.inf)``,
    so that all ticks will be labeled.

    To disable labeling of minor ticks when 'labelOnlyBase' is False,
    use ``minor_thresholds=(0, 0)``.  This is the default for the
    "classic" style.

    Examples
    --------
    To label a subset of minor ticks when the view limits span up
    to 2 decades, and all of the ticks when zoomed in to 0.5 decades
    or less, use ``minor_thresholds=(2, 0.5)``.

    To label all minor ticks when the view limits span up to 1.5
    decades, use ``minor_thresholds=(1.5, 1.5)``.
    """

    def __init__(
        self,
        base: Sequence[float] = ...,
        labelOnlyBase: bool = False,
        minor_thresholds: Sequence[float] = ...,
        linthresh: None | float = None,
    ) -> None: ...
    def base(self, base):
        """
        Change the *base* for labeling.

        .. warning::
           Should always match the base used for :class:`LogLocator`
        """
        ...
    def label_minor(self, labelOnlyBase: bool):
        """
        Switch minor tick labeling on or off.

        Parameters
        ----------
        labelOnlyBase : bool
            If True, label ticks only at integer powers of base.
        """
        ...
    def set_locs(self, locs=...):
        """
        Use axis view limits to control which ticks are labeled.

        The *locs* parameter is ignored in the present algorithm.
        """
        ...
    def __call__(self, x: float, pos: int = ...): ...
    def format_data(self, value) -> str: ...
    def format_data_short(self, value) -> str: ...

class LogFormatterExponent(LogFormatter):
    """
    Format values for log axis using ``exponent = log_base(value)``.
    """

    ...

class LogFormatterMathtext(LogFormatter):
    """
    Format values for log axis using ``exponent = log_base(value)``.
    """

    def __call__(self, x: float, pos: int = ...): ...

class LogFormatterSciNotation(LogFormatterMathtext):
    """
    Format values following scientific notation in a logarithmic axis.
    """

    ...

class LogitFormatter(Formatter):
    """
    Probability formatter (using Math text).
    """

    def __init__(
        self,
        *,
        use_overline: bool = False,
        one_half: str = "\\frac{1}{2}",
        minor: bool = False,
        minor_threshold: int = 25,
        minor_number: int = 6
    ) -> None:
        r"""
        Parameters
        ----------
        use_overline : bool, default: False
            If x > 1/2, with x = 1-v, indicate if x should be displayed as
            $\overline{v}$. The default is to display $1-v$.

        one_half : str, default: r"\frac{1}{2}"
            The string used to represent 1/2.

        minor : bool, default: False
            Indicate if the formatter is formatting minor ticks or not.
            Basically minor ticks are not labelled, except when only few ticks
            are provided, ticks with most space with neighbor ticks are
            labelled. See other parameters to change the default behavior.

        minor_threshold : int, default: 25
            Maximum number of locs for labelling some minor ticks. This
            parameter have no effect if minor is False.

        minor_number : int, default: 6
            Number of ticks which are labelled when the number of ticks is
            below the threshold.
        """
        ...
    def use_overline(self, use_overline: bool = False):
        r"""
        Switch display mode with overline for labelling p>1/2.

        Parameters
        ----------
        use_overline : bool, default: False
            If x > 1/2, with x = 1-v, indicate if x should be displayed as
            $\overline{v}$. The default is to display $1-v$.
        """
        ...
    def set_one_half(self, one_half: str = "\\frac{1}{2}"):
        r"""
        Set the way one half is displayed.

        one_half : str, default: r"\frac{1}{2}"
            The string used to represent 1/2.
        """
        ...
    def set_minor_threshold(self, minor_threshold: int):
        """
        Set the threshold for labelling minors ticks.

        Parameters
        ----------
        minor_threshold : int
            Maximum number of locations for labelling some minor ticks. This
            parameter have no effect if minor is False.
        """
        ...
    def set_minor_number(self, minor_number: int):
        """
        Set the number of minor ticks to label when some minor ticks are
        labelled.

        Parameters
        ----------
        minor_number : int
            Number of ticks which are labelled when the number of ticks is
            below the threshold.
        """
        ...
    def set_locs(self, locs): ...
    def __call__(self, x: float, pos: int = ...): ...
    def format_data_short(self, value) -> str: ...

class EngFormatter(Formatter):
    """
    Format axis values using engineering prefixes to represent powers
    of 1000, plus a specified unit, e.g., 10 MHz instead of 1e7.
    """

    ENG_PREFIXES = ...
    def __init__(
        self,
        unit: str = "",
        places: int | None = None,
        sep: str = " ",
        *,
        usetex: bool = ...,
        useMathText: bool = ...
    ) -> None:
        r"""
        Parameters
        ----------
        unit : str, default: ""
            Unit symbol to use, suitable for use with single-letter
            representations of powers of 1000. For example, 'Hz' or 'm'.

        places : int, default: None
            Precision with which to display the number, specified in
            digits after the decimal point (there will be between one
            and three digits before the decimal point). If it is None,
            the formatting falls back to the floating point format '%g',
            which displays up to 6 *significant* digits, i.e. the equivalent
            value for *places* varies between 0 and 5 (inclusive).

        sep : str, default: " "
            Separator used between the value and the prefix/unit. For
            example, one get '3.14 mV' if ``sep`` is " " (default) and
            '3.14mV' if ``sep`` is "". Besides the default behavior, some
            other useful options may be:

            * ``sep=""`` to append directly the prefix/unit to the value;
            * ``sep="\N{THIN SPACE}"`` (``U+2009``);
            * ``sep="\N{NARROW NO-BREAK SPACE}"`` (``U+202F``);
            * ``sep="\N{NO-BREAK SPACE}"`` (``U+00A0``).

        usetex : bool, default: :rc:`text.usetex`
            To enable/disable the use of TeX's math mode for rendering the
            numbers in the formatter.

        useMathText : bool, default: :rc:`axes.formatter.use_mathtext`
            To enable/disable the use mathtext for rendering the numbers in
            the formatter.
        """
        ...
    def get_usetex(self) -> bool: ...
    def set_usetex(self, val: bool) -> None: ...

    usetex = ...
    def get_useMathText(self) -> bool: ...
    def set_useMathText(self, val: bool) -> None: ...

    useMathText = ...
    def __call__(self, x: float, pos: int = ...): ...
    def format_eng(self, num) -> str:
        """
        Format a number in engineering notation, appending a letter
        representing the power of 1000 of the original number.
        Some examples:

        >>> format_eng(0)        # for self.places = 0
        '0'

        >>> format_eng(1000000)  # for self.places = 1
        '1.0 M'

        >>> format_eng("-1e-6")  # for self.places = 2
        '-1.00 \N{MICRO SIGN}'
        """
        ...

class PercentFormatter(Formatter):
    """
    Format numbers as a percentage.

    Parameters
    ----------
    xmax : float
        Determines how the number is converted into a percentage.
        *xmax* is the data value that corresponds to 100%.
        Percentages are computed as ``x / xmax * 100``. So if the data is
        already scaled to be percentages, *xmax* will be 100. Another common
        situation is where *xmax* is 1.0.

    decimals : None or int
        The number of decimal places to place after the point.
        If *None* (the default), the number will be computed automatically.

    symbol : str or None
        A string that will be appended to the label. It may be
        *None* or empty to indicate that no symbol should be used. LaTeX
        special characters are escaped in *symbol* whenever latex mode is
        enabled, unless *is_latex* is *True*.

    is_latex : bool
        If *False*, reserved LaTeX characters in *symbol* will be escaped.
    """

    def __init__(
        self,
        xmax: float = ...,
        decimals: None | int = ...,
        symbol: str | None = ...,
        is_latex: bool = ...,
    ) -> None: ...
    def __call__(self, x: float, pos: int = ...):
        """Format the tick as a percentage with the appropriate scaling."""
        ...
    def format_pct(self, x, display_range) -> str:
        """
        Format the number as a percentage number with the correct
        number of decimals and adds the percent symbol, if any.

        If ``self.decimals`` is `None`, the number of digits after the
        decimal point is set based on the *display_range* of the axis
        as follows:

        +---------------+----------+------------------------+
        | display_range | decimals |          sample        |
        +---------------+----------+------------------------+
        | >50           |     0    | ``x = 34.5`` => 35%    |
        +---------------+----------+------------------------+
        | >5            |     1    | ``x = 34.5`` => 34.5%  |
        +---------------+----------+------------------------+
        | >0.5          |     2    | ``x = 34.5`` => 34.50% |
        +---------------+----------+------------------------+
        |      ...      |    ...   |          ...           |
        +---------------+----------+------------------------+

        This method will not be very good for tiny axis ranges or
        extremely large ones. It assumes that the values on the chart
        are percentages displayed on a reasonable scale.
        """
        ...
    def convert_to_pct(self, x): ...
    @property
    def symbol(self) -> str:
        r"""
        The configured percent symbol as a string.

        If LaTeX is enabled via :rc:`text.usetex`, the special characters
        ``{'#', '$', '%', '&', '~', '_', '^', '\', '{', '}'}`` are
        automatically escaped in the string.
        """
        ...
    @symbol.setter
    def symbol(self, symbol: str): ...

class Locator(TickHelper):
    """
    Determine the tick locations;

    Note that the same locator should not be used across multiple
    `~Axis` because the locator stores references to the Axis
    data and view limits.
    """

    MAXTICKS = ...
    def tick_values(self, vmin: float, vmax: float):
        """
        Return the values of the located ticks given **vmin** and **vmax**.

        .. note::
            To get tick locations with the vmin and vmax values defined
            automatically for the associated ``axis`` simply call
            the Locator instance::

                >>> print(type(loc))
                <type 'Locator'>
                >>> print(loc())
                [1, 2, 3, 4]

        """
        ...
    def set_params(self, **kwargs):
        """
        Do nothing, and raise a warning. Any locator class not supporting the
        set_params() function will call this.
        """
        ...
    def __call__(self):
        """Return the locations of the ticks."""
        ...
    def raise_if_exceeds(self, locs):
        """
        Log at WARNING level if *locs* is longer than `Locator.MAXTICKS`.

        This is intended to be called immediately before returning *locs* from
        ``__call__`` to inform users in case their Locator returns a huge
        number of ticks, causing Matplotlib to run out of memory.

        The "strange" name of this method dates back to when it would raise an
        exception instead of emitting a log.
        """
        ...
    def nonsingular(self, v0: float, v1: float) -> tuple[float, float]:
        """
        Adjust a range as needed to avoid singularities.

        This method gets called during autoscaling, with ``(v0, v1)`` set to
        the data limits on the axes if the axes contains any data, or
        ``(-inf, +inf)`` if not.

        - If ``v0 == v1`` (possibly up to some floating point slop), this
          method returns an expanded interval around this value.
        - If ``(v0, v1) == (-inf, +inf)``, this method returns appropriate
          default view limits.
        - Otherwise, ``(v0, v1)`` is returned without modification.
        """
        ...
    def view_limits(self, vmin: float, vmax: float):
        """
        Select a scale for the range from vmin to vmax.

        Subclasses should override this method to change locator behaviour.
        """
        ...

class IndexLocator(Locator):
    """
    Place a tick on every multiple of some base number of points
    plotted, e.g., on every 5th point.  It is assumed that you are doing
    index plotting; i.e., the axis is 0, len(data).  This is mainly
    useful for x ticks.
    """

    def __init__(self, base: float, offset: float) -> None:
        """Place ticks every *base* data point, starting at *offset*."""
        ...
    def set_params(self, base: float = ..., offset: float = ...):
        """Set parameters within this locator"""
        ...
    def __call__(self):
        """Return the locations of the ticks"""
        ...
    def tick_values(self, vmin: float, vmax: float): ...

class FixedLocator(Locator):
    """
    Tick locations are fixed.  If nbins is not None,
    the array of possible positions will be subsampled to
    keep the number of ticks <= nbins +1.
    The subsampling will be done so as to include the smallest
    absolute value; for example, if zero is included in the
    array of possibilities, then it is guaranteed to be one of
    the chosen ticks.
    """

    def __init__(self, locs, nbins: int | None = ...) -> None: ...
    def set_params(self, nbins: int | None = ...):
        """Set parameters within this locator."""
        ...
    def __call__(self): ...
    def tick_values(self, vmin: float, vmax: float):
        """
        Return the locations of the ticks.

        .. note::

            Because the values are fixed, vmin and vmax are not used in this
            method.

        """
        ...

class NullLocator(Locator):
    """
    No ticks
    """

    def __call__(self) -> list: ...
    def tick_values(self, vmin: float, vmax: float) -> list:
        """
        Return the locations of the ticks.

        .. note::

            Because the values are Null, vmin and vmax are not used in this
            method.
        """
        ...

class LinearLocator(Locator):
    """
    Determine the tick locations

    The first time this function is called it will try to set the
    number of ticks to make a nice tick partitioning.  Thereafter the
    number of ticks will be fixed so that interactive navigation will
    be nice

    """

    def __init__(self, numticks: int = ..., presets: dict = ...) -> None:
        """
        Use presets to set locs based on lom.  A dict mapping vmin, vmax->locs
        """
        ...
    @property
    def numticks(self): ...
    @numticks.setter
    def numticks(self, numticks: int): ...
    def set_params(self, numticks: int = ..., presets: dict = ...):
        """Set parameters within this locator."""
        ...
    def __call__(self):
        """Return the locations of the ticks."""
        ...
    def tick_values(self, vmin: float, vmax: float): ...
    def view_limits(self, vmin: float, vmax: float):
        """Try to choose the view limits intelligently."""
        ...

class MultipleLocator(Locator):
    """
    Set a tick on each integer multiple of a base within the view interval.
    """

    def __init__(self, base: float = ...) -> None: ...
    def set_params(self, base: float):
        """Set parameters within this locator."""
        ...
    def __call__(self):
        """Return the locations of the ticks."""
        ...
    def tick_values(self, vmin: float, vmax: float): ...
    def view_limits(self, dmin: float, dmax: float):
        """
        Set the view limits to the nearest multiples of base that
        contain the data.
        """
        ...

def scale_range(
    vmin: float, vmax: float, n: int = ..., threshold: int = ...
) -> tuple[float, int]: ...

class _Edge_integer:
    """
    Helper for MaxNLocator, MultipleLocator, etc.

    Take floating point precision limitations into account when calculating
    tick locations as integer multiples of a step.
    """

    def __init__(self, step: float, offset: float) -> None:
        """
        *step* is a positive floating-point interval between ticks.
        *offset* is the offset subtracted from the data limits
        prior to calculating tick locations.
        """
        ...
    def closeto(self, ms, edge): ...
    def le(self, x: float) -> float:
        """Return the largest n: n*step <= x."""
        ...
    def ge(self, x: float) -> float:
        """Return the smallest n: n*step >= x."""
        ...

class MaxNLocator(Locator):
    """
    Find nice tick locations with no more than N being within the view limits.
    Locations beyond the limits are added to support autoscaling.
    """

    default_params = ...
    def __init__(self, nbins: int | Literal["auto"] = 10, **kwargs) -> None:
        """
        Parameters
        ----------
        nbins : int or 'auto', default: 10
            Maximum number of intervals; one less than max number of
            ticks.  If the string 'auto', the number of bins will be
            automatically determined based on the length of the axis.

        steps : array-like, optional
            Sequence of nice numbers starting with 1 and ending with 10;
            e.g., [1, 2, 4, 5, 10], where the values are acceptable
            tick multiples.  i.e. for the example, 20, 40, 60 would be
            an acceptable set of ticks, as would 0.4, 0.6, 0.8, because
            they are multiples of 2.  However, 30, 60, 90 would not
            be allowed because 3 does not appear in the list of steps.

        integer : bool, default: False
            If True, ticks will take only integer values, provided at least
            *min_n_ticks* integers are found within the view limits.

        symmetric : bool, default: False
            If True, autoscaling will result in a range symmetric about zero.

        prune : {'lower', 'upper', 'both', None}, default: None
            Remove edge ticks -- useful for stacked or ganged plots where
            the upper tick of one axes overlaps with the lower tick of the
            axes above it, primarily when :rc:`axes.autolimit_mode` is
            ``'round_numbers'``.  If ``prune=='lower'``, the smallest tick will
            be removed.  If ``prune == 'upper'``, the largest tick will be
            removed.  If ``prune == 'both'``, the largest and smallest ticks
            will be removed.  If *prune* is *None*, no ticks will be removed.

        min_n_ticks : int, default: 2
            Relax *nbins* and *integer* constraints if necessary to obtain
            this minimum number of ticks.
        """
        ...
    def set_params(self, **kwargs) -> None:
        """
        Set parameters for this locator.

        Parameters
        ----------
        nbins : int or 'auto', optional
            see `.MaxNLocator`
        steps : array-like, optional
            see `.MaxNLocator`
        integer : bool, optional
            see `.MaxNLocator`
        symmetric : bool, optional
            see `.MaxNLocator`
        prune : {'lower', 'upper', 'both', None}, optional
            see `.MaxNLocator`
        min_n_ticks : int, optional
            see `.MaxNLocator`
        """
        ...
    def __call__(self): ...
    def tick_values(self, vmin: float, vmax: float): ...
    def view_limits(self, dmin: float, dmax: float) -> tuple[float, float]: ...

def is_decade(x, base=..., *, rtol=...): ...
def is_close_to_int(x, *, atol=...): ...

class LogLocator(Locator):
    """
    Determine the tick locations for log axes
    """

    def __init__(
        self,
        base: float = ...,
        subs: None | str | Sequence[float] = ...,
        numdecs: int = ...,
        numticks: None | int = ...,
    ) -> None:
        """
        Place ticks on the locations : subs[j] * base**i

        Parameters
        ----------
        base : float, default: 10.0
            The base of the log used, so ticks are placed at ``base**n``.
        subs : None or str or sequence of float, default: (1.0,)
            Gives the multiples of integer powers of the base at which
            to place ticks.  The default places ticks only at
            integer powers of the base.
            The permitted string values are ``'auto'`` and ``'all'``,
            both of which use an algorithm based on the axis view
            limits to determine whether and how to put ticks between
            integer powers of the base.  With ``'auto'``, ticks are
            placed only between integer powers; with ``'all'``, the
            integer powers are included.  A value of None is
            equivalent to ``'auto'``.
        numticks : None or int, default: None
            The maximum number of ticks to allow on a given axis. The default
            of ``None`` will try to choose intelligently as long as this
            Locator has already been assigned to an axis using
            `~.axis.Axis.get_tick_space`, but otherwise falls back to 9.
        """
        ...
    def set_params(
        self,
        base: float = ...,
        subs: None | str | Sequence[float] = ...,
        numdecs: int = ...,
        numtick: None | int = ...,
    ):
        """Set parameters within this locator."""
        ...
    def base(self, base: float) -> None:
        """Set the log base (major tick every ``base**i``, i integer)."""
        ...
    def subs(self, subs: None | str | Sequence[float]) -> None:
        """
        Set the minor ticks for the log scaling every ``base**i*subs[j]``.
        """
        ...
    def __call__(self):
        """Return the locations of the ticks."""
        ...
    def tick_values(self, vmin: float, vmax: float): ...
    def view_limits(self, vmin: float, vmax: float):
        """Try to choose the view limits intelligently."""
        ...
    def nonsingular(self, vmin: float, vmax: float) -> tuple[float, float]: ...

class SymmetricalLogLocator(Locator):
    """
    Determine the tick locations for symmetric log axes.
    """

    def __init__(
        self,
        transform: SymmetricalLogTransform = ...,
        subs: Sequence[float] = ...,
        linthresh: float = ...,
        base: float = ...,
    ) -> None:
        """
        Parameters
        ----------
        transform : `~.scale.SymmetricalLogTransform`, optional
            If set, defines the *base* and *linthresh* of the symlog transform.
        base, linthresh : float, optional
            The *base* and *linthresh* of the symlog transform, as documented
            for `.SymmetricalLogScale`.  These parameters are only used if
            *transform* is not set.
        subs : sequence of float, default: [1]
            The multiples of integer powers of the base where ticks are placed,
            i.e., ticks are placed at
            ``[sub * base**i for i in ... for sub in subs]``.

        Notes
        -----
        Either *transform*, or both *base* and *linthresh*, must be given.
        """
        ...
    def set_params(self, subs: Sequence[float] = ..., numticks: int | None = ...):
        """Set parameters within this locator."""
        ...
    def __call__(self):
        """Return the locations of the ticks."""
        ...
    def tick_values(self, vmin: float, vmax: float): ...
    def view_limits(self, vmin: float, vmax: float):
        """Try to choose the view limits intelligently."""
        ...

class AsinhLocator(Locator):
    """
    An axis tick locator specialized for the inverse-sinh scale

    This is very unlikely to have any use beyond
    the `~.scale.AsinhScale` class.

    .. note::

       This API is provisional and may be revised in the future
       based on early user feedback.
    """

    def __init__(
        self,
        linear_width: float,
        numticks: int = 11,
        symthresh: float = 0.2,
        base: int = 10,
        subs: Sequence[int] = ...,
    ) -> None:
        """
        Parameters
        ----------
        linear_width : float
            The scale parameter defining the extent
            of the quasi-linear region.
        numticks : int, default: 11
            The approximate number of major ticks that will fit
            along the entire axis
        symthresh : float, default: 0.2
            The fractional threshold beneath which data which covers
            a range that is approximately symmetric about zero
            will have ticks that are exactly symmetric.
        base : int, default: 10
            The number base used for rounding tick locations
            on a logarithmic scale. If this is less than one,
            then rounding is to the nearest integer multiple
            of powers of ten.
        subs : tuple, default: None
            Multiples of the number base, typically used
            for the minor ticks, e.g. (2, 5) when base=10.
        """
        ...
    def set_params(
        self,
        numticks: int = ...,
        symthresh: float = ...,
        base: int = ...,
        subs: Sequence[int] = ...,
    ):
        """Set parameters within this locator."""
        ...
    def __call__(self): ...
    def tick_values(self, vmin: float, vmax: float): ...

class LogitLocator(MaxNLocator):
    """
    Determine the tick locations for logit axes
    """

    def __init__(
        self, minor: bool = ..., *, nbins: int | Literal["auto"] = ...
    ) -> None:
        """
        Place ticks on the logit locations

        Parameters
        ----------
        nbins : int or 'auto', optional
            Number of ticks. Only used if minor is False.
        minor : bool, default: False
            Indicate if this locator is for minor ticks or not.
        """
        ...
    def set_params(self, minor: None = ..., **kwargs) -> None:
        """Set parameters within this locator."""
        ...
    @property
    def minor(self): ...
    @minor.setter
    def minor(self, value): ...
    def tick_values(self, vmin: float, vmax: float): ...
    def nonsingular(self, vmin: float, vmax: float) -> tuple[float, float]: ...

class AutoLocator(MaxNLocator):
    """
    Dynamically find major tick positions. This is actually a subclass
    of `~matplotlib.ticker.MaxNLocator`, with parameters *nbins = 'auto'*
    and *steps = [1, 2, 2.5, 5, 10]*.
    """

    def __init__(self) -> None:
        """
        To know the values of the non-public parameters, please have a
        look to the defaults of `~matplotlib.ticker.MaxNLocator`.
        """
        ...

class AutoMinorLocator(Locator):
    """
    Dynamically find minor tick positions based on the positions of
    major ticks. The scale must be linear with major ticks evenly spaced.
    """

    def __init__(self, n: int | None = ...) -> None:
        """
        *n* is the number of subdivisions of the interval between
        major ticks; e.g., n=2 will place a single minor tick midway
        between major ticks.

        If *n* is omitted or None, it will be set to 5 or 4.
        """
        ...
    def __call__(self) -> list:
        """Return the locations of the ticks."""
        ...
    def tick_values(self, vmin: float, vmax: float): ...
