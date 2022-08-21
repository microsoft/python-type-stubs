from typing import Literal
from ._typing import *
from .collections import LineCollection
from .lines import Line2D
from .patches import Rectangle
from typing import Type

class Container(tuple):
    """
    Base class for containers.

    Containers are classes that collect semantically related Artists such as
    the bars of a bar plot.
    """

    def __repr__(self) -> str: ...
    def __new__(cls: Type[Container], *args, **kwargs) -> Container: ...
    def __init__(self, kl: list[Rectangle], label: str = ...) -> None: ...
    def remove(self) -> None: ...
    def get_children(self) -> list[Rectangle]: ...

    get_label = ...
    set_label = ...
    add_callback = ...
    remove_callback = ...
    pchanged = ...

class BarContainer(Container):
    """
    Container for the artists of bar plots (e.g. created by `.Axes.bar`).

    The container can be treated as a tuple of the *patches* themselves.
    Additionally, you can access these and further parameters by the
    attributes.

    Attributes
    ----------
    patches : list of :class:`~matplotlib.patches.Rectangle`
        The artists of the bars.

    errorbar : None or :class:`~ErrorbarContainer`
        A container for the error bar artists if error bars are present.
        *None* otherwise.

    datavalues : None or array-like
        The underlying data values corresponding to the bars.

    orientation : {'vertical', 'horizontal'}, default: None
        If 'vertical', the bars are assumed to be vertical.
        If 'horizontal', the bars are assumed to be horizontal.

    """

    patches: list[Rectangle]
    errorbar: None | ErrorbarContainer
    datavalues: None | ArrayLike
    orientation: None | Literal["horizontal", "vertical"]

    def __init__(
        self,
        patches: list[Rectangle],
        errorbar: ErrorbarContainer | None = ...,
        *,
        datavalues=...,
        orientation=...,
        **kwargs
    ) -> None: ...

class ErrorbarContainer(Container):
    """
    Container for the artists of error bars (e.g. created by `.Axes.errorbar`).

    The container can be treated as the *lines* tuple itself.
    Additionally, you can access these and further parameters by the
    attributes.

    Attributes
    ----------
    lines : tuple
        Tuple of ``(data_line, caplines, barlinecols)``.

        - data_line : :class:`~Line2D` instance of
          x, y plot markers and/or line.
        - caplines : tuple of :class:`~Line2D` instances of
          the error bar caps.
        - barlinecols : list of :class:`~LineCollection`
          with the horizontal and vertical error ranges.

    has_xerr, has_yerr : bool
        ``True`` if the errorbar has x/y errors.

    """

    lines: tuple[Line2D, tuple[Line2D, ...], list[LineCollection]]
    has_xerr: bool
    has_yerr: bool

    def __init__(
        self,
        lines: tuple[Line2D, tuple[Line2D, ...], list[LineCollection]],
        has_xerr: bool = ...,
        has_yerr: bool = ...,
        **kwargs
    ) -> None: ...

class StemContainer(Container):
    """
    Container for the artists created in a :meth:`.Axes.stem` plot.

    The container can be treated like a namedtuple ``(markerline, stemlines,
    baseline)``.

    Attributes
    ----------
    markerline :  :class:`~Line2D`
        The artist of the markers at the stem heads.

    stemlines : list of :class:`~Line2D`
        The artists of the vertical lines for all stems.

    baseline : :class:`~Line2D`
        The artist of the horizontal baseline.
    """

    markerline: Line2D
    stemlines: list[Line2D]
    baseline: Line2D

    def __init__(
        self,
        markerline_stemlines_baseline: tuple[Line2D, list[Line2D], Line2D],
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        markerline_stemlines_baseline : tuple
            Tuple of ``(markerline, stemlines, baseline)``.
            ``markerline`` contains the `.LineCollection` of the markers,
            ``stemlines`` is a `.LineCollection` of the main lines,
            ``baseline`` is the `.Line2D` of the baseline.
        """
        ...
