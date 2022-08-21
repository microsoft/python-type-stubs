from .backend_bases import RendererBase
import functools

class TexManager:
    """
    Convert strings to dvi files using TeX, caching the results to a directory.

    Repeated calls to this constructor always return the same instance.
    """

    texcache = ...

    grey_arrayd = ...
    font_family = ...
    font_families = ...
    font_info = ...
    @functools.lru_cache()
    def __new__(cls) -> TexManager: ...
    def get_font_config(self): ...
    @classmethod
    def get_basefile(cls, tex: str, fontsize: float, dpi: None = ...) -> str:
        """
        Return a filename based on a hash of the string, fontsize, and dpi.
        """
        ...
    @classmethod
    def get_font_preamble(cls):
        """
        Return a string containing font configuration for the tex preamble.
        """
        ...
    @classmethod
    def get_custom_preamble(cls) -> str:
        """Return a string containing user additions to the tex preamble."""
        ...
    @classmethod
    def make_tex(cls, tex: str, fontsize: float) -> str:
        """
        Generate a tex file to render the tex string at a specific font size.

        Return the file name.
        """
        ...
    @classmethod
    def make_dvi(cls, tex: str, fontsize: float):
        """
        Generate a dvi file containing latex's layout of tex string.

        Return the file name.
        """
        ...
    @classmethod
    def make_png(cls, tex: str, fontsize: float, dpi: float):
        """
        Generate a png file containing latex's rendering of tex string.

        Return the file name.
        """
        ...
    @classmethod
    def get_grey(cls, tex: str, fontsize: float = ..., dpi: float = ...):
        """Return the alpha channel."""
        ...
    @classmethod
    def get_rgba(cls, tex: str, fontsize: float = ..., dpi: float = ..., rgb=...):
        r"""
        Return latex's rendering of the tex string as an rgba array.

        Examples
        --------
        >>> texmanager = TexManager()
        >>> s = r"\TeX\ is $\displaystyle\sum_n\frac{-e^{i\pi}}{2^n}$!"
        >>> Z = texmanager.get_rgba(s, fontsize=12, dpi=80, rgb=(1, 0, 0))
        """
        ...
    @classmethod
    def get_text_width_height_descent(
        cls, tex: str, fontsize: float, renderer: RendererBase = ...
    ):
        """Return width, height and descent of the text."""
        ...
