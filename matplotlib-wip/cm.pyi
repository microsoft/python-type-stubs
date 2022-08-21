from ._typing import *
from .colors import Colormap, Normalize

from collections.abc import Mapping

class __getattr__:
    LUTSIZE = ...

class ColormapRegistry(Mapping):
    def __init__(self, cmaps) -> None: ...
    def __getitem__(self, item: str): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __str__(self) -> str: ...
    def __call__(self):
        """
        Return a list of the registered colormap names.

        This exists only for backward-compatibility in `.pyplot` which had a
        ``plt.colormaps()`` method. The recommended way to get this list is
        now ``list(colormaps)``.
        """
        ...
    def register(self, cmap: Colormap, *, name: str = ..., force: bool = ...) -> None:
        """
        Register a new colormap.

        The colormap name can then be used as a string argument to any ``cmap``
        parameter in Matplotlib. It is also available in ``pyplot.get_cmap``.

        The colormap registry stores a copy of the given colormap, so that
        future changes to the original colormap instance do not affect the
        registered colormap. Think of this as the registry taking a snapshot
        of the colormap at registration.

        Parameters
        ----------
        cmap : Colormap
            The colormap to register.

        name : str, optional
            The name for the colormap. If not given, ``cmap.name`` is used.

        force : bool, default: False
            If False, a ValueError is raised if trying to overwrite an already
            registered name. True supports overwriting registered colormaps
            other than the builtin colormaps.
        """
        ...
    def unregister(self, name: str) -> None:
        """
        Remove a colormap from the registry.

        You cannot remove built-in colormaps.

        If the named colormap is not registered, returns with no error, raises
        if you try to de-register a default colormap.

        .. warning::

            Colormap names are currently a shared namespace that may be used
            by multiple packages. Use `unregister` only if you know you
            have registered that name before. In particular, do not
            unregister just in case to clean the name before registering a
            new colormap.

        Parameters
        ----------
        name : str
            The name of the colormap to be removed.

        Raises
        ------
        ValueError
            If you try to remove a default built-in colormap.
        """
        ...

def register_cmap(
    name: str = ..., cmap: Colormap = ..., *, override_builtin: bool = ...
) -> None:
    """
    Add a colormap to the set recognized by :func:`get_cmap`.

    Register a new colormap to be accessed by name ::

        LinearSegmentedColormap('swirly', data, lut)
        register_cmap(cmap=swirly_cmap)

    Parameters
    ----------
    name : str, optional
       The name that can be used in :func:`get_cmap` or :rc:`image.cmap`

       If absent, the name will be the :attr:`~Colormap.name`
       attribute of the *cmap*.

    cmap : Colormap
       Despite being the second argument and having a default value, this
       is a required argument.

    override_builtin : bool

        Allow built-in colormaps to be overridden by a user-supplied
        colormap.

        Please do not use this unless you are sure you need it.
    """
    ...

def get_cmap(name: Colormap | str | None = ..., lut: int | None = ...) -> Colormap:
    """
    Get a colormap instance, defaulting to rc values if *name* is None.

    Colormaps added with :func:`register_cmap` take precedence over
    built-in colormaps.

    Parameters
    ----------
    name : `Colormap` or str or None, default: None
        If a `.Colormap` instance, it will be returned. Otherwise, the name of
        a colormap known to Matplotlib, which will be resampled by *lut*. The
        default, None, means :rc:`image.cmap`.
    lut : int or None, default: None
        If *name* is not already a Colormap instance and *lut* is not None, the
        colormap will be resampled to have *lut* entries in the lookup table.
    """
    ...

def unregister_cmap(name: str) -> Colormap | None:
    """
    Remove a colormap recognized by :func:`get_cmap`.

    You may not remove built-in colormaps.

    If the named colormap is not registered, returns with no error, raises
    if you try to de-register a default colormap.

    .. warning::

      Colormap names are currently a shared namespace that may be used
      by multiple packages. Use `unregister_cmap` only if you know you
      have registered that name before. In particular, do not
      unregister just in case to clean the name before registering a
      new colormap.

    Parameters
    ----------
    name : str
        The name of the colormap to be un-registered

    Returns
    -------
    ColorMap or None
        If the colormap was registered, return it if not return `None`

    Raises
    ------
    ValueError
       If you try to de-register a default built-in colormap.
    """
    ...

class ScalarMappable:
    """
    A mixin class to map scalar data to RGBA.

    The ScalarMappable applies data normalization before returning RGBA colors
    from the given colormap.
    """

    def __init__(
        self, norm: Normalize | None = ..., cmap: str | Colormap = ...
    ) -> None:
        """

        Parameters
        ----------
        norm : `Normalize` (or subclass thereof)
            The normalizing object which scales data, typically into the
            interval ``[0, 1]``.
            If *None*, *norm* defaults to a *colors.Normalize* object which
            initializes its scaling based on the first data processed.
        cmap : str or `~Colormap`
            The colormap used to map normalized data values to RGBA colors.
        """
        ...
    callbacksSM = ...
    def to_rgba(self, x, alpha=..., bytes=..., norm=...):
        """
        Return a normalized rgba array corresponding to *x*.

        In the normal case, *x* is a 1D or 2D sequence of scalars, and
        the corresponding np.ndarray of rgba values will be returned,
        based on the norm and colormap set for this ScalarMappable.

        There is one special case, for handling images that are already
        rgb or rgba, such as might have been read from an image file.
        If *x* is an np.ndarray with 3 dimensions,
        and the last dimension is either 3 or 4, then it will be
        treated as an rgb or rgba array, and no mapping will be done.
        The array can be uint8, or it can be floating point with
        values in the 0-1 range; otherwise a ValueError will be raised.
        If it is a masked array, the mask will be ignored.
        If the last dimension is 3, the *alpha* kwarg (defaulting to 1)
        will be used to fill in the transparency.  If the last dimension
        is 4, the *alpha* kwarg is ignored; it does not
        replace the preexisting alpha.  A ValueError will be raised
        if the third dimension is other than 3 or 4.

        In either case, if *bytes* is *False* (default), the rgba
        array will be floats in the 0-1 range; if it is *True*,
        the returned rgba array will be uint8 in the 0 to 255 range.

        If norm is False, no normalization of the input data is
        performed, and it is assumed to be in the range (0-1).

        """
        ...
    def set_array(self, A: ArrayLike | None) -> None:
        """
        Set the value array from array-like *A*.

        Parameters
        ----------
        A : array-like or None
            The values that are mapped to colors.

            The base class `.ScalarMappable` does not make any assumptions on
            the dimensionality and shape of the value array *A*.
        """
        ...
    def get_array(self):
        """
        Return the array of values, that are mapped to colors.

        The base class `.ScalarMappable` does not make any assumptions on
        the dimensionality and shape of the array.
        """
        ...
    def get_cmap(self) -> Colormap:
        """Return the `.Colormap` instance."""
        ...
    def get_clim(self) -> tuple:
        """
        Return the values (min, max) that are mapped to the colormap limits.
        """
        ...
    def set_clim(self, vmin: float = ..., vmax: float = ...):
        """
        Set the norm limits for image scaling.

        Parameters
        ----------
        vmin, vmax : float
             The limits.

             The limits may also be passed as a tuple (*vmin*, *vmax*) as a
             single positional argument.

             .. ACCEPTS: (vmin: float, vmax: float)
        """
        ...
    def get_alpha(self) -> float:
        """
        Returns
        -------
        float
            Always returns 1.
        """
        ...
    def set_cmap(self, cmap: Colormap | str | None):
        """
        Set the colormap for luminance data.

        Parameters
        ----------
        cmap : `.Colormap` or str or None
        """
        ...
    @property
    def norm(self) -> Normalize: ...
    @norm.setter
    def norm(self, norm): ...
    def set_norm(self, norm: Normalize | None):
        """
        Set the normalization instance.

        Parameters
        ----------
        norm : `.Normalize` or None

        Notes
        -----
        If there are any colorbars using the mappable for this norm, setting
        the norm of the mappable will reset the norm, locator, and formatters
        on the colorbar to default.
        """
        ...
    def autoscale(self) -> None:
        """
        Autoscale the scalar limits on the norm instance using the
        current array
        """
        ...
    def autoscale_None(self) -> None:
        """
        Autoscale the scalar limits on the norm instance using the
        current array, changing only limits that are None
        """
        ...
    def changed(self) -> None:
        """
        Call this whenever the mappable is changed to notify all the
        callbackSM listeners to the 'changed' signal.
        """
        ...
