from ._typing import *
from .font_manager import FontProperties

from types import SimpleNamespace

get_unicode_index = ...

class MathtextBackend:
    """
    The base class for the mathtext backend-specific code.  `MathtextBackend`
    subclasses interface between mathtext and specific Matplotlib graphics
    backends.

    Subclasses need to override the following:

    - :meth:`render_glyph`
    - :meth:`render_rect_filled`
    - :meth:`get_results`

    And optionally, if you need to use a FreeType hinting style:

    - :meth:`get_hinting_type`
    """

    def __init__(self) -> None: ...
    def set_canvas_size(self, w: float, h: float, d: float) -> None:
        """Set the dimension of the drawing canvas."""
        ...
    def render_glyph(self, ox: float, oy: float, info: SimpleNamespace):
        """
        Draw a glyph described by *info* to the reference point (*ox*,
        *oy*).
        """
        ...
    def render_rect_filled(self, x1: float, y1: float, x2: float, y2: float):
        """
        Draw a filled black rectangle from (*x1*, *y1*) to (*x2*, *y2*).
        """
        ...
    def get_results(self, box) -> tuple:
        """
        Return a backend-specific tuple to return to the backend after
        all processing is done.
        """
        ...
    def get_hinting_type(self) -> int:
        """
        Get the FreeType hinting type to use with this particular
        backend.
        """
        ...

class MathtextBackendAgg(MathtextBackend):
    """
    Render glyphs and rectangles to an FTImage buffer, which is later
    transferred to the Agg image by the Agg backend.
    """

    def __init__(self) -> None: ...
    def set_canvas_size(self, w: float, h: float, d: float) -> None: ...
    def render_glyph(self, ox: float, oy: float, info: SimpleNamespace) -> None: ...
    def render_rect_filled(
        self, x1: float, y1: float, x2: float, y2: float
    ) -> None: ...
    def get_results(self, box): ...
    def get_hinting_type(self) -> int: ...

class MathtextBackendPath(MathtextBackend):
    """
    Store information to write a mathtext rendering to the text path
    machinery.
    """

    def __init__(self) -> None: ...
    def render_glyph(self, ox: float, oy: float, info: SimpleNamespace) -> None: ...
    def render_rect_filled(
        self, x1: float, y1: float, x2: float, y2: float
    ) -> None: ...
    def get_results(self, box): ...

class MathTextWarning(Warning): ...

class MathTextParser:
    def __init__(self, output: str) -> None:
        """Create a MathTextParser for the given backend *output*."""
        ...
    def parse(self, s: str, dpi: float = ..., prop: FontProperties = ...):
        """
        Parse the given math expression *s* at the given *dpi*.  If *prop* is
        provided, it is a `.FontProperties` object specifying the "default"
        font to use in the math expression, used for all non-math text.

        The results are cached, so multiple calls to `parse`
        with the same expression should be fast.
        """
        ...

def math_to_image(
    s: str,
    filename_or_obj: str | PathLike | FileLike,
    prop: FontProperties = ...,
    dpi: float = ...,
    format: str = ...,
    *,
    color: str = ...
):
    """
    Given a math expression, renders it in a closely-clipped bounding
    box to an image file.

    Parameters
    ----------
    s : str
        A math expression.  The math portion must be enclosed in dollar signs.
    filename_or_obj : str or path-like or file-like
        Where to write the image data.
    prop : `.FontProperties`, optional
        The size and style of the text.
    dpi : float, optional
        The output dpi.  If not set, the dpi is determined as for
        `.Figure.savefig`.
    format : str, optional
        The output format, e.g., 'svg', 'pdf', 'ps' or 'png'.  If not set, the
        format is determined as for `.Figure.savefig`.
    color : str, optional
        Foreground color, defaults to :rc:`text.color`.
    """
    ...
