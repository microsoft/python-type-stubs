from typing import Sequence
from cycler import Cycler
import ast

interactive_bk = ...
non_interactive_bk = ...
all_backends = ...

class ValidateInStrings:
    def __init__(
        self,
        key: str,
        valid: Sequence[str] | _ignorecase,
        ignorecase: bool = ...,
        *,
        _deprecated_since=...
    ) -> None:
        """*valid* is a list of legal strings."""
        ...
    def __call__(self, s: str) -> str: ...

def validate_any(s): ...

validate_anylist = ...

def validate_bool(b) -> bool:
    """Convert b to ``bool`` or raise."""
    ...

def validate_axisbelow(s) -> bool | str: ...
def validate_dpi(s) -> float | str:
    """Confirm s is string 'figure' or convert s to float or raise."""
    ...

validate_string = ...
validate_string_or_None = ...
validate_stringlist = ...
validate_int = ...
validate_int_or_None = ...
validate_float = ...
validate_float_or_None = ...
validate_floatlist = ...

def validate_fonttype(s) -> int:
    """
    Confirm that this is a Postscript or PDF font type that we know how to
    convert to.
    """
    ...

def validate_backend(s) -> str: ...
def validate_color_or_inherit(s) -> str:
    """Return a valid color arg."""
    ...

def validate_color_or_auto(s) -> str: ...
def validate_color_for_prop_cycle(s) -> str: ...
def validate_color(s) -> str:
    """Return a valid color arg."""
    ...

validate_colorlist = ...

def validate_aspect(s) -> str: ...
def validate_fontsize_None(s) -> None: ...
def validate_fontsize(s) -> float | str: ...

validate_fontsizelist = ...

def validate_fontweight(s) -> str: ...
def validate_fontstretch(s) -> str: ...
def validate_font_properties(s) -> str: ...
def validate_whiskers(s) -> float: ...
def validate_ps_distiller(s) -> None: ...

validate_fillstyle = ...
validate_fillstylelist = ...

def validate_markevery(s):
    """
    Validate the markevery property of a Line2D object.

    Parameters
    ----------
    s : None, int, (int, int), slice, float, (float, float), or list[int]

    Returns
    -------
    None, int, (int, int), slice, float, (float, float), or list[int]
    """
    ...

validate_markeverylist = ...

def validate_bbox(s) -> None: ...
def validate_sketch(s) -> None | tuple[float, ...]: ...
def validate_hatch(s):
    r"""
    Validate a hatch pattern.
    A hatch pattern string can have any sequence of the following
    characters: ``\ / | - + * . x o O``.
    """
    ...

validate_hatchlist = ...
validate_dashlist = ...

def cycler(*args, **kwargs) -> Cycler:
    """
    Create a `~cycler.Cycler` object much like :func:`cycler.cycler`,
    but includes input validation.

    Call signatures::

      cycler(cycler)
      cycler(label=values[, label2=values2[, ...]])
      cycler(label, values)

    Form 1 copies a given `~cycler.Cycler` object.

    Form 2 creates a `~cycler.Cycler` which cycles over one or more
    properties simultaneously. If multiple properties are given, their
    value lists must have the same length.

    Form 3 creates a `~cycler.Cycler` for a single property. This form
    exists for compatibility with the original cycler. Its use is
    discouraged in favor of the kwarg form, i.e. ``cycler(label=values)``.

    Parameters
    ----------
    cycler : Cycler
        Copy constructor for Cycler.

    label : str
        The property key. Must be a valid `.Artist` property.
        For example, 'color' or 'linestyle'. Aliases are allowed,
        such as 'c' for 'color' and 'lw' for 'linewidth'.

    values : iterable
        Finite-length iterable of the property values. These values
        are validated and will raise a ValueError if invalid.

    Returns
    -------
    Cycler
        A new :class:`~cycler.Cycler` for the given properties.

    Examples
    --------
    Creating a cycler for a single property:

    >>> c = cycler(color=['red', 'green', 'blue'])

    Creating a cycler for simultaneously cycling over multiple properties
    (e.g. red circle, green plus, blue cross):

    >>> c = cycler(color=['red', 'green', 'blue'],
    ...            marker=['o', '+', 'x'])

    """
    ...

class _DunderChecker(ast.NodeVisitor):
    def visit_Attribute(self, node): ...

def validate_cycler(s) -> Cycler:
    """Return a Cycler object from a string repr or the object itself."""
    ...

def validate_hist_bins(s) -> int: ...

class _ignorecase(list):
    """A marker class indicating that a list-of-str is case-insensitive."""

    ...
