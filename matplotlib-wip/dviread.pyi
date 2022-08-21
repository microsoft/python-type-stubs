from ._typing import *
from .path import Path

from collections import namedtuple
from functools import lru_cache

Page = ...
Box = ...

class Text(namedtuple("Text", "x y font glyph width")):
    """
    A glyph in the dvi file.

    The *x* and *y* attributes directly position the glyph.  The *font*,
    *glyph*, and *width* attributes are kept public for back-compatibility,
    but users wanting to draw the glyph themselves are encouraged to instead
    load the font specified by `font_path` at `font_size`, warp it with the
    effects specified by `font_effects`, and load the glyph specified by
    `glyph_name_or_index`.
    """

    @property
    def font_path(self) -> Path:
        """The `~pathlib.Path` to the font for this glyph."""
        ...
    @property
    def font_size(self):
        """The font size."""
        ...
    @property
    def font_effects(self):
        """
        The "font effects" dict for this glyph.

        This dict contains the values for this glyph of SlantFont and
        ExtendFont (if any), read off :file:`pdftex.map`.
        """
        ...
    @property
    def glyph_name_or_index(self):
        """
        Either the glyph name or the native charmap glyph index.

        If :file:`pdftex.map` specifies an encoding for this glyph's font, that
        is a mapping of glyph indices to Adobe glyph names; use it to convert
        dvi indices to glyph names.  Callers can then convert glyph names to
        glyph indices (with FT_Get_Name_Index/get_name_index), and load the
        glyph using FT_Load_Glyph/load_glyph.

        If :file:`pdftex.map` specifies no encoding, the indices directly map
        to the font's "native" charmap; glyphs should directly loaded using
        FT_Load_Char/load_char after selecting the native charmap.
        """
        ...

class Dvi:
    """
    A reader for a dvi ("device-independent") file, as produced by TeX.

    The current implementation can only iterate through pages in order,
    and does not even attempt to verify the postamble.

    This class can be used as a context manager to close the underlying
    file upon exit. Pages can be read via iteration. Here is an overly
    simple way to extract text without trying to detect whitespace::

        >>> with matplotlib.dviread.Dvi('input.dvi', 72) as dvi:
        ...     for page in dvi:
        ...         print(''.join(chr(t.glyph) for t in page.text))
    """

    def __init__(self, filename, dpi) -> None:
        """
        Read the data from the file named *filename* and convert
        TeX's internal units to units of *dpi* per inch.
        *dpi* only sets the units and does not limit the resolution.
        Use None to return TeX's internal units.
        """
        ...
    baseline = ...
    def __enter__(self):
        """Context manager enter method, does nothing."""
        ...
    def __exit__(self, etype, evalue, etrace):
        """
        Context manager exit method, closes the underlying file if it is open.
        """
        ...
    def __iter__(self):
        """
        Iterate through the pages of the file.

        Yields
        ------
        Page
            Details of all the text and box objects on the page.
            The Page tuple contains lists of Text and Box tuples and
            the page dimensions, and the Text and Box tuples contain
            coordinates transformed into a standard Cartesian
            coordinate system at the dpi value given when initializing.
            The coordinates are floating point numbers, but otherwise
            precision is not lost and coordinate values are not clipped to
            integers.
        """
        ...
    def close(self) -> None:
        """Close the underlying file if it is open."""
        ...

class DviFont:
    """
    Encapsulation of a font that a DVI file can refer to.

    This class holds a font's texname and size, supports comparison,
    and knows the widths of glyphs in the same units as the AFM file.
    There are also internal attributes (for use by dviread.py) that
    are *not* used for comparison.

    The size is in Adobe points (converted from TeX points).

    Parameters
    ----------
    scale : float
        Factor by which the font is scaled from its natural size.
    tfm : Tfm
        TeX font metrics for this font
    texname : bytes
       Name of the font as used internally by TeX and friends, as an ASCII
       bytestring.  This is usually very different from any external font
       names; `PsfontsMap` can be used to find the external name of the font.
    vf : Vf
       A TeX "virtual font" file, or None if this font is not virtual.

    Attributes
    ----------
    texname : bytes
    size : float
       Size of the font in Adobe points, converted from the slightly
       smaller TeX points.
    widths : list
       Widths of glyphs in glyph-space units, typically 1/1000ths of
       the point size.

    """

    def __init__(self, scale: float, tfm: Tfm, texname: bytes, vf: Vf) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __repr__(self) -> str: ...

class Vf(Dvi):
    r"""
    A virtual font (\*.vf file) containing subroutines for dvi files.

    Parameters
    ----------
    filename : str or path-like

    Notes
    -----
    The virtual font format is a derivative of dvi:
    http://mirrors.ctan.org/info/knuth/virtual-fonts
    This class reuses some of the machinery of `Dvi`
    but replaces the `_read` loop and dispatch mechanism.

    Examples
    --------
    ::

        vf = Vf(filename)
        glyph = vf[code]
        glyph.text, glyph.boxes, glyph.width
    """
    def __init__(self, filename: str | PathLike) -> None: ...
    def __getitem__(self, code): ...

class Tfm:
    """
    A TeX Font Metric file.

    This implementation covers only the bare minimum needed by the Dvi class.

    Parameters
    ----------
    filename : str or path-like

    Attributes
    ----------
    checksum : int
       Used for verifying against the dvi file.
    design_size : int
       Design size of the font (unknown units)
    width, height, depth : dict
       Dimensions of each character, need to be scaled by the factor
       specified in the dvi file. These are dicts because indexing may
       not start from 0.
    """

    def __init__(self, filename: str | PathLike) -> None: ...

PsFont = ...

class PsfontsMap:
    """
    A psfonts.map formatted file, mapping TeX fonts to PS fonts.

    Parameters
    ----------
    filename : str or path-like

    Notes
    -----
    For historical reasons, TeX knows many Type-1 fonts by different
    names than the outside world. (For one thing, the names have to
    fit in eight characters.) Also, TeX's native fonts are not Type-1
    but Metafont, which is nontrivial to convert to PostScript except
    as a bitmap. While high-quality conversions to Type-1 format exist
    and are shipped with modern TeX distributions, we need to know
    which Type-1 fonts are the counterparts of which native fonts. For
    these reasons a mapping is needed from internal font names to font
    file names.

    A texmf tree typically includes mapping files called e.g.
    :file:`psfonts.map`, :file:`pdftex.map`, or :file:`dvipdfm.map`.
    The file :file:`psfonts.map` is used by :program:`dvips`,
    :file:`pdftex.map` by :program:`pdfTeX`, and :file:`dvipdfm.map`
    by :program:`dvipdfm`. :file:`psfonts.map` might avoid embedding
    the 35 PostScript fonts (i.e., have no filename for them, as in
    the Times-Bold example above), while the pdf-related files perhaps
    only avoid the "Base 14" pdf fonts. But the user may have
    configured these files differently.

    Examples
    --------
    >>> map = PsfontsMap(find_tex_file('pdftex.map'))
    >>> entry = map[b'ptmbo8r']
    >>> entry.texname
    b'ptmbo8r'
    >>> entry.psname
    b'Times-Bold'
    >>> entry.encoding
    '/usr/local/texlive/2008/texmf-dist/fonts/enc/dvips/base/8r.enc'
    >>> entry.effects
    {'slant': 0.16700000000000001}
    >>> entry.filename
    """

    @lru_cache()
    def __new__(cls, filename): ...
    def __getitem__(self, texname): ...

class _LuatexKpsewhich:
    @lru_cache()
    def __new__(cls): ...
    def search(self, filename): ...

def find_tex_file(filename: str | PathLike, format: str | bytes = ...): ...
