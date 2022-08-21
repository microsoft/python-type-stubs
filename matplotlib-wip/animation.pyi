from typing import Callable, Iterable
from .figure import Figure

from itertools import count
from typing import Callable, Dict, List, Tuple

import abc
import contextlib

subprocess_creation_flags = ...

def adjusted_figsize(w: float, h: float, dpi: float, n: int) -> tuple[float, float]: ...

class MovieWriterRegistry:
    def __init__(self) -> None: ...
    def register(self, name: str) -> Callable: ...
    def is_available(self, name: str) -> bool: ...
    def __iter__(self): ...
    def list(self) -> list[MovieWriter]: ...
    def __getitem__(self, name) -> MovieWriter: ...

writers = ...

class AbstractMovieWriter(abc.ABC):
    def __init__(
        self,
        fps: int = ...,
        metadata: Dict[str, str] = ...,
        codec=...,
        bitrate=...,
    ) -> None: ...
    @abc.abstractmethod
    def setup(self, fig: Figure, outfile: str, dpi: float = ...): ...
    @property
    def frame_size(self) -> Tuple[int, int]: ...
    @abc.abstractmethod
    def grab_frame(self, **savefig_kwargs): ...
    @abc.abstractmethod
    def finish(self): ...
    @contextlib.contextmanager
    def saving(self, fig: Figure, outfile, dpi, *args, **kwargs): ...

class MovieWriter(AbstractMovieWriter):

    frame_format: str
    fig: Figure

    supported_formats = ...
    def __init__(
        self,
        fps: int = ...,
        codec: str | None = ...,
        bitrate: int = ...,
        extra_args: list[str] | None = ...,
        metadata: Dict[str, str] = ...,
    ) -> None: ...
    def setup(self, fig: Figure, outfile: str, dpi: float = ...): ...
    def finish(self): ...
    def grab_frame(self, **savefig_kwargs): ...
    @classmethod
    def bin_path(cls) -> str: ...
    @classmethod
    def isAvailable(cls) -> bool:
        """Return whether a MovieWriter subclass is actually available."""
        ...

class FileMovieWriter(MovieWriter):
    """
    `MovieWriter` for writing to individual files and stitching at the end.

    This must be sub-classed to be useful.
    """

    def __init__(self, *args, **kwargs) -> None: ...
    def setup(
        self, fig: Figure, outfile: str, dpi: float = ..., frame_prefix: str = ...
    ):
        """
        Setup for writing the movie file.

        Parameters
        ----------
        fig : `~Figure`
            The figure to grab the rendered frames from.
        outfile : str
            The filename of the resulting movie file.
        dpi : float, default: ``fig.dpi``
            The dpi of the output file. This, with the figure size,
            controls the size in pixels of the resulting movie file.
        frame_prefix : str, optional
            The filename prefix to use for temporary files.  If *None* (the
            default), files are written to a temporary directory which is
            deleted by `cleanup`; if not *None*, no temporary files are
            deleted.
        """
        ...
    def __del__(self): ...
    @property
    def frame_format(self):
        """
        Format (png, jpeg, etc.) to use for saving the frames, which can be
        decided by the individual subclasses.
        """
        ...
    @frame_format.setter
    def frame_format(self, frame_format): ...
    def grab_frame(self, **savefig_kwargs): ...
    def finish(self): ...

class PillowWriter(AbstractMovieWriter):
    @classmethod
    def isAvailable(cls): ...
    def setup(self, fig: Figure, outfile: str, dpi: float = ...): ...
    def grab_frame(self, **savefig_kwargs): ...
    def finish(self): ...

class FFMpegBase:
    """
    Mixin class for FFMpeg output.

    This is a base class for the concrete `FFMpegWriter` and `FFMpegFileWriter`
    classes.
    """

    @property
    def output_args(self) -> list[str]: ...

class FFMpegWriter(FFMpegBase, MovieWriter):
    """
    Pipe-based ffmpeg writer.

    Frames are streamed directly to ffmpeg via a pipe and written in a single
    pass.
    """

    ...

class FFMpegFileWriter(FFMpegBase, FileMovieWriter):
    """
    File-based ffmpeg writer.

    Frames are written to temporary files on disk and then stitched
    together at the end.
    """

    supported_formats = ...

class ImageMagickBase:
    """
    Mixin class for ImageMagick output.

    This is a base class for the concrete `ImageMagickWriter` and
    `ImageMagickFileWriter` classes, which define an ``input_names`` attribute
    (or property) specifying the input names passed to ImageMagick.
    """

    @property
    def delay(self): ...
    @property
    def output_args(self): ...
    @classmethod
    def bin_path(cls): ...
    @classmethod
    def isAvailable(cls): ...

class ImageMagickWriter(ImageMagickBase, MovieWriter):
    """
    Pipe-based animated gif.

    Frames are streamed directly to ImageMagick via a pipe and written
    in a single pass.
    """

    input_names = ...

class ImageMagickFileWriter(ImageMagickBase, FileMovieWriter):
    """
    File-based animated gif writer.

    Frames are written to temporary files on disk and then stitched
    together at the end.
    """

    supported_formats = ...
    input_names = ...

class HTMLWriter(FileMovieWriter):
    """Writer for JavaScript-based HTML movies."""

    supported_formats = ...
    @classmethod
    def isAvailable(cls): ...
    def __init__(
        self,
        fps=...,
        codec=...,
        bitrate=...,
        extra_args=...,
        metadata=...,
        embed_frames=...,
        default_mode=...,
        embed_limit=...,
    ) -> None: ...
    def setup(self, fig: Figure, outfile: str, dpi: float, frame_dir=...): ...
    def grab_frame(self, **savefig_kwargs): ...
    def finish(self): ...

class Animation:
    """
    A base class for Animations.

    This class is not usable as is, and should be subclassed to provide needed
    behavior.

    .. note::

        You must store the created Animation in a variable that lives as long
        as the animation should run. Otherwise, the Animation object will be
        garbage-collected and the animation stops.

    Parameters
    ----------
    fig : `~Figure`
        The figure object used to get needed events, such as draw or resize.

    event_source : object, optional
        A class that can run a callback when desired events
        are generated, as well as be stopped and started.

        Examples include timers (see `TimedAnimation`) and file
        system notifications.

    blit : bool, default: False
        Whether blitting is used to optimize drawing.

    See Also
    --------
    FuncAnimation,  ArtistAnimation
    """

    def __init__(
        self, fig: Figure, event_source: object = ..., blit: bool = ...
    ) -> None: ...
    def __del__(self): ...
    def save(
        self,
        filename: str,
        writer: MovieWriter | str = ...,
        fps: int = ...,
        dpi: float = ...,
        codec: str = ...,
        bitrate: int = ...,
        extra_args: list[str] | None = ...,
        metadata: dict[str, str] = ...,
        extra_anim: list = ...,
        savefig_kwargs: dict = ...,
        *,
        progress_callback: Callable = ...
    ):
        """
        Save the animation as a movie file by drawing every frame.

        Parameters
        ----------
        filename : str
            The output filename, e.g., :file:`mymovie.mp4`.

        writer : `MovieWriter` or str, default: :rc:`animation.writer`
            A `MovieWriter` instance to use or a key that identifies a
            class to use, such as 'ffmpeg'.

        fps : int, optional
            Movie frame rate (per second).  If not set, the frame rate from the
            animation's frame interval.

        dpi : float, default: :rc:`savefig.dpi`
            Controls the dots per inch for the movie frames.  Together with
            the figure's size in inches, this controls the size of the movie.

        codec : str, default: :rc:`animation.codec`.
            The video codec to use.  Not all codecs are supported by a given
            `MovieWriter`.

        bitrate : int, default: :rc:`animation.bitrate`
            The bitrate of the movie, in kilobits per second.  Higher values
            means higher quality movies, but increase the file size.  A value
            of -1 lets the underlying movie encoder select the bitrate.

        extra_args : list of str or None, optional
            Extra command-line arguments passed to the underlying movie
            encoder.  The default, None, means to use
            :rc:`animation.[name-of-encoder]_args` for the builtin writers.

        metadata : dict[str, str], default: {}
            Dictionary of keys and values for metadata to include in
            the output file. Some keys that may be of use include:
            title, artist, genre, subject, copyright, srcform, comment.

        extra_anim : list, default: []
            Additional `Animation` objects that should be included
            in the saved movie file. These need to be from the same
            `Figure` instance. Also, animation frames will
            just be simply combined, so there should be a 1:1 correspondence
            between the frames from the different animations.

        savefig_kwargs : dict, default: {}
            Keyword arguments passed to each `~.Figure.savefig` call used to
            save the individual frames.

        progress_callback : function, optional
            A callback function that will be called for every frame to notify
            the saving progress. It must have the signature ::

                def func(current_frame: int, total_frames: int) -> Any

            where *current_frame* is the current frame number and
            *total_frames* is the total number of frames to be saved.
            *total_frames* is set to None, if the total number of frames can
            not be determined. Return values may exist but are ignored.

            Example code to write the progress to stdout::

                progress_callback =\
                    lambda i, n: print(f'Saving frame {i} of {n}')

        Notes
        -----
        *fps*, *codec*, *bitrate*, *extra_args* and *metadata* are used to
        construct a `.MovieWriter` instance and can only be passed if
        *writer* is a string.  If they are passed as non-*None* and *writer*
        is a `.MovieWriter`, a `RuntimeError` will be raised.
        """
        ...
    def new_frame_seq(self):
        """Return a new sequence of frame information."""
        ...
    def new_saved_frame_seq(self):
        """Return a new sequence of saved/cached frame information."""
        ...
    def to_html5_video(self, embed_limit: float = ...) -> str:
        """
        Convert the animation to an HTML5 ``<video>`` tag.

        This saves the animation as an h264 video, encoded in base64
        directly into the HTML5 video tag. This respects :rc:`animation.writer`
        and :rc:`animation.bitrate`. This also makes use of the
        ``interval`` to control the speed, and uses the ``repeat``
        parameter to decide whether to loop.

        Parameters
        ----------
        embed_limit : float, optional
            Limit, in MB, of the returned animation. No animation is created
            if the limit is exceeded.
            Defaults to :rc:`animation.embed_limit` = 20.0.

        Returns
        -------
        str
            An HTML5 video tag with the animation embedded as base64 encoded
            h264 video.
            If the *embed_limit* is exceeded, this returns the string
            "Video too large to embed."
        """
        ...
    def to_jshtml(
        self, fps: int = ..., embed_frames: bool = ..., default_mode: str = ...
    ):
        """
        Generate HTML representation of the animation.

        Parameters
        ----------
        fps : int, optional
            Movie frame rate (per second). If not set, the frame rate from
            the animation's frame interval.
        embed_frames : bool, optional
        default_mode : str, optional
            What to do when the animation ends. Must be one of ``{'loop',
            'once', 'reflect'}``. Defaults to ``'loop'`` if ``self.repeat``
            is True, otherwise ``'once'``.
        """
        ...
    def pause(self):
        """Pause the animation."""
        ...
    def resume(self):
        """Resume the animation."""
        ...

class TimedAnimation(Animation):
    """
    `Animation` subclass for time-based animation.

    A new frame is drawn every *interval* milliseconds.

    .. note::

        You must store the created Animation in a variable that lives as long
        as the animation should run. Otherwise, the Animation object will be
        garbage-collected and the animation stops.

    Parameters
    ----------
    fig : `~Figure`
        The figure object used to get needed events, such as draw or resize.
    interval : int, default: 200
        Delay between frames in milliseconds.
    repeat_delay : int, default: 0
        The delay in milliseconds between consecutive animation runs, if
        *repeat* is True.
    repeat : bool, default: True
        Whether the animation repeats when the sequence of frames is completed.
    blit : bool, default: False
        Whether blitting is used to optimize drawing.
    """

    def __init__(
        self,
        fig: Figure,
        interval: int = ...,
        repeat_delay: int = ...,
        repeat: bool = ...,
        event_source=...,
        *args,
        **kwargs
    ) -> None: ...

class ArtistAnimation(TimedAnimation):
    """
    Animation using a fixed set of `.Artist` objects.

    Before creating an instance, all plotting should have taken place
    and the relevant artists saved.

    .. note::

        You must store the created Animation in a variable that lives as long
        as the animation should run. Otherwise, the Animation object will be
        garbage-collected and the animation stops.

    Parameters
    ----------
    fig : `~Figure`
        The figure object used to get needed events, such as draw or resize.
    artists : list
        Each list entry is a collection of `.Artist` objects that are made
        visible on the corresponding frame.  Other artists are made invisible.
    interval : int, default: 200
        Delay between frames in milliseconds.
    repeat_delay : int, default: 0
        The delay in milliseconds between consecutive animation runs, if
        *repeat* is True.
    repeat : bool, default: True
        Whether the animation repeats when the sequence of frames is completed.
    blit : bool, default: False
        Whether blitting is used to optimize drawing.
    """

    def __init__(self, fig: Figure, artists: list, *args, **kwargs) -> None: ...

class FuncAnimation(TimedAnimation):
    """
    Makes an animation by repeatedly calling a function *func*.

    .. note::

        You must store the created Animation in a variable that lives as long
        as the animation should run. Otherwise, the Animation object will be
        garbage-collected and the animation stops.

    Parameters
    ----------
    fig : `~Figure`
        The figure object used to get needed events, such as draw or resize.

    func : callable
        The function to call at each frame.  The first argument will
        be the next value in *frames*.   Any additional positional
        arguments can be supplied via the *fargs* parameter.

        The required signature is::

            def func(frame, *fargs) -> iterable_of_artists

        If ``blit == True``, *func* must return an iterable of all artists
        that were modified or created. This information is used by the blitting
        algorithm to determine which parts of the figure have to be updated.
        The return value is unused if ``blit == False`` and may be omitted in
        that case.

    frames : iterable, int, generator function, or None, optional
        Source of data to pass *func* and each frame of the animation

        - If an iterable, then simply use the values provided.  If the
          iterable has a length, it will override the *save_count* kwarg.

        - If an integer, then equivalent to passing ``range(frames)``

        - If a generator function, then must have the signature::

             def gen_function() -> obj

        - If *None*, then equivalent to passing ``itertools.count``.

        In all of these cases, the values in *frames* is simply passed through
        to the user-supplied *func* and thus can be of any type.

    init_func : callable, optional
        A function used to draw a clear frame. If not given, the results of
        drawing from the first item in the frames sequence will be used. This
        function will be called once before the first frame.

        The required signature is::

            def init_func() -> iterable_of_artists

        If ``blit == True``, *init_func* must return an iterable of artists
        to be re-drawn. This information is used by the blitting algorithm to
        determine which parts of the figure have to be updated.  The return
        value is unused if ``blit == False`` and may be omitted in that case.

    fargs : tuple or None, optional
        Additional arguments to pass to each call to *func*.

    save_count : int, default: 100
        Fallback for the number of values from *frames* to cache. This is
        only used if the number of frames cannot be inferred from *frames*,
        i.e. when it's an iterator without length or a generator.

    interval : int, default: 200
        Delay between frames in milliseconds.

    repeat_delay : int, default: 0
        The delay in milliseconds between consecutive animation runs, if
        *repeat* is True.

    repeat : bool, default: True
        Whether the animation repeats when the sequence of frames is completed.

    blit : bool, default: False
        Whether blitting is used to optimize drawing.  Note: when using
        blitting, any animated artists will be drawn according to their zorder;
        however, they will be drawn on top of any previous artists, regardless
        of their zorder.

    cache_frame_data : bool, default: True
        Whether frame data is cached.  Disabling cache might be helpful when
        frames contain large objects.
    """

    def __init__(
        self,
        fig: Figure,
        func: Callable,
        frames: Callable | Iterable | int | None = ...,
        init_func: Callable = ...,
        fargs: tuple | None = ...,
        save_count: int = ...,
        *,
        cache_frame_data: bool = ...,
        **kwargs
    ) -> None: ...
    def new_frame_seq(self) -> count: ...
    def new_saved_frame_seq(self): ...
