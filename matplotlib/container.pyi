# COMPLETE

from typing import Any, Callable, List, Optional, Tuple, TypeVar, Union

from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle

_T = TypeVar("_T")


# These would be better represented as variadic types, which are not yet accepted.
class Container(Tuple[_T]):
    eventson: bool

    def __init__(self, kl: Any, label: Optional[str] = ...) -> None: ... 

    def get_children(self) -> List[_T]: ...

    # Copied from Artist.
    def add_callback(self, func: Callable[[_T], Any]) -> int: ...
    def remove_callback(self, oid: int) -> None: ...
    def get_label(self) -> str: ...
    def set_label(self, s: object) -> None: ...
    def pchanged(self) -> None: ...

class BarContainer(Container[Rectangle]):
    patches: List[Rectangle]
    errorbar: Optional[ErrorbarContainer]

    def __init__(self, patches: List[Rectangle], errorbar: Optional[ErrorbarContainer] = ..., **kwargs: Any) -> None: ...

class ErrorbarContainer(Container[Union[LineCollection, Line2D]]):
    has_xerr: bool
    has_yerr: bool

    def __init__(self, lines: Tuple[Line2D, Tuple[Line2D, ...], List[LineCollection]], has_xerr: bool = ..., has_yerr: bool = ..., **kwargs: Any) -> None: ...

class StemContainer(Container[Union[LineCollection, Line2D]]):
    markerline: LineCollection
    stemlines: LineCollection
    baseline: Line2D

    def __init__(self, markerline_stemlines_baseline: Tuple[LineCollection, LineCollection, Line2D], **kwargs: Any) -> None: ...
