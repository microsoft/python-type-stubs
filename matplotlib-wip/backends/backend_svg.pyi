import datetime
import numpy as np
from typing import Any, Callable, Iterable, Literal, Sequence
from matplotlib._typing import *
from matplotlib.transforms import Transform
from matplotlib.text import Text
from matplotlib.backend_bases import RendererBase
from matplotlib.backend_bases import GraphicsContextBase
from matplotlib.font_manager import FontProperties
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.figure import Figure
from matplotlib.backend_bases import _Backend
from matplotlib.transforms import Affine2DBase
from matplotlib.transforms import Affine2D

"""
This type stub file was generated by pyright.
"""

from matplotlib import _api
from matplotlib.backend_bases import FigureCanvasBase, RendererBase, _Backend
from encodings.utf_8 import StreamWriter
from io import BytesIO, TextIOWrapper
from matplotlib.font_manager import FontProperties
from typing import Dict, Optional, Tuple, Union

backend_version = ...

def escape_cdata(s): ...
def escape_comment(s): ...
def escape_attrib(s): ...
def short_float_fmt(x): ...

class XMLWriter:
    """
    Parameters
    ----------
    file : writable text file-like object
    """

    def __init__(self, file: Union[TextIOWrapper, StreamWriter]) -> None: ...
    def start(self, tag: str, attrib: Dict[str, str] = ..., **extra) -> int:  # -> int:
        """
        Open a new element.  Attributes can be given as keyword
        arguments, or as a string/string dictionary. The method returns
        an opaque identifier that can be passed to the :meth:`close`
        method, to close all open elements up to and including this one.

        Parameters
        ----------
        tag
            Element tag.
        attrib
            Attribute dictionary.  Alternatively, attributes can be given as
            keyword arguments.

        Returns
        -------
        An element identifier.
        """
        ...
    def comment(self, comment: str) -> None:  # -> None:
        """
        Add a comment to the output stream.

        Parameters
        ----------
        comment : str
            Comment text.
        """
        ...
    def data(self, text: str) -> None:  # -> None:
        """
        Add character data to the output stream.

        Parameters
        ----------
        text : str
            Character data.
        """
        ...
    def end(self, tag: Optional[str] = ..., indent: bool = ...) -> None:  # -> None:
        """
        Close the current element (opened by the most recent call to
        :meth:`start`).

        Parameters
        ----------
        tag
            Element tag.  If given, the tag must match the start tag.  If
            omitted, the current element is closed.
        """
        ...
    def close(self, id: int) -> None:  # -> None:
        """
        Close open elements, up to (and including) the element identified
        by the given identifier.

        Parameters
        ----------
        id
            Element identifier, as returned by the :meth:`start` method.
        """
        ...
    def element(
        self, tag: str, text: Optional[str] = ..., attrib: Dict[str, str] = ..., **extra
    ) -> None:  # -> None:
        """
        Add an entire element.  This is the same as calling :meth:`start`,
        :meth:`data`, and :meth:`end` in sequence. The *text* argument can be
        omitted.
        """
        ...
    def flush(self):  # -> None:
        """Flush the output stream."""
        ...

def generate_transform(transform_list=...): ...
def generate_css(attrib=...): ...

class RendererSVG(RendererBase):
    def __init__(
        self, width, height, svgwriter, basename=..., image_dpi=..., *, metadata=...
    ) -> None: ...
    def finalize(self) -> None: ...
    def open_group(self, s: str, gid: Optional[str] = ...) -> None: ...
    def close_group(self, s: str) -> None: ...
    def option_image_nocomposite(self) -> bool: ...
    def draw_path(self, gc, path, transform, rgbFace=...): ...
    def draw_markers(
        self,
        gc: GraphicsContextBase,
        marker_path,
        marker_trans: Transform,
        path,
        trans: Transform,
        rgbFace=...,
    ): ...
    def draw_path_collection(
        self,
        gc,
        master_transform,
        paths,
        all_transforms,
        offsets,
        offsetTrans,
        facecolors,
        edgecolors,
        linewidths,
        linestyles,
        antialiaseds,
        urls,
        offset_position,
    ): ...
    def draw_gouraud_triangle(self, gc: GraphicsContextBase, points, colors, trans): ...
    def draw_gouraud_triangles(
        self, gc, triangles_array, colors_array, transform: Transform
    ): ...
    def option_scale_image(self) -> bool: ...
    def get_image_magnification(self) -> float: ...
    def draw_image(
        self,
        gc: GraphicsContextBase,
        x: Scalar,
        y: Scalar,
        im,
        transform: Affine2DBase = ...,
    ): ...
    def draw_tex(self, gc, x, y, s, prop, angle, *, mtext=...): ...
    def draw_text(
        self,
        gc: GraphicsContextBase,
        x: float,
        y: float,
        s: str,
        prop: FontProperties,
        angle: float,
        ismath=...,
        mtext: Text = ...,
    ): ...
    def flipy(self) -> bool: ...
    def get_canvas_width_height(self): ...
    def get_text_width_height_descent(
        self, s: str, prop: FontProperties, ismath: bool
    ) -> Tuple[float, float, float]: ...

class FigureCanvasSVG(FigureCanvasBase):
    filetypes = ...
    fixed_dpi = ...

    def print_svg(
        self,
        filename: Union[BytesIO, str],
        *args,
        bbox_inches_restore=...,
        metadata: dict[str, Any] = ...
    ) -> None:  # -> None:
        """
        Parameters
        ----------
        filename : str or path-like or file-like
            Output target; if a string, a file will be opened for writing.

        metadata : dict[str, Any], optional
            Metadata in the SVG file defined as key-value pairs of strings,
            datetimes, or lists of strings, e.g., ``{'Creator': 'My software',
            'Contributor': ['Me', 'My Friend'], 'Title': 'Awesome'}``.

            The standard keys and their value types are:

            * *str*: ``'Coverage'``, ``'Description'``, ``'Format'``,
              ``'Identifier'``, ``'Language'``, ``'Relation'``, ``'Source'``,
              ``'Title'``, and ``'Type'``.
            * *str* or *list of str*: ``'Contributor'``, ``'Creator'``,
              ``'Keywords'``, ``'Publisher'``, and ``'Rights'``.
            * *str*, *date*, *datetime*, or *tuple* of same: ``'Date'``. If a
              non-*str*, then it will be formatted as ISO 8601.

            Values have been predefined for ``'Creator'``, ``'Date'``,
            ``'Format'``, and ``'Type'``. They can be removed by setting them
            to `None`.

            Information is encoded as `Dublin Core Metadata`__.

            .. _DC: https://www.dublincore.org/specifications/dublin-core/

            __ DC_
        """
        ...
    def print_svgz(self, filename, *args, **kwargs): ...
    def get_default_filetype(self): ...
    def draw(self): ...

FigureManagerSVG = ...
svgProlog = ...

class _BackendSVG(_Backend):
    FigureCanvas = FigureCanvasSVG
