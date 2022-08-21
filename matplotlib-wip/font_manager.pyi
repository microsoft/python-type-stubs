from matplotlib.ft2font import FT2Font
from typing import Literal
from ._typing import *
from ._afm import AFM

from pathlib import PosixPath

import json
from functools import lru_cache

font_scalings = ...
stretch_dict = ...
weight_dict = ...

font_family_aliases = ...
MSFolders = ...
MSFontDirectories = ...
MSUserFontDirectories = ...
X11FontDirectories = ...
OSXFontDirectories = ...

def get_fontext_synonyms(fontext):
    """
    Return a list of file extensions that are synonyms for
    the given file extension *fileext*.
    """
    ...

def list_fonts(directory, extensions):
    """
    Return a list of all fonts matching any of the extensions, found
    recursively under the directory.
    """
    ...

def win32FontDirectory():
    r"""
    Return the user-specified font directory for Win32.  This is
    looked up from the registry key ::

      \\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders\Fonts

    If the key is not found, ``%WINDIR%\Fonts`` will be returned.
    """
    ...

def win32InstalledFonts(directory=..., fontext=...):
    """
    Search for fonts in the specified font directory, or use the
    system directories if none given. Additionally, it is searched for user
    fonts installed. A list of TrueType font filenames are returned by default,
    or AFM fonts if *fontext* == 'afm'.
    """
    ...

def get_fontconfig_fonts(fontext=...):
    """List font filenames known to ``fc-list`` having the given extension."""
    ...

def findSystemFonts(fontpaths=..., fontext=...):
    """
    Search for fonts in the specified font paths.  If no paths are
    given, will use a standard set of system paths, as well as the
    list of fonts tracked by fontconfig if fontconfig is installed and
    available.  A list of TrueType fonts are returned by default with
    AFM fonts as an option.
    """
    ...

FontEntry = ...

def ttfFontProperty(font: FT2Font) -> FontEntry:
    """
    Extract information from a TrueType font file.

    Parameters
    ----------
    font : `.FT2Font`
        The TrueType font file from which information will be extracted.

    Returns
    -------
    `FontEntry`
        The extracted font properties.

    """
    ...

def afmFontProperty(fontpath, font: AFM) -> FontEntry:
    """
    Extract information from an AFM font file.

    Parameters
    ----------
    font : AFM
        The AFM font file from which information will be extracted.

    Returns
    -------
    `FontEntry`
        The extracted font properties.
    """
    ...

class FontProperties:
    """
    A class for storing and manipulating font properties.

    The font properties are the six properties described in the
    `W3C Cascading Style Sheet, Level 1
    <http://www.w3.org/TR/1998/REC-CSS2-19980512/>`_ font
    specification and *math_fontfamily* for math fonts:

    - family: A list of font names in decreasing order of priority.
      The items may include a generic font family name, either
      'sans-serif', 'serif', 'cursive', 'fantasy', or 'monospace'.
      In that case, the actual font to be used will be looked up
      from the associated rcParam. Default: :rc:`font.family`

    - style: Either 'normal', 'italic' or 'oblique'.
      Default: :rc:`font.style`

    - variant: Either 'normal' or 'small-caps'.
      Default: :rc:`font.variant`

    - stretch: A numeric value in the range 0-1000 or one of
      'ultra-condensed', 'extra-condensed', 'condensed',
      'semi-condensed', 'normal', 'semi-expanded', 'expanded',
      'extra-expanded' or 'ultra-expanded'. Default: :rc:`font.stretch`

    - weight: A numeric value in the range 0-1000 or one of
      'ultralight', 'light', 'normal', 'regular', 'book', 'medium',
      'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy',
      'extra bold', 'black'. Default: :rc:`font.weight`

    - size: Either an relative value of 'xx-small', 'x-small',
      'small', 'medium', 'large', 'x-large', 'xx-large' or an
      absolute font size, e.g., 10. Default: :rc:`font.size`

    - math_fontfamily: The family of fonts used to render math text.
      Supported values are: 'dejavusans', 'dejavuserif', 'cm',
      'stix', 'stixsans' and 'custom'. Default: :rc:`mathtext.fontset`

    Alternatively, a font may be specified using the absolute path to a font
    file, by using the *fname* kwarg.  However, in this case, it is typically
    simpler to just pass the path (as a `pathlib.Path`, not a `str`) to the
    *font* kwarg of the `.Text` object.

    The preferred usage of font sizes is to use the relative values,
    e.g.,  'large', instead of absolute font sizes, e.g., 12.  This
    approach allows all text sizes to be made larger or smaller based
    on the font manager's default font size.

    This class will also accept a fontconfig_ pattern_, if it is the only
    argument provided.  This support does not depend on fontconfig; we are
    merely borrowing its pattern syntax for use here.

    .. _fontconfig: https://www.freedesktop.org/wiki/Software/fontconfig/
    .. _pattern:
       https://www.freedesktop.org/software/fontconfig/fontconfig-user.html

    Note that Matplotlib's internal font manager and fontconfig use a
    different algorithm to lookup fonts, so the results of the same pattern
    may be different in Matplotlib than in other applications that use
    fontconfig.
    """

    def __init__(
        self,
        family: list[str]
        | str
        | Literal["sans-serif", "serif", "cursive", "fantasy", "monospace"] = ...,
        style: Literal["normal", "italic", "oblique"] = ...,
        variant: Literal["normal", "small-caps"] = ...,
        weight: int
        | Literal[
            "ultralight",
            "light",
            "normal",
            "regular",
            "book",
            "medium",
            "roman",
            "semibold",
            "demibold",
            "demi",
            "bold",
            "heavy",
            "extra bold",
            "black",
        ] = ...,
        stretch: int
        | Literal[
            "ultra-condensed",
            "extra-condensed",
            "condensed",
            "semi-condensed",
            "normal",
            "semi-expanded",
            "expanded",
            "extra-expanded",
            "ultra-expanded",
        ] = ...,
        size: float
        | Literal[
            "xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"
        ] = ...,
        fname: PosixPath | None = ...,
        math_fontfamily: Literal[
            "dejavusans", "dejavuserif", "cm", "stix", "stixsans", "custom"
        ] = ...,
    ) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: "FontProperties") -> bool: ...
    def __str__(self) -> str: ...
    def get_family(self) -> list[str]:
        """
        Return a list of font names that comprise the font family.
        """
        ...
    def get_name(self) -> str:
        """
        Return the name of the font that best matches the font properties.
        """
        ...
    def get_style(self) -> str:
        """
        Return the font style.  Values are: 'normal', 'italic' or 'oblique'.
        """
        ...
    def get_variant(self) -> str:
        """
        Return the font variant.  Values are: 'normal' or 'small-caps'.
        """
        ...
    def get_weight(self) -> str:
        """
        Set the font weight.  Options are: A numeric value in the
        range 0-1000 or one of 'light', 'normal', 'regular', 'book',
        'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold',
        'heavy', 'extra bold', 'black'
        """
        ...
    def get_stretch(self) -> str:
        """
        Return the font stretch or width.  Options are: 'ultra-condensed',
        'extra-condensed', 'condensed', 'semi-condensed', 'normal',
        'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'.
        """
        ...
    def get_size(self) -> float:
        """
        Return the font size.
        """
        ...
    def get_file(self) -> str | None:
        """
        Return the filename of the associated font.
        """
        ...
    def get_fontconfig_pattern(self) -> str:
        """
        Get a fontconfig_ pattern_ suitable for looking up the font as
        specified with fontconfig's ``fc-match`` utility.

        This support does not depend on fontconfig; we are merely borrowing its
        pattern syntax for use here.
        """
        ...
    def set_family(
        self,
        family: str
        | list[str]
        | Literal["sans-serif", "serif", "cursive", "fantasy", "monospace"],
    ) -> None:
        """
        Change the font family.  May be either an alias (generic name
        is CSS parlance), such as: 'serif', 'sans-serif', 'cursive',
        'fantasy', or 'monospace', a real font name or a list of real
        font names.  Real font names are not supported when
        :rc:`text.usetex` is `True`. Default: :rc:`font.family`
        """
        ...
    def set_style(self, style: Literal["normal", "italic", "oblique"]) -> None:
        """
        Set the font style.

        Parameters
        ----------
        style : {'normal', 'italic', 'oblique'}, default: :rc:`font.style`
        """
        ...
    def set_variant(self, variant: Literal["normal", "small-caps"]) -> None:
        """
        Set the font variant.

        Parameters
        ----------
        variant : {'normal', 'small-caps'}, default: :rc:`font.variant`
        """
        ...
    def set_weight(
        self,
        weight: int
        | Literal[
            "ultralight",
            "light",
            "normal",
            "regular",
            "book",
            "medium",
            "roman",
            "semibold",
            "demibold",
            "demi",
            "bold",
            "heavy",
            "extra bold",
            "black",
        ],
    ) -> None:
        """
        Set the font weight.

        Parameters
        ----------
        weight : int or {'ultralight', 'light', 'normal', 'regular', 'book', \
'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', \
'extra bold', 'black'}, default: :rc:`font.weight`
            If int, must be in the range  0-1000.
        """
        ...
    def set_stretch(
        self,
        stretch: int
        | Literal[
            "ultra-condensed",
            "extra-condensed",
            "condensed",
            "semi-condensed",
            "normal",
            "semi-expanded",
            "expanded",
            "extra-expanded",
            "ultra-expanded",
        ],
    ) -> None:
        """
        Set the font stretch or width.

        Parameters
        ----------
        stretch : int or {'ultra-condensed', 'extra-condensed', 'condensed', \
'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', \
'ultra-expanded'}, default: :rc:`font.stretch`
            If int, must be in the range  0-1000.
        """
        ...
    def set_size(
        self,
        size: float
        | Literal[
            "xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"
        ],
    ) -> None:
        """
        Set the font size.

        Parameters
        ----------
        size : float or {'xx-small', 'x-small', 'small', 'medium', \
'large', 'x-large', 'xx-large'}, default: :rc:`font.size`
            If float, the font size in points. The string values denote sizes
            relative to the default font size.
        """
        ...
    def set_file(self, file: PosixPath | None) -> None:
        """
        Set the filename of the fontfile to use.  In this case, all
        other properties will be ignored.
        """
        ...
    def set_fontconfig_pattern(self, pattern: str) -> None:
        """
        Set the properties by parsing a fontconfig_ *pattern*.

        This support does not depend on fontconfig; we are merely borrowing its
        pattern syntax for use here.
        """
        ...
    def get_math_fontfamily(self) -> str:
        """
        Return the name of the font family used for math text.

        The default font is :rc:`mathtext.fontset`.
        """
        ...
    def set_math_fontfamily(
        self,
        fontfamily: Literal[
            "dejavusans", "dejavuserif", "cm", "stix", "stixsans", "custom"
        ],
    ) -> None:
        """
        Set the font family for text in math mode.

        If not set explicitly, :rc:`mathtext.fontset` will be used.

        Parameters
        ----------
        fontfamily : str
            The name of the font family.

            Available font families are defined in the
            matplotlibrc.template file
            :ref:`here <customizing-with-matplotlibrc-files>`

        See Also
        --------
        .text.Text.get_math_fontfamily
        """
        ...
    def copy(self) -> "FontProperties":
        """Return a copy of self."""
        ...
    set_name = ...
    get_slant = ...
    set_slant = ...
    get_size_in_points = ...

class _JSONEncoder(json.JSONEncoder):
    def default(self, o): ...

def json_dump(data, filename):
    """
    Dump `FontManager` *data* as JSON to the file named *filename*.

    See Also
    --------
    json_load

    Notes
    -----
    File paths that are children of the Matplotlib data path (typically, fonts
    shipped with Matplotlib) are stored relative to that data path (to remain
    valid across virtualenvs).

    This function temporarily locks the output file to prevent multiple
    processes from overwriting one another's output.
    """
    ...

def json_load(filename: PosixPath) -> FontManager:
    """
    Load a `FontManager` from the JSON file named *filename*.

    See Also
    --------
    json_dump
    """
    ...

class FontManager:
    """
    On import, the `FontManager` singleton instance creates a list of ttf and
    afm fonts and caches their `FontProperties`.  The `FontManager.findfont`
    method does a nearest neighbor search to find the font that most closely
    matches the specification.  If no good enough match is found, the default
    font is returned.
    """

    def __init__(self, size=..., weight=...) -> None: ...
    def addfont(self, path: str | PathLike):
        """
        Cache the properties of the font at *path* to make it available to the
        `FontManager`.  The type of font is inferred from the path suffix.

        Parameters
        ----------
        path : str or path-like
        """
        ...
    @property
    def defaultFont(self): ...
    def get_default_weight(self):
        """
        Return the default font weight.
        """
        ...
    @staticmethod
    def get_default_size() -> float:
        """
        Return the default font size.
        """
        ...
    def set_default_weight(
        self,
        weight: int
        | Literal[
            "ultralight",
            "light",
            "normal",
            "regular",
            "book",
            "medium",
            "roman",
            "semibold",
            "demibold",
            "demi",
            "bold",
            "heavy",
            "extra bold",
            "black",
        ],
    ):
        """
        Set the default font weight.  The initial value is 'normal'.
        """
        ...
    def score_family(self, families: list[str], family2: str) -> float:
        """
        Return a match score between the list of font families in
        *families* and the font family name *family2*.

        An exact match at the head of the list returns 0.0.

        A match further down the list will return between 0 and 1.

        No match will return 1.0.
        """
        ...
    def score_style(self, style1: str, style2: str) -> float:
        """
        Return a match score between *style1* and *style2*.

        An exact match returns 0.0.

        A match between 'italic' and 'oblique' returns 0.1.

        No match returns 1.0.
        """
        ...
    def score_variant(self, variant1: str, variant2: str) -> float:
        """
        Return a match score between *variant1* and *variant2*.

        An exact match returns 0.0, otherwise 1.0.
        """
        ...
    def score_stretch(self, stretch1: str, stretch2: str) -> float:
        """
        Return a match score between *stretch1* and *stretch2*.

        The result is the absolute value of the difference between the
        CSS numeric values of *stretch1* and *stretch2*, normalized
        between 0.0 and 1.0.
        """
        ...
    def score_weight(self, weight1: str, weight2: int) -> float:
        """
        Return a match score between *weight1* and *weight2*.

        The result is 0.0 if both weight1 and weight 2 are given as strings
        and have the same value.

        Otherwise, the result is the absolute value of the difference between
        the CSS numeric values of *weight1* and *weight2*, normalized between
        0.05 and 1.0.
        """
        ...
    def score_size(self, size1: float, size2: str) -> float:
        """
        Return a match score between *size1* and *size2*.

        If *size2* (the size specified in the font file) is 'scalable', this
        function always returns 0.0, since any font size can be generated.

        Otherwise, the result is the absolute distance between *size1* and
        *size2*, normalized so that the usual range of font sizes (6pt -
        72pt) will lie between 0.0 and 1.0.
        """
        ...
    def findfont(
        self,
        prop: FontProperties | str,
        fontext: Literal["ttf", "afm"] = ...,
        directory: str = ...,
        fallback_to_default: bool = ...,
        rebuild_if_missing: bool = ...,
    ) -> str:
        """
        Find a font that most closely matches the given font properties.

        Parameters
        ----------
        prop : str or `~FontProperties`
            The font properties to search for. This can be either a
            `.FontProperties` object or a string defining a
            `fontconfig patterns`_.

        fontext : {'ttf', 'afm'}, default: 'ttf'
            The extension of the font file:

            - 'ttf': TrueType and OpenType fonts (.ttf, .ttc, .otf)
            - 'afm': Adobe Font Metrics (.afm)

        directory : str, optional
            If given, only search this directory and its subdirectories.

        fallback_to_default : bool
            If True, will fallback to the default font family (usually
            "DejaVu Sans" or "Helvetica") if the first lookup hard-fails.

        rebuild_if_missing : bool
            Whether to rebuild the font cache and search again if the first
            match appears to point to a nonexisting font (i.e., the font cache
            contains outdated entries).

        Returns
        -------
        str
            The filename of the best matching font.

        Notes
        -----
        This performs a nearest neighbor search.  Each font is given a
        similarity score to the target font properties.  The first font with
        the highest score is returned.  If no matches below a certain
        threshold are found, the default font (usually DejaVu Sans) is
        returned.

        The result is cached, so subsequent lookups don't have to
        perform the O(n) nearest neighbor search.

        See the `W3C Cascading Style Sheet, Level 1
        <http://www.w3.org/TR/1998/REC-CSS2-19980512/>`_ documentation
        for a description of the font finding algorithm.

        .. _fontconfig patterns:
           https://www.freedesktop.org/software/fontconfig/fontconfig-user.html
        """
        ...
    def get_font_names(self) -> list:
        """Return the list of available fonts."""
        ...

@lru_cache()
def is_opentype_cff_font(filename):
    """
    Return whether the given font is a Postscript Compact Font Format Font
    embedded in an OpenType wrapper.  Used by the PostScript and PDF backends
    that can not subset these fonts.
    """
    ...

def get_font(filename, hinting_factor=...): ...

fontManager = ...
findfont = ...
get_font_names = ...
