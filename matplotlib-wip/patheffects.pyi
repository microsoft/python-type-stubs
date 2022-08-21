from typing import Callable, Iterable, Sequence
from ._typing import *
from .transforms import Transform
from .backend_bases import GraphicsContextBase, RendererBase

class AbstractPathEffect:
    """
    A base class for path effects.

    Subclasses should override the ``draw_path`` method to add effect
    functionality.
    """

    def __init__(self, offset: Sequence[float] = ...) -> None:
        """
        Parameters
        ----------
        offset : (float, float), default: (0, 0)
            The (x, y) offset to apply to the path, measured in points.
        """
        ...
    def draw_path(
        self,
        renderer: RendererBase,
        gc: GraphicsContextBase,
        tpath,
        affine,
        rgbFace=...,
    ):
        """
        Derived should override this method. The arguments are the same
        as :meth:`RendererBase.draw_path`
        except the first argument is a renderer.
        """
        ...

class PathEffectRenderer(RendererBase):
    """
    Implements a Renderer which contains another renderer.

    This proxy then intercepts draw calls, calling the appropriate
    :class:`AbstractPathEffect` draw method.

    .. note::
        Not all methods have been overridden on this RendererBase subclass.
        It may be necessary to add further methods to extend the PathEffects
        capabilities further.
    """

    def __init__(
        self, path_effects: Iterable[AbstractPathEffect], renderer: RendererBase
    ) -> None:
        """
        Parameters
        ----------
        path_effects : iterable of :class:`AbstractPathEffect`
            The path effects which this renderer represents.
        renderer : `RendererBase` subclass

        """
        ...
    def copy_with_path_effect(self, path_effects): ...
    def draw_path(self, gc: GraphicsContextBase, tpath, affine, rgbFace=...): ...
    def draw_markers(
        self,
        gc: GraphicsContextBase,
        marker_path,
        marker_trans: Transform,
        path,
        *args,
        **kwargs
    ): ...
    def draw_path_collection(
        self, gc: GraphicsContextBase, master_transform, paths, *args, **kwargs
    ): ...
    def __getattribute__(
        self, name: str
    ) -> Callable | list[Stroke | Normal] | RendererBase: ...

class Normal(AbstractPathEffect):
    """
    The "identity" PathEffect.

    The Normal PathEffect's sole purpose is to draw the original artist with
    no special path effect.
    """

    ...

class Stroke(AbstractPathEffect):
    """A line based PathEffect which re-draws a stroke."""

    def __init__(self, offset: Sequence[float] = ..., **kwargs) -> None:
        """
        The path will be stroked with its gc updated with the given
        keyword arguments, i.e., the keyword arguments should be valid
        gc parameter values.
        """
        ...
    def draw_path(
        self,
        renderer: RendererBase,
        gc: GraphicsContextBase,
        tpath,
        affine,
        rgbFace: Color,
    ):
        """Draw the path with updated gc."""
        ...

withStroke = ...

class SimplePatchShadow(AbstractPathEffect):
    """A simple shadow via a filled patch."""

    def __init__(
        self,
        offset: Sequence[float] = ...,
        shadow_rgbFace: Color = ...,
        alpha: float = 0.3,
        rho: float = 0.3,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        offset : (float, float), default: (2, -2)
            The (x, y) offset of the shadow in points.
        shadow_rgbFace : color
            The shadow color.
        alpha : float, default: 0.3
            The alpha transparency of the created shadow patch.
            http://matplotlib.1069221.n5.nabble.com/path-effects-question-td27630.html
        rho : float, default: 0.3
            A scale factor to apply to the rgbFace color if *shadow_rgbFace*
            is not specified.
        **kwargs
            Extra keywords are stored and passed through to
            :meth:`AbstractPathEffect._update_gc`.

        """
        ...
    def draw_path(
        self,
        renderer: RendererBase,
        gc: GraphicsContextBase,
        tpath,
        affine,
        rgbFace: Color,
    ):
        """
        Overrides the standard draw_path to add the shadow offset and
        necessary color changes for the shadow.
        """
        ...

withSimplePatchShadow = ...

class SimpleLineShadow(AbstractPathEffect):
    """A simple shadow via a line."""

    def __init__(
        self,
        offset: Sequence[float] = ...,
        shadow_color: Color = "black",
        alpha: float = 0.3,
        rho: float = 0.3,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        offset : (float, float), default: (2, -2)
            The (x, y) offset to apply to the path, in points.
        shadow_color : color, default: 'black'
            The shadow color.
            A value of ``None`` takes the original artist's color
            with a scale factor of *rho*.
        alpha : float, default: 0.3
            The alpha transparency of the created shadow patch.
        rho : float, default: 0.3
            A scale factor to apply to the rgbFace color if *shadow_color*
            is ``None``.
        **kwargs
            Extra keywords are stored and passed through to
            :meth:`AbstractPathEffect._update_gc`.
        """
        ...
    def draw_path(
        self,
        renderer: RendererBase,
        gc: GraphicsContextBase,
        tpath,
        affine,
        rgbFace: Color,
    ):
        """
        Overrides the standard draw_path to add the shadow offset and
        necessary color changes for the shadow.
        """
        ...

class PathPatchEffect(AbstractPathEffect):
    """
    Draws a `.PathPatch` instance whose Path comes from the original
    PathEffect artist.
    """

    def __init__(self, offset: Sequence[float] = ..., **kwargs) -> None:
        """
        Parameters
        ----------
        offset : (float, float), default: (0, 0)
            The (x, y) offset to apply to the path, in points.
        **kwargs
            All keyword arguments are passed through to the
            :class:`~matplotlib.patches.PathPatch` constructor. The
            properties which cannot be overridden are "path", "clip_box"
            "transform" and "clip_path".
        """
        ...
    def draw_path(
        self,
        renderer: RendererBase,
        gc: GraphicsContextBase,
        tpath,
        affine,
        rgbFace: Color,
    ): ...

class TickedStroke(AbstractPathEffect):
    """
    A line-based PathEffect which draws a path with a ticked style.

    This line style is frequently used to represent constraints in
    optimization.  The ticks may be used to indicate that one side
    of the line is invalid or to represent a closed boundary of a
    domain (i.e. a wall or the edge of a pipe).

    The spacing, length, and angle of ticks can be controlled.

    This line style is sometimes referred to as a hatched line.

    See also the :doc:`contour demo example
    </gallery/lines_bars_and_markers/lines_with_ticks_demo>`.

    See also the :doc:`contours in optimization example
    </gallery/images_contours_and_fields/contours_in_optimization_demo>`.
    """

    def __init__(
        self,
        offset: Sequence[float] = ...,
        spacing: float = 10,
        angle: float = 45,
        length: float = 1.414,
        **kwargs
    ) -> None:
        """
        Parameters
        ----------
        offset : (float, float), default: (0, 0)
            The (x, y) offset to apply to the path, in points.
        spacing : float, default: 10.0
            The spacing between ticks in points.
        angle : float, default: 45.0
            The angle between the path and the tick in degrees.  The angle
            is measured as if you were an ant walking along the curve, with
            zero degrees pointing directly ahead, 90 to your left, -90
            to your right, and 180 behind you.
        length : float, default: 1.414
            The length of the tick relative to spacing.
            Recommended length = 1.414 (sqrt(2)) when angle=45, length=1.0
            when angle=90 and length=2.0 when angle=60.
        **kwargs
            Extra keywords are stored and passed through to
            :meth:`AbstractPathEffect._update_gc`.

        Examples
        --------
        See :doc:`/gallery/misc/tickedstroke_demo`.
        """
        ...
    def draw_path(
        self,
        renderer: RendererBase,
        gc: GraphicsContextBase,
        tpath,
        affine,
        rgbFace: Color,
    ):
        """Draw the path with updated gc."""
        ...

withTickedStroke = ...
