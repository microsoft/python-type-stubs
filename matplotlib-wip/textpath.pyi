from matplotlib.texmanager import TexManager
from typing import Literal, Sequence
from .path import Path
from .font_manager import FontProperties

class TextToPath:
    """A class that converts strings to paths."""

    FONT_SCALE = ...
    DPI = ...
    def __init__(self) -> None: ...
    def get_text_width_height_descent(
        self, s: str, prop: FontProperties, ismath: bool | Literal["TeX"]
    ): ...
    def get_text_path(
        self, prop: FontProperties, s: str, ismath: bool | Literal["TeX"] = ...
    ):
        """
        Convert text *s* to path (a tuple of vertices and codes for
        Path).

        Parameters
        ----------
        prop : `~FontProperties`
            The font properties for the text.

        s : str
            The text to be converted.

        ismath : {False, True, "TeX"}
            If True, use mathtext parser.  If "TeX", use tex for rendering.

        Returns
        -------
        verts : list
            A list of numpy arrays containing the x and y coordinates of the
            vertices.

        codes : list
            A list of path codes.

        Examples
        --------
        Create a list of vertices and codes from a text, and create a `.Path`
        from those::

            from matplotlib.path import Path
            from matplotlib.textpath import TextToPath
            from matplotlib.font_manager import FontProperties

            fp = FontProperties(family="Humor Sans", style="italic")
            verts, codes = TextToPath().get_text_path(fp, "ABC")
            path = Path(verts, codes, closed=False)

        Also see `TextPath` for a more direct way to create a path from a text.
        """
        ...
    def get_glyphs_with_font(
        self, font: FontProperties, s: str, glyph_map=..., return_new_glyphs_only=...
    ):
        """
        Convert string *s* to vertices and codes using the provided ttf font.
        """
        ...
    def get_glyphs_mathtext(
        self, prop: FontProperties, s: str, glyph_map=..., return_new_glyphs_only=...
    ):
        """
        Parse mathtext string *s* and convert it to a (vertices, codes) pair.
        """
        ...
    def get_texmanager(self) -> TexManager:
        """Return the cached `~.texmanager.TexManager` instance."""
        ...
    def get_glyphs_tex(
        self, prop: FontProperties, s: str, glyph_map=..., return_new_glyphs_only=...
    ):
        """Convert the string *s* to vertices and codes using usetex mode."""
        ...

text_to_path = ...

class TextPath(Path):
    """
    Create a path from the text.
    """

    def __init__(
        self,
        xy: Sequence[float],
        s: str,
        size=...,
        prop: FontProperties = ...,
        _interpolation_steps: int = ...,
        usetex: bool = False,
    ) -> None:
        r"""
        Create a path from the text. Note that it simply is a path,
        not an artist. You need to use the `.PathPatch` (or other artists)
        to draw this path onto the canvas.

        Parameters
        ----------
        xy : tuple or array of two float values
            Position of the text. For no offset, use ``xy=(0, 0)``.

        s : str
            The text to convert to a path.

        size : float, optional
            Font size in points. Defaults to the size specified via the font
            properties *prop*.

        prop : `FontProperties`, optional
            Font property. If not provided, will use a default
            ``FontProperties`` with parameters from the
            :ref:`rcParams<customizing-with-dynamic-rc-settings>`.

        _interpolation_steps : int, optional
            (Currently ignored)

        usetex : bool, default: False
            Whether to use tex rendering.

        Examples
        --------
        The following creates a path from the string "ABC" with Helvetica
        font face; and another path from the latex fraction 1/2::

            from matplotlib.textpath import TextPath
            from matplotlib.font_manager import FontProperties

            fp = FontProperties(family="Helvetica", style="italic")
            path1 = TextPath((12, 12), "ABC", size=12, prop=fp)
            path2 = TextPath((0, 0), r"$\frac{1}{2}$", size=12, usetex=True)

        Also see :doc:`/gallery/text_labels_and_annotations/demo_text_path`.
        """
        ...
    def set_size(self, size: float):
        """Set the text size."""
        ...
    def get_size(self) -> float:
        """Get the text size."""
        ...
    @property
    def vertices(self) -> Path:
        """
        Return the cached path after updating it if necessary.
        """
        ...
    @property
    def codes(self):
        """
        Return the codes
        """
        ...
