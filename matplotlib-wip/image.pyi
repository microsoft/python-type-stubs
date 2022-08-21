import numpy as np
from typing import Literal, Sequence
from ._typing import *
from .cm import ScalarMappable
from .backend_bases import MouseEvent, RendererBase
from .figure import Figure
from .colors import Colormap, Normalize
from .transforms import Bbox
from .axes import Axes
from .artist import Artist, allow_rasterization
from .transforms import Affine2D
from PIL.Image import Image

interpolations_names = ...

def composite_images(
    images: list[Image], renderer: RendererBase, magnification: float = 1
) -> tuple[np.ndarray, tuple[float, float]]:
    """
    Composite a number of RGBA images into one.  The images are
    composited in the order in which they appear in the *images* list.

    Parameters
    ----------
    images : list of Images
        Each must have a `make_image` method.  For each image,
        `can_composite` should return `True`, though this is not
        enforced by this function.  Each image must have a purely
        affine transformation with no shear.

    renderer : `.RendererBase`

    magnification : float, default: 1
        The additional magnification to apply for the renderer in use.

    Returns
    -------
    image : uint8 array (M, N, 4)
        The composited RGBA image.
    offset_x, offset_y : float
        The (left, bottom) offset where the composited image should be placed
        in the output figure.
    """
    ...

class _ImageBase(Artist, ScalarMappable):
    """
    Base class for images.

    interpolation and cmap default to their rc settings

    cmap is a colors.Colormap instance
    norm is a colors.Normalize instance to map luminance to 0-1

    extent is data axes (left, right, bottom, top) for making image plots
    registered with data plots.  Default is to label the pixel
    centers with the zero-based row and column indices.

    Additional kwargs are matplotlib.artist properties
    """

    zorder = ...
    def __init__(
        self,
        ax: Axes,
        cmap: Colormap = ...,
        norm: Normalize = ...,
        interpolation=...,
        origin=...,
        filternorm=...,
        filterrad=...,
        resample=...,
        *,
        interpolation_stage=...,
        **kwargs
    ) -> None: ...
    def __str__(self) -> str: ...
    def __getstate__(self): ...
    def get_size(self):
        """Return the size of the image as tuple (numrows, numcols)."""
        ...
    def set_alpha(self, alpha: float | ArrayLike | None):
        """
        Set the alpha value used for blending - not supported on all backends.

        Parameters
        ----------
        alpha : float or 2D array-like or None
        """
        ...
    def changed(self):
        """
        Call this whenever the mappable is changed so observers can update.
        """
        ...
    def make_image(
        self, renderer, magnification=..., unsampled=...
    ) -> tuple[np.ndarray, tuple[float, float], Affine2D]:
        """
        Normalize, rescale, and colormap this image's data for rendering using
        *renderer*, with the given *magnification*.

        If *unsampled* is True, the image will not be scaled, but an
        appropriate affine transformation will be returned instead.

        Returns
        -------
        image : (M, N, 4) uint8 array
            The RGBA image, resampled unless *unsampled* is True.
        x, y : float
            The upper left corner where the image should be drawn, in pixel
            space.
        trans : Affine2D
            The affine transformation from image to pixel space.
        """
        ...
    @allow_rasterization
    def draw(self, renderer: RendererBase, *args, **kwargs): ...
    def contains(self, mouseevent: MouseEvent):
        """Test whether the mouse event occurred within the image."""
        ...
    def write_png(self, fname: str):
        """Write the image to png file *fname*."""
        ...
    def set_data(self, A: ArrayLike | Image):
        """
        Set the image array.

        Note that this function does *not* update the normalization used.

        Parameters
        ----------
        A : array-like or `PIL.Image.Image`
        """
        ...
    def set_array(self, A: ArrayLike):
        """
        Retained for backwards compatibility - use set_data instead.

        Parameters
        ----------
        A : array-like
        """
        ...
    def get_interpolation(self) -> str:
        """
        Return the interpolation method the image uses when resizing.

        One of 'antialiased', 'nearest', 'bilinear', 'bicubic', 'spline16',
        'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
        'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos',
        or 'none'.
        """
        ...
    def set_interpolation(
        self,
        s: Literal[
            "antialiased",
            "nearest",
            "bilinear",
            "bicubic",
            "spline16",
            "spline36",
            "hanning",
            "hamming",
            "hermite",
            "kaiser",
            "quadric",
            "catrom",
            "gaussian",
            "bessel",
            "mitchell",
            "sinc",
            "lanczos",
            "none",
        ]
        | None,
    ):
        """
        Set the interpolation method the image uses when resizing.

        If None, use :rc:`image.interpolation`. If 'none', the image is
        shown as is without interpolating. 'none' is only supported in
        agg, ps and pdf backends and will fall back to 'nearest' mode
        for other backends.

        Parameters
        ----------
        s : {'antialiased', 'nearest', 'bilinear', 'bicubic', 'spline16', \
'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', \
'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos', 'none'} or None
        """
        ...
    def set_interpolation_stage(self, s: Literal["data", "rgba"] | None):
        """
        Set when interpolation happens during the transform to RGBA.

        Parameters
        ----------
        s : {'data', 'rgba'} or None
            Whether to apply up/downsampling interpolation in data or rgba
            space.
        """
        ...
    def can_composite(self) -> bool:
        """Return whether the image can be composited with its neighbors."""
        ...
    def set_resample(self, v: bool | None):
        """
        Set whether image resampling is used.

        Parameters
        ----------
        v : bool or None
            If None, use :rc:`image.resample`.
        """
        ...
    def get_resample(self) -> bool:
        """Return whether image resampling is used."""
        ...
    def set_filternorm(self, filternorm: bool):
        """
        Set whether the resize filter normalizes the weights.

        See help for `~.Axes.imshow`.

        Parameters
        ----------
        filternorm : bool
        """
        ...
    def get_filternorm(self) -> bool:
        """Return whether the resize filter normalizes the weights."""
        ...
    def set_filterrad(self, filterrad: float):
        """
        Set the resize filter radius only applicable to some
        interpolation schemes -- see help for imshow

        Parameters
        ----------
        filterrad : positive float
        """
        ...
    def get_filterrad(self) -> float:
        """Return the filterrad setting."""
        ...

class AxesImage(_ImageBase):
    """
    An image attached to an Axes.

    Parameters
    ----------
    ax : `~.axes.Axes`
        The axes the image will belong to.
    cmap : str or `~Colormap`, default: :rc:`image.cmap`
        The Colormap instance or registered colormap name used to map scalar
        data to colors.
    norm : `~Normalize`
        Maps luminance to 0-1.
    interpolation : str, default: :rc:`image.interpolation`
        Supported values are 'none', 'antialiased', 'nearest', 'bilinear',
        'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite',
        'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell',
        'sinc', 'lanczos', 'blackman'.
    interpolation_stage : {'data', 'rgba'}, default: 'data'
        If 'data', interpolation
        is carried out on the data provided by the user.  If 'rgba', the
        interpolation is carried out after the colormapping has been
        applied (visual interpolation).
    origin : {'upper', 'lower'}, default: :rc:`image.origin`
        Place the [0, 0] index of the array in the upper left or lower left
        corner of the axes. The convention 'upper' is typically used for
        matrices and images.
    extent : tuple, optional
        The data axes (left, right, bottom, top) for making image plots
        registered with data plots.  Default is to label the pixel
        centers with the zero-based row and column indices.
    filternorm : bool, default: True
        A parameter for the antigrain image resize filter
        (see the antigrain documentation).
        If filternorm is set, the filter normalizes integer values and corrects
        the rounding errors. It doesn't do anything with the source floating
        point values, it corrects only integers according to the rule of 1.0
        which means that any sum of pixel weights must be equal to 1.0. So,
        the filter function must produce a graph of the proper shape.
    filterrad : float > 0, default: 4
        The filter radius for filters that have a radius parameter, i.e. when
        interpolation is one of: 'sinc', 'lanczos' or 'blackman'.
    resample : bool, default: False
        When True, use a full resampling method. When False, only resample when
        the output image is larger than the input image.
    **kwargs : `.Artist` properties
    """

    def __init__(
        self,
        ax: Axes,
        cmap: str | Colormap = ...,
        norm: Normalize = ...,
        interpolation: str = ...,
        origin: Literal["upper", "lower"] = ...,
        extent: tuple = ...,
        filternorm: bool = True,
        filterrad: float = 4,
        resample: bool = False,
        *,
        interpolation_stage: Literal["data", "rgba"] = ...,
        **kwargs
    ) -> None: ...
    def get_window_extent(self, renderer: RendererBase = ...): ...
    def make_image(
        self, renderer: RendererBase, magnification: float = ..., unsampled=...
    ): ...
    def set_extent(self, extent: Sequence[float]):
        """
        Set the image extent.

        Parameters
        ----------
        extent : 4-tuple of float
            The position and size of the image as tuple
            ``(left, right, bottom, top)`` in data coordinates.

        Notes
        -----
        This updates ``ax.dataLim``, and, if autoscaling, sets ``ax.viewLim``
        to tightly fit the image, regardless of ``dataLim``.  Autoscaling
        state is not changed, so following this with ``ax.autoscale_view()``
        will redo the autoscaling in accord with ``dataLim``.
        """
        ...
    def get_extent(self) -> tuple[float, float, float, float]:
        """Return the image extent as tuple (left, right, bottom, top)."""
        ...
    def get_cursor_data(self, event: MouseEvent):
        """
        Return the image value at the event position or *None* if the event is
        outside the image.

        See Also
        --------
        Artist.get_cursor_data
        """
        ...

class NonUniformImage(AxesImage):
    mouseover = ...
    def __init__(
        self,
        ax: Axes,
        *,
        interpolation: Literal["nearest", "bilinear"] = "nearest",
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        interpolation : {'nearest', 'bilinear'}, default: 'nearest'

        **kwargs
            All other keyword arguments are identical to those of `.AxesImage`.
        """
        ...
    def make_image(
        self, renderer: RendererBase, magnification: float = ..., unsampled=...
    ): ...
    def set_data(self, x: ArrayLike, y: ArrayLike, A: ArrayLike):
        """
        Set the grid for the pixel centers, and the pixel values.

        Parameters
        ----------
        x, y : 1D array-like
            Monotonic arrays of shapes (N,) and (M,), respectively, specifying
            pixel centers.
        A : array-like
            (M, N) np.ndarray or masked array of values to be colormapped, or
            (M, N, 3) RGB array, or (M, N, 4) RGBA array.
        """
        ...
    def set_array(self, *args): ...
    def set_interpolation(self, s: Literal["nearest", "bilinear"] | None):
        """
        Parameters
        ----------
        s : {'nearest', 'bilinear'} or None
            If None, use :rc:`image.interpolation`.
        """
        ...
    def get_extent(self): ...
    def set_filternorm(self, s): ...
    def set_filterrad(self, s): ...
    def set_norm(self, norm: Normalize | None): ...
    def set_cmap(self, cmap: Colormap | str | None): ...

class PcolorImage(AxesImage):
    """
    Make a pcolor-style plot with an irregular rectangular grid.

    This uses a variation of the original irregular image code,
    and it is used by pcolorfast for the corresponding grid type.
    """

    def __init__(
        self,
        ax: Axes,
        x: ArrayLike = ...,
        y: ArrayLike = ...,
        A: ArrayLike = ...,
        cmap: str | Colormap = ...,
        norm: Normalize = ...,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        ax : `~.axes.Axes`
            The axes the image will belong to.
        x, y : 1D array-like, optional
            Monotonic arrays of length N+1 and M+1, respectively, specifying
            rectangle boundaries.  If not given, will default to
            ``range(N + 1)`` and ``range(M + 1)``, respectively.
        A : array-like
            The data to be color-coded. The interpretation depends on the
            shape:

            - (M, N) np.ndarray or masked array: values to be colormapped
            - (M, N, 3): RGB array
            - (M, N, 4): RGBA array

        cmap : str or `~Colormap`, default: :rc:`image.cmap`
            The Colormap instance or registered colormap name used to map
            scalar data to colors.
        norm : `~Normalize`
            Maps luminance to 0-1.
        **kwargs : `.Artist` properties
        """
        ...
    def make_image(
        self, renderer: RendererBase, magnification: float = ..., unsampled=...
    ): ...
    def set_data(self, x: ArrayLike, y: ArrayLike, A: ArrayLike):
        """
        Set the grid for the rectangle boundaries, and the data values.

        Parameters
        ----------
        x, y : 1D array-like, optional
            Monotonic arrays of length N+1 and M+1, respectively, specifying
            rectangle boundaries.  If not given, will default to
            ``range(N + 1)`` and ``range(M + 1)``, respectively.
        A : array-like
            The data to be color-coded. The interpretation depends on the
            shape:

            - (M, N) np.ndarray or masked array: values to be colormapped
            - (M, N, 3): RGB array
            - (M, N, 4): RGBA array
        """
        ...
    def set_array(self, *args): ...
    def get_cursor_data(self, event: MouseEvent): ...

class FigureImage(_ImageBase):
    """An image attached to a figure."""

    zorder = ...

    def __init__(
        self,
        fig: Figure,
        cmap: Colormap = ...,
        norm: Normalize = ...,
        offsetx=...,
        offsety=...,
        origin=...,
        **kwargs
    ) -> None:
        """
        cmap is a colors.Colormap instance
        norm is a colors.Normalize instance to map luminance to 0-1

        kwargs are an optional list of Artist keyword args
        """
        ...
    def get_extent(self) -> tuple[float, float, float, float]:
        """Return the image extent as tuple (left, right, bottom, top)."""
        ...
    def make_image(
        self, renderer: RendererBase, magnification: float = ..., unsampled=...
    ): ...
    def set_data(self, A):
        """Set the image array."""
        ...

class BboxImage(_ImageBase):
    """The Image class whose size is determined by the given bbox."""

    def __init__(
        self,
        bbox: Bbox,
        cmap: Colormap = ...,
        norm: Normalize = ...,
        interpolation=...,
        origin=...,
        filternorm=...,
        filterrad=...,
        resample=...,
        **kwargs
    ) -> None:
        """
        cmap is a colors.Colormap instance
        norm is a colors.Normalize instance to map luminance to 0-1

        kwargs are an optional list of Artist keyword args
        """
        ...
    def get_window_extent(
        self, renderer: RendererBase = ...
    ) -> tuple[float, float, float, float]: ...
    def contains(self, mouseevent: MouseEvent) -> bool:
        """Test whether the mouse event occurred within the image."""
        ...
    def make_image(
        self, renderer: RendererBase, magnification: float = ..., unsampled=...
    ): ...

def imread(fname: str | FileLike, format: str = ...) -> np.ndarray:
    """
    Read an image from a file into an array.

    .. note::

        This function exists for historical reasons.  It is recommended to
        use `PIL.Image.open` instead for loading images.

    Parameters
    ----------
    fname : str or file-like
        The image file to read: a filename, a URL or a file-like object opened
        in read-binary mode.

        Passing a URL is deprecated.  Please open the URL
        for reading and pass the result to Pillow, e.g. with
        ``np.array(PIL.Image.open(urllib.request.urlopen(url)))``.
    format : str, optional
        The image file format assumed for reading the data.  The image is
        loaded as a PNG file if *format* is set to "png", if *fname* is a path
        or opened file with a ".png" extension, or if it is an URL.  In all
        other cases, *format* is ignored and the format is auto-detected by
        `PIL.Image.open`.

    Returns
    -------
    `numpy.array`
        The image data. The returned array has shape

        - (M, N) for grayscale images.
        - (M, N, 3) for RGB images.
        - (M, N, 4) for RGBA images.

        PNG images are returned as float arrays (0-1).  All other formats are
        returned as int arrays, with a bit depth determined by the file's
        contents.
    """
    ...

def imsave(
    fname: str | PathLike | FileLike,
    arr: ArrayLike,
    vmin: float = ...,
    vmax: float = ...,
    cmap: str | Colormap = ...,
    format: str = ...,
    origin: Literal["upper", "lower"] = ...,
    dpi: float = ...,
    *,
    metadata: dict = ...,
    pil_kwargs: dict = ...
):
    """
    Save an array as an image file.

    Parameters
    ----------
    fname : str or path-like or file-like
        A path or a file-like object to store the image in.
        If *format* is not set, then the output format is inferred from the
        extension of *fname*, if any, and from :rc:`savefig.format` otherwise.
        If *format* is set, it determines the output format.
    arr : array-like
        The image data. The shape can be one of
        MxN (luminance), MxNx3 (RGB) or MxNx4 (RGBA).
    vmin, vmax : float, optional
        *vmin* and *vmax* set the color scaling for the image by fixing the
        values that map to the colormap color limits. If either *vmin*
        or *vmax* is None, that limit is determined from the *arr*
        min/max value.
    cmap : str or `~Colormap`, default: :rc:`image.cmap`
        A Colormap instance or registered colormap name. The colormap
        maps scalar data to colors. It is ignored for RGB(A) data.
    format : str, optional
        The file format, e.g. 'png', 'pdf', 'svg', ...  The behavior when this
        is unset is documented under *fname*.
    origin : {'upper', 'lower'}, default: :rc:`image.origin`
        Indicates whether the ``(0, 0)`` index of the array is in the upper
        left or lower left corner of the axes.
    dpi : float
        The DPI to store in the metadata of the file.  This does not affect the
        resolution of the output image.  Depending on file format, this may be
        rounded to the nearest integer.
    metadata : dict, optional
        Metadata in the image file.  The supported keys depend on the output
        format, see the documentation of the respective backends for more
        information.
    pil_kwargs : dict, optional
        Keyword arguments passed to `PIL.Image.Image.save`.  If the 'pnginfo'
        key is present, it completely overrides *metadata*, including the
        default 'Software' key.
    """
    ...

def pil_to_array(pilImage) -> np.ndarray:
    """
    Load a `PIL image`_ and return it as a numpy int array.

    .. _PIL image: https://pillow.readthedocs.io/en/latest/reference/Image.html

    Returns
    -------
    numpy.array

        The array shape depends on the image type:

        - (M, N) for grayscale images.
        - (M, N, 3) for RGB images.
        - (M, N, 4) for RGBA images.
    """
    ...

def thumbnail(
    infile: str | FileLike,
    thumbfile: str | FileLike,
    scale: float = ...,
    interpolation: str = ...,
    preview: bool = ...,
) -> Figure:
    """
    Make a thumbnail of image in *infile* with output filename *thumbfile*.

    See :doc:`/gallery/misc/image_thumbnail_sgskip`.

    Parameters
    ----------
    infile : str or file-like
        The image file. Matplotlib relies on Pillow_ for image reading, and
        thus supports a wide range of file formats, including PNG, JPG, TIFF
        and others.

        .. _Pillow: https://python-pillow.org/

    thumbfile : str or file-like
        The thumbnail filename.

    scale : float, default: 0.1
        The scale factor for the thumbnail.

    interpolation : str, default: 'bilinear'
        The interpolation scheme used in the resampling. See the
        *interpolation* parameter of `~.Axes.imshow` for possible values.

    preview : bool, default: False
        If True, the default backend (presumably a user interface
        backend) will be used which will cause a figure to be raised if
        `~matplotlib.pyplot.show` is called.  If it is False, the figure is
        created using `.FigureCanvasBase` and the drawing backend is selected
        as `.Figure.savefig` would normally do.

    Returns
    -------
    `.Figure`
        The figure instance containing the thumbnail.
    """
    ...
